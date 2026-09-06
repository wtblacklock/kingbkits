import os, sys
REPO = "/Users/BIGWilly/Projects/kingbkits"
sys.path.insert(0, os.path.join(REPO, "scripts"))
from gen_clean_listing import (write, bokeh, single_image_slide, hero_slide, bundle_slide,
                                hero_bg_only, paper_bg, paper_pal)

SHADOW = "0 10px 24px rgba(40,32,18,0.16), 0 50px 80px -30px rgba(40,32,18,0.28)"

# Advent gets its own daylight "tracking desk" look - warm paper, a faint
# calendar grid, pine + gold accents - not the party kits' after-dark bar.
# This product is a companion you use alone each night, not a hosting kit.
GOLD = "255,196,90"

def advent_bg():
    checks = bokeh([(140, 1750, 5, 0.5, 3), (1850, 120, 5, 0.5, 3), (1920, 1800, 5, 0.4, 3)],
                    rgb="47,74,58")
    return paper_bg(accent_rgb=GOLD, motif=checks)


bg, pal = advent_bg(), paper_pal("0.12")

SRC = f"{REPO}/listing_images_raw/listing_images_advent"
OUT = f"{REPO}/listing_marketing/listing_clean_advent"
os.makedirs(OUT, exist_ok=True)

# 1. HERO - one tracking card front and center, not a fan of pages. This is a
# tool you use each night, so the hero should read "here's the sheet" not
# "here's a stack of paper."
pages = f"""
<div style="position:absolute;left:50%;top:660px;transform:translateX(-50%) rotate(-1.5deg);">
  <img src="{SRC}/page-9.png" style="width:1080px;box-shadow:{SHADOW};border-radius:6px;">
</div>
<div style="position:absolute;left:18%;top:1420px;transform:translateX(-50%) rotate(-8deg);">
  <img src="{SRC}/page-2.png" style="width:520px;box-shadow:{SHADOW};border-radius:6px;">
</div>
<div style="position:absolute;left:83%;top:1440px;transform:translateX(-50%) rotate(7deg);">
  <img src="{SRC}/page-8.png" style="width:540px;box-shadow:{SHADOW};border-radius:6px;">
</div>"""
write(OUT, "1-hero.html", bg, pal, hero_slide(
    "The Whisky Advent Companion", "Track Every<br>Night",
    "The printable sheet for a calendar you already own &middot; Instant Download",
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

write(OUT, "site-hero.html", bg, pal, hero_bg_only(""))
write(OUT, "site-card.html", bg, pal, hero_bg_only(pages))

# 7. BUNDLE / What's Inside
bundle_pages = f"""
<div style="position:absolute;left:66%;top:640px;transform:translateX(-50%) rotate(-6deg);">
  <img src="{SRC}/page-8.png" style="width:620px;box-shadow:{SHADOW};border-radius:6px;">
</div>
<div style="position:absolute;left:88%;top:900px;transform:translateX(-50%) rotate(5deg);">
  <img src="{SRC}/page-9.png" style="width:600px;box-shadow:{SHADOW};border-radius:6px;">
</div>"""
items = ["How to Use", "24 Numbered Tasting Cards (6 sheets)", "Month Tracker", "Flavor Wheel"]
write(OUT, "7-bundle.html", bg, pal, bundle_slide(pal, "9 Pages", items, bundle_pages))

print("advent clean slides written")
