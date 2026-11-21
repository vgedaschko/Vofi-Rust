# -*- coding: utf-8 -*-
"""Stellen, an denen der Text allein nicht entschieden hat: Wirkung der anderen Lesart in Zahlen.
Kein Sollwertvergleich; die Zeilen gehen in den Bericht (Abschnitt 'Stellen, an denen geraten werden musste')."""
from kern import *
from rf11g import geb
from rf12f import foerderfall


def main():
    print('\n== Lesarten und Ursachensuche (ohne Zaehlung)')
    c = ankauf()
    # (1) R-10.9: Endwertueberschuss im Stressfall -- Sollwert des Fliesstexts stammt aus dem Stand mit neun Stressgroessen
    S8 = rechne(c, stress=True, detail=False)
    S9 = rechne(mit(c, H_st_inst=D('0.10')), stress=True, detail=False)
    print(' 1 R-10.9 Endwertueberschuss Stress: acht Groessen', fmt(S8['EU']), '| mit Instandhaltung +10 % (Altstand)', fmt(S9['EU']),
          'dEW', fmt(S9['dEW']), '(Text R-10.9: -739.303,12; R-15.6 nennt 216.856,20 fuer neun Groessen)')
    # (2) R-11.11: frei gegen gefoerdert, 38 Jahre
    Rf = rechne(mit(neubau(), n=38), detail=False)
    Rg = rechne(foerderfall(), detail=False)
    print(' 2 R-11.11 frei 38 J: EW', fmt(Rf['EW']), 'EW_U', fmt(Rf['EWU']), 'dEW', fmt(Rf['dEW']), '| gefoerdert dEW', fmt(Rg['dEW']),
          '| Differenz', fmt(Rg['dEW'] - Rf['dEW']), '(Text: -10.726.689,93; daraus frei dEW', fmt(Rg['dEW'] + D('10726689.93')) + ')')
    # (3) R-5.12 Beispiel: Rohertrag_n des gebundenen Bestands
    G = rechne(geb(), nur_bemessung=True)
    print(' 3 R-5.12 Rohertrag_n gebunden', fmt(G['roh_n']), '- Mietausfall', fmt(G['ausf_n']), '- Bew', fmt(G['bew_vj']), '= RE_n', fmt(G['re_n']),
          '| Text nennt Rohertrag_n 123.869,76 (ergaebe RE_n', fmt(D('123869.76') - G['ausf_n'] - G['bew_vj']) + ')')
    # (4) R-5.12 Beispiel: H-25 fest 4 % "fuer uebernommene Darlehen" und "Lesart (2)" -- beide Stellgroessen gibt es nicht mehr
    G4 = rechne(geb(H_h25=D('0.04')), nur_bemessung=True)
    print(' 4 R-5.12 gebunden, H-25 fest 4 % als ein Wert fuer alle Tranchen: KD_UE', fmt(G4['KD_U']), 'L', fmt(G4['L']),
          '| Text: 826.660,00 (nur mit H-25 je Tranchenart: (RE_n/1,2 - 19.200)/7 % =', fmt(floor2((G['re_n'] / D('1.2') - 19200) / D('0.07'))) + ')',
          '| "Lesart (2)" 1.034.436,66 = (RE_n/1,2 - 15.000)/6 % =', fmt(floor2((G['re_n'] / D('1.2') - 15000) / D('0.06'))))
    # (5) R-10.14 Nr. 4: erstes Planjahr nach dem Ende der zinslosen Zeit (Ende im Monat 438, mitten im Planjahr 37)
    Rg = rechne(foerderfall())
    print(' 5 R-10.14 Nr. 4 gefoerdert: Deckung Planjahr 37', fmt(Rg['deck'][37][0], 4), '(Text) | Planjahr 38, das erste ganz nach dem Ende', fmt(Rg['deck'][38][0], 4))
    # (6) R-11.15: Planjahr, in dem die Mindestdeckung erstmals erreicht ist -- ohne die Abgrenzung "ganz in der Vermietung"
    print(' 6 R-11.15 gefoerdert: Deckung je Planjahr 1 bis 10:', ' / '.join('k.KD' if Rg['deck'][j][0] is None else fmt(Rg['deck'][j][0], 3) for j in range(1, 11)),
          '-> erstes Jahr >= 1,2 ohne Abgrenzung:', min(j for j in Rg['deck'] if Rg['deck'][j][0] is not None and Rg['deck'][j][0] >= D('1.2')), '| mit Abgrenzung: 9 (Text)')
    # (7) R-10.16 mit Kennzeichen E-41 ohne E-69: Steuer "die ohne Verkaufsgewinn anfiele"
    K = rechne(mit(c, kennz=True))
    gewst_lfd = D('7952.00')
    a = K['restwertbeitrag'] / K['EW']
    b = (K['restwertbeitrag'] - gewst_lfd) / K['EW']
    print(' 7 R-10.16 mit E-41: Steuer auf den Verkaufsgewinn', fmt(K['steuer_verkauf']), '(Verkaufsjahr ohne Gewinn, Kuerzung entfaellt) | Restwertanteil', pct(a, 2),
          '| andere Lesart (Jahr ohne Verkauf, Kuerzung bleibt): Steuer', fmt(K['steuer_verkauf'] + gewst_lfd), 'Restwertanteil', pct(b, 2))
    # (8) R-11.8: kalkulatorischer Zins im Stressfall mit oder ohne Anschlussstress
    re = rechne(c, nur_bemessung=True)['re_n']
    print(' 8 R-11.8 Stress-Bemessung: i_k = 4,5 % + 1 = 5,5 %: L', fmt(S8['L']), '| mit Anschlussstress 6,5 %: L', fmt(floor2(re / D('1.2') / D('0.085'))))
    # (9) R-12.4: Bemessungszins auf zwoelf Stellen -- des Satzes oder des Prozentwerts
    print(' 9 R-5.19 H-32 15 Jahre: i_B = runde12(0,0333...) = 3,3333333333 % (Text schreibt 3,333333333333 %); KD_UE in beiden Schreibweisen 159.999,96')
    # (10) R-11.5: Steigung am Knick aus gerundeten oder ungerundeten Renditen
    rs = [lauf(c, 1887092 + x)['r'] for x in (-10000, 0, 10000)]
    print('10 R-11.5 Steigung links', fmt((rs[1] - rs[0]) * 10000, 3), 'rechts', fmt((rs[2] - rs[1]) * 10000, 3), 'Basispunkte je 10.000 Euro (Text: -7,11 und -9,61)')
    # (11) R-11.8 mit R-5.8: uebernommenes Darlehen mit dem voreingestellten Anschlusszins E-45 + H-05 -- folgt er im
    #      Stressfall dem Bankdarlehen (+0,5 bis zur Zusage, +1 Anschluss) oder gilt er als eingegeben (+1)?
    ue = dict(rest=D(500000), nenn=D(600000), zins=D('0.005'), tilg=D('0.02'), zb=8, anschluss=None, beitrag=D(0))
    a = rechne(mit(geb(), uebern=ue), stress=True, detail=False)
    b = rechne(mit(geb(), uebern=dict(ue, anschluss=D('0.05'))), stress=True, detail=False)
    print('11 R-11.8 uebernommenes Darlehen mit voreingestelltem Anschlusszins, Stressfall: folgt der Bank (6,5 %): L', fmt(a['L']), 'dEW', fmt(a['dEW']),
          '| gilt als eingegeben (6,0 %): L', fmt(b['L']), 'dEW', fmt(b['dEW']))
    # (12) Betrag B negativ: abrunden zur Null hin oder nach unten
    print('12 R-5.12 Tabelle RF-09: B = (180.000/1,2 - 155.571,428571)/6 % = -92.857,142857 -> zur Null hin -92.857,14 (Text), nach unten -92.857,15')


if __name__ == '__main__':
    main()
