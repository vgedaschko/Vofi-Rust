"""Pruefrunde 3, Controller: Was geschieht, wenn der Auftrag die Voreinstellungen nicht mitfuehrt (R-3.1)?
Erwerbsnebenkosten 3 % statt KAT-01 10 %: einmal mit, einmal ohne 'voreinstellungen' im Auftrag."""
import sys, io, contextlib
from dataclasses import replace
from decimal import Decimal as D
R = "/home/user/vofi-rust/research_notes/VOFI Immobiliensoftware Marktrecherche/skripte/referenzrechner"
sys.path.insert(0, R)
with contextlib.redirect_stdout(io.StringIO()):
    from rf_grob import VG, KAT, A
    import grobkalkulation as g
for titel, vor in (("mit Voreinstellung im Auftrag", {"enk_satz": (D("0.10"), "KAT-01")}), ("ohne Voreinstellung im Auftrag", None)):
    ein = replace(A.ANKAUF, enk_satz=D("0.03"), voreinstellungen=vor)
    try:
        g.pruefe_begruendungen(ein, VG, KAT, mit_preis=False)
        e = g.rechne_grob(ein, VG, KAT)
        print(f"{titel}: gerechnet; Liste {[a['kennung'] for a in e.abweichungen] if hasattr(e,'abweichungen') else '?'}; Meldungen {sorted(m['kennung'] for m in e.meldungen)}")
    except g.Meldung as m:
        print(f"{titel}: {m.kennung} {str(m)[:120]}")
