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
- Reviews (2026-11-10): 14 total, newest first — Mark Jennings (Google,
  Apr 2026), Chad Scott & Shawna Neihoff (Google, Feb 2026), Joseph
  Daniels (Google, Dec 2025), Patricia Dorsey, Liz Sims, Lisa Atteberry,
  Tonya Anders, Bryan Groves (Google, Nov 2025), then the five
  DealerRater reviews (Jul 2022 back to Jan 2016). Months are approximate,
  worked out from the screenshots' relative dates. New reviews go at the
  top. Reviews naming other salespeople (Doug Bishop, John McCarthy,
  Taylor Upshaw, Brian/John, Adam) were left out. Homepage shows the 3
  most recent with a "View all 14 reviews" toggle (JS, `#reviews-grid`
  + `#reviews-toggle`); review quotes render in ink, not muted gray.
- About page (2026-11-10): personal rewrite from Cade — Gus is a father
  of five kids, two dogs, one cat; loves family vacations; selling cars
  at Green Hyundai since 2013, started at the bottom and worked his way
  up, Salesman of the Month many times. Four brothers, most in car sales
  past or present, following their father who served thousands at Green
  Hyundai. Photos (all supplied by Cade, resized to 1200px max):
  `gus-jana.jpg` (Gus + Jana selfie), `gus-brothers-parents.jpg` (Gus
  with his four brothers and parents), `gus-family-formal.jpg` and
  `gus-family-garden.jpg` (vacation gallery, `.photo-grid` — 2 cols
  desktop, stacks on mobile). CSS-ordering lesson, again: base rules
  must sit BEFORE the media query or mobile overrides lose — the
  photo-grid base rule was appended after it and the gallery stayed
  2-col on phones until moved.
- How It Works (2026-11-10): 5-step section on the homepage between the
  message builder and reviews (Tell Gus what you need → He narrows it
  down → See it and drive it → Trade-in → Drive it home). Idea from
  Cody Carter's Express Store How It Works page; every step is a
  restatement of copy already on Gus's site. Reuses the `.steps`
  component.
- Message builder (2026-11-10): "Text Gus this request" (SMS prefill),
  "Email Gus this request" (mailto to his work email
  gus.mcclellan@greenfamilystores.net, subject "Car shopping request",
  body = the built message, kept in sync by the same `buildMessage()`),
  and Copy request. Intro copy mentions the email option for computers.
- Referrals (2026-11-10): "Send Gus's info to a friend" share card — a
  read-only text block with his name, dealership, address, since-2013 line,
  phone, work email, the $200 referral bonus, and his site link, plus a
  "Text this to a friend" button (SMS prefill, no fixed recipient) and a
  "Copy Gus's info" button (clipboard + fallback, same handler pattern as
  the homepage message builder).
- Hero photo: `assets/dealership-2.jpg` — the sharper wide dealership shot
  Cade supplied 2026-11-10 (replaced the blurry original
  `dealership.jpg`). Referenced in `assets/style.css` `.hero::before`
  (`center 58% / cover`). New filename used so cached copies of the old
  photo don't linger.
  Family, one row on mobile. Current page link is highlighted cyan
  (`.topnav a.current`); remember to set it on each page. Smart header
  (`assets/nav.js`, included on all pages): hides on scroll down, pops
  back on scroll up; solid navy once scrolled, transparent over the hero
  only at the very top. Anchor sections get `scroll-margin-top:70px` so
  the fixed nav never covers a jumped-to heading.
- Full pass (2026-11-10): SOTM section structure repaired — my reviews
  reorder had silently eaten the section open + heading/intro (divs went
  36/38); always run the HTML parser balance check after block edits.
  Referral steps were unreadable on light pages (pale-blue text on white)
  — light step colors are now scoped to `.referral .steps` only. Footer
  stacks vertically (was 3 squeezed columns on desktop). About page got
  a reasons block (quote + 3 items, all grounded in existing copy) using
  the previously unused `.reasons` CSS. Referrals page's family-deal line
  is now an offer card. Footer disclaimer no longer claims "no vehicle
  photos" (the hero is a dealership photo). Homepage copy fix: the
  message form is ABOVE the New/Used section, not below it.
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
