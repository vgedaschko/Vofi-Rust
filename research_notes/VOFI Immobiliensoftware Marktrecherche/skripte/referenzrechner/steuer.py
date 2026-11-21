"""Kapitel 7 der Fachspezifikation: Steuer in Kurzform je Steuerstatus (R-7.1 bis R-7.19).

Die Steuer eines Planjahres haengt ab vom operativen Ergebnis e_op (Mieten abzueglich abziehbarer Kosten,
Abschreibung, Finanzierungskosten), den Habenzinsen z_h, dem Verkaufsgewinn g_v und, fuer die Hinzurechnung
(GEWSTG-8), von den Entgelten fuer Schulden und dem Erbbauzins. Steuersaetze, Freibetraege und Anteile sind
Katalogwerte oder Eingaben; in diesem Modul steht kein Satz als Festwert.
"""
from dataclasses import dataclass
from decimal import Decimal as D
from typing import Callable, Optional
from zahlen import NULL, EINS, d, abrunden_auf, FEHLER

KOERPERSCHAFT = "koerperschaft"                 # voll steuerpflichtige Koerperschaft
KOERPERSCHAFT_OHNE_GEWST = "koerperschaft_ohne_gewerbesteuer"   # Verein, Stiftung (GEWSTG-2)
GEPRAEGTE_PG = "gewerblich_gepraegte_personengesellschaft"      # ESTG-15; Kennzeichen der Kuerzung moeglich
GEWERBLICHE_PG = "originaer_gewerbliche_personengesellschaft"   # ohne Kennzeichen der Kuerzung
EINZELUNTERNEHMEN = "einzelunternehmen_bv"      # Einzelunternehmen mit Betriebsvermoegen; ohne Kennzeichen
PRIVAT = "privat"                               # Privatperson, vermoegensverwaltende Personengesellschaft
BEFREIT = "befreit"                             # befreite Koerperschaft: Satz null
LEHRBUCH = "lehrbuch"                           # ein pauschaler Satz; nur Referenzfaelle im Jahresmodus

PERSONENGESELLSCHAFT = (GEPRAEGTE_PG, GEWERBLICHE_PG)
PERSONENUNTERNEHMEN = (GEPRAEGTE_PG, GEWERBLICHE_PG, EINZELUNTERNEHMEN)
MIT_KENNZEICHEN = (KOERPERSCHAFT, GEPRAEGTE_PG)     # R-7.1: nur hier ist das Kennzeichen E-41 zulaessig
BETRIEBSVERMOEGEN = (KOERPERSCHAFT, GEPRAEGTE_PG, GEWERBLICHE_PG, EINZELUNTERNEHMEN)
# R-7.11, R-7.17: Ueberschusseinkuenfte nach dem Zahlungsprinzip (ESTG-11) mit der Frist des privaten Verkaufs
# (ESTG-23): Privatperson; Verein und Stiftung (KSTG-8, KSTG-1: nicht kraft Rechtsform gewerblich)
UEBERSCHUSS = (PRIVAT, KOERPERSCHAFT_OHNE_GEWST)


@dataclass
class Steuerparameter:
    """Aufgeloester Katalog- und Eingabestand fuer die Kurzform. Alle Saetze als Dezimalbruch."""
    status: str
    verlust: str = "vortrag"                    # H-38 (MA-016), fester Hauswert: "vortrag" (Voreinstellung) oder "sofort"
    # Koerperschaft (KSTG-23, SOLZG-4)
    kst_satz: Optional[Callable[[int], D]] = None   # Satz je Kalenderjahr
    soli_satz: D = NULL
    # Gewerbesteuer (GEWSTG-11, GEWSTG-16, GEWSTG-9)
    messzahl: D = NULL
    hebesatz: D = NULL                          # 4 = 400 %
    abrundung: D = NULL                         # Abrundung des Gewerbeertrags auf volle Betraege (GEWSTG-11)
    erweiterte_kuerzung: bool = False           # E-41
    kuerzung_bleibt_verkaufsjahr: bool = False  # E-69: es verbleibt weiterer Grundbesitz, oder Besitz, Nutzen und Lasten
                                                # gehen zum 31.12., 23:59 Uhr, ueber; nur dann bleibt die Kuerzung im
                                                # Verkaufsjahr (BFH-III-R-1-23, BFH-I-R-89-03; R-7.8)
    freibetrag: D = NULL                        # nur Personenunternehmen (GEWSTG-11)
    hinzu_anteil: D = NULL                      # GEWSTG-8: hinzugerechneter Anteil der Entgelte fuer Schulden
    hinzu_freibetrag: D = NULL                  # GEWSTG-8: Freibetrag der Hinzurechnung
    hinzu_pacht: D = NULL                       # GEWSTG-8: Anteil des Erbbauzinses, der als Entgelt zaehlt
    # Personen (ESTG-35, ESTG-23)
    est_satz: D = NULL                          # eingegebener Steuersatz einschliesslich Zuschlagsteuern
    zins_satz: Optional[D] = None               # Satz auf Habenzinsen (PRIVAT: ESTG-32D; LEHRBUCH); None = est_satz
    anrechnungsfaktor: D = NULL                 # Vielfaches des Messbetrags (ESTG-35)
    anteil_natuerliche: D = EINS                # Anteil natuerlicher Personen am Gewinn (R-7.9)
    aufgabegewinn: bool = False                 # MA-036, Lesart des Hauses: Objektverkauf ist Aufgabegewinn (GEWSTG-7)
    frist_privatverkauf: int = 0                # Jahre (ESTG-23)
    haltedauer: int = 0
    sockel_verlust: Optional[D] = None          # ESTG-10D, GEWSTG-10A: Sockelbetrag; nur fuer den Hinweis M-45
    # Lehrbuch
    satz: D = NULL
    verkaufsgewinn_pflichtig: bool = True


