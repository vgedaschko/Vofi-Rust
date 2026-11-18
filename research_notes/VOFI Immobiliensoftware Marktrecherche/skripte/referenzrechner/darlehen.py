"""Kapitel 5 der Fachspezifikation: Darlehen (R-5.1 bis R-5.16).

Eine Tranche fuehrt ihren Plan Periode fuer Periode; der Finanzplan (finanzplan.py) ruft sie auf.
Zinsen einer Periode haengen nur von der Restschuld der Vorperiode ab (R-4.2).
"""
from decimal import Decimal as D
from zahlen import NULL, EINS, d, ab_cent

ARTEN = ("annuitaet_prozent", "annuitaet_laufzeit", "raten", "endfaellig", "frei")
ANSCHLUSSREGELN = ("tilgungssatz", "rate", "restlaufzeit")


class Tranche:
    """Eine Kredittranche (Bankdarlehen, Foerderdarlehen, uebernommenes Darlehen).

    betrag            Nennbetrag (bei uebernommenem Darlehen die Restschuld am Stichtag)
    art               Tilgungsart, siehe ARTEN
    zins              nominaler Jahreszins waehrend der Zinsbindung (R-5.2)
    tilgungssatz      anfaenglicher Tilgungssatz je Jahr (nur annuitaet_prozent)
    laufzeit          Zahl der Tilgungsperioden (annuitaet_laufzeit, raten)
    auszahlung        {Periode: Betrag}; Voreinstellung alles in Periode 0
    einbehalt         bei der ersten Auszahlung einbehaltener Betrag (Disagio, Entgelt), R-5.14
    tilgungsbeginn    Periode der ersten Tilgung (Voreinstellung 1)
    bindung           Zahl der Perioden mit festem Zins ab Stichtag (None = bis zum Ende)
    anschluss_zins    nominaler Jahreszins nach der Bindung (R-5.8)
    anschluss_regel   "tilgungssatz" (Voreinstellung), "rate" oder "restlaufzeit" (R-5.9)
    anschluss_tilgung Tilgungssatz der Anschlussfinanzierung (Voreinstellung: der anfaengliche)
    beitrag_satz      laufender Beitrag je Jahr auf die Restschuld (Verwaltungskostenbeitrag), R-5.13
    tilgungszuschuss  {Periode: Betrag} Minderung der Restschuld ohne Geldfluss, R-5.15
    rundung           "kaufm" (Voreinstellung), "ab" oder "keine" je Darlehen (MA-013)
    bank              True fuer das Bankdarlehen der Regel R-5.12, False fuer uebrige Darlehen
    """

    def __init__(self, name, betrag, art, zins, tilgungssatz=None, laufzeit=None, auszahlung=None,
                 einbehalt=0, tilgungsbeginn=1, bindung=None, anschluss_zins=None,
                 anschluss_regel="tilgungssatz", anschluss_tilgung=None, beitrag_satz=0,
                 tilgungszuschuss=None, rundung="kaufm", bank=True, vfe_pflichtig=True):
        assert art in ARTEN and anschluss_regel in ANSCHLUSSREGELN
        self.name, self.betrag, self.art = name, d(betrag), art
        self.zins = d(zins)
        self.tilgungssatz = None if tilgungssatz is None else d(tilgungssatz)
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
        self.vfe_pflichtig = vfe_pflichtig      # R-5.16: Foerderdarlehen ohne Vorfaelligkeitsentschaedigung
        # Zustand
        self.rest = NULL
        self.rate = None
        self.ausgezahlt = NULL
        self._erste_auszahlung = min(self.auszahlung)

    # ------------------------------------------------------------------ Hilfen
    def zins_der_periode(self, u):
        if self.bindung is not None and u > self.bindung:
            if self.anschluss_zins is None:
                raise ValueError(f"M-24: {self.name}: Zinsbindung endet in Periode {self.bindung}, "
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
    def laufzeit_prozentannuitaet(zins_periode, tilgung_periode):
        """Rechnerische Gesamtlaufzeit einer Prozentannuitaet in Perioden (reelle Zahl), fuer R-5.9 'restlaufzeit':
        n = ln((i + t) / t) / ln(1 + i); bei Zins null n = 1 / t."""
        if zins_periode == 0:
            return EINS / tilgung_periode
        return ((zins_periode + tilgung_periode) / tilgung_periode).ln() / (EINS + zins_periode).ln()

    # ------------------------------------------------------------------ eine Periode
    def periode(self, u, p, rd, letzte=False, liquiditaet=None):
        """Rechnet Periode u (0..N). p = Perioden je Jahr. Gibt die Zahlungen als dict zurueck.

        liquiditaet: frei verfuegbarer Betrag vor der Tilgung (nur Tilgungsart 'frei', R-5.7).
        letzte=True: nach der planmaessigen Rate wird die Restschuld abgeloest (R-8.6).
        """
        z = dict(auszahlung=NULL, einbehalt=NULL, zins=NULL, tilgung=NULL, beitrag=NULL,
                 tilgungszuschuss=NULL, abloesung=NULL)
        rest_vor = self.rest
        if u >= 1 and rest_vor > 0:
            satz = self.zins_der_periode(u)
            # R-5.3 / R-12.5: Kapital x Satz, Division zuletzt, dann Rundung
            z["zins"] = self._geld(rd, rest_vor * satz / p)
            if self.beitrag_satz:
                z["beitrag"] = self._geld(rd, rest_vor * self.beitrag_satz / p)
            if u >= self.tilgungsbeginn:
                z["tilgung"] = self._tilgung(u, p, rd, rest_vor, z["zins"], satz, liquiditaet)
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
        if self.art == "annuitaet_prozent":
            if self.rate is None:               # R-5.4: Rate aus dem Nennbetrag, einmal gerundet
                self.rate = self._geld(rd, self.betrag * (self.zins + self.tilgungssatz) / p)
                self._rate0, self._zins0 = self.rate, self.zins
            if anschluss_start:                 # R-5.9
                self._neue_rate(p, rd, rest_vor, satz)
            return min(rest_vor, max(NULL, self.rate - zins))
        if self.art == "annuitaet_laufzeit":
            if self.rate is None:
                self.rate = self._geld(rd, self.annuitaet(self.betrag, self.zins / p, self.laufzeit))
            if anschluss_start:
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
        if regel == "rate":
            # Rate bleibt; sie deckt mindestens die Zinsen (keine negative Tilgung)
            self.rate = max(self.rate, self._geld(rd, rest_vor * satz_neu / p))
        elif regel == "tilgungssatz":
            t = self.anschluss_tilgung if self.anschluss_tilgung is not None else self.tilgungssatz
            self.rate = self._geld(rd, rest_vor * (satz_neu + t) / p)
        else:                                   # restlaufzeit: Volltilgung zum urspruenglichen Termin
            gesamt = self.laufzeit_prozentannuitaet(self._zins0 / p, self.tilgungssatz / p)
            rest_perioden = max(EINS, gesamt - D(self.bindung - self.tilgungsbeginn + 1))
            ip = satz_neu / p
            if ip == 0:
                self.rate = self._geld(rd, rest_vor / rest_perioden)
            else:
                q = (EINS + ip) ** rest_perioden
                self.rate = self._geld(rd, rest_vor * ip * q / (q - EINS))


def kapitaldienst_prozentannuitaet(betrag, zins, tilgungssatz, p, rd):
    """Kapitaldienst eines Jahres der Tilgungsphase: p x gerundete Rate (R-5.12 b)."""
    return p * rd.geld(betrag * (zins + tilgungssatz) / p)


def bankdarlehen(wertansatz, quote, reinertrag_vj, mindestdeckung, zins, tilgungssatz, mittelbedarf,
                 uebrige_darlehen=NULL, kd_uebrige=NULL, zuschuesse=NULL, ek_min=NULL,
                 nur_eigenes=False, p=12, rd=None):
    """R-5.12: Hoehe des Bankdarlehens = kleinster Wert aus (a), (b), (c), nie negativ (MA-026).

    (a) Beleihungsquote x Wertansatz abzueglich der uebrigen Darlehen
    (b) groesstes Darlehen, mit dem der Kapitaldienst aller Darlehen die Mindestdeckung im ersten
        Jahr der Vollvermietung einhaelt
    (c) Restfinanzierung = Mittelbedarf - uebrige Darlehen - Zuschuesse - Mindesteigenkapital
    nur_eigenes=True: andere Lesart von MA-026 (Quote und Deckung nur fuer das eigene Darlehen).
    Rueckgabe: dict mit a, b, c, darlehen, eigenkapital, bindend (Liste), meldung.
    """
    from zahlen import Rundung
    rd = rd or Rundung("cent")
    a = quote * wertansatz - (NULL if nur_eigenes else uebrige_darlehen)
    tragbar = reinertrag_vj / mindestdeckung - (NULL if nur_eigenes else kd_uebrige)
    b = tragbar / (zins + tilgungssatz)
    if b > 0:
        # sichere Seite: groesster Centbetrag, dessen gerundete Raten die Deckung einhalten
        b = ab_cent(b)
        while b > 0 and kapitaldienst_prozentannuitaet(b, zins, tilgungssatz, p, rd) > tragbar:
            b -= D("0.01")
    c = mittelbedarf - uebrige_darlehen - zuschuesse - ek_min
    kleinster = min(a, b, c)
    darlehen = max(NULL, ab_cent(kleinster))
    meldung = "M-21" if b <= 0 else None    # Reinertrag deckt den Kapitaldienst der uebrigen Darlehen nicht
    grenzen = {"a": a, "b": b, "c": c}
    if darlehen == 0:
        bindend = [k for k, v in grenzen.items() if v <= 0]
    else:
        bindend = [k for k, v in grenzen.items() if ab_cent(v) == darlehen]
    ek = mittelbedarf - uebrige_darlehen - zuschuesse - darlehen
    return dict(a=a, b=b, c=c, darlehen=darlehen, eigenkapital=ek, bindend=bindend, meldung=meldung)
