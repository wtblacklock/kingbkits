import os, sys
REPO = "/Users/BIGWilly/Projects/kingbkits"
sys.path.insert(0, os.path.join(REPO, "scripts"))
from gen_clean_listing import write, bokeh, confetti, single_image_slide, hero_slide, badge

SHADOW_DARK = "0 14px 30px rgba(0,0,0,0.55), 0 90px 130px -40px rgba(0,0,0,0.9)"
SHADOW_LIGHT = "0 10px 22px rgba(70,45,20,0.3), 0 70px 100px -34px rgba(70,45,20,0.5)"


# ======================================================================
#  AGAVE - warm terracotta/concrete patio counter, not a wood bar.
#  Distinct material + a cool turquoise accent (agave-blue) against cigar's amber.
# ======================================================================
def agave_bar(horizon=560):
    bg = f"""
<div style="position:absolute;inset:0;background:
  radial-gradient(ellipse 1600px 1300px at 66% 14%,#9a5230 0%,#6b3620 40%,#3c1f14 76%,#1e100a 100%);"></div>
<div style="position:absolute;left:760px;top:-320px;width:1560px;height:1750px;
  background:radial-gradient(ellipse at 50% 30%,rgba(90,205,185,0.30),rgba(255,150,70,0.14) 46%,rgba(0,0,0,0) 68%);
  filter:blur(24px);"></div>
<div style="position:absolute;left:0;right:0;top:120px;height:900px;filter:url(#haze);
  opacity:0.16;mix-blend-mode:screen;background:#f0d8ae;"></div>
{bokeh([(150,250,150,0.32,26),(1800,180,150,0.24,26)])}
{bokeh([(420,150,96,0.4,18),(1560,330,120,0.36,22),(940,120,84,0.34,16),(260,520,80,0.3,16)], rgb="90,210,190")}
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;
  background:linear-gradient(180deg,#b06f45 0%,#7a4a2c 45%,#48301e 100%);"></div>
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;filter:url(#stone);
  opacity:0.46;mix-blend-mode:multiply;background:#3e2818;"></div>
<div style="position:absolute;left:0;right:0;top:{horizon}px;height:9px;
  background:linear-gradient(180deg,rgba(90,210,190,0.4),rgba(90,210,190,0));"></div>"""
    return bg, dict(eyebrow="#f0a860", head="#fbeddb", sub="#e6c8a8", grain="0.36")


# Pale travertine / caliche stone counter - warm sand tones, mottled speckle not wood grain.
def agave_bright(horizon=1900):
    bg = f"""
<div style="position:absolute;inset:0;background:
  linear-gradient(172deg,#f3ecdd 0%,#ebdfc4 46%,#dfcda3 58%,#c7ac7c 100%);"></div>
<div style="position:absolute;left:-220px;top:-320px;width:1550px;height:1550px;
  background:radial-gradient(circle,rgba(255,255,255,0.82),rgba(255,255,255,0) 62%);"></div>
<div style="position:absolute;inset:0;filter:url(#stone);opacity:0.4;mix-blend-mode:multiply;background:#9c8256;"></div>
<div style="position:absolute;inset:0;filter:url(#stone-fine);opacity:0.55;mix-blend-mode:overlay;background:#fff;"></div>"""
    return bg, dict(eyebrow="#8a6338", head="#241a0c", sub="#5a4128", grain="0.24")


SRC_A = f"{REPO}/listing_images_raw/listing_images_agave"
OUT_A = f"{REPO}/listing_marketing/listing_clean_agave"
os.makedirs(OUT_A, exist_ok=True)

# 1. HERO
bg, pal = agave_bar()
pages = f"""
<div style="position:absolute;left:24%;top:780px;transform:translateX(-50%) rotate(-6deg);">
  <img src="{SRC_A}/page-2.png" style="width:860px;box-shadow:{SHADOW_DARK};filter:brightness(0.88);">
</div>
<div style="position:absolute;left:50%;top:700px;transform:translateX(-50%) rotate(0deg);">
  <img src="{SRC_A}/page-4.png" style="width:930px;box-shadow:{SHADOW_DARK};">
</div>
<div style="position:absolute;left:76%;top:780px;transform:translateX(-50%) rotate(6deg);">
  <img src="{SRC_A}/page-1.png" style="width:860px;box-shadow:{SHADOW_DARK};">
</div>"""
write(OUT_A, "1-hero.html", bg, pal, hero_slide(
    "The Agave Tasting Journey", "Tequila &amp; Mezcal", "8-Page Printable Tasting Kit &middot; Instant Download",
    pal, pages))

