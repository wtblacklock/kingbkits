import os, sys
REPO = "/Users/BIGWilly/Projects/kingbkits"
sys.path.insert(0, os.path.join(REPO, "scripts"))
from gen_clean_listing import (write, bokeh, confetti, single_image_slide, hero_slide, bundle_slide,
                                photo_slide, hero_bg_only, midnight_bg, midnight_pal)

SHADOW = "0 14px 30px rgba(0,0,0,0.6), 0 90px 130px -40px rgba(0,0,0,0.95)"

# ======================================================================
#  AGAVE - patio at dusk: warm terracotta glow + a cool agave-turquoise
#  counter-glow, keeping the two-tone identity the old warm version had.
# ======================================================================
TINT_A = "#241811"
GLOW_A1 = "255,150,70"
GLOW_A2 = "90,210,190"


def agave_bg():
    dust = bokeh([(160, 260, 8, 0.4, 12), (1800, 200, 7, 0.32, 12), (1720, 940, 6, 0.3, 10)], rgb=GLOW_A2)
    return midnight_bg(TINT_A, GLOW_A1, glow2_rgb=GLOW_A2, motif=dust)


bg_a, pal_a = agave_bg(), midnight_pal("0.3")

SRC_A = f"{REPO}/listing_images_raw/listing_images_agave"
OUT_A = f"{REPO}/listing_marketing/listing_clean_agave"
os.makedirs(OUT_A, exist_ok=True)

pages_a = f"""
<div style="position:absolute;left:24%;top:780px;transform:translateX(-50%) rotate(-6deg);">
  <img src="{SRC_A}/page-2.png" style="width:860px;box-shadow:{SHADOW};filter:brightness(0.9);">
</div>
<div style="position:absolute;left:50%;top:700px;transform:translateX(-50%) rotate(0deg);">
  <img src="{SRC_A}/page-4.png" style="width:930px;box-shadow:{SHADOW};">
</div>
<div style="position:absolute;left:76%;top:780px;transform:translateX(-50%) rotate(6deg);">
  <img src="{SRC_A}/page-1.png" style="width:860px;box-shadow:{SHADOW};">
</div>"""
write(OUT_A, "1-hero.html", bg_a, pal_a, hero_slide(
    "The Agave Tasting Journey", "Tequila &amp;<br>Mezcal",
    "Six pairings, three tiers, one backyard-ready night &middot; Instant Download",
    pal_a, pages_a))

singles_a = [
    ("2-guide.html",     "01 &middot; Party Guide",           "page-1.png"),
    ("3-primer.html",    "02 &middot; Primer",                "page-2.png"),
    ("4-agavebase.html", "03 &middot; Agavebase",             "page-3.png"),
    ("5-wheels.html",    "04 &middot; Flavor Wheels",         "page-4.png"),
    ("6-cards.html",     "05&ndash;07 &middot; Tasting Cards", "page-6.png"),
]
for fname, cap, img in singles_a:
    write(OUT_A, fname, bg_a, pal_a, single_image_slide(cap, f"{SRC_A}/{img}", pal_a["eyebrow"], w=1520, top=300, shadow=SHADOW))

bundle_pages_a = f"""
<div style="position:absolute;left:66%;top:640px;transform:translateX(-50%) rotate(-6deg);">
  <img src="{SRC_A}/page-5.png" style="width:620px;box-shadow:{SHADOW};">
</div>
<div style="position:absolute;left:88%;top:900px;transform:translateX(-50%) rotate(5deg);">
  <img src="{SRC_A}/page-7.png" style="width:600px;box-shadow:{SHADOW};">
</div>"""
items_a = ["Party Guide", "Agave Primer", "Agavebase (bottle matches)", "Flavor Wheels",
           "Tasting Cards (3 tiers)", "Checklist &amp; Scorecard", "Invitation template"]
write(OUT_A, "7-bundle.html", bg_a, pal_a, bundle_slide(pal_a, "8 Pages", items_a, bundle_pages_a))

write(OUT_A, "site-hero.html", bg_a, pal_a, hero_bg_only(""))
write(OUT_A, "site-card.html", bg_a, pal_a, hero_bg_only(pages_a))

