"""Zufallsfaelle mit zulaessigen Eingaben: sucht Abstuerze (kalkuliere endet mit Ausnahme) und Fehlalarme der Proben
(Status 'gesperrt' ohne eingeschleusten Fehler). Aufruf: python3 fuzz.py ANZAHL SAAT"""
import random
from h import *
from steuer import KOERPERSCHAFT, KOERPERSCHAFT_OHNE_GEWST, GEPRAEGTE_PG, GEWERBLICHE_PG, EINZELUNTERNEHMEN, PRIVAT, BEFREIT

STATUS = [KOERPERSCHAFT, KOERPERSCHAFT_OHNE_GEWST, GEPRAEGTE_PG, GEWERBLICHE_PG, EINZELUNTERNEHMEN, PRIVAT, BEFREIT]


def q(lo, hi, st=4):
    return D(str(round(random.uniform(lo, hi), st)))


def zufall_ankauf():
    fl = q(30, 5000, 2)
    leer = random.choice([NULL, NULL, q(0, float(fl), 2), fl])
    geb = random.choice([NULL, NULL, q(0, 1, 2), D(1)])
    n = random.choice([1, 2, 3, 5, 10, 11, 12, 15, 25, 42])
    ue = None
    if random.random() < 0.3:
        rs = q(1000, 3000000, 2)
        ue = dict(restschuld=rs, nennbetrag=rs * q(1, 1.5), zins=q(0, 0.08), tilgungssatz=q(0, 0.05),
                  bindung_jahre=random.choice([1, 3, 8, 15, 30]), foerderdarlehen=random.random() < 0.5,
                  rang=random.choice(["vor", "nach"]))
    ist = q(3, 20)
    st = A.steuer(random.choice(STATUS))
    if st.status in (KOERPERSCHAFT, GEPRAEGTE_PG) and random.random() < 0.3:
        st = replace(st, erweiterte_kuerzung=True)
    e = replace(ANK, kaufpreis=q(10000, 20000000, 0), wohnflaeche=fl, einheiten=random.randint(1, 80),
                ist_miete=ist, vergleichsmiete=q(3, 20), markt_miete=q(3, 25), leere_flaeche=leer,
                anpassungsdauer=random.randint(0, 20), haltedauer=n, zinsbindung_jahre=random.randint(1, 40),
                zins=q(0, 0.12), tilgungssatz=random.choice([None, q(0.02, 0.2)]), verkaufsfaktor=q(1, 40),
                enk_satz=q(0, 0.2), bodenanteil=q(0, 1, 2), baujahr=random.randint(1850, 2027),
                stau_betrag=random.choice([NULL, q(0, 3000000, 2)]), stau_jahr=random.randint(0, 45),
                stau_art=random.choice(["erhaltung", "modernisierung"]), gebunden_anteil=geb,
                bindung_jahre=random.randint(1, 50), gebundene_miete=random.choice([None, q(2, 15)]),
                uebernommen=ue, steuer=st, sonstige_ertraege=random.choice([NULL, q(0, 100000, 2)]),
                mietenhistorie=random.choice([None, (random.randint(0, 60), ist * q(0.5, 1))]),
                erbbauzins=random.choice([NULL, NULL, q(0, 200000, 2)]), erbbauzins_steigerung=q(-0.05, 0.15),
                verfuegbares_ek=None)
    return e


def zufall_vg():
    return replace(VG, leerstand=q(0, 0.6), forderungsausfall=q(0, 0.3), mietsteigerung=q(-0.05, 0.15),
                   kostensteigerung=q(-0.05, 0.15), baupreissteigerung=q(-0.05, 0.15), fluktuation=random.choice([NULL, q(0, 1)]),
                   beleihungsquote=q(0, 1), mindestdeckung=q(1, 2), mindesttilgung=random.choice([NULL, D("0.02")]),
                   anschluss_aufschlag=q(0, 0.03), anlaufleerstand=random.randint(0, 24), h_kurz=q(0, 0.06),
                   kk_zins=D("0.08"), anschluss_regel=random.choice(["tilgungssatz", "rate", "restlaufzeit"]),
                   kk_linie=random.choice([D(0), None, q(0, 500000, 2)]), ma037_vorsicht=random.random() < 0.7,
                   ma026_vertragszins=random.random() < 0.3, ma026_ertrag_vorhaben=random.random() < 0.2,
                   kalk_zins=random.choice([None, q(0, 0.1)]))


def zufall_neubau():
    f = None
    if random.random() < 0.5:
        f = replace(A.FOERDERUNG_B, darlehensquote=q(0, 0.6), zuschussquote=q(0, 0.3), eigenmittelquote=q(0, 0.2))
    kfw = random.choice([NULL, q(0, 1, 2)])
    einh = random.randint(1, 60)
    e = replace(NB, grundstueckspreis=q(10000, 8000000, 0), grundstuecksflaeche=q(100, 20000, 2), bodenrichtwert=q(10, 3000, 2),
                bgf=q(100, 10000, 2), kostenkennwert=q(1000, 5000, 2), bauzeit_monate=random.randint(1, 48),
                haltedauer=random.randint(6, 42), markt_miete=q(6, 25), wohnflaeche=q(80, 8000, 2), einheiten=einh,
                kfw_betrag=(kfw * einh * A.KFW.hoechstbetrag_je_einheit).quantize(D("0.01")), foerderung=f,
                zins=q(0, 0.1), zinsbindung_jahre=random.randint(1, 40), verkaufsfaktor=q(5, 35),
                stellplaetze=random.randint(0, 40), stellplatz_miete=q(0, 150, 2), steuer=A.steuer(random.choice(STATUS)))
    return e


if __name__ == "__main__":
    anzahl, saat = int(sys.argv[1]), int(sys.argv[2])
    random.seed(saat)
    zaehl = {}
    for i in range(anzahl):
        neubau = random.random() < 0.35
        e = zufall_neubau() if neubau else zufall_ankauf()
        vg = zufall_vg()
        stress = random.random() < 0.3
        p = 12 if (neubau or random.random() < 0.8) else 1
        s, r = kalk(e, vg, KATN if neubau else KAT, stress=stress, p=p)
        key = s if s != "eingabe" else "eingabe " + r[:4]
        zaehl[key] = zaehl.get(key, 0) + 1
        if s in ("ABSTURZ", "gesperrt"):
            print(f"--- Fall {i} ({'Neubau' if neubau else 'Ankauf'}, stress {stress}, p {p}): {s}")
            print("    ", r if s == "ABSTURZ" else r.befunde[:5])
            print("     EIN", e)
            print("     VG", {k: getattr(vg, k) for k in ("leerstand", "forderungsausfall", "mietsteigerung", "fluktuation", "beleihungsquote",
                                                     "mindestdeckung", "mindesttilgung", "anlaufleerstand", "anschluss_regel", "kk_linie",
                                                     "ma037_vorsicht", "ma026_vertragszins", "ma026_ertrag_vorhaben", "kalk_zins", "h_kurz",
                                                     "kostensteigerung", "baupreissteigerung", "anschluss_aufschlag")})
    print("Zaehlung", zaehl)
