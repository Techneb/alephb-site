# CLAUDE.md

The AlephB home page at <https://alephb.uk>: one static page listing the projects, plus a privacy page. Plain HTML and one `site.css`, no build step; GitHub Pages (legacy Jekyll build from `main`, `/`) serves the repo, so every file is public unless `_config.yml` excludes it. Edited by the supermain session (`~/Projets`), not by a project's main.

## Pages

- `index.html`: the logo, Hillel's motto, then one card per project (logo, name, one-line tagline, a lead sentence, a few bullets opening in bold, a grey `.status` line). What's my size? is shown without a link until it ships (its subdomain is a "Coming soon" page, a likely AdSense rejection reason). No intro paragraph and no About page (owner, 2026-10-09).
- `privacy.html`: each project's own policy linked, this site (GitHub Pages, no cookies), Advertising with Google's required AdSense wording (keep those sentences), and the consent message for the EEA, UK and Switzerland.
- Every page carries the `google-adsense-account` meta tag and the footer nav (Home, Privacy). The logo `<svg>` is inlined in both pages (see `LOGO.md`).

## AdSense

- Publisher `pub-9765732642926043`; application for the root domain alephb.uk sent 2026-10-03, pending. Readiness audit: `~/Projets/2023-2026-AlbertSchool/SQL-Mystery-Game/docs/audits/2026-10-09-adsense-readiness.md`.
- Keep `ads.txt` and the meta tag as they are. Never remove or re-add the site in AdSense while it is under review (Google says that delays it); editing pages is fine.
- The consent message should point at `https://alephb.uk/privacy.html`.

## Status sources

- Repos: this one only (`origin` = github.com/Techneb/alephb-site, public, trunk `main`, direct push). A push is a live deploy of the public home page: the owner approves each one.
- CI: GitHub's own `pages-build-deployment` on every push (`gh run list --limit 3`); then check `curl -s https://alephb.uk/` serves the change.
- Sessions: the supermain at `~/Projets`; no main of its own.
- Docs to keep current: this file, `LOGO.md`, and the supermain's memory (`~/.claude/projects/-Users-techneb-Projets/memory/`).
