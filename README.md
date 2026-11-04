# partner-bootcamp-lab-assets

Public, downloadable assets for the Posit Partner Bootcamp hands-on labs. Lab VMs and Posit
products fetch these over HTTPS, which is why this repository is public.

> **This repository is world-readable. Never commit a secret to it** (API keys, tokens,
> client secrets, license files, private keys). Like `partner-bootcamp-skilljar-lab-host` and
> `partner-bootcamp-cert-host`, it holds only content that is safe to publish.

## Contents

| Path | Used by | What it is |
|---|---|---|
| `vsx/` | Package Manager lab: private VS Code extension lifecycle | Sample private extension `posit-bootcamp.lab-snippets`, source plus prebuilt `.vsix` releases |
| `plugins/` *(planned)* | Package Manager lab: `git-plugins` source | AI agent plugin marketplace that Package Manager mirrors from Git |
| `gallery/` *(planned)* | Connect lab: custom Gallery feed | `extensions.json` feed served to the Connect Gallery |

## `vsx/`: sample private extension

`posit-bootcamp.lab-snippets` is a declarative extension (snippets only, no extension code), so
installing it runs nothing. Its publisher namespace, `posit-bootcamp`, does not exist on Open VSX,
so it never collides with a mirrored extension, and it gives the lab a namespace to declare with
`rspm create source --type=local-vsx --publisher-namespaces=posit-bootcamp`.

Two releases exist so the lab can show an update reaching a session:

| Release | Download | Change |
|---|---|---|
| 1.0.0 | [`posit-bootcamp.lab-snippets-1.0.0.vsix`](vsx/dist/posit-bootcamp.lab-snippets-1.0.0.vsix) | R and Python snippets; `bootcamp-hello` prints `v1.0.0` |
| 1.0.1 | [`posit-bootcamp.lab-snippets-1.0.1.vsix`](vsx/dist/posit-bootcamp.lab-snippets-1.0.1.vsix) | Adds the `bootcamp-report` Quarto snippet; `bootcamp-hello` prints `v1.0.1` |

Fetch a release on a lab VM and check it against `vsx/dist/SHA256SUMS`:

```bash
curl -fLO https://github.com/sol-eng/partner-bootcamp-lab-assets/raw/main/vsx/dist/posit-bootcamp.lab-snippets-1.0.0.vsix
sha256sum posit-bootcamp.lab-snippets-1.0.0.vsix
```

Package Manager requires only a publisher, name, version, and `extension.vsixmanifest` in the
archive; both releases carry all four.

### Rebuild

`vsx/lab-snippets/` is the source at the newest release. `vsx/build.sh` shapes a copy for each
release (`build_version.py` drops the Quarto snippets for 1.0.0), packages it with
`@vscode/vsce@4.1.0`, and rewrites `dist/SHA256SUMS`. It needs `node`/`npx` and `python3`:

```bash
./vsx/build.sh
```

The `.vsix` files are zip archives with embedded timestamps, so a rebuild changes their
checksums even when the content is identical. Commit the new `SHA256SUMS` with them.
