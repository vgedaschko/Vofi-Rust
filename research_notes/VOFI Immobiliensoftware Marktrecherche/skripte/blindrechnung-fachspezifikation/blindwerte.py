# -*- coding: utf-8 -*-
"""Blindrechnung zur Fachspezifikation Rechenkern, Stand 2026-11-21 (Pruefrunde 3).
Ein Lauf gibt alle nachgerechneten Werte mit Sollwert aus, danach die Zaehlung je Fall, die Abweichungen,
die Zahlen zu den offenen Lesarten und eigene Werte ohne Sollwert im Dokument.

    python3 blindwerte.py            alle Werte
    python3 blindwerte.py --kurz     nur Abweichungen, Zaehlung, Lesarten, eigene Werte

Quelle ist allein docs/fachspezifikation-rechenkern.md. Der Stand nach Pruefrunde 1 liegt in stand-runde2/."""
import sys
import io
import contextlib
from kern import *
import rf06, rf11, rf11b, rf11g, rf13, rf12, rf12k, rf12f, rf17, extra, lesarten


def z(name, R):
    print(f"   {name:58s} EW {fmt(R['EW']):>14s}  EW_U {fmt(R['EWU']):>14s}  dEW {fmt(R['dEW']):>14s}  r {pct(R['r']):>9s}  r_U {pct(R['rU']):>8s}  L {fmt(R['L']):>12s}")


def alles():
    rf11.main(); rf11b.main(); rf11g.main(); rf13.main()
    rf12.main(); rf12k.main(); rf12f.main(); rf17.main()
    rf06.main(); extra.main()


def eigene():
    print('\n== Eigene Werte ohne Sollwert im Dokument (zum Abgleich mit dem Referenzrechner)')
    c = ankauf()
    z('Ankauf Stressfall', rechne(c, stress=True, detail=False))
    g = rf11g.geb()
    z('Ankauf gebunden mit uebernommenem Darlehen', rechne(g, detail=False))
    z('Ankauf gebunden, Stressfall', rechne(g, stress=True, detail=False))
    z('Ankauf gebunden, Haltedauer fuenf Jahre', rechne(mit(g, n=5), detail=False))
    z('Ankauf gebunden, Lesart 4 von MA-026', rechne(mit(g, ma026_4=True), detail=False))
    z('Ankauf im Jahresmodus', rechne(mit(c, p=1), detail=False))
    n_ = neubau()
    z('Neubau frei, 15 Jahre', rechne(n_, detail=False))
    z('Neubau frei, 15 Jahre, Stressfall', rechne(n_, stress=True, detail=False))
    z('Neubau frei, 38 Jahre', rechne(mit(n_, n=38), detail=False))
    k = rf12k.kfwfall()
    z('Neubau mit KfW-Darlehen, 15 Jahre', rechne(k, detail=False))
    z('Neubau mit KfW-Darlehen, Stressfall', rechne(k, stress=True, detail=False))
    f = rf12f.foerderfall()
    z('Neubau gefoerdert, 38 Jahre', rechne(f, detail=False))
    z('Neubau gefoerdert, 38 Jahre, Stressfall', rechne(f, stress=True, detail=False))
    z('Neubau gefoerdert, 20 Jahre', rechne(mit(f, n=20), detail=False))
    z('Neubau gefoerdert, sofortige Einnahme, 20 Jahre', rechne(mit(f, n=20, ma031='sofort'), detail=False))
    z('Neubau gefoerdert als Privatperson', rechne(mit(f, status='privat'), detail=False))
    z('Neubau gefoerdert als Privatperson mit E-70', rechne(mit(f, status='privat', e70=True), detail=False))
    R = rechne(f)
    print('   gefoerdert: operatives Ergebnis PJ 1 bis 3:', ' / '.join(fmt(j['e_op']) for j in R['jahr'][:3]),
          '| Kontokorrentzinsen bis Bauende', fmt(sum(R['kz_u'][:19])), '| Stress: Eigenkapital der Investitionsphase',
          fmt(rechne(f, stress=True, detail=False)['ek_inv']))
    ps = preissuche(k, stress=True)
    print('   Neubau mit KfW-Darlehen, tragbarer Grundstueckspreis im Stressfall:', ps['P'], ps['meld'])


if __name__ == '__main__':
    kurz = '--kurz' in sys.argv
    if kurz:
        with contextlib.redirect_stdout(io.StringIO()):
            alles()
    else:
        alles()
    Z.summe()
    lesarten.main()
    eigene()
