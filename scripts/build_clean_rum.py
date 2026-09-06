import os, sys
REPO = "/Users/BIGWilly/Projects/kingbkits"
sys.path.insert(0, os.path.join(REPO, "scripts"))
from gen_clean_listing import (write, bokeh, single_image_slide, hero_slide, bundle_slide,
                                hero_bg_only, midnight_bg, midnight_pal)

SHADOW = "0 14px 30px rgba(0,0,0,0.6), 0 90px 130px -40px rgba(0,0,0,0.95)"

# Rum & Tiki: deep tropical-night green-black with warm amber rum glow and a
# lime/tiki-teal secondary glow - distinct from cigar's mahogany, agave's
# terracotta, and halloween's violet, but still the same after-dark party look.
TINT = "#182417"
GLOW1 = "255,175,90"
GLOW2 = "90,215,150"


def rum_bg():
    fireflies = bokeh([(120, 200, 8, 0.5, 6), (1830, 160, 7, 0.42, 5), (1720, 920, 9, 0.4, 8),
                        (260, 950, 7, 0.35, 6), (1080, 130, 6, 0.4, 5)], rgb=GLOW2)
    return midnight_bg(TINT, GLOW1, glow2_rgb=GLOW2, motif=fireflies)


bg, pal = rum_bg(), midnight_pal("0.32")

SRC = f"{REPO}/listing_images_raw/listing_images_rum"
OUT = f"{REPO}/listing_marketing/listing_clean_rum"
os.makedirs(OUT, exist_ok=True)

# 1. HERO
pages = f"""
<div style="position:absolute;left:24%;top:780px;transform:translateX(-50%) rotate(-6deg);">
  <img src="{SRC}/page-2.png" style="width:860px;box-shadow:{SHADOW};filter:brightness(0.9);">
</div>
<div style="position:absolute;left:50%;top:700px;transform:translateX(-50%) rotate(0deg);">
  <img src="{SRC}/page-4.png" style="width:930px;box-shadow:{SHADOW};">
</div>
<div style="position:absolute;left:76%;top:780px;transform:translateX(-50%) rotate(6deg);">
  <img src="{SRC}/page-1.png" style="width:860px;box-shadow:{SHADOW};">
</div>"""
write(OUT, "1-hero.html", bg, pal, hero_slide(
    "The Rum &amp; Tiki Journey", "Rum &amp; Tiki",
    "8-Page Printable Tasting Kit &middot; Instant Download", pal, pages))

singles = [
    ("2-guide.html",    "01 &middot; Party Guide",     "page-1.png"),
    ("3-primer.html",   "02 &middot; Tiki Primer",     "page-2.png"),
    ("4-rumbase.html",  "03 &middot; Rumbase",         "page-3.png"),
    ("5-wheels.html",   "04 &middot; Flavor Wheels",   "page-4.png"),
    ("6-cards.html",    "05&ndash;07 &middot; Tasting Cards", "page-6.png"),
]
for fname, cap, img in singles:
    write(OUT, fname, bg, pal, single_image_slide(cap, f"{SRC}/{img}", pal["eyebrow"], w=1520, top=300, shadow=SHADOW))

write(OUT, "site-hero.html", bg, pal, hero_bg_only(""))
write(OUT, "site-card.html", bg, pal, hero_bg_only(pages))

# 7. BUNDLE
bundle_pages = f"""
<div style="position:absolute;left:66%;top:640px;transform:translateX(-50%) rotate(-6deg);">
  <img src="{SRC}/page-5.png" style="width:620px;box-shadow:{SHADOW};">
</div>
<div style="position:absolute;left:88%;top:900px;transform:translateX(-50%) rotate(5deg);">
  <img src="{SRC}/page-7.png" style="width:600px;box-shadow:{SHADOW};">
</div>"""
items = ["Party Guide", "Tiki Primer", "Rumbase", "Flavor Wheels",
         "Tasting Cards (3 tiers)", "Checklist &amp; Scorecard", "Invitation template"]
write(OUT, "7-bundle.html", bg, pal, bundle_slide(pal, "8 Pages", items, bundle_pages))

print("rum clean slides written")