class Steuer:
    """Steuerliche Nebenrechnung mit Verlustvortrag als Zustand (R-7.5).

    alternative=True: Besteuerung der Unterlassensalternative (R-9.5). Sie verwaltet nur Kapital: Das Kennzeichen
    der erweiterten Kuerzung wirkt fuer sie nicht.
    """

    def __init__(self, par: Steuerparameter, raster, rd, alternative=False):
        self.par, self.raster, self.rd = par, raster, rd
        self.alternative = alternative
        self.vv = NULL          # Verlustvortrag Einkommen-/Koerperschaftsteuer
        self.vv_gew = NULL      # Verlustvortrag Gewerbesteuer (GEWSTG-10A)
        self.protokoll = []
        self.hinweise = set()
        self._jahr = None

    # ------------------------------------------------------------- Grenzsaetze fuer Kennzahlen (R-7.14)
    def _kuerzung(self):
        p = self.par
        # R-7.8 (BFH-III-R-1-23): Im Verkaufsjahr entfaellt die erweiterte Kuerzung ganz, ausser sie bleibt nach E-69
        # erhalten; dann ist nach GEWSTR-9-2 auch der Verkaufsgewinn gekuerzt (strengere Lesart: MA-030)
        if self._jahr is not None and self._jahr == p.haltedauer and not p.kuerzung_bleibt_verkaufsjahr:
            return False
        return p.erweiterte_kuerzung and not self.alternative

    def _gew_voll(self):
        return self.par.messzahl * self.par.hebesatz

    def _anrechnung_voll(self):
        """Grenzwirkung der Anrechnung je Euro Gewerbeertrag (ohne Freibetrag und Hoechstbetrag)."""
        p = self.par
        anteil = EINS if p.status == EINZELUNTERNEHMEN else p.anteil_natuerliche
        return anteil * p.messzahl * min(p.anrechnungsfaktor, p.hebesatz)

    def _grenzsatz(self, j, gewerbesteuer):
        p = self.par
        if p.status == BEFREIT:
            return NULL
        if p.status == LEHRBUCH:
            return p.satz
        if p.status == KOERPERSCHAFT_OHNE_GEWST:
            return p.kst_satz(self.raster.kalenderjahr(j)) * (EINS + p.soli_satz)
        if p.status == KOERPERSCHAFT:
            return p.kst_satz(self.raster.kalenderjahr(j)) * (EINS + p.soli_satz) + (self._gew_voll() if gewerbesteuer else NULL)
        if p.status in PERSONENUNTERNEHMEN:
            return p.est_satz + ((self._gew_voll() - self._anrechnung_voll()) if gewerbesteuer else NULL)
        return p.est_satz

    def grenzsatz_operativ(self, j):
        """s_op(j): bei gesetztem Kennzeichen der Kuerzung ohne Gewerbesteuer."""
        return self._grenzsatz(j, not self._kuerzung())

    def grenzsatz_zinsen(self, j):
        """s_Z(j): Zinsertraege bleiben auch bei gesetztem Kennzeichen gewerbesteuerpflichtig (GEWSTG-9)."""
        p = self.par
        if p.status in (PRIVAT, LEHRBUCH):
            return p.zins_satz if p.zins_satz is not None else (p.satz if p.status == LEHRBUCH else p.est_satz)
        return self._grenzsatz(j, True)

    def grenzsatz_sollzinsen(self, j):
        """s_FK(j): Entlastung je Euro Sollzins; bei sofortiger Verrechnung um die Hinzurechnung gemindert."""
        p = self.par
        s = self.grenzsatz_operativ(j)
        if p.verlust == "sofort" and not self._kuerzung() and p.status in (KOERPERSCHAFT, EINZELUNTERNEHMEN):
            s -= p.hinzu_anteil * (self._gew_voll() - (self._anrechnung_voll() if p.status == EINZELUNTERNEHMEN else NULL))
        return s

    # ------------------------------------------------------------- Verlustvortrag
    def _nach_vortrag(self, ergebnis, topf, teile):
        """R-7.5: Verlust erhoeht den Vortrag; Gewinn wird bis zur Hoehe des Vortrags verrechnet."""
        vv = getattr(self, topf)
        zugang = max(-ergebnis, NULL)
        genutzt = min(vv, max(ergebnis, NULL))
        if "vortrag_nicht_verbraucht" in FEHLER:    # Fehlerbild RF-16
            genutzt = NULL
        setattr(self, topf, vv + zugang - genutzt)
        teile[topf + "_anfang"], teile[topf + "_zugang"], teile[topf + "_genutzt"] = vv, zugang, genutzt
        sockel = self.par.sockel_verlust
        if sockel is not None and genutzt > sockel:
            self.hinweise.add("M-45")
        return max(ergebnis, NULL) - genutzt

    def _gewerbeertrag(self, e_op, z_h, g_v, entgelte, pacht, freibetrag_verbraucht, teile):
        """R-7.8, R-7.16: Gewerbeertrag vor Verlustvortrag, Abrundung und Freibetrag."""
        p = self.par
        g_gew = g_v
        if p.aufgabegewinn and p.status in PERSONENGESELLSCHAFT:      # MA-036, andere Lesart (GEWSTG-7)
            g_gew = g_v * (EINS - p.anteil_natuerliche)
        if self._kuerzung():
            # GEWSTG-9: gekuerzt wird der Ertrag aus Verwaltung und Nutzung des eigenen Grundbesitzes samt der
            # darauf entfallenden Hinzurechnung; Zinsertraege bleiben, der Verkaufsgewinn nach MA-030
            hinzu = NULL
            ertrag = z_h                             # MA-030: der Verkaufsgewinn ist mitgekuerzt (GEWSTR-9-2)
        else:
            frei = NULL if freibetrag_verbraucht else p.hinzu_freibetrag
            hinzu = p.hinzu_anteil * max(NULL, entgelte + p.hinzu_pacht * pacht - frei)
            ertrag = e_op + z_h + g_gew + hinzu
        teile["hinzurechnung"] = hinzu
        teile["gewerbeertrag"] = ertrag         # nach Hinzurechnung und Kuerzung, vor dem Verlustvortrag (GEWSTG-10A)
        return ertrag

    # ------------------------------------------------------------- Jahressteuer
    def jahr(self, j, e_op, z_h, g_v=NULL, entgelte=NULL, pacht=NULL, vfe_verkauf=NULL):
        """Steuerzahlung des Planjahres j (positiv = Zahlung, negativ = Erstattung).

        entgelte: im Jahr abgezogene Entgelte fuer Schulden; pacht: Erbbauzins des Jahres (beide fuer GEWSTG-8).
        vfe_verkauf: Vorfaelligkeitsentschaedigung der Privatperson (Veraeusserungskosten, R-7.11).
        """
        p, g = self.par, self.rd.geld
        self._jahr = j
        teile = dict(jahr=j, e_op=e_op, z_h=z_h, g_v=g_v, entgelte=entgelte, pacht=pacht, vfe_verkauf=vfe_verkauf,
                     vv_anfang=self.vv, vv_zugang=NULL, vv_genutzt=NULL,
                     vv_gew_anfang=self.vv_gew, vv_gew_zugang=NULL, vv_gew_genutzt=NULL, arten={}, anrechnung=NULL)
        arten = teile["arten"]
        sofort = p.verlust == "sofort"
        if p.status == BEFREIT:
            pass
        elif p.status == LEHRBUCH:
            sz = p.zins_satz if p.zins_satz is not None else p.satz
            basis = e_op + (g_v if p.verkaufsgewinn_pflichtig else NULL)
            if sofort:
                steuer = p.satz * basis + sz * z_h
            elif sz == p.satz:
                steuer = p.satz * self._nach_vortrag(basis + z_h, "vv", teile)
            else:
                steuer = p.satz * self._nach_vortrag(basis, "vv", teile) + sz * z_h
            arten["lehrbuch"] = g(steuer)
        elif p.status in (KOERPERSCHAFT, KOERPERSCHAFT_OHNE_GEWST):
            kj = self.raster.kalenderjahr(j) + (1 if "steuerjahr_falsch" in FEHLER else 0)   # Fehlerbild RF-16
            kst = p.kst_satz(kj) * (EINS + p.soli_satz)
            einkommen = e_op + z_h + g_v
            mit_gew = p.status == KOERPERSCHAFT and not (self.alternative and "alternative_ohne_gewerbesteuer" in FEHLER)
            if p.status == KOERPERSCHAFT_OHNE_GEWST:
                # R-7.17 (KSTG-8, KSTG-1): Einkuenfte aus Vermietung und Kapital; der Verkauf ist nur innerhalb der
                # Frist des privaten Verkaufs steuerpflichtig (ESTG-23), die Vorfaelligkeit gehoert zum Verkauf
                pflichtig = p.haltedauer <= p.frist_privatverkauf
                gewinn = g_v - vfe_verkauf
                zusatz = gewinn if (pflichtig and gewinn > 0) else NULL
                einkommen = e_op + z_h + zusatz
                teile.update(verkauf_pflichtig=pflichtig, verkaufsgewinn_steuerlich=zusatz)
            ertrag = self._gewerbeertrag(e_op, z_h, g_v, entgelte, pacht, sofort, teile) if mit_gew else NULL
            if sofort:                          # R-7.6: lineare Steuer, Erstattung bei Verlust
                arten["koerperschaftsteuer"] = g(kst * einkommen)
                arten["gewerbesteuer"] = g(self._gew_voll() * ertrag) if mit_gew else NULL
            else:
                arten["koerperschaftsteuer"] = g(kst * self._nach_vortrag(einkommen, "vv", teile))
                arten["gewerbesteuer"] = NULL
                if mit_gew:
                    abgerundet = abrunden_auf(self._nach_vortrag(ertrag, "vv_gew", teile), p.abrundung)
                    arten["gewerbesteuer"] = g(abgerundet * p.messzahl * p.hebesatz)
        elif p.status in PERSONENUNTERNEHMEN:
            gewinn = e_op + z_h + g_v
            anteil = EINS if p.status == EINZELUNTERNEHMEN else p.anteil_natuerliche
            pg = p.status in PERSONENGESELLSCHAFT
            # R-7.6 (GEWSTG-10A): Die Personengesellschaft traegt ihren Gewerbeverlust auch bei sofortiger
            # Verrechnung selbst vor; nur beim Einzelunternehmen ist die Gewerbesteuer dann linear.
            gew_linear = sofort and not pg
            ertrag = self._gewerbeertrag(e_op, z_h, g_v, entgelte, pacht, gew_linear, teile)
            if sofort:
                est = g(p.est_satz * gewinn)
            else:
                est = g(p.est_satz * self._nach_vortrag(gewinn, "vv", teile))
            if gew_linear:
                messbetrag = NULL
                gew = g(self._gew_voll() * ertrag)
                anr = g(anteil * p.messzahl * min(p.anrechnungsfaktor, p.hebesatz) * ertrag)
            else:
                abgerundet = max(NULL, abrunden_auf(self._nach_vortrag(ertrag, "vv_gew", teile), p.abrundung) - p.freibetrag)
                messbetrag = g(abgerundet * p.messzahl)
                gew = g(messbetrag * p.hebesatz)
                # R-7.9 (ESTG-35): Vielfaches des anteiligen Messbetrags, hoechstens die anteilige Gewerbesteuer,
                # im Vortragsmodus hoechstens die anteilige Einkommensteuer des Jahres
                grenzen = [anteil * p.anrechnungsfaktor * messbetrag, anteil * gew]
                if not sofort:
                    grenzen.append(anteil * est)
                anr = g(min(grenzen))
            arten["einkommensteuer"], arten["gewerbesteuer"] = est, gew
            teile.update(anrechnung=anr, messbetrag=messbetrag)
        elif p.status == PRIVAT:
            sz = p.zins_satz if p.zins_satz is not None else p.est_satz
            pflichtig = p.haltedauer <= p.frist_privatverkauf       # R-7.11 (ESTG-23)
            gewinn = g_v - vfe_verkauf              # R-7.11: die Vorfaelligkeit ist Veraeusserungskosten (MA-032)
            zusatz = gewinn if (pflichtig and gewinn > 0) else NULL
            # R-7.11 (ESTG-10D): der steuerpflichtige Verkaufsgewinn wird mit dem Vermietungsergebnis und dem
            # Verlustvortrag verrechnet; ein Verlust aus dem Verkauf bleibt unberuecksichtigt
            if sofort:
                verm = g(p.est_satz * (e_op + zusatz))
            else:
                verm = g(p.est_satz * self._nach_vortrag(e_op + zusatz, "vv", teile))
            arten["vermietung_und_verkauf"] = verm
            arten["kapital"] = g(sz * z_h)
            teile.update(verkauf_pflichtig=pflichtig, verkaufsgewinn_steuerlich=zusatz)
        else:
            raise ValueError(p.status)
        steuer = sum(arten.values(), NULL) - teile["anrechnung"]
        teile.update(steuer=steuer, vv=self.vv, vv_gew=self.vv_gew)
        teile.update(arten)
        self.protokoll.append(teile)
        return steuer
