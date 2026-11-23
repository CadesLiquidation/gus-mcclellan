#!/usr/bin/env python3
"""Build the Guides + Models pages for gusatgreen.com (Nov 2026).

12 pages: /guides/ + 4 guides, /models/ + 6 model pages.
Template mirrors about/index.html (subpage pattern). Positioning per Cade:
push NEW (Gus earns more on new), but never trash used — a used sale beats
no sale. Every page funnels to Gus: call / text / message builder.
Hyundai-rules discipline holds: no prices, no inventory, no incentives/APR,
no logos, no copied vehicle photos. Model facts verified via search
2026-11-23 (seats, hybrid/EV availability, EPA-est. hybrid mpg).

Layout (Nov 2026, Cade: "doesnt just look like header paragraph header
paragraph"): the pages mix prose sections with callouts (.gus-note), stat
rows (.facts), side-by-side comparisons (.compare), checklists, numbered
steps (.steps), option cards, and photo splits (Gus's own showroom and
portrait photos — the only vehicle-adjacent photos the site publishes).
Footer on every page links Guides + Models.
"""
import os

SITE = "/home/hatch/workspace/gus-mcclellan-site"
GA_ID = "G-SXFHL5LZR1"

GA_BLOCK = """<!-- Google tag (gtag.js) — library loads after page load so analytics
     never blocks rendering or interactivity -->
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  window.addEventListener('load', function() {
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=G-SXFHL5LZR1';
    document.head.appendChild(s);
    gtag('config', 'G-SXFHL5LZR1');
  });
</script>"""

NAV = """  <nav class="topnav">
    <div class="wrap">
      <a href="{p}">Home</a>
      <a href="{p}about/">About</a>
      <a href="{p}achievements/">Achievements</a>
      <a href="{p}referrals/">Referrals</a>
      <a href="{p}family/">Family</a>
    </div>
  </nav>"""


def footer(p):
    return f"""  <footer>
    <div class="wrap">
      <p><strong>Green Hyundai</strong> — 601 W. Stanford Ave., Springfield, IL 62704 · Sales <a href="tel:+12175251370">(217) 525-1370</a> · Gus direct <a href="tel:+12176712520">(217) 671-2520</a> · Mon–Fri 9:00 AM–7:00 PM, Sat 9:00 AM–6:00 PM, Sun closed. Dealership inventory, prices, incentives, and availability are maintained by Green Hyundai and may change — check <a href="https://www.greenhyundai.com/" target="_blank" rel="noopener">greenhyundai.com</a> for current details.</p>
      <p>This is Gus McClellan's personal sales page. It is not the official Green Hyundai or Hyundai Motor America website, and it is not affiliated with or endorsed by Hyundai Motor America. Hyundai and Hyundai model names are registered trademarks of Hyundai Motor Company / Hyundai Motor America. All rights reserved. Vehicle photos courtesy of Hyundai Motor America. No prices or inventory are published here — for current inventory, pricing, and offers, see greenhyundai.com.</p>
      <p><a href="{p}guides/">Car buying guides</a> · <a href="{p}models/">New Hyundai models</a></p>
      <a href="https://www.facebook.com/share/1K6tKdTTzo/?mibextid=wwXIfr" target="_blank" rel="noopener">Gus on Facebook <span aria-hidden="true">↗</span></a>
    </div>
  </footer>"""


def cta_split(p, blurb):
    return f"""    <section>
      <div class="wrap">
        <div class="cta-split">
          <h2>Talk to Gus first.</h2>
          <p>{blurb}</p>
          <div class="actions">
            <a class="btn dark" href="tel:+12176712520">Call Gus — (217) 671-2520</a>
            <a class="btn" href="sms:+12176712520">Text Gus</a>
            <a class="btn" href="{p}#car-match">Tell Gus what you need</a>
          </div>
        </div>
      </div>
    </section>"""


def info_split(heading, *paras):
    ps = "\n".join(f"            <p>{x}</p>" for x in paras)
    return f"""    <section>
      <div class="wrap">
        <div style="max-width:720px;">
          <h2>{heading}</h2>
{ps}
        </div>
      </div>
    </section>"""


def related(p, links):
    items = "\n".join(f'          <li><a href="{p}{href}">{label}</a></li>' for href, label in links)
    return f"""    <section>
      <div class="wrap">
        <div class="section-head">
          <h2>Keep reading.</h2>
        </div>
        <ul>
{items}
        </ul>
      </div>
    </section>"""


