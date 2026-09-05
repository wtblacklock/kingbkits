import os, sys
sys.path.insert(0, "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad")
from gen_clean_listing import write, bokeh, single_image_slide, hero_slide, badge

ROOT = "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad"

SHADOW_DARK = "0 14px 30px rgba(0,0,0,0.55), 0 90px 130px -40px rgba(0,0,0,0.9)"
SHADOW_LIGHT = "0 10px 22px rgba(70,45,20,0.3), 0 70px 100px -34px rgba(70,45,20,0.5)"


def cigar_bar(horizon=560):
    bg = f"""
<div style="position:absolute;inset:0;background:
  radial-gradient(ellipse 1600px 1300px at 66% 14%,#4a3a2c 0%,#2b211a 40%,#17110d 76%,#0f0a07 100%);"></div>
<div style="position:absolute;left:760px;top:-320px;width:1560px;height:1750px;
  background:radial-gradient(ellipse at 50% 30%,rgba(255,198,120,0.30),rgba(255,170,80,0.10) 42%,rgba(0,0,0,0) 68%);
  filter:blur(24px);"></div>
<div style="position:absolute;left:0;right:0;top:120px;height:900px;filter:url(#haze);
  opacity:0.15;mix-blend-mode:screen;background:#e8d3b0;"></div>
{bokeh([(150,250,150,0.42,26),(420,150,96,0.36,18),(1560,330,120,0.34,22),
        (1800,180,150,0.30,26),(940,120,84,0.26,16),(260,520,80,0.22,16)])}
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;
  background:linear-gradient(180deg,#3a2418 0%,#21130a 45%,#120a04 100%);"></div>
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;filter:url(#wood);
  opacity:0.58;mix-blend-mode:multiply;background:#170c05;"></div>"""
    return bg, dict(eyebrow="#d8a55f", head="#f6e9d6", sub="#d9c9b4", grain="0.42")

def cigar_patio(horizon=560):
    bg = f"""
<div style="position:absolute;inset:0;background:
  linear-gradient(176deg,#6d2f16 0%,#a34f28 20%,#c9743d 38%,#dc9155 50%,#a8612f 60%,#5f3319 100%);"></div>
<div style="position:absolute;left:1150px;top:-120px;width:1200px;height:1200px;border-radius:50%;
  background:radial-gradient(circle,rgba(255,214,140,0.55),rgba(255,180,90,0.18) 45%,rgba(255,160,70,0) 70%);
  filter:blur(30px);"></div>
{bokeh([(150,250,150,0.42,26),(420,150,96,0.36,18),(1560,330,120,0.34,22),
        (1800,180,150,0.30,26),(940,120,84,0.26,16),(260,520,80,0.22,16)])}
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;
  background:linear-gradient(180deg,#6b3a1f 0%,#43230f 45%,#2b1509 100%);"></div>
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;filter:url(#wood);
  opacity:0.5;mix-blend-mode:multiply;background:#2a150a;"></div>"""
    return bg, dict(eyebrow="#ffd9a0", head="#fff5e6", sub="#ffeeda", grain="0.5")

def cigar_bright(horizon=1900):
    bg = f"""
<div style="position:absolute;inset:0;background:
  linear-gradient(172deg,#f4efe6 0%,#ece3d5 46%,#e0d4c0 58%,#cdbca3 100%);"></div>
<div style="position:absolute;left:-220px;top:-320px;width:1550px;height:1550px;
  background:radial-gradient(circle,rgba(255,255,255,0.85),rgba(255,255,255,0) 62%);"></div>"""
    return bg, dict(eyebrow="#8a6f45", head="#141414", sub="#4a4034", grain="0.3")


SRC = "../listing_images"
OUT = os.path.join(ROOT, "listing_clean_cigar")
os.makedirs(OUT, exist_ok=True)

# 1. HERO
bg, pal = cigar_bar()
pages = f"""
<div style="position:absolute;left:24%;top:780px;transform:translateX(-50%) rotate(-6deg);">
  <img src="{SRC}/page-2.png" style="width:860px;box-shadow:{SHADOW_DARK};filter:brightness(0.88);">
</div>
<div style="position:absolute;left:50%;top:700px;transform:translateX(-50%) rotate(0deg);">
  <img src="{SRC}/page-4.png" style="width:930px;box-shadow:{SHADOW_DARK};">
</div>
<div style="position:absolute;left:76%;top:780px;transform:translateX(-50%) rotate(6deg);">
  <img src="{SRC}/page-1.png" style="width:860px;box-shadow:{SHADOW_DARK};">
</div>"""
write(OUT, "1-hero.html", bg, pal, hero_slide(
    "The Cigar &amp; Whisky Journey", "Cigar &amp; Whisky", "7-Page Printable Pairing Kit &middot; Instant Download",
    pal, pages))

singles = [
    ("2-guide.html",    "01 &middot; Party Guide",     "page-1.png", cigar_bar,    "#e0c397"),
    ("3-primer.html",   "02 &middot; Primer",          "page-2.png", cigar_bright, "#8a6f45"),
    ("4-pairbase.html", "03 &middot; Pairbase",        "page-3.png", cigar_bar,    "#e0c397"),
    ("5-wheels.html",   "04 &middot; Flavor Wheels",   "page-4.png", cigar_bright, "#8a6f45"),
    ("6-cards.html",    "05&ndash;07 &middot; Pairing Cards", "page-6.png", cigar_bar, "#e0c397"),
]
for fname, cap, img, moodfn, capcolor in singles:
    bg, pal = moodfn()
    shadow = SHADOW_DARK if moodfn is cigar_bar else SHADOW_LIGHT
    write(OUT, fname, bg, pal, single_image_slide(cap, f"{SRC}/{img}", capcolor, w=1520, top=300, shadow=shadow))

bg, pal = cigar_bright()
badge_html = f"""
<div style="position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);text-align:center;">
  <div style="font-weight:300;font-size:96px;color:#141414;">7 Pages</div>
  <div style="font-size:36px;color:#4a4034;margin-top:10px;">Instant Digital Download &middot; Print at Home</div>
</div>
{badge()}
<div style="position:absolute;left:24%;top:1200px;transform:translateX(-50%) rotate(-8deg);">
  <img src="{SRC}/page-5.png" style="width:640px;box-shadow:{SHADOW_LIGHT};">
</div>
<div style="position:absolute;left:50%;top:1130px;transform:translateX(-50%) rotate(0deg);">
  <img src="{SRC}/page-3.png" style="width:680px;box-shadow:{SHADOW_LIGHT};">
</div>
<div style="position:absolute;left:76%;top:1200px;transform:translateX(-50%) rotate(8deg);">
  <img src="{SRC}/page-7.png" style="width:640px;box-shadow:{SHADOW_LIGHT};">
</div>"""
write(OUT, "7-bundle.html", bg, pal, badge_html)

print("cigar clean slides written")
