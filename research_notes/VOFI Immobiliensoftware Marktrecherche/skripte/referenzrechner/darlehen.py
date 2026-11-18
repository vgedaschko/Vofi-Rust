"""Kapitel 5 der Fachspezifikation: Darlehen (R-5.1 bis R-5.19).

Eine Tranche fuehrt ihren Plan Periode fuer Periode; der Finanzplan (finanzplan.py) ruft sie auf.
Zinsen einer Periode haengen nur von der Restschuld der Vorperiode ab (R-4.2).
"""
from decimal import Decimal as D, ROUND_FLOOR
from zahlen import NULL, EINS, d, ab_cent, Meldung, FEHLER

ARTEN = ("annuitaet_prozent", "annuitaet_laufzeit", "raten", "endfaellig", "frei")
ANSCHLUSSREGELN = ("tilgungssatz", "rate", "restlaufzeit")


class Tranche:
    """Eine Kredittranche (Bankdarlehen, KfW-Darlehen, Foerderdarlehen, uebernommenes Darlehen).

    betrag            Nennbetrag (bei uebernommenem Darlehen die Restschuld am Stichtag)
    art               Tilgungsart, siehe ARTEN
    zins              nominaler Jahreszins waehrend der Zinsbindung (R-5.2)
    tilgungssatz      anfaenglicher Tilgungssatz je Jahr (nur annuitaet_prozent)
    rate_betrag       Bezugsgroesse der Rate einer Prozentannuitaet (R-5.11: beim uebernommenen Darlehen der
                      urspruengliche Nennbetrag); Voreinstellung der Nennbetrag
    laufzeit          Zahl der Tilgungsperioden (annuitaet_laufzeit, raten)
    auszahlung        {Periode: Betrag}; Voreinstellung alles in Periode 0
    einbehalt         bei der ersten Auszahlung einbehaltener Betrag (Disagio, Entgelt), R-5.14
    tilgungsbeginn    Periode der ersten Tilgung (Voreinstellung 1)
    bindung           Zahl der Perioden mit festem Zins ab Stichtag (None = bis zum Ende)
    anschluss_zins    nominaler Jahreszins nach der Bindung (R-5.8)
    anschluss_regel   "tilgungssatz" (Voreinstellung, MA-034), "rate" oder "restlaufzeit" (R-5.9)
    anschluss_tilgung Tilgungssatz der Anschlussfinanzierung (Voreinstellung: der anfaengliche)
    beitrag_satz      laufender Beitrag je Jahr auf die Restschuld (Verwaltungskostenbeitrag), R-5.13
    tilgungszuschuss  {Periode: Betrag} Minderung der Restschuld ohne Geldfluss, R-5.15
    rundung           "kaufm" (Voreinstellung), "ab" oder "keine" je Darlehen (MA-013)
    bank              True fuer das Bankdarlehen der Regel R-5.12, False fuer uebrige Darlehen
    foerder           Kennzeichen Foerderdarlehen: keine Vorfaelligkeitsentschaedigung (R-5.16)
    vfe_bis           Periode, bis zu der eine Vorfaelligkeitsentschaedigung anfaellt: das Ende der Zinsbindung,
                      hoechstens der frueheste Kuendigungstermin (BGB-489); Voreinstellung die Zinsbindung
    bereit_satz       Bereitstellungszins je Monat auf den nicht ausgezahlten Betrag (R-5.18)
    bereit_frei       bereitstellungsfreie Monate ab dem Stichtag
    """

    def __init__(self, name, betrag, art, zins, tilgungssatz=None, laufzeit=None, auszahlung=None,
                 einbehalt=0, tilgungsbeginn=1, bindung=None, anschluss_zins=None,
                 anschluss_regel="tilgungssatz", anschluss_tilgung=None, beitrag_satz=0,
                 tilgungszuschuss=None, rundung="kaufm", bank=True, foerder=False, rate_betrag=None,
                 vfe_bis=None, bereit_satz=0, bereit_frei=0):
        assert art in ARTEN and anschluss_regel in ANSCHLUSSREGELN
        self.name, self.betrag, self.art = name, d(betrag), art
        self.zins = d(zins)
        self.tilgungssatz = None if tilgungssatz is None else d(tilgungssatz)
        self.rate_betrag = self.betrag if rate_betrag is None else d(rate_betrag)
        self.laufzeit = laufzeit
        self.auszahlung = {int(k): d(v) for k, v in (auszahlung or {0: betrag}).items()}
        assert sum(self.auszahlung.values()) == self.betrag, "Auszahlungen muessen den Nennbetrag ergeben"
        self.einbehalt = d(einbehalt)
        self.tilgungsbeginn = tilgungsbeginn
        self.bindung = bindung
        self.anschluss_zins = None if anschluss_zins is None else d(anschluss_zins)
        self.anschluss_regel = anschluss_regel
        self.anschluss_tilgung = None if anschluss_tilgung is None else d(anschluss_tilgung)
        self.beitrag_satz = d(beitrag_satz)
        self.tilgungszuschuss = {int(k): d(v) for k, v in (tilgungszuschuss or {}).items()}
        self.rundung_art = rundung
        self.bank = bank
        self.foerder = foerder
        self.vfe_bis = bindung if vfe_bis is None else vfe_bis
        self.bereit_satz, self.bereit_frei = d(bereit_satz), bereit_frei
        # Zustand
        self.rest = NULL
        self.rate = None
        self.ausgezahlt = NULL
        self.hinweise = []
        self._erste_auszahlung = min(self.auszahlung)
        self._letzte_auszahlung = max(self.auszahlung)

    # ------------------------------------------------------------------ Hilfen
    def zins_der_periode(self, u):
        if self.bindung is not None and u > self.bindung and "zins_ohne_anschluss" not in FEHLER:
            if self.anschluss_zins is None:
                raise Meldung("M-24", f"{self.name}: Zinsbindung endet in Periode {self.bindung}, "
                                      "Anschlusszins fehlt (R-5.8: keine stille Fortschreibung)")
            return self.anschluss_zins
        return self.zins

    def _geld(self, rd, x):
        return rd.geld(x, self.rundung_art)

    @staticmethod
    def annuitaet(kapital, zins_periode, perioden):
        """R-5.4: Laufzeitannuitaet; bei Zins null gleichmaessige Tilgung (R-14.1)."""
        if zins_periode == 0:
            return kapital / perioden
        q = (EINS + zins_periode) ** perioden
        return kapital * zins_periode * q / (q - EINS)

    @staticmethod
    def restlaufzeit(restschuld, rate, zins_periode):
        """R-5.9 'Restlaufzeit bleibt': Zahl der Perioden, nach denen die bisherige Rate die Restschuld zum
        bisherigen Zins getilgt haette (reelle Zahl): m = ln(R / (R - S x i)) / ln(1 + i); bei Zins null S / R.
        None, wenn die Rate keine Tilgung enthaelt."""
        if rate <= restschuld * zins_periode:
            return None
        if zins_periode == 0:
            return restschuld / rate
        return (rate / (rate - restschuld * zins_periode)).ln() / (EINS + zins_periode).ln()

    # ------------------------------------------------------------------ eine Periode
    def periode(self, u, p, rd, letzte=False, liquiditaet=None):
        """Rechnet Periode u (0..N). p = Perioden je Jahr. Gibt die Zahlungen als dict zurueck.

        liquiditaet: frei verfuegbarer Betrag vor der Tilgung (nur Tilgungsart 'frei', R-5.7).
        letzte=True: nach der planmaessigen Rate wird die Restschuld abgeloest (R-8.6).
        """
        z = dict(auszahlung=NULL, einbehalt=NULL, zins=NULL, tilgung=NULL, beitrag=NULL,
                 tilgungszuschuss=NULL, abloesung=NULL, bereit=NULL, satz=NULL, rate=None)
        rest_vor = self.rest
        if u >= 1 and rest_vor > 0:
            satz = z["satz"] = self.zins_der_periode(u)
            # R-5.3 / R-12.5: Kapital x Satz, Division zuletzt, dann Rundung
            z["zins"] = self._geld(rd, rest_vor * satz / p)
            if self.beitrag_satz:
                z["beitrag"] = self._geld(rd, rest_vor * self.beitrag_satz / p)
            if u >= self.tilgungsbeginn:
                z["tilgung"] = self._tilgung(u, p, rd, rest_vor, z["zins"], satz, liquiditaet)
                z["rate"] = self.rate
        # R-5.18: Bereitstellungszins auf den am Ende der Vorperiode nicht ausgezahlten Betrag
        if self.bereit_satz and u >= 1 and u * 12 // p > self.bereit_frei and self.ausgezahlt < self.betrag:
            z["bereit"] = self._geld(rd, (self.betrag - self.ausgezahlt) * self.bereit_satz * 12 / p)
        if u in self.auszahlung:
            z["auszahlung"] = self.auszahlung[u]
            if u == self._erste_auszahlung:
                z["einbehalt"] = self.einbehalt
            self.ausgezahlt += z["auszahlung"]
        if u in self.tilgungszuschuss:
            z["tilgungszuschuss"] = min(self.tilgungszuschuss[u], rest_vor - z["tilgung"] + z["auszahlung"])
        self.rest = rest_vor + z["auszahlung"] - z["tilgung"] - z["tilgungszuschuss"]
        if letzte and u >= 1:
            z["abloesung"] = self.rest
            self.rest = NULL
        return z

    def _tilgung(self, u, p, rd, rest_vor, zins, satz, liquiditaet):
        k = u - self.tilgungsbeginn            # 0 = erste Tilgungsperiode
        anschluss_start = self.bindung is not None and u == self.bindung + 1
        nach_bindung = self.bindung is not None and u > self.bindung
        if self.art == "annuitaet_prozent":
            if self.rate is None:
                # R-5.4, R-5.10: Die erste Rate wird in der Periode des Tilgungsbeginns gebildet, aus dem Bezugsbetrag
                # und dem Zins dieser Periode. Liegt der Tilgungsbeginn nach dem Ende der Zinsbindung, ist das der
                # Anschlusszins mit dem Tilgungssatz der Anschlussfinanzierung; H-07 greift dann nicht.
                t = self.tilgungssatz
                if nach_bindung and self.anschluss_tilgung is not None:
                    t = self.anschluss_tilgung
                zins_rate = self.zins if "rate_ohne_anschluss" in FEHLER else satz
                self.rate = self._geld(rd, self.rate_betrag * (zins_rate + t) / p)
            elif anschluss_start:               # R-5.9
                self._neue_rate(p, rd, rest_vor, satz)
            return min(rest_vor, max(NULL, self.rate - zins))
        if self.art == "annuitaet_laufzeit":
            if self.rate is None:               # R-5.4, R-5.10: mit dem Zins der Periode des Tilgungsbeginns
                self.rate = self._geld(rd, self.annuitaet(self.betrag, satz / p, self.laufzeit))
            elif anschluss_start:
                rest_perioden = self.laufzeit - k
                self.rate = self._geld(rd, self.annuitaet(rest_vor, satz / p, rest_perioden))
            if k == self.laufzeit - 1:          # Schlussrate gleicht Rundungsreste aus
                return rest_vor
            return min(rest_vor, max(NULL, self.rate - zins))
        if self.art == "raten":
            if self.rate is None:
                self.rate = self._geld(rd, self.betrag / self.laufzeit)
            if k == self.laufzeit - 1:
                return rest_vor
            return min(rest_vor, self.rate)
        if self.art == "endfaellig":
            if self.laufzeit is not None and k == self.laufzeit - 1:
                return rest_vor
            return NULL
        if self.art == "frei":                  # R-5.7: der Periodenueberschuss tilgt
            return max(NULL, min(rest_vor, liquiditaet))
        raise ValueError(self.art)

    def _neue_rate(self, p, rd, rest_vor, satz_neu):
        regel = self.anschluss_regel
        t = self.anschluss_tilgung if self.anschluss_tilgung is not None else self.tilgungssatz
        if regel == "restlaufzeit":
            # R-5.9: Laufzeitannuitaet ueber die auf ganze Perioden abgerundete Restlaufzeit, mindestens eine
            ohne_tilgung = self.rate <= self._geld(rd, rest_vor * self.zins / p)
            m = None if ohne_tilgung else self.restlaufzeit(rest_vor, self.rate, self.zins / p)
            if m is None:                       # Rate ohne Tilgung: Rueckfall auf "Tilgungssatz bleibt" (M-40)
                self.hinweise.append("M-40")
                regel = "tilgungssatz"
            else:
                perioden = max(1, int(m.to_integral_value(ROUND_FLOOR)))
                self.rate = self._geld(rd, self.annuitaet(rest_vor, satz_neu / p, perioden))
                return
        if regel == "rate":
            # Rate bleibt; sie deckt mindestens die Zinsen (keine negative Tilgung)
            self.rate = max(self.rate, self._geld(rd, rest_vor * satz_neu / p))
        else:
            self.rate = self._geld(rd, rest_vor * (satz_neu + t) / p)


