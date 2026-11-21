"""GF3-K Katalogwerte ausserhalb jedes sinnvollen Bereichs: Prueft R-3.7 den Bereich oder nur die Vollstaendigkeit?"""
from h import *
F = A.FOERDERUNG_B
faelle = [
    ("KAT-10 Rueckzahlungsfrist 0 Jahre", GEF, VG, KATN, dict(), dict(foerderung=replace(F, tilgung_jahre=0))),
    ("KAT-10 Rueckzahlungsfrist 1 Jahr, Bauzeit 36", replace(GEF, bauzeit_monate=36), VG, KATN, dict(), dict(foerderung=replace(F, tilgung_jahre=1))),
    ("KAT-10 Tilgungsfrist -5 Monate", GEF, VG, KATN, dict(), dict(foerderung=replace(F, tilgungsfrist_monate=-5))),
    ("KAT-10 Darlehensquote 1,5", GEF, VG, KATN, dict(), dict(foerderung=replace(F, darlehensquote=D("1.5")))),
    ("KAT-10 Verwaltungskostenbeitrag -0,5 %", GEF, VG, KATN, dict(), dict(foerderung=replace(F, vkb_satz=D("-0.005")))),
    ("KAT-10 Bindung 0 Jahre", GEF, VG, KATN, dict(), dict(foerderung=replace(F, bindung_jahre=0))),
    ("KAT-07 AfA-Satz 2,0 (200 %)", ANK, VG, replace(KAT, afa_satz=D(2)), dict(), dict()),
    ("KAT-07 AfA-Satz -2 %", ANK, VG, replace(KAT, afa_satz=D("-0.02")), dict(), dict()),
    ("KAT-08 Kappung -15 %", ANK, VG, replace(KAT, kappung=D("-0.15")), dict(), dict()),
    ("KAT-08 Wartefrist 0 Monate", ANK, VG, replace(KAT, wartefrist=0), dict(), dict()),
    ("KAT-13 Sperrfrist -120", ANK, VG, replace(KAT, kuendigung_sperre=-120), dict(), dict()),
    ("KAT-14 Mindestansatz 150 %", ANK, VG, replace(KAT, bewirtschaftung_mindest=D("1.5")), dict(), dict()),
    ("KAT-03 KSt 150 %", ANK, VG, KAT, dict(), dict(steuer=replace(ANK.steuer, kst_satz=lambda j: D("1.5")))),
    ("KAT-04 Hebesatz -400 %", ANK, VG, KAT, dict(), dict(steuer=replace(ANK.steuer, hebesatz=D(-4)))),
    ("KAT-15 KfW Zinsbindung 0", KFWF, VG, replace(KATN, kfw=replace(A.KFW, zinsbindung_jahre=0)), dict(), dict()),
    ("KAT-15 KfW Bereitstellung -0,15 %", KFWF, VG, replace(KATN, kfw=replace(A.KFW, bereit_satz=D("-0.0015"))), dict(), dict()),
]
for name, e, vg, kat, _, ae in faelle:
    print(f"  {name}:", zeig(replace(e, **ae), vg, kat))
