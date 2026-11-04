#!/usr/bin/env bash
# Rebuild both sample releases into dist/. Needs node/npx and python3.
set -euo pipefail
cd "$(dirname "$0")"
VSCE="@vscode/vsce@4.1.0"
mkdir -p dist
for v in 1.0.0 1.0.1; do
  work="$(mktemp -d)"
  cp -r lab-snippets/. "$work/"
  python3 build_version.py "$work" "$v"
  (cd "$work" && npx --yes "$VSCE" package --skip-license --out "$OLDPWD/dist/posit-bootcamp.lab-snippets-$v.vsix")
  rm -rf "$work"
done
(cd dist && sha256sum ./*.vsix | sed 's# \./# #' > SHA256SUMS)