def page(prefix, slug_path, title, desc, og_url, kicker, h1, intro, body):
    nav = NAV.format(p=prefix)
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <meta name="color-scheme" content="light" />
  <meta name="theme-color" content="#073b64" />
  <meta name="description" content="{desc}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{og_url}" />
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23073b64'/%3E%3Ctext x='32' y='45' font-family='Arial,sans-serif' font-size='36' font-weight='700' fill='%23ffffff' text-anchor='middle'%3EG%3C/text%3E%3C/svg%3E" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Newsreader:opsz,wght@6..72,500;6..72,650&display=swap" rel="stylesheet">
  <title>{title}</title>
  <link rel="stylesheet" href="{prefix}assets/style.css?v=11">
{GA_BLOCK}
</head>
<body>
{nav}
  <main>
    <div class="wrap page-head">
      <p class="kicker">{kicker}</p>
      <h1>{h1}</h1>
      <p>{intro}</p>
    </div>

{body}
  </main>

{footer(prefix)}
  <script src="{prefix}assets/nav.js" defer></script>
</body>
</html>
"""
    path = os.path.join(SITE, slug_path, "index.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)
    print("wrote", slug_path)


def section(h2, *paras):
    ps = "\n".join(f"          <p>{p}</p>" for p in paras)
    return f"""    <section>
      <div class="wrap">
        <div class="section-head">
          <h2>{h2}</h2>
{ps}
        </div>
      </div>
    </section>"""


def gus_note(label, text):
    return f"""    <section>
      <div class="wrap">
        <div class="gus-note">
          <span class="note-label">{label}</span>
          <p>{text}</p>
        </div>
      </div>
    </section>"""


def steps_block(h2, items):
    lis = "\n".join(f'          <li><div><strong>{t}</strong><span>{s}</span></div></li>' for t, s in items)
    return f"""    <section>
      <div class="wrap">
        <div class="section-head">
          <h2>{h2}</h2>
        </div>
        <ol class="steps">
{lis}
        </ol>
      </div>
    </section>"""


def checklist_block(h2, items):
    lis = "\n".join(f"          <li>{x}</li>" for x in items)
    return f"""    <section>
      <div class="wrap">
        <div class="section-head">
          <h2>{h2}</h2>
        </div>
        <ul class="checklist">
{lis}
        </ul>
      </div>
    </section>"""


def compare_block(h2, new_title, new_items, used_title, used_items):
    ni = "\n".join(f"            <li>{x}</li>" for x in new_items)
    ui = "\n".join(f"            <li>{x}</li>" for x in used_items)
    return f"""    <section>
      <div class="wrap">
        <div class="section-head">
          <h2>{h2}</h2>
        </div>
        <div class="compare">
          <article class="go-new">
            <h3>{new_title}</h3>
            <ul>
{ni}
            </ul>
          </article>
          <article class="go-used">
            <h3>{used_title}</h3>
            <ul>
{ui}
            </ul>
          </article>
        </div>
      </div>
    </section>"""


def facts_row(facts):
    blocks = "\n".join(f'          <div class="fact"><span>{k}</span><strong>{v}</strong></div>' for k, v in facts)
    return f"""    <section>
      <div class="wrap">
        <div class="section-head">
          <h2>At a glance.</h2>
        </div>
        <div class="facts">
{blocks}
        </div>
      </div>
    </section>"""


def car_cards(p, card_list):
    arts = "\n".join(
        f'          <article class="car-card"><img src="{p}assets/{img}" alt="{year} {name}" loading="lazy" /><div class="car-body"><span class="tag">{year}</span><h3>{name}</h3><p>{desc}</p><p><a href="{href}">Learn more &rarr;</a></p></div></article>'
        for img, year, name, desc, href in card_list
    )
    return f"""    <section>
      <div class="wrap">
        <div class="cards">
{arts}
        </div>
      </div>
    </section>"""


def cards(card_list, two=False):
    cls = "cards two" if two else "cards"
    arts = "\n".join(
        f'          <article class="card"><span class="tag">{tag}</span><h3>{h3}</h3><p>{p}</p><p><a href="{href}">{label}</a></p></article>'
        for tag, h3, p, href, label in card_list
    )
    return f"""    <section>
      <div class="wrap">
        <div class="{cls}">
{arts}
        </div>
      </div>
    </section>"""


# ---------------------------------------------------------------- guides hub
page("../", "guides",
     "Car Buying Guides | Gus McClellan, Green Hyundai",
     "Straight answers to the questions people ask before they buy a car — trade-ins, new vs. used, first cars, EVs and hybrids. From Gus McClellan at Green Hyundai in Springfield, IL.",
     "https://gusatgreen.com/guides/",
     "Car buying guides", "Buying a car? Start here.",
     "Straight answers to the questions people actually ask before they buy — written to help, not to pressure you. Every guide ends the same way: text Gus, and he will take it from there. He has been doing this at the same store since 2013, and most of his business is repeat customers and referrals.",
     gus_note("Gus’s take", "Most people overthink the car and underthink the person selling it. Read the guide that fits you, then text Gus — he will give you a straight answer, new or used, before you ever set foot in the store.") + "\n" +
     cards([
         ("Guide", "Trading in your car", "Your current car is worth something — usually more than people expect. Here is how a trade-in works, what makes yours worth more, and how to get your number before you come in.", "trade-in/", "Read the guide →"),
         ("Guide", "New vs. used", "The honest answer: if the numbers work, buy new. If they don’t, buy used from someone you trust. Here is how to tell which one you are.", "new-vs-used/", "Read the guide →"),
         ("Guide", "Buying your first car", "First cars are exciting and a little nerve-wracking. Start with the monthly number, not the car — and have one person to call through the whole thing.", "first-car/", "Read the guide →"),
         ("Guide", "EVs and hybrids, explained", "Gas, hybrid, plug-in hybrid, and fully electric — in plain English. Which one fits how you actually drive.", "ev-hybrid/", "Read the guide →"),
     ]) + "\n" + cta_split("../", "Read a guide, then text Gus with what you are thinking. He will give you a straight answer — new or used — before you ever set foot in the store.") + "\n" + related("../", [
         ("models/", "Popular Hyundai models"),
         ("../#car-match", "Tell Gus what you need"),
         ("../about/", "More about Gus"),
     ]))

# ---------------------------------------------------------------- trade-in
page("../../", "guides/trade-in",
     "Trading In Your Car | Gus McClellan, Green Hyundai",
     "How trading in your car works at Green Hyundai in Springfield, IL — what your trade is worth, what makes it worth more, and how to get your number from Gus before you come in.",
     "https://gusatgreen.com/guides/trade-in/",
     "Car buying guide", "Trading in your car? Here’s how it works.",
     "Your current car is worth something — usually more than people expect — and trading it in is the simplest way to put that value toward your next one. Here is the whole process, with no surprises.",
     section("How a trade-in works",
             "You bring the car in, Gus looks it over, and he gives you a number. That number comes straight off the price of the car you are buying — you only pay the difference. In Illinois, the trade-in value also comes off the price before sales tax is figured, so you only pay tax on the difference too.",
             "If your car is worth more than the car you are buying, the difference comes back to you. And if you still owe money on your trade, Gus will walk you through exactly how that works — no guessing.") + "\n" +
     steps_block("Getting your number takes three steps", [
         ("Text Gus the details", "Year, make, model, and miles on your current car — a photo or two helps. He will give you a ballpark number before you ever come in."),
         ("Bring it in", "Gus looks the car over and gives you a real number. No games, and he will tell you straight if something is not a good fit."),
         ("Drive away", "The trade value comes off the price of your next car, and in Illinois you only pay sales tax on the difference."),
     ]) + "\n" +
     checklist_block("What makes your trade worth more", [
         "A car that runs, drives, and is cleaned out is worth more than the same car dirty and full of stuff — wash it and clear out the trunk and glove box.",
         "Bring both keys if you have them, and service records if you kept them.",
         "Be straight about the dents and the noises — Gus will find them anyway, and honesty gets you a real number faster.",
     ]) + "\n" +
     section("You don’t have to buy new to trade in",
             "A trade-in works toward a used car too. If a used car is the right call for your budget, Gus will find you a good one — a used sale beats no sale, and he would rather put you in the right car than the wrong one. The trade-in still counts the same way.") + "\n" +
     gus_note("The best moment to go new", "If you are trading in, it is usually the best moment to buy new: full factory warranty from day one, the latest safety tech, no unknown history, and you pick the exact car — color, features, all of it. Hyundai backs its new vehicles with a 10-year / 100,000-mile powertrain limited warranty, so you are covered long after the trade is forgotten.") + "\n" +
     cta_split("../../", "Text Gus the year, make, model, and miles on your current car — a photo or two helps — and he will give you a ballpark number before you ever come in.") + "\n" + related("../../", [
         ("../new-vs-used/", "New vs. used: which is right for you?"),
         ("../first-car/", "Buying your first car"),
         ("../../models/", "Popular Hyundai models"),
     ]))

# ---------------------------------------------------------------- new vs used
page("../../", "guides/new-vs-used",
     "New vs. Used Cars | Gus McClellan, Green Hyundai",
     "New or used — which is the better buy? The honest answer from Gus McClellan at Green Hyundai in Springfield, IL: if the numbers work, buy new. If they don’t, buy used from someone you trust.",
     "https://gusatgreen.com/guides/new-vs-used/",
     "Car buying guide", "New vs. used: which one is right for you?",
     "The honest answer: if the numbers work, buy new. If they don’t, buy used from someone you trust. Here is how to tell which one you are — and either way, Gus sells both, so you will get the straight answer, not a sales pitch.",
     compare_block("New or used, side by side",
         "New — usually the better buy",
         ["Full factory warranty from day one — Hyundai backs its new vehicles with a 10-year / 100,000-mile powertrain limited warranty",
          "The latest safety tech, and no unknown history",
          "You pick the exact car: the color, the features, all of it",
          "Financing is often cheaper on new cars too",
          "If the monthly payment fits, new is the easiest car to own"],
         "Used — the smart call when it fits",
         ["Costs less to buy and less per month",
          "Someone else already took the biggest depreciation hit",
          "Certified used Hyundais are inspected and carry extra coverage",
          "A good used car from the right place beats a new car you cannot afford"],
     ) + "\n" +
     gus_note("The middle ground", "<strong>Hyundai Certified Used</strong> vehicles are inspected before they go on the lot and carry additional warranty coverage. It is the closest thing to new without the new price — a good middle ground if new is just out of reach.") + "\n" +
     checklist_block("How to decide in five minutes", [
         "What monthly payment can you live with, including insurance?",
         "How long will you keep the car?",
         "Do you drive a lot — because warranty coverage matters more the more you drive?",
         "Do you need the latest safety features, for kids or for peace of mind?",
     ]) + "\n" +
     section("Then ask Gus",
             "Text Gus your budget and he will tell you which side of the line you are on — new or used — before you ever set foot in the store.") + "\n" +
     cta_split("../../", "Not sure which way to go? Tell Gus your routine and your budget, and he will narrow it down — honestly.") + "\n" + related("../../", [
         ("../trade-in/", "Trading in your car"),
         ("../first-car/", "Buying your first car"),
         ("../../models/", "Popular Hyundai models"),
     ]))

# ---------------------------------------------------------------- first car
page("../../", "guides/first-car",
     "Buying Your First Car | Gus McClellan, Green Hyundai",
     "Buying your first car in Springfield, IL — start with the monthly number, not the car. Gus McClellan at Green Hyundai walks first-time buyers through it, no pressure.",
     "https://gusatgreen.com/guides/first-car/",
     "Car buying guide", "Buying your first car.",
     "First cars are exciting and a little nerve-wracking. Here is how to do it without the regret — and why having one person to call makes the whole thing easier.",
     section("Start with the monthly number, not the car",
             "Figure out what you can pay each month — car payment plus insurance — before you fall in love with anything. Insurance is higher for first-time and younger drivers, so get an insurance quote on the car you are eyeing before you buy it. The right car is the one you can comfortably afford every month, not just the one you can drive off the lot today.") + "\n" +
     cards([
         ("New", "New for a first car", "Full warranty, no surprises, no wondering what the last owner did to it. If the payment fits, it is the best first car.", "../new-vs-used/", "New vs. used →"),
         ("Certified used", "Certified used for a first car", "Inspected, covered, and a lower payment. The next best thing — and Gus will be straight about which one fits your budget.", "../new-vs-used/", "New vs. used →"),
     ], two=True) + "\n" +
     checklist_block("What to bring", [
         "Your driver’s license.",
         "Proof of insurance — or arrange it before you drive off.",
         "Pay stubs, if you are financing.",
         "The title, if you have a car to trade in. That is about it — Gus handles the rest, and he will tell you ahead of time if anything else is needed.",
     ]) + "\n" +
     steps_block("The process with Gus", [
         ("Text first", "Tell Gus what you need and what you can spend, and he will narrow it down before you come in."),
         ("Come drive it", "Ask every question you have and take your time — there is no pressure, and he will tell you straight if something is not a good fit."),
         ("Drive it home", "Gus handles the paperwork and walks you through it — no guessing."),
         ("Same person after the sale", "If anything comes up, you call Gus. The relationship lasts past delivery day."),
     ]) + "\n" +
     cta_split("../../", "First car? Text Gus what you are looking for and what you can spend. He will take it from there.") + "\n" + related("../../", [
         ("../new-vs-used/", "New vs. used: which is right for you?"),
         ("../trade-in/", "Trading in your car"),
         ("../../models/elantra/", "Hyundai Elantra — a great first car"),
         ("../../models/kona/", "Hyundai Kona"),
     ]))

# ---------------------------------------------------------------- EV / hybrid
page("../../", "guides/ev-hybrid",
     "EVs and Hybrids, Explained | Gus McClellan, Green Hyundai",
     "Gas, hybrid, plug-in hybrid, or fully electric — in plain English. Which Hyundai fits how you actually drive, from Gus McClellan at Green Hyundai in Springfield, IL.",
     "https://gusatgreen.com/guides/ev-hybrid/",
     "Car buying guide", "Electric, hybrid, or gas? Here’s the simple version.",
     "Gas, hybrid, plug-in hybrid, and fully electric — Hyundai makes all four, and the right one depends on how you drive, not on what is trendy.",
     cards([
         ("Gas", "Gas", "Fill up anywhere, the simplest choice. No charging, no new habits.", "../../models/tucson/", "See the Tucson →"),
         ("Hybrid", "Hybrid", "A gas engine plus an electric motor — much better mileage without ever plugging in. The Tucson, Santa Fe, Palisade, and Elantra all come as hybrids.", "../../models/tucson/", "See the Tucson →"),
         ("Plug-in hybrid", "Plug-in hybrid", "Charge it at home and drive electric for daily trips, with gas there for long ones. The Tucson comes this way.", "../../models/tucson/", "See the Tucson →"),
         ("Electric", "Fully electric", "No gas at all, charge at home overnight, and the cheapest to run day to day. The IONIQ 5 and the Kona Electric.", "../../models/ioniq-5/", "See the IONIQ 5 →"),
     ], two=True) + "\n" +
     section("Who each one fits",
             "A hybrid is the easy switch — no lifestyle change, just fewer trips to the gas station, and it fits almost everyone. A plug-in hybrid fits if you have a short commute and can charge at home. Fully electric fits if you can charge at home and most of your driving is local — or if you are ready for fast chargers on road trips. If you cannot charge at home, a hybrid is the better call, and Gus will say so.") + "\n" +
     section("Charging, honestly",
             "Most EV owners charge at home overnight, the same way you charge your phone — you wake up to a full car. On road trips, fast chargers do the job: the IONIQ 5 can charge from 10% to 80% in about 20 minutes on a fast charger. If home charging is not an option for you, that is fine — that is exactly what the hybrids are for.") + "\n" +
     gus_note("New is the way to go here", "EV and hybrid tech moves fast — batteries, charging, and driver-assist tech all get better every year. Buying new gets you the latest version, the full factory warranty, and the newest safety tech. Incentives and tax credits change all the time, so ask Gus what is available right now rather than trusting something you read months ago.") + "\n" +
     cta_split("../../", "Curious about electric or hybrid? Tell Gus how you drive — commute, road trips, charging at home — and he will point you to the right one.") + "\n" + related("../../", [
         ("../../models/ioniq-5/", "Hyundai IONIQ 5 — fully electric"),
         ("../../models/tucson/", "Hyundai Tucson — gas, hybrid, or plug-in hybrid"),
         ("../../models/santa-fe/", "Hyundai Santa Fe — hybrid available"),
     ]))

# ---------------------------------------------------------------- models hub
page("../", "models",
     "New Hyundai Models | Gus McClellan, Green Hyundai",
     "The new Hyundai models people ask Gus about most — Tucson, Santa Fe, Palisade, Elantra, Kona, and the electric IONIQ 5. From Gus McClellan at Green Hyundai in Springfield, IL.",
     "https://gusatgreen.com/models/",
     "New Hyundai models", "The new Hyundai lineup.",
     "Gus sells the full new Hyundai lineup at Green Hyundai in Springfield — gas, hybrid, plug-in hybrid, and fully electric. These are the models people ask him about most. No prices or inventory here on purpose — that changes daily, so text Gus for what is on the lot right now.",
     car_cards("../", [
         ("hyundai-2026-tucson.webp", "2026", "Hyundai Tucson", "The do-everything compact SUV. Five seats, gas, hybrid, or plug-in hybrid — the one Gus recommends most.", "tucson/"),
         ("hyundai-2027-santa-fe.webp", "2027", "Hyundai Santa Fe", "Three rows for growing families, without going full-size. Gas or hybrid, six or seven seats.", "santa-fe/"),
         ("hyundai-2027-palisade.webp", "2027", "Hyundai Palisade", "The biggest Hyundai. Seven or eight seats, the most room in the lineup, now with a hybrid.", "palisade/"),
         ("hyundai-2026-elantra.webp", "2026", "Hyundai Elantra", "The commuter’s Hyundai. Five seats, great mileage, and a hybrid that sips fuel.", "elantra/"),
         ("hyundai-2027-kona.webp", "2027", "Hyundai Kona", "Small outside, roomy inside. The city-friendly SUV — gas or fully electric.", "kona/"),
         ("hyundai-2027-ioniq-5.webp", "2027", "Hyundai IONIQ 5", "The all-electric SUV. Five seats, very fast charging, and room to stretch out.", "ioniq-5/"),
     ]) + "\n" +
     info_split("Looking for used instead?",
             "Gus sells used Hyundais and used cars from other brands too — same store, same person to call. If a used car is the right call for your budget, he will find you a good one.",
             "Read the new vs. used guide first if you are torn — it will tell you which side of the line you are on.",
             "<a href=\"../guides/new-vs-used/\">New vs. used: which is right for you? &rarr;</a>") + "\n" +
     cta_split("../", "Know which one you want — or want Gus to pick for you? Text him and he will check what is on the lot.") + "\n" + related("../", [
         ("../guides/new-vs-used/", "New vs. used: which is right for you?"),
         ("../guides/ev-hybrid/", "EVs and hybrids, explained"),
         ("../#car-match", "Tell Gus what you need"),
     ]))


def model(slug, name, year, title_h1, intro, facts, sections, note, related_links, photo, coming_soon=None):
    body = f"""    <section>
      <div class="wrap">
        <figure class="car-hero">
          <img src="../../assets/{photo}" alt="{year} Hyundai {name}" />
          <figcaption>The {year} Hyundai {name}. Photo: Hyundai.</figcaption>
        </figure>
      </div>
    </section>"""
    body += "\n" + facts_row(facts)
    body += "\n" + info_split("See it in person.",
        "The cars are at Green Hyundai, 601 W. Stanford Ave. in Springfield. Text Gus before you come and he will have the one you want ready to drive — or tell you honestly if it is not there yet.",
        "<a href=\"https://www.greenhyundai.com/all-inventory/index.htm\" target=\"_blank\" rel=\"noopener\">Browse current inventory &nearr;</a> · <a href=\"https://www.hyundaiusa.com/us/en/vehicles\" target=\"_blank\" rel=\"noopener\">See photos of the whole lineup on Hyundai’s site &nearr;</a>")
    body += "\n" + "\n".join(section(h2, *paras) for h2, paras in sections)
    body += "\n" + gus_note("Why buy new", note)
    if coming_soon:
        body += "\n" + gus_note("Coming soon", coming_soon)
    body += "\n" + section("New or used?",
        "A new one gets you the full factory warranty, the latest safety tech, and your pick of color and features — and if the numbers work, that is the one Gus will usually steer you toward. A used one costs less and still gets the same person to call after the sale. Either way, you buy from Gus.",
        "Inventory, prices, and offers change daily, so text Gus for what is on the lot right now.")
    body += "\n" + cta_split("../../", f"Want a {name}? Text Gus and he will check what is on the lot — or what is coming in.")
    body += "\n" + related("../../", related_links)
    page("../../", f"models/{slug}",
         f"{year} Hyundai {name} | Gus McClellan, Green Hyundai",
         f"The {year} Hyundai {name} at Green Hyundai in Springfield, IL — {intro}",
         f"https://gusatgreen.com/models/{slug}/",
         f"Hyundai {name}", title_h1, intro, body)


# ---------------------------------------------------------------- Tucson
model("tucson", "Tucson", 2026, "The 2026 Hyundai Tucson.",
      "The do-everything compact SUV — five seats, room for the family and the gear, and your choice of gas, hybrid, or plug-in hybrid. It is the model Gus recommends most, because it fits the most people.",
      [("Seats", "5"), ("Powertrains", "Gas, hybrid, or plug-in hybrid"), ("Best for", "Families of four, commuters")],
      [("Why people pick the Tucson",
        ["It is the right size for most lives: big enough for car seats, strollers, and sports gear, small enough to park anywhere. Five seats, a roomy back seat, and a cargo area that handles the weekly shop and the weekend trip."]),
       ("Gas, hybrid, or plug-in hybrid?",
        ["Gas is the simplest choice and the lowest price to get in. The hybrid is the one most people end up happiest with — up to 38 mpg combined (EPA-estimated) with no plugging in and no change to how you drive. The plug-in hybrid charges at home and drives electric for daily trips, with gas there for long ones. Tell Gus your commute and he will point you to the right one."])],
      "A new Tucson gets the full factory warranty, the latest safety tech, and your pick of color and features — and hybrids hold their value well. If the payment fits, new is the way to go.",
      [("../santa-fe/", "Hyundai Santa Fe — need a third row?"),
       ("../ioniq-5/", "Hyundai IONIQ 5 — fully electric"),
       ("../../guides/new-vs-used/", "New vs. used: which is right for you?"),
       ("../../guides/ev-hybrid/", "EVs and hybrids, explained")],
      "hyundai-2026-tucson-hero.webp",
      coming_soon="The all-new 2027 Tucson has been revealed — bigger, redesigned from the ground up, with a new 1.6-liter turbo and hybrid options. It is not on the lot yet; text Gus to be first in line when it lands.")

# ---------------------------------------------------------------- Santa Fe
model("santa-fe", "Santa Fe", 2027, "The 2027 Hyundai Santa Fe.",
      "Three rows for growing families, without going full-size. Six or seven seats, a boxy shape that makes the inside huge, and a hybrid that sips fuel.",
      [("Seats", "6 or 7"), ("Powertrains", "Gas or hybrid"), ("Best for", "Growing families, carpools")],
      [("Three rows, without the full-size feel",
        ["The Santa Fe gives you a real third row — one that works for kids every day and for adults on shorter trips — in a midsize SUV that still fits in a normal garage and a normal parking spot. Fold the third row flat and the cargo space opens right up."]),
       ("Hybrid: the easy upgrade",
        ["The Santa Fe Hybrid gets up to 36 mpg combined (EPA-estimated) with no plugging in and no change to how you drive — same car, much better mileage. For most families, it is the version Gus recommends."])],
      "A new Santa Fe gets the full factory warranty, the newest safety tech for the people riding in those three rows, and your pick of seating layout — bench or captain’s chairs. If the payment fits, new is the way to go.",
      [("../palisade/", "Hyundai Palisade — need even more room?"),
       ("../tucson/", "Hyundai Tucson — the smaller SUV"),
       ("../../guides/new-vs-used/", "New vs. used: which is right for you?"),
       ("../../guides/ev-hybrid/", "EVs and hybrids, explained")],
      "hyundai-2027-santa-fe-hero.webp")

# ---------------------------------------------------------------- Palisade
model("palisade", "Palisade", 2027, "The 2027 Hyundai Palisade.",
      "The biggest Hyundai — seven or eight seats, the most room in the lineup, and now with a hybrid. For big families, road trips, and everything that comes with them.",
      [("Seats", "7 or 8"), ("Powertrains", "Gas or hybrid"), ("Best for", "Big families, road trips")],
      [("The biggest Hyundai",
        ["Three real rows, room for eight, and the biggest cargo space Hyundai makes — up to 86.7 cubic feet with the rear seats folded. Second-row captain’s chairs are available, so the third row is easy to reach. This is the one for families who actually fill all three rows."]),
       ("The new hybrid",
        ["The Palisade went all new for 2026, and the 2027 carries over the first-ever hybrid — up to 34 mpg combined (EPA-estimated) in a full-size three-row SUV. Big car, much better mileage, no plugging in."])],
      "A new Palisade gets the full factory warranty, the newest safety tech, and your pick of seating and features. It is the flagship for a reason — and if the payment fits, new is the way to go.",
      [("../santa-fe/", "Hyundai Santa Fe — three rows, smaller footprint"),
       ("../tucson/", "Hyundai Tucson"),
       ("../../guides/new-vs-used/", "New vs. used: which is right for you?"),
       ("../../guides/trade-in/", "Trading in your car")],
      "hyundai-2027-palisade-hero.webp")

# ---------------------------------------------------------------- Elantra
model("elantra", "Elantra", 2026, "The 2026 Hyundai Elantra.",
      "The commuter’s Hyundai — a compact sedan with five seats, great mileage, and a hybrid that barely sips fuel. Low cost to buy, low cost to run.",
      [("Seats", "5"), ("Powertrains", "Gas or hybrid"), ("Best for", "Commuters, first cars")],
      [("The commuter’s Hyundai",
        ["The Elantra is built for the daily drive: comfortable, quiet, easy to park, and cheap to run. Five seats, a real trunk, and everything you need without paying for size you will not use."]),
       ("Hybrid: the mileage king",
        ["The Elantra Hybrid gets up to 54 mpg combined (EPA-estimated) — the best mileage in the Hyundai lineup. If you drive a lot, the fuel savings alone can cover a real chunk of the payment."]),
       ("A great first car",
        ["Low price, low insurance compared to an SUV, full warranty, and nothing to worry about — the Elantra is one of the best first cars Gus sells. Read the first-car guide, then text him."])],
      "A new Elantra gets the full factory warranty, the newest safety tech, and your pick of color and features — and at this price, the payment usually works. If it fits, new is the way to go.",
      [("../../guides/first-car/", "Buying your first car"),
       ("../kona/", "Hyundai Kona — want an SUV instead?"),
       ("../../guides/new-vs-used/", "New vs. used: which is right for you?"),
       ("../../guides/ev-hybrid/", "EVs and hybrids, explained")],
      "hyundai-2026-elantra-hero.webp",
      coming_soon="The redesigned 2027 Elantra is coming — bigger and bolder, with a hybrid rated up to 53 mpg combined (EPA-estimated). The first 2027s reach dealers early next year; the hybrid follows as a 2028. Text Gus to be first in line.")

# ---------------------------------------------------------------- Kona
model("kona", "Kona", 2027, "The 2027 Hyundai Kona.",
      "Small outside, roomy inside. The city-friendly SUV — easy to park, easy on gas, and available as a fully electric Kona Electric.",
      [("Seats", "5"), ("Powertrains", "Gas or fully electric"), ("Best for", "City driving, a first SUV")],
      [("Small outside, roomy inside",
        ["The Kona is the smallest Hyundai SUV, and that is the point: it slips into tight parking spots and tight garages, but the inside is roomy for five people and their stuff. It is a great first SUV, and a great second car."]),
       ("Gas or electric?",
        ["The gas Kona is simple and affordable. The Kona Electric — the 2025 model, while stock lasts — is fully electric with up to 261 miles of range (EPA-estimated). Charge at home overnight and skip gas stations entirely. Availability varies, so ask Gus what is in stock."])],
      "A new Kona gets the full factory warranty and the newest safety tech, and the electric version gets the latest battery. If the payment fits, new is the way to go.",
      [("../elantra/", "Hyundai Elantra — the sedan option"),
       ("../ioniq-5/", "Hyundai IONIQ 5 — the bigger electric SUV"),
       ("../../guides/first-car/", "Buying your first car"),
       ("../../guides/ev-hybrid/", "EVs and hybrids, explained")],
      "hyundai-2027-kona-hero.webp")

# ---------------------------------------------------------------- Ioniq 5
model("ioniq-5", "IONIQ 5", 2027, "The 2027 Hyundai IONIQ 5.",
      "The all-electric SUV — five seats, very fast charging, and room to stretch out. Electric without the compromises.",
      [("Seats", "5"), ("Powertrains", "Fully electric, rear- or all-wheel drive"), ("Best for", "Going electric, fast charging")],
      [("Electric without the compromises",
        ["The IONIQ 5 is a proper SUV that happens to be electric: five seats, a flat floor, sliding rear seats, and more rear legroom than most gas SUVs its size. No gas, no oil changes, and the cheapest daily running costs in the lineup."]),
       ("Charging in real life",
        ["Most owners charge at home overnight and wake up to a full car. On road trips, fast chargers do the job — the IONIQ 5 can charge from 10% to 80% in about 20 minutes on a fast charger. If you cannot charge at home, a hybrid is the better call, and Gus will say so."])],
      "EV tech moves fast — batteries, charging, and driver-assist tech all get better every year. Buying new gets you the latest version, the full factory warranty, and the newest safety tech. That is why Gus recommends new here more than anywhere.",
      [("../kona/", "Hyundai Kona — the smaller electric option"),
       ("../tucson/", "Hyundai Tucson — hybrid instead?"),
       ("../../guides/ev-hybrid/", "EVs and hybrids, explained"),
       ("../../guides/new-vs-used/", "New vs. used: which is right for you?")],
      "hyundai-2027-ioniq-5-hero.webp")

print("done")
