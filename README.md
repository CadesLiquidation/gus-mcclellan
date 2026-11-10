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
- Photos: both removed from the site 2026-11-10 at Cade's request — they
  never sat right on mobile. The files are still in assets/ if needed.
  Cade may find better ones later.
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
