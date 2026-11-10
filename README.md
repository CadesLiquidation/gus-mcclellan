# Gus McClellan — Green Hyundai, Springfield, IL

Personal sales page for Gus McClellan, sales consultant at Green Hyundai,
601 W. Stanford Ave, Springfield, IL 62704.

- Static site, GitHub Pages. No build step.
- The site is about Gus first: call/text him direct, message builder,
  reviews, referral bonus. No live inventory, no prices, no incentives,
  no Hyundai logos or vehicle photos. Inventory / pricing / offers live
  only on greenhyundai.com, linked out from the site.
- He sells new Hyundais, used Hyundais (incl. Hyundai Certified Used),
  and used cars from other brands through Green Hyundai's pre-owned
  inventory — that is stated on the site, with no specific vehicles listed.
- Contact: Gus direct (217) 671-2520, Facebook link on the page.
- Referral bonus: $200 cash when a referral buys (confirmed by Cade
  2026-11-09). Ask Gus for terms.
- Photo: the dealership building photo only. No portrait of Gus is
  published here yet — add a verified photo of him when one is supplied.
- Pages (added 2026-11-10): Home plus `about/`, `achievements/`,
  `referrals/`, `family/` — the family page is Gus's own version of the
  cross-promotion (no redirect to cadesliquidation.com/family). All
  pages share `assets/style.css` and a top nav.
- Reviews: three Google reviews naming Gus added 2026-11-10 (Chad Scott,
  Shawna Neihoff, Mark Jennings — from Cade's screenshots of Green
  Hyundai's Google profile; months worked out from the "9 months ago" /
  "7 months ago" labels, so approximate). Other reviews in those
  screenshots name other salespeople and were left out.
- Nav (2026-11-10): transparent over the hero on the homepage; on phones
  two deliberate rows (brand on top, links spread evenly below). Lesson:
  rules appended AFTER the media query beat the mobile overrides — keep
  base rules before the media query in style.css.
- Mobile check (2026-11-10): render the live page at 390px with
  Playwright before announcing a mobile fix — `npx playwright install
  chromium` (no --with-deps), `playwright-core` in /tmp, download the
  live HTML + dealership.jpg with curl and screenshot the local file
  (the headless browser can't reach the internet through the egress
  proxy). A missing `.award { display:flex }` rule was found this way.
- Design: the original navy/serif design (Manrope/Newsreader, hero with
  dealership photo, proof bar, cards). A plain redesign was built
  2026-11-10 and reverted the same night at Cade's request — he liked
  the old design more; it was kept, and the Salesman of the Month
  section (September & October 2026) added in the same style.

To update: edit index.html, commit, push to main. Pages serves it at
https://cadesliquidation.github.io/gus-mcclellan/