def kapitaldienst_kalkulatorisch(schuld, zins, tilgungssatz, p, rd):
    """R-5.12 (b): Kapitaldienst eines Jahres aus p kaufmaennisch gerundeten Raten auf die Schuld."""
    return p * rd.geld(schuld * (zins + tilgungssatz) / p)


def bemessungszins(vertragszins, bindung, kalk_zins, zeitraum, rd):
    """R-5.12 (b): Bemessungszins einer uebrigen Tranche: zeitgewichtetes Mittel aus dem Vertragszins bis zum Ende
    ihrer Zinsbindung und dem kalkulatorischen Zins danach, ueber den Bemessungszeitraum (beide in Perioden ab dem
    Stichtag); auf zwoelf Nachkommastellen (R-12.4). bindung None = fest bis zum Ende."""
    if bindung is None or bindung >= zeitraum:
        return vertragszins
    fest = max(0, bindung)
    return rd.satz((vertragszins * fest + kalk_zins * (zeitraum - fest)) / zeitraum)


def bemessungskapitaldienst(art, bezug, zins_b, mindesttilgung, p, rd, tilgungssatz=None, laufzeit=None,
                            beitrag_basis=NULL, beitrag_satz=NULL):
    """R-5.12 (b): kalkulatorischer Kapitaldienst einer uebrigen Tranche fuer ein Jahr: p-mal die Rate, die die
    Tranche nach ihrer Tilgungsart ab dem Tilgungsbeginn haette, gebildet mit dem Bemessungszins und mindestens
    der Mindesttilgung, je Rate kaufmaennisch gerundet; dazu der laufende Beitrag.

    art "annuitaet_prozent": Bezugsbetrag x (i_B + max(Tilgungssatz; H-04)) / p
        "raten":             Nennbetrag x (i_B + max(p / Tilgungsperioden; H-04)) / p
        "annuitaet_laufzeit": der groessere Wert aus der Annuitaet ueber die Tilgungsperioden zum Bemessungszins
                             und Nennbetrag x (i_B + H-04) / p
    """
    if art == "annuitaet_prozent":
        rate = rd.geld(bezug * (zins_b + max(tilgungssatz, mindesttilgung)) / p)
    elif art == "raten":
        rate = rd.geld(bezug * (zins_b + max(D(p) / D(laufzeit), mindesttilgung)) / p)
    elif art == "annuitaet_laufzeit":
        rate = max(rd.geld(Tranche.annuitaet(bezug, zins_b / p, laufzeit)), rd.geld(bezug * (zins_b + mindesttilgung) / p))
    else:
        raise ValueError(art)
    return p * rate + p * rd.geld(beitrag_basis * beitrag_satz / p)


