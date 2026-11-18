#!/usr/bin/env bash
# "Anything else?" – erinnert Claude an ausstehende Aufgaben aus TASKS.md.
#
#   anything-else.sh start   SessionStart: offene Aufgaben in den Kontext legen
#   anything-else.sh stop    Stop: vor dem Beenden einmal nachfragen, ob unter
#                            "## Jetzt" noch etwas offen ist
#
# Konvention in TASKS.md: Abschnitte "## Jetzt", "## Als Nächstes",
# "## Wartet auf Nutzer", "## Später", "## Erledigt"; Aufgaben als "- [ ] ...".
# Nur offene Punkte unter "## Jetzt" halten einen Stopp auf.
# "- [~] ..." = läuft im Hintergrund / wartet auf ein Ergebnis: wird beim
# Start angezeigt, hält einen Stopp aber nicht auf.
# Braucht nur bash + awk + grep (kein jq).

mode="${1:-stop}"
input="$(cat 2>/dev/null || true)"
root="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
tasks="${ANYTHING_ELSE_TASKS_FILE:-$root/TASKS.md}"

[ -f "$tasks" ] || exit 0

# Offene Aufgaben eines Abschnitts ausgeben (Vergleich über Überschrift-Präfix).
open_in() {
  awk -v want="$1" '
    /^## / { sec = substr($0, 4); next }
    index(sec, want) == 1 && /^[[:space:]]*- \[ \]/ { sub(/^[[:space:]]*- \[ \] */, ""); print "  - " $0 }
  ' "$tasks"
}

# Laufende Aufgaben ("- [~]") aus allen Abschnitten.
running="$(awk '/^[[:space:]]*- \[~\]/ { sub(/^[[:space:]]*- \[~\] */, ""); print "  - " $0 }' "$tasks")"

now="$(open_in "Jetzt")"
next="$(open_in "Als Nächstes")"
waiting="$(open_in "Wartet auf Nutzer")"
later_count="$(open_in "Später" | grep -c . || true)"

case "$mode" in
  start)
    if [ -f "$root/docs/spezifikation.md" ]; then
      echo "Verbindlich und vor inhaltlicher Arbeit zu lesen: CLAUDE.md (Abschnitt Pflichtlektüre), docs/spezifikation.md, docs/entwicklungsplan.md. Änderungen an Festlegungen zuerst dort und in docs/entscheidungen.md."
    fi
    # Stimmt die Pflichtlektüre in CLAUDE.md noch mit dem Bestand überein?
    if [ -f "$root/CLAUDE.md" ]; then
      missing="$(awk '/^## Pflichtlektüre/{on=1;next} /^## /{on=0} on' "$root/CLAUDE.md" \
        | grep -o '`[A-Za-z0-9_./-]*\.md`' | tr -d '`' | sort -u \
        | while read -r f; do [ -e "$root/$f" ] || printf '  - %s\n' "$f"; done)"
      [ -n "$missing" ] && printf 'Pflichtlektüre in CLAUDE.md nennt Dateien, die es nicht gibt – Liste berichtigen:\n%s\n' "$missing"
    fi
    if [ -f "$root/docs/README.md" ]; then
      unlisted="$(for f in "$root"/docs/*.md; do b="$(basename "$f")"; [ "$b" = "README.md" ] && continue
        grep -q "$b" "$root/docs/README.md" || printf '  - docs/%s\n' "$b"; done)"
      [ -n "$unlisted" ] && printf 'Nicht in der Dokumentationsübersicht (docs/README.md) verzeichnet – eintragen oder löschen:\n%s\n' "$unlisted"
    fi
    if [ -f "$root/scripts/quellenkataster.py" ] && command -v python3 >/dev/null 2>&1; then
      kat="$(python3 "$root/scripts/quellenkataster.py" --pruefen 2>&1 >/dev/null)" || printf '%s\n' "$kat" | head -8
    fi
    [ -z "$now$running$next$waiting" ] && [ "$later_count" = "0" ] && exit 0
    echo "Ausstehende Aufgaben laut TASKS.md (Quelle der Wahrheit, bitte aktuell halten):"
    [ -n "$now" ] && printf 'Jetzt:\n%s\n' "$now"
    [ -n "$running" ] && printf 'Läuft im Hintergrund / wartet auf Ergebnis (Stand prüfen):\n%s\n' "$running"
    [ -n "$next" ] && printf 'Als Nächstes:\n%s\n' "$next"
    [ -n "$waiting" ] && printf 'Wartet auf Nutzer (beim Nutzer nachfragen, wenn passend):\n%s\n' "$waiting"
    [ "$later_count" != "0" ] && echo "Später: $later_count weitere Punkte (siehe TASKS.md)."
    exit 0
    ;;
  stop)
    # Schon einmal in diesem Stopp nachgefragt -> durchlassen (keine Endlosschleife).
    if printf '%s' "$input" | grep -Eq '"stop_hook_active"[[:space:]]*:[[:space:]]*true'; then
      exit 0
    fi
    [ -z "$now" ] && exit 0
    {
      echo "Anything else? Unter \"## Jetzt\" in TASKS.md ist noch offen:"
      echo "$now"
      echo "Bevor du stoppst: (1) Was davon ohne Rückfrage machbar ist, jetzt erledigen."
      echo "(2) Erledigtes in TASKS.md abhaken; was auf den Nutzer wartet, nach \"## Wartet auf Nutzer\" verschieben; neu entdeckte Aufgaben eintragen."
      echo "(3) Erst dann stoppen und in der Abschlussnachricht kurz sagen, was offen bleibt und warum."
    } >&2
    exit 2
    ;;
esac
exit 0
