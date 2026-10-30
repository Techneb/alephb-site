# CLAUDE.md

The AlephB home page at <https://alephb.uk>: one static page listing the projects, plus a privacy page. Plain HTML and one `site.css`, no build step; GitHub Pages (legacy Jekyll build from `main`, `/`) serves the repo, so every file is public unless `_config.yml` excludes it. Edited by the supermain session (`~/Projets`), not by a project's main.

## Pages

- `index.html` (`main.home`, 1240 px wide; other pages keep the 640 px reading width): the logo, Hillel's motto and a day/night switch (`#theme`, saved in localStorage `alephb.theme`), then one `section.project` per project. Each has a lead with **bold** highlights, bullets (`li[data-slide]`), a carousel of marketing images in `img/` (`[data-carousel]` in `home.js`: hovering or clicking a bullet shows its slide, auto-advance every 4 s, paused on hover), big `.cta` buttons, and a grey `.status` line, links separated by ` · `. Day/night image pairs (`.day`/`.night`) follow the theme.
  - Compromise (two columns): a reel clip plus five Instagram-post slides on pure white, blended into the page (`multiply` by day, inverted `screen` by night); the official App Store badge, unlinked until 1.0 is approved, and "How it works".
  - The Ritz Affair (`.stack`: intro, full-width media, three bullets in three columns): chapter, handbook (`learn/group-by-having.html`) and leaderboard shots from the game's session.
  - What's my size? (`.stack`, linked to whatsmysize.alephb.uk at the owner's request): product panel (the owner's real Wooden Store jeans on drapeur.com), wardrobe, brands; model faces softly blurred. An "Outfit ideas" bullet and slide come once What's my size · Main shoots them.
  - Then the four articles as cards. Fonts: Nunito (headings, buttons) and Nunito Sans (body), self-hosted in `fonts/` (OFL), on every page.
  - Owner, 2026-10-24: wider, more text and marketing images, copy run through `humanizer` (replaced the 2026-10-16 "links, not prose" rule); no bar names in the copy; "350+ cities". No About page. Facts come from each project's docs (release state, city count, handbook size): re-check them before each update. Check every new link returns 200.
- `privacy.html`: each project's own policy linked, this site (GitHub Pages, no cookies), Advertising with Google's required AdSense wording (keep those sentences), and the consent message for the EEA, UK and Switzerland.
- `ritz-affair.html` (linked from its home card's status line) and `articles.html` with one page per article (`article-*.html`): original long-form text written for AdSense after the 2026-10-11 "Contenu a faible valeur informative" refusal. No clue, answer or chapter-specific shortcut of the game in them (the game's Shortcut check applies). Never copy text from compromise.alephb.uk or the game's pages (duplicate content). A new article = a page plus a row in `articles.html`.
- `learn/` is The Clerk's Handbook (17 pages, moved from mystery.alephb.uk on 2026-10-30 so the domain AdSense reviews carries the substance): generated, never edited here. The game repo writes it (`node move_handbook.mjs export <commit> ../alephb-site`, which also writes `learn/sitemap.xml` and copies the game modules into `learn/lib/`); its tests and rules live in the game's CLAUDE.md. `robots.txt` lists `sitemap.xml` (this site's own pages, by hand) and `learn/sitemap.xml`.
- Every page carries the `google-adsense-account` meta tag and the footer nav (Home, Articles, Privacy). The logo `<svg>` is inlined in both pages (see `LOGO.md`).

## AdSense

- Publisher `pub-9765732642926043`; application for the root domain alephb.uk sent 2026-10-03, refused 2026-10-11 for low-value content; the Ritz Affair page and three articles followed, then a new review request on 2026-10-19 (still under review on 10-23). Readiness audit: `~/Projets/2023-2026-AlbertSchool/SQL-Mystery-Game/docs/audits/2026-10-09-adsense-readiness.md`.
- Keep `ads.txt` and the meta tag as they are. Never remove or re-add the site in AdSense while it is under review (Google says that delays it); editing pages is fine.
- The consent message should point at `https://alephb.uk/privacy.html`.

## Status sources

- Repos: this one only (`origin` = github.com/Techneb/alephb-site, public, trunk `main`, direct push). A push is a live deploy of the public home page: the owner approves each one.
- CI: GitHub's own `pages-build-deployment` on every push (`gh run list --limit 3`); then check `curl -s https://alephb.uk/` serves the change.
- Sessions: the supermain at `~/Projets`; no main of its own.
- Docs to keep current: this file, `LOGO.md`, and the supermain's memory (`~/.claude/projects/-Users-techneb-Projets/memory/`).
