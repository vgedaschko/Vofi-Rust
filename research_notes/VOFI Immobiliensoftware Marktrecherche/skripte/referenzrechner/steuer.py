"""Kapitel 7 der Fachspezifikation: Steuer in Kurzform je Steuerstatus (R-7.1 bis R-7.14).

Die Steuer eines Planjahres haengt von drei Groessen ab: dem operativen Ergebnis e_op (Mieten abzueglich
abziehbarer Kosten, Abschreibung, Soll- und Kontokorrentzinsen, Finanzierungskosten), den Habenzinsen
z_h und dem Verkaufsgewinn g_v. Steuersaetze sind Katalogwerte oder Eingaben; in diesem Modul steht
kein Satz als Festwert.
"""
from dataclasses import dataclass, field
from decimal import Decimal as D
from typing import Callable, Optional
from zahlen import NULL, EINS, d, ab_hundert

KOERPERSCHAFT = "koerperschaft"                 # voll steuerpflichtige Koerperschaft
GEWERBLICHE_PG = "gewerbliche_personengesellschaft"   # auch gewerblich gepraegt (ESTG-15)
EINZELUNTERNEHMEN = "einzelunternehmen_bv"      # Einzelunternehmen mit Betriebsvermoegen
PRIVAT = "privat"                               # Privatperson, vermoegensverwaltende Personengesellschaft
BEFREIT = "befreit"                             # befreite Koerperschaft: Satz null
LEHRBUCH = "lehrbuch"                           # ein pauschaler Satz; nur Referenzfaelle im Jahresmodus


@dataclass
class Steuerparameter:
    """Aufgeloester Katalog- und Eingabestand fuer die Kurzform. Alle Saetze als Dezimalbruch."""
    status: str
    verlust: str = "vortrag"                    # MA-016: "vortrag" (Voreinstellung) oder "sofort"
    # Koerperschaft (KSTG-23, SOLZG-4)
    kst_satz: Optional[Callable[[int], D]] = None   # Satz je Kalenderjahr
    soli_satz: D = NULL
    # Gewerbesteuer (GEWSTG-11, GEWSTG-16, GEWSTG-9)
    messzahl: D = NULL
    hebesatz: D = NULL                          # 4 = 400 %
    erweiterte_kuerzung: bool = False
    freibetrag: D = NULL                        # nur Personenunternehmen (GEWSTG-11)
    # Personen (ESTG-35, ESTG-23)
    est_satz: D = NULL                          # eingegebener Steuersatz einschliesslich Zuschlagsteuern
    zins_satz: Optional[D] = None               # Satz auf Habenzinsen (PRIVAT, LEHRBUCH); None = est_satz
    anrechnungsfaktor: D = NULL                 # Vielfaches des Messbetrags (ESTG-35)
    anteil_natuerliche: D = EINS                # Anteil natuerlicher Personen am Gewinn (R-7.9)
    frist_privatverkauf: int = 0                # Jahre (ESTG-23)
    haltedauer: int = 0
    # Lehrbuch
    satz: D = NULL
    verkaufsgewinn_pflichtig: bool = True


