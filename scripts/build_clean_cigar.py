import os, sys
REPO = "/Users/BIGWilly/Projects/kingbkits"
sys.path.insert(0, os.path.join(REPO, "scripts"))
from gen_clean_listing import (write, bokeh, single_image_slide, hero_slide, bundle_slide,
                                photo_slide, hero_bg_only, midnight_bg, midnight_pal)

SHADOW = "0 14px 30px rgba(0,0,0,0.6), 0 90px 130px -40px rgba(0,0,0,0.95)"

# Cigar lounge at night: warm ember glow off a cigar cherry, deep mahogany-black base.
TINT = "#241a12"
GLOW = "255,175,90"


def cigar_bg():
    embers = bokeh([(150, 250, 10, 0.55, 10), (1820, 190, 8, 0.45, 8), (1700, 900, 9, 0.4, 10),
                     (260, 940, 7, 0.35, 8), (1120, 140, 6, 0.4, 6)], rgb=GLOW)
    return midnight_bg(TINT, GLOW, motif=embers)


bg, pal = cigar_bg(), midnight_pal("0.32")

SRC = f"{REPO}/listing_images_raw/listing_images"
OUT = f"{REPO}/listing_marketing/listing_clean_cigar"
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
    "The Cigar &amp; Whisky Journey", "Cigar &amp;<br>Whisky",
    "Six pairings, three tiers, one lounge-ready night &middot; Instant Download",
    pal, pages))

singles = [
    ("2-guide.html",    "01 &middot; Party Guide",           "page-1.png"),
    ("3-primer.html",   "02 &middot; Primer",                "page-2.png"),
    ("4-pairbase.html", "03 &middot; Pairbase",              "page-3.png"),
    ("5-wheels.html",   "04 &middot; Flavor Wheels",         "page-4.png"),
    ("6-cards.html",    "05&ndash;07 &middot; Pairing Cards", "page-6.png"),
]
for fname, cap, img in singles:
    write(OUT, fname, bg, pal, single_image_slide(cap, f"{SRC}/{img}", pal["eyebrow"], w=1520, top=300, shadow=SHADOW))

# 7. BUNDLE / What's Inside
bundle_pages = f"""
<div style="position:absolute;left:66%;top:640px;transform:translateX(-50%) rotate(-6deg);">
  <img src="{SRC}/page-5.png" style="width:620px;box-shadow:{SHADOW};">
</div>
<div style="position:absolute;left:88%;top:900px;transform:translateX(-50%) rotate(5deg);">
  <img src="{SRC}/page-7.png" style="width:600px;box-shadow:{SHADOW};">
</div>"""
items = ["Party Guide", "Cigar &amp; Whisky Primer", "Pairbase (bottle + leaf matches)",
         "Flavor Wheels", "Pairing Cards (3 tiers)", "Checklist &amp; Scorecard", "Invitation template"]
write(OUT, "7-bundle.html", bg, pal, bundle_slide(pal, "8 Pages", items, bundle_pages))

# SITE HERO — same background + fanned pages, no baked-in text (the marketing
# site overlays its own heading on top; text-in-text would duplicate/garble).
write(OUT, "site-hero.html", bg, pal, hero_bg_only(""))

# 8. INVITE — reframe the existing lifestyle photo in the same dark system
INVITE_PHOTO = f"{REPO}/ETSY_UPLOAD/cigar/08-invite.png"
write(OUT, "8-invite.html", bg, pal, photo_slide("08 &middot; Invitation Template", INVITE_PHOTO, pal["eyebrow"]))

print("cigar clean slides written")
