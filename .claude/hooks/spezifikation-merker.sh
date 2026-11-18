#!/usr/bin/env bash
# Nach einer Änderung an steuernden Dokumenten: an die Folgepflichten erinnern.
# PostToolUse (Edit|Write). Liest das Hook-JSON von stdin; braucht kein jq.
f="$(sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)"
case "$f" in
  */docs/spezifikation.md)
    msg='Spezifikation geändert. Im selben Arbeitsgang: Stand-Datum prüfen; bei geänderter oder neuer Festlegung Eintrag in docs/entscheidungen.md (Datum, Grund, Auslöser, was ersetzt wird); betroffene Stellen in docs/entwicklungsplan.md und TASKS.md nachziehen.' ;;
  */docs/entwicklungsplan.md)
    msg='Entwicklungsplan geändert. Passt er noch zur Spezifikation (Stufen, Freigabepunkte) und zu TASKS.md? Stand-Datum prüfen.' ;;
  *) exit 0 ;;
esac
printf '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"%s"}}\n' "$msg"