def bankdarlehen(wertansatz, quote, ertrag_nachhaltig, mindestdeckung, zins_kalk, tilgung_kalk, mittelbedarf,
                 uebrige_darlehen=NULL, uebrige_im_beleihungsraum=None, kd_uebrige=NULL, zuschuesse=NULL,
                 ek_min=NULL, p=12, rd=None):
    """R-5.12: Hoehe des Bankdarlehens = kleinster Wert aus (a), (b), (c), nie negativ.

    (a) Beleihungsquote x Wertansatz abzueglich der uebrigen Darlehen, die den Beleihungsraum belegen (MA-026)
    (b) groesstes Darlehen, mit dem der nachhaltige Reinertrag den kalkulatorischen Kapitaldienst aller Darlehen
        mit der Mindestdeckung deckt (Festlegung: immer alle Darlehen)
    (c) Restfinanzierung = Mittelbedarf - uebrige Darlehen - Zuschuesse - Mindesteigenkapital
    Bei kalkulatorischem Zins plus Tilgung null ist (b) unbegrenzt, wenn der Ertrag die uebrigen Darlehen deckt.
    Rueckgabe: dict mit a, b (None = unbegrenzt), c, darlehen, eigenkapital, bindend (Liste), meldung.
    """
    from zahlen import Rundung
    rd = rd or Rundung("cent")
    im_raum = uebrige_darlehen if uebrige_im_beleihungsraum is None else uebrige_im_beleihungsraum
    a = quote * wertansatz - im_raum
    tragbar = ertrag_nachhaltig / mindestdeckung - kd_uebrige
    satz = zins_kalk + tilgung_kalk
    if satz == 0:
        b = None if tragbar >= 0 else NULL      # R-14.1: kein Kapitaldienst; (b) bindet nicht oder sperrt
    else:
        b = tragbar / satz
        if "bemessung_ohne_deckung" in FEHLER:      # Fehlerbild RF-16: Mindestdeckung vergessen
            b = ertrag_nachhaltig / satz
        elif b > 0:
            # sichere Seite: groesster Centbetrag, dessen gerundete Raten die Deckung einhalten
            b = ab_cent(b)
            while b > 0 and kapitaldienst_kalkulatorisch(b, zins_kalk, tilgung_kalk, p, rd) > tragbar:
                b -= D("0.01")
    c = mittelbedarf - uebrige_darlehen - zuschuesse - ek_min
    grenzen = {"a": a, "c": c}
    if b is not None:
        grenzen["b"] = b
    darlehen = max(NULL, ab_cent(min(grenzen.values())))
    meldung = "M-21" if (b is not None and b <= 0) else None
    if darlehen == 0:
        bindend = sorted(k for k, v in grenzen.items() if v <= 0)
    else:
        bindend = sorted(k for k, v in grenzen.items() if ab_cent(v) == darlehen)
    ek = mittelbedarf - uebrige_darlehen - zuschuesse - darlehen
    return dict(a=a, b=b, c=c, darlehen=darlehen, eigenkapital=ek, bindend=bindend, meldung=meldung,
                tragbar=tragbar, satz=satz)
