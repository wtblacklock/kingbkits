import os, sys
REPO = "/Users/BIGWilly/Projects/kingbkits"
sys.path.insert(0, os.path.join(REPO, "scripts"))
from gen_clean_listing import (write, bokeh, single_image_slide, hero_slide, bundle_slide,
                                hero_bg_only, midnight_bg, midnight_pal)

SHADOW = "0 14px 30px rgba(0,0,0,0.6), 0 90px 130px -40px rgba(0,0,0,0.95)"

# Advent: a string of warm gold fairy lights against a near-black winter evening,
# with a whisper of pine green - the one kit where the motif is literally decor
# from the occasion itself, not an ambient add-on.
TINT = "#1c160d"
GLOW1 = "255,215,120"
GLOW2 = "70,120,85"


def advent_bg():
    lights = bokeh([(120, 210, 9, 0.6, 6), (340, 160, 7, 0.5, 5), (600, 240, 8, 0.55, 6),
                     (900, 150, 7, 0.5, 5), (1220, 230, 9, 0.6, 6), (1500, 160, 7, 0.5, 5),
                     (1780, 220, 8, 0.55, 6), (1900, 900, 7, 0.4, 8)], rgb=GLOW1)
    return midnight_bg(TINT, GLOW1, glow2_rgb=GLOW2, motif=lights)


bg, pal = advent_bg(), midnight_pal("0.3")

SRC = f"{REPO}/listing_images_raw/listing_images_advent"
OUT = f"{REPO}/listing_marketing/listing_clean_advent"
os.makedirs(OUT, exist_ok=True)

# 1. HERO
pages = f"""
<div style="position:absolute;left:24%;top:800px;transform:translateX(-50%) rotate(-6deg);">
  <img src="{SRC}/page-1.png" style="width:840px;box-shadow:{SHADOW};filter:brightness(0.9);">
</div>
<div style="position:absolute;left:50%;top:720px;transform:translateX(-50%) rotate(0deg);">
  <img src="{SRC}/page-9.png" style="width:920px;box-shadow:{SHADOW};">
</div>
<div style="position:absolute;left:76%;top:800px;transform:translateX(-50%) rotate(6deg);">
  <img src="{SRC}/page-6.png" style="width:840px;box-shadow:{SHADOW};">
</div>"""
write(OUT, "1-hero.html", bg, pal, hero_slide(
    "The Whisky Advent Companion", "24 Nights<br>of Whisky",
    "A tasting card for every night, a tracker, and a flavor wheel &middot; Instant Download",
    pal, pages, tiers=False))

singles = [
    ("2-guide.html",   "01 &middot; How to Use",      "page-1.png"),
    ("3-cards.html",   "02&ndash;07 &middot; Tasting Cards", "page-2.png"),
    ("4-tracker.html", "08 &middot; Month Tracker",   "page-8.png"),
    ("5-wheel.html",   "09 &middot; Flavor Wheel",    "page-9.png"),
    ("6-more.html",    "02&ndash;07 &middot; Tasting Cards", "page-6.png"),
]
for fname, cap, img in singles:
    write(OUT, fname, bg, pal, single_image_slide(cap, f"{SRC}/{img}", pal["eyebrow"], w=1520, top=300, shadow=SHADOW))

write(OUT, "site-hero.html", bg, pal, hero_bg_only(pages))

# 7. BUNDLE / What's Inside
bundle_pages = f"""
<div style="position:absolute;left:66%;top:640px;transform:translateX(-50%) rotate(-6deg);">
  <img src="{SRC}/page-8.png" style="width:620px;box-shadow:{SHADOW};">
</div>
<div style="position:absolute;left:88%;top:900px;transform:translateX(-50%) rotate(5deg);">
  <img src="{SRC}/page-9.png" style="width:600px;box-shadow:{SHADOW};">
</div>"""
items = ["How to Use", "24 Numbered Tasting Cards (6 sheets)", "Month Tracker", "Flavor Wheel"]
write(OUT, "7-bundle.html", bg, pal, bundle_slide(pal, "9 Pages", items, bundle_pages))

print("advent clean slides written")