class Steuer:
    """Steuerliche Nebenrechnung mit Verlustvortrag als Zustand (R-7.5)."""

    def __init__(self, par: Steuerparameter, raster, rd):
        self.par, self.raster, self.rd = par, raster, rd
        self.vv = NULL          # Verlustvortrag Einkommen-/Koerperschaftsteuer
        self.vv_gew = NULL      # Verlustvortrag Gewerbesteuer (GEWSTG-10A)
        self.protokoll = []

    # ------------------------------------------------------------- Grenzsaetze fuer Kennzahlen
    def _gew_satz(self):
        p = self.par
        return NULL if p.erweiterte_kuerzung else p.messzahl * p.hebesatz

    def _anrechnung_satz(self):
        """Grenzwirkung der Anrechnung je Euro Gewerbeertrag (ohne Freibetrag und Hoechstbetrag)."""
        p = self.par
        if p.erweiterte_kuerzung:
            return NULL
        return p.anteil_natuerliche * p.messzahl * min(p.anrechnungsfaktor, p.hebesatz)

    def grenzsatz_operativ(self, j):
        p = self.par
        if p.status == BEFREIT:
            return NULL
        if p.status == LEHRBUCH:
            return p.satz
        if p.status == KOERPERSCHAFT:
            return p.kst_satz(self.raster.kalenderjahr(j)) * (EINS + p.soli_satz) + self._gew_satz()
        if p.status in (GEWERBLICHE_PG, EINZELUNTERNEHMEN):
            return p.est_satz + self._gew_satz() - self._anrechnung_satz()
        return p.est_satz

    def grenzsatz_zinsen(self, j):
        """R-10.4: Steuersatz auf Zinsertraege fuer den Vergleichsfaktor der Rendite."""
        p = self.par
        if p.status in (PRIVAT, LEHRBUCH):
            return p.zins_satz if p.zins_satz is not None else (p.satz if p.status == LEHRBUCH else p.est_satz)
        return self.grenzsatz_operativ(j)

    # ------------------------------------------------------------- Verlustvortrag
    def _nach_vortrag(self, ergebnis, topf):
        """R-7.5: Verlust erhoeht den Vortrag; Gewinn wird bis zur Hoehe des Vortrags verrechnet."""
        vv = getattr(self, topf)
        if ergebnis < 0:
            setattr(self, topf, vv - ergebnis)
            return NULL
        genutzt = min(vv, ergebnis)
        setattr(self, topf, vv - genutzt)
        return ergebnis - genutzt

    # ------------------------------------------------------------- Jahressteuer
    def jahr(self, j, e_op, z_h, g_v=NULL):
        """Steuerzahlung des Planjahres j (positiv = Zahlung, negativ = Erstattung)."""
        p, g = self.par, self.rd.geld
        teile = dict(jahr=j, e_op=e_op, z_h=z_h, g_v=g_v)
        if p.status == BEFREIT:
            steuer = NULL
        elif p.status == LEHRBUCH:
            sz = p.zins_satz if p.zins_satz is not None else p.satz
            basis = e_op + (g_v if p.verkaufsgewinn_pflichtig else NULL)
            if p.verlust == "sofort":
                steuer = p.satz * basis + sz * z_h
            elif sz == p.satz:
                steuer = p.satz * self._nach_vortrag(basis + z_h, "vv")
            else:
                steuer = p.satz * self._nach_vortrag(basis, "vv") + sz * z_h
            steuer = g(steuer)
        elif p.status == KOERPERSCHAFT:
            kst = p.kst_satz(self.raster.kalenderjahr(j)) * (EINS + p.soli_satz)
            einkommen = e_op + z_h + g_v
            if p.verlust == "sofort":           # R-7.6: lineare Steuer, Erstattung bei Verlust
                koerp, gew = g(kst * einkommen), g(self._gew_satz() * einkommen)
            else:
                koerp = g(kst * self._nach_vortrag(einkommen, "vv"))
                gew = NULL
                if not p.erweiterte_kuerzung:
                    ertrag = ab_hundert(self._nach_vortrag(einkommen, "vv_gew"))
                    gew = g(ertrag * p.messzahl * p.hebesatz)
            teile.update(koerperschaftsteuer=koerp, gewerbesteuer=gew)
            steuer = koerp + gew
        elif p.status in (GEWERBLICHE_PG, EINZELUNTERNEHMEN):
            gewinn = e_op + z_h + g_v
            anteil = EINS if p.status == EINZELUNTERNEHMEN else p.anteil_natuerliche
            if p.verlust == "sofort":
                est = g(p.est_satz * gewinn)
                gew = g(self._gew_satz() * gewinn)
                anr = g(self._anrechnung_satz() * gewinn)
                messbetrag = NULL
            else:
                est = g(p.est_satz * self._nach_vortrag(gewinn, "vv"))
                gew = anr = messbetrag = NULL
                if not p.erweiterte_kuerzung:
                    ertrag = max(NULL, ab_hundert(self._nach_vortrag(gewinn, "vv_gew")) - p.freibetrag)
                    messbetrag = g(ertrag * p.messzahl)
                    gew = g(messbetrag * p.hebesatz)
                    # R-7.9: Vierfaches des anteiligen Messbetrags, hoechstens die anteilige
                    # Gewerbesteuer, hoechstens die anteilige Einkommensteuer des Jahres (ESTG-35)
                    anr = g(min(anteil * p.anrechnungsfaktor * messbetrag, anteil * gew, anteil * est))
            teile.update(einkommensteuer=est, gewerbesteuer=gew, anrechnung=anr, messbetrag=messbetrag)
            steuer = est + gew - anr
        elif p.status == PRIVAT:
            sz = p.zins_satz if p.zins_satz is not None else p.est_satz
            if p.verlust == "sofort":
                verm = g(p.est_satz * e_op)
            else:
                verm = g(p.est_satz * self._nach_vortrag(e_op, "vv"))
            kap = g(sz * z_h)
            pflichtig = p.haltedauer <= p.frist_privatverkauf       # R-7.11 (ESTG-23)
            verk = g(p.est_satz * g_v) if (pflichtig and g_v > 0) else NULL
            teile.update(vermietung=verm, kapital=kap, verkauf=verk, verkauf_pflichtig=pflichtig)
            steuer = verm + kap + verk
        else:
            raise ValueError(p.status)
        teile.update(steuer=steuer, vv=self.vv, vv_gew=self.vv_gew)
        self.protokoll.append(teile)
        return steuer
