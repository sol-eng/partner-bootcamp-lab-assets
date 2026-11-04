# Posit Bootcamp Lab Snippets

A sample **private** VS Code / Positron extension used in the Posit Partner Bootcamp
Package Manager lab. Learners upload it to a Package Manager `local-vsx` source and then
install and update it from a Workbench session, the way a customer distributes an internal
extension that isn't on Open VSX.

It is declarative only (snippets, no extension code), so installing it runs nothing.

| Prefix | Language | Inserts |
|---|---|---|
| `bootcamp-hello` | R, Python | A line that prints the installed extension version |
| `ppm-repos` | R | `options(repos = ...)` pointing at a Package Manager CRAN binary repo |
| `connect-deploy` | R | An `rsconnect::deployApp()` call |
| `connect-client` | Python | A Posit Connect SDK client built from `CONNECT_SERVER` / `CONNECT_API_KEY` |
| `bootcamp-report` | Quarto | Front matter for a report to publish to Connect *(added in 1.0.1)* |
