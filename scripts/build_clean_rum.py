import os, sys
REPO = "/Users/BIGWilly/Projects/kingbkits"
sys.path.insert(0, os.path.join(REPO, "scripts"))
from gen_clean_listing import (write, bokeh, single_image_slide, hero_slide, bundle_slide,
                                hero_bg_only, tropical_bg, tropical_pal)

SHADOW = "0 14px 30px rgba(0,0,0,0.55), 0 90px 130px -40px rgba(0,0,0,0.8)"

# Rum & Tiki: loud, lively tropical sunset (teal -> hot pink -> orange-gold)
# with palm fronds fanning in from two corners - real tiki-menu-art energy,
# a deliberate departure from the other kits' moody after-dark bar look.
sparkle = bokeh([(120, 200, 7, 0.6, 5), (1850, 220, 6, 0.55, 4), (1780, 1000, 7, 0.5, 6),
                  (220, 1020, 6, 0.5, 5)], rgb="255,255,255")

bg, pal = tropical_bg(motif=sparkle), tropical_pal()

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
