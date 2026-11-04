"""Shape a copy of lab-snippets/ into a specific release before packaging.

Usage: python3 build_version.py <copied-extension-dir> <version>
Only 1.0.0 and 1.0.1 are defined. 1.0.0 drops the Quarto snippets added in 1.0.1.
"""
import json, pathlib, re, sys

root, version = pathlib.Path(sys.argv[1]), sys.argv[2]
if version not in ("1.0.0", "1.0.1"):
    sys.exit(f"unknown version {version}")
pkg = json.loads((root / "package.json").read_text())
pkg["version"] = version
if version == "1.0.0":
    pkg["contributes"]["snippets"] = [s for s in pkg["contributes"]["snippets"] if s["language"] != "quarto"]
    (root / "snippets" / "quarto.json").unlink()
    cl = (root / "CHANGELOG.md").read_text()
    (root / "CHANGELOG.md").write_text(re.sub(r"## 1\.0\.1\n.*?(?=## 1\.0\.0)", "", cl, flags=re.S))
    rd = (root / "README.md").read_text()
    (root / "README.md").write_text("\n".join(l for l in rd.splitlines() if "added in 1.0.1" not in l) + "\n")
(root / "package.json").write_text(json.dumps(pkg, indent=2) + "\n")
for f in (root / "snippets").glob("*.json"):
    f.write_text(f.read_text().replace("__VERSION__", version))