singles = [
    ("2-guide.html",    "01 &middot; Party Guide",     "page-1.png", agave_bar,    "#e0c397"),
    ("3-primer.html",   "02 &middot; Primer",          "page-2.png", agave_bright, "#8a6338"),
    ("4-agavebase.html","03 &middot; Agavebase",       "page-3.png", agave_bar,    "#e0c397"),
    ("5-wheels.html",   "04 &middot; Flavor Wheels",   "page-4.png", agave_bright, "#8a6338"),
    ("6-cards.html",    "05&ndash;07 &middot; Tasting Cards", "page-6.png", agave_bar, "#e0c397"),
]
for fname, cap, img, moodfn, capcolor in singles:
    bg, pal = moodfn()
    shadow = SHADOW_DARK if moodfn is agave_bar else SHADOW_LIGHT
    write(OUT_A, fname, bg, pal, single_image_slide(cap, f"{SRC_A}/{img}", capcolor, w=1520, top=300, shadow=shadow))

bg, pal = agave_bright()
badge_html = f"""
<div style="position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);text-align:center;">
  <div style="font-weight:300;font-size:96px;color:#241a0c;">8 Pages</div>
  <div style="font-size:36px;color:#5a4128;margin-top:10px;">Instant Digital Download &middot; Print at Home</div>
</div>
{badge()}
<div style="position:absolute;left:24%;top:1200px;transform:translateX(-50%) rotate(-8deg);">
  <img src="{SRC_A}/page-5.png" style="width:640px;box-shadow:{SHADOW_LIGHT};">
</div>
<div style="position:absolute;left:50%;top:1130px;transform:translateX(-50%) rotate(0deg);">
  <img src="{SRC_A}/page-3.png" style="width:680px;box-shadow:{SHADOW_LIGHT};">
</div>
<div style="position:absolute;left:76%;top:1200px;transform:translateX(-50%) rotate(8deg);">
  <img src="{SRC_A}/page-7.png" style="width:640px;box-shadow:{SHADOW_LIGHT};">
</div>"""
write(OUT_A, "7-bundle.html", bg, pal, badge_html)

print("agave clean slides written")


# ======================================================================
#  HALLOWEEN - black soapstone/slate kitchen counter, where the candy bowl
#  actually sits. Cool charcoal stone instead of tinted wood, warm pumpkin glow.
# ======================================================================
def hw_haunted(horizon=575):
    bg = f"""
<div style="position:absolute;inset:0;background:
  radial-gradient(ellipse 1600px 1300px at 66% 14%,#5a2f6e 0%,#341b42 40%,#1a0e22 76%,#0a0510 100%);"></div>
<div style="position:absolute;left:760px;top:-320px;width:1560px;height:1750px;
  background:radial-gradient(ellipse at 50% 30%,rgba(255,140,60,0.24),rgba(255,110,60,0.08) 42%,rgba(0,0,0,0) 68%);
  filter:blur(24px);"></div>
<div style="position:absolute;left:0;right:0;top:120px;height:900px;filter:url(#haze);
  opacity:0.2;mix-blend-mode:screen;background:#c98be0;"></div>
{confetti([(120,760,9,'#ffb703',0.4),(1840,700,8,'#e0763a',0.35),(1700,140,7,'#c94f7a',0.4),
           (300,140,6,'#ffb703',0.3),(1600,950,7,'#e0763a',0.3)])}
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;
  background:linear-gradient(180deg,#2c2a2f 0%,#19171b 45%,#0a090b 100%);"></div>
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;filter:url(#stone);
  opacity:0.58;mix-blend-mode:multiply;background:#0c0b0d;"></div>
<div style="position:absolute;left:0;right:0;top:{horizon}px;height:9px;
  background:linear-gradient(180deg,rgba(255,150,80,0.35),rgba(255,150,80,0));"></div>"""
    return bg, dict(eyebrow="#e0a866", head="#f2e3da", sub="#d8c2be", grain="0.4")


