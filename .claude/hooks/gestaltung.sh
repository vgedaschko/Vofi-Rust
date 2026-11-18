#!/usr/bin/env bash
# Gestaltungsarbeit absichern.
#
#   gestaltung.sh merker     PostToolUse (Edit|Write): beim ersten Anfassen einer
#                            Oberflächendatei in der Sitzung an die Pflichtschritte erinnern
#   gestaltung.sh stop       Stop: Haben sich Oberflächendateien seit der letzten
#                            Gestaltungsprüfung geändert, den Stopp einmal aufhalten
#   gestaltung.sh bestanden  nach bestandener Gestaltungsprüfung aufrufen: Stand merken
#
# Oberflächendateien: *.tsx *.jsx *.css *.scss *.html *.svelte *.vue außerhalb von
# docs/, reports/, research_notes/, node_modules/, target/, dist/.
# Ohne Wirkung, solange es keine solchen Dateien gibt. Braucht kein jq.

mode="${1:-stop}"
input="$(cat 2>/dev/null || true)"
root="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
cd "$root" 2>/dev/null || exit 0
gitdir="$(git rev-parse --git-dir 2>/dev/null)" || exit 0
mark="$gitdir/gestaltung-pruefung.bestanden"

ist_oberflaeche() {
  case "$1" in
    docs/*|reports/*|research_notes/*|*/node_modules/*|node_modules/*|*/target/*|target/*|*/dist/*|dist/*) return 1 ;;
    *.tsx|*.jsx|*.css|*.scss|*.html|*.svelte|*.vue) return 0 ;;
    *) return 1 ;;
  esac
}

abdruck() {
  { git ls-files; git ls-files -o --exclude-standard; } 2>/dev/null | sort -u | while read -r p; do
    ist_oberflaeche "$p" && [ -f "$p" ] && sha1sum "$p"
  done | sha1sum | cut -d' ' -f1
}
leer="$(printf '' | sha1sum | cut -d' ' -f1)"

case "$mode" in
  merker)
    f="$(printf '%s' "$input" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)"
    rel="${f#"$root"/}"
    ist_oberflaeche "$rel" || exit 0
    sid="$(printf '%s' "$input" | sed -n 's/.*"session_id"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)"
    einmal="$gitdir/gestaltung-merker.${sid:-ohne}"
    [ -f "$einmal" ] && exit 0
    : > "$einmal"
    printf '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"%s"}}\n' \
      "Oberflächendatei geändert. Pflicht bei jeder Gestaltungsarbeit: (1) Skill frontend-design geladen? Ohne ihn wird nicht gestaltet – ist er nicht verfügbar, den Auftraggeber bitten, das Plugin zu aktivieren. (2) Vorbilder aus docs/gestaltungsreferenzen.md angesehen und das Muster benannt? (3) Vor dem Stopp die Gestaltungsprüfung: im Browser rendern, Bildschirmfotos, dann Rolle pruefer-gestaltung mit design:design-critique und design:accessibility-review; danach .claude/hooks/gestaltung.sh bestanden."
    exit 0
    ;;
  bestanden)
    abdruck > "$mark"
    echo "Gestaltungsprüfung vermerkt."
    exit 0
    ;;
  stop)
    printf '%s' "$input" | grep -Eq '"stop_hook_active"[[:space:]]*:[[:space:]]*true' && exit 0
    now="$(abdruck)"
    [ "$now" = "$leer" ] && exit 0
    [ -f "$mark" ] && [ "$(cat "$mark")" = "$now" ] && exit 0
    {
      echo "Gestaltungsprüfung fällig: Oberflächendateien haben sich seit der letzten Prüfung geändert."
      echo "(1) Im Browser rendern und Bildschirmfotos bei 1280 und 1920 Pixeln sowie von einem bedienten Zustand ablegen."
      echo "(2) Rolle pruefer-gestaltung prüfen lassen (frontend-design als Maßstab, design:design-critique, design:accessibility-review); bei Texten design:ux-copy, bei Diagrammen dataviz."
      echo "(3) Kritische und wichtige Befunde beheben, Ergebnis in docs/pruefung/protokoll.md vermerken."
      echo "(4) Danach: .claude/hooks/gestaltung.sh bestanden"
      echo "Ist die Arbeit bewusst unfertig, das dem Auftraggeber sagen statt die Prüfung zu überspringen."
    } >&2
    exit 2
    ;;
esac
exit 0
