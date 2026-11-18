#!/usr/bin/env bash
# Nach jeder Änderung an einer Rust-Datei: das Paket formatieren.
# PostToolUse (Edit|Write). Ohne Wirkung, solange es keinen Rust-Code gibt.
f="$(sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)"
case "$f" in *.rs) ;; *) exit 0 ;; esac
[ -f "$f" ] || exit 0
command -v cargo >/dev/null 2>&1 || exit 0
d="$(dirname "$f")"
while [ "$d" != "/" ] && [ ! -f "$d/Cargo.toml" ]; do d="$(dirname "$d")"; done
[ -f "$d/Cargo.toml" ] || exit 0
cargo fmt --manifest-path "$d/Cargo.toml" >/dev/null 2>&1 || true
exit 0