# Warm kraft-paper / butcherblock counter - rust-orange wood grain, distinct hue from cigar's oak.
def hw_candy(horizon=1900):
    bg = f"""
<div style="position:absolute;inset:0;background:
  linear-gradient(172deg,#f6e6d4 0%,#eecfa8 46%,#e0ac72 58%,#b97a42 100%);"></div>
<div style="position:absolute;left:-220px;top:-320px;width:1550px;height:1550px;
  background:radial-gradient(circle,rgba(255,255,255,0.8),rgba(255,255,255,0) 62%);"></div>
<div style="position:absolute;inset:0;filter:url(#wood);opacity:0.22;mix-blend-mode:multiply;background:#7a4a20;"></div>
{confetti([(1780,120,10,'#c0563f',0.28),(1850,300,7,'#7b5544',0.3),(60,700,8,'#d99a3f',0.28)])}"""
    return bg, dict(eyebrow="#9a4e1e", head="#2a1608", sub="#5a3418", grain="0.26")


SRC_H = f"{REPO}/listing_images_raw/listing_images_halloween"
OUT_H = f"{REPO}/listing_marketing/listing_clean_halloween"
os.makedirs(OUT_H, exist_ok=True)

# 1. HERO
bg, pal = hw_haunted()
pages = f"""
<div style="position:absolute;left:24%;top:780px;transform:translateX(-50%) rotate(-6deg);">
  <img src="{SRC_H}/page-2.png" style="width:860px;box-shadow:{SHADOW_DARK};filter:brightness(0.88);">
</div>
<div style="position:absolute;left:50%;top:700px;transform:translateX(-50%) rotate(0deg);">
  <img src="{SRC_H}/page-4.png" style="width:930px;box-shadow:{SHADOW_DARK};">
</div>
<div style="position:absolute;left:76%;top:780px;transform:translateX(-50%) rotate(6deg);">
  <img src="{SRC_H}/page-1.png" style="width:860px;box-shadow:{SHADOW_DARK};">
</div>"""
write(OUT_H, "1-hero.html", bg, pal, hero_slide(
    "The Halloween Pairing Kit", "Candy &amp; Whisky", "8-Page Printable Tasting Kit &middot; Instant Download",
    pal, pages))

singles = [
    ("2-guide.html",    "01 &middot; Party Guide",   "page-1.png", hw_haunted, "#e0b48c"),
    ("3-primer.html",   "02 &middot; Primer",        "page-2.png", hw_candy,   "#9a4e1e"),
    ("4-pairbase.html", "03 &middot; Pairbase",      "page-3.png", hw_haunted, "#e0b48c"),
    ("5-wheels.html",   "04 &middot; Flavor Wheels", "page-4.png", hw_candy,   "#9a4e1e"),
    ("6-cards.html",    "05&ndash;07 &middot; Tasting Cards", "page-6.png", hw_haunted, "#e0b48c"),
]
for fname, cap, img, moodfn, capcolor in singles:
    bg, pal = moodfn()
    shadow = SHADOW_DARK if moodfn is hw_haunted else SHADOW_LIGHT
    write(OUT_H, fname, bg, pal, single_image_slide(cap, f"{SRC_H}/{img}", capcolor, w=1520, top=300, shadow=shadow))

bg, pal = hw_candy()
badge_html = f"""
<div style="position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);text-align:center;">
  <div style="font-weight:300;font-size:96px;color:#2a1608;">8 Pages</div>
  <div style="font-size:36px;color:#5a3418;margin-top:10px;">Instant Digital Download &middot; Print at Home</div>
</div>
{badge()}
<div style="position:absolute;left:24%;top:1200px;transform:translateX(-50%) rotate(-8deg);">
  <img src="{SRC_H}/page-5.png" style="width:640px;box-shadow:{SHADOW_LIGHT};">
</div>
<div style="position:absolute;left:50%;top:1130px;transform:translateX(-50%) rotate(0deg);">
  <img src="{SRC_H}/page-3.png" style="width:680px;box-shadow:{SHADOW_LIGHT};">
</div>
<div style="position:absolute;left:76%;top:1200px;transform:translateX(-50%) rotate(8deg);">
  <img src="{SRC_H}/page-7.png" style="width:640px;box-shadow:{SHADOW_LIGHT};">
</div>"""
write(OUT_H, "7-bundle.html", bg, pal, badge_html)

print("halloween clean slides written")
