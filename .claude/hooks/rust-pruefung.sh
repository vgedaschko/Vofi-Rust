#!/usr/bin/env bash
# Vor dem Stopp: Hat sich Rust-Code seit der letzten bestandenen Prüfung geändert,
# laufen Lint (clippy, Warnungen gelten als Fehler) und Tests. Schlägt etwas fehl,
# wird der Stopp einmal aufgehalten. Ohne Wirkung, solange es keinen Rust-Code gibt.
input="$(cat 2>/dev/null || true)"
printf '%s' "$input" | grep -Eq '"stop_hook_active"[[:space:]]*:[[:space:]]*true' && exit 0
root="${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}"
[ -f "$root/Cargo.toml" ] || exit 0
command -v cargo >/dev/null 2>&1 || exit 0
cd "$root" || exit 0

# Fingerabdruck aller Rust- und Cargo-Dateien (versioniert und neu).
mark="$(git rev-parse --git-dir 2>/dev/null)/rust-pruefung.bestanden"
now="$( { git ls-files -- '*.rs' 'Cargo.toml' '*/Cargo.toml' 'Cargo.lock'; git ls-files -o --exclude-standard -- '*.rs' '*/Cargo.toml'; } 2>/dev/null \
        | sort -u | while read -r p; do [ -f "$p" ] && sha1sum "$p"; done | sha1sum | cut -d' ' -f1)"
[ -f "$mark" ] && [ "$(cat "$mark")" = "$now" ] && exit 0

out="$(cargo clippy --workspace --all-targets --quiet -- -D warnings 2>&1)" || {
  { echo "Rust-Prüfung: clippy meldet Fehler. Beheben, dann stoppen:"; printf '%s\n' "$out" | tail -40; } >&2; exit 2; }
out="$(cargo test --workspace --quiet 2>&1)" || {
  { echo "Rust-Prüfung: Tests schlagen fehl. Beheben, dann stoppen – keine Tests abschalten, um grün zu werden:"; printf '%s\n' "$out" | tail -40; } >&2; exit 2; }
printf '%s' "$now" > "$mark"
exit 0