INVITE_PHOTO_A = f"{REPO}/ETSY_UPLOAD/agave/08-invite.png"
write(OUT_A, "8-invite.html", bg_a, pal_a, photo_slide("08 &middot; Invitation Template", INVITE_PHOTO_A, pal_a["eyebrow"]))

print("agave clean slides written")


# ======================================================================
#  HALLOWEEN - haunted violet glow + a warm pumpkin-orange counter-glow,
#  candy-corn confetti scattered like spilled candy, not decorative orbs.
# ======================================================================
TINT_H = "#1c1420"
GLOW_H1 = "170,110,220"
GLOW_H2 = "255,140,60"


def halloween_bg():
    candy = confetti([(140, 780, 8, "#ffb703", 0.4), (1840, 700, 7, "#e0763a", 0.35),
                       (1700, 150, 6, "#c94f7a", 0.38), (300, 150, 6, "#ffb703", 0.3),
                       (1600, 960, 6, "#e0763a", 0.3)])
    return midnight_bg(TINT_H, GLOW_H1, glow2_rgb=GLOW_H2, motif=candy)


bg_h, pal_h = halloween_bg(), midnight_pal("0.32")

SRC_H = f"{REPO}/listing_images_raw/listing_images_halloween"
OUT_H = f"{REPO}/listing_marketing/listing_clean_halloween"
os.makedirs(OUT_H, exist_ok=True)

pages_h = f"""
<div style="position:absolute;left:24%;top:780px;transform:translateX(-50%) rotate(-6deg);">
  <img src="{SRC_H}/page-2.png" style="width:860px;box-shadow:{SHADOW};filter:brightness(0.9);">
</div>
<div style="position:absolute;left:50%;top:700px;transform:translateX(-50%) rotate(0deg);">
  <img src="{SRC_H}/page-4.png" style="width:930px;box-shadow:{SHADOW};">
</div>
<div style="position:absolute;left:76%;top:780px;transform:translateX(-50%) rotate(6deg);">
  <img src="{SRC_H}/page-1.png" style="width:860px;box-shadow:{SHADOW};">
</div>"""
write(OUT_H, "1-hero.html", bg_h, pal_h, hero_slide(
    "The Halloween Pairing Kit", "Candy &amp;<br>Whisky",
    "Six pairings, three tiers, one candy-bowl-ready night &middot; Instant Download",
    pal_h, pages_h))

singles_h = [
    ("2-guide.html",    "01 &middot; Party Guide",           "page-1.png"),
    ("3-primer.html",   "02 &middot; Primer",                "page-2.png"),
    ("4-pairbase.html", "03 &middot; Pairbase",              "page-3.png"),
    ("5-wheels.html",   "04 &middot; Flavor Wheels",         "page-4.png"),
    ("6-cards.html",    "05&ndash;07 &middot; Tasting Cards", "page-6.png"),
]
for fname, cap, img in singles_h:
    write(OUT_H, fname, bg_h, pal_h, single_image_slide(cap, f"{SRC_H}/{img}", pal_h["eyebrow"], w=1520, top=300, shadow=SHADOW))

bundle_pages_h = f"""
<div style="position:absolute;left:66%;top:640px;transform:translateX(-50%) rotate(-6deg);">
  <img src="{SRC_H}/page-5.png" style="width:620px;box-shadow:{SHADOW};">
</div>
<div style="position:absolute;left:88%;top:900px;transform:translateX(-50%) rotate(5deg);">
  <img src="{SRC_H}/page-7.png" style="width:600px;box-shadow:{SHADOW};">
</div>"""
items_h = ["Party Guide", "Candy Primer", "Pairbase (bottle matches)", "Flavor Wheels",
           "Tasting Cards (3 tiers)", "Checklist &amp; Scorecard", "Invitation template"]
write(OUT_H, "7-bundle.html", bg_h, pal_h, bundle_slide(pal_h, "8 Pages", items_h, bundle_pages_h))

write(OUT_H, "site-hero.html", bg_h, pal_h, hero_bg_only(""))
write(OUT_H, "site-card.html", bg_h, pal_h, hero_bg_only(pages_h))

INVITE_PHOTO_H = f"{REPO}/ETSY_UPLOAD/halloween/08-invite.png"
write(OUT_H, "8-invite.html", bg_h, pal_h, photo_slide("08 &middot; Invitation Template", INVITE_PHOTO_H, pal_h["eyebrow"]))

print("halloween clean slides written")
