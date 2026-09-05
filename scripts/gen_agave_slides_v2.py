import os

BASE = "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad/listing_v2"
os.makedirs(BASE, exist_ok=True)
SRC = "../listing_images_agave"

FONTS = ("@import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,300;0,400;"
         "0,500;0,600;0,700;0,800;1,400&family=Archivo+Black&display=swap');")

FILTERS = """
<svg style="position:absolute;width:0;height:0"><defs>
  <filter id="wood">
    <feTurbulence type="fractalNoise" baseFrequency="0.0016 0.09" numOctaves="4" seed="7"/>
    <feColorMatrix type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.42"/></feComponentTransfer>
  </filter>
  <filter id="grain">
    <feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="3" seed="3"/>
    <feColorMatrix type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.22"/></feComponentTransfer>
  </filter>
  <filter id="haze">
    <feTurbulence type="fractalNoise" baseFrequency="0.004 0.011" numOctaves="5" seed="11"/>
    <feColorMatrix type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.5"/></feComponentTransfer>
  </filter>
</defs></svg>
"""

def bokeh(spec):
    out = ""
    for x, y, r, a, blur in spec:
        out += (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{r}px;height:{r}px;'
                f'border-radius:50%;background:radial-gradient(circle at 38% 34%,rgba(255,225,160,{a}),'
                f'rgba(255,196,110,{a*0.55}) 55%,rgba(255,170,80,0) 72%);filter:blur({blur}px);"></div>')
    return out


# ---------- MOODS ----------
# each returns (background html, palette)
def mood_patio(horizon=560):
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
  opacity:0.5;mix-blend-mode:multiply;background:#2a150a;"></div>
<div style="position:absolute;left:0;right:0;top:{horizon-12}px;height:26px;
  background:linear-gradient(180deg,rgba(255,196,120,0.5),rgba(255,196,120,0));"></div>"""
    pal = dict(eyebrow="#ffd9a0", head="#fff5e6", sub="#ffeeda",
               shadow="text-shadow:0 4px 26px rgba(60,20,0,0.5);", grain="0.5")
    return bg, pal


def mood_bar(horizon=575):
    bg = f"""
<div style="position:absolute;inset:0;background:
  radial-gradient(ellipse 1600px 1300px at 66% 14%,#4a3a2c 0%,#2b211a 40%,#17110d 76%,#0f0a07 100%);"></div>
<div style="position:absolute;left:760px;top:-320px;width:1560px;height:1750px;
  background:radial-gradient(ellipse at 50% 30%,rgba(255,198,120,0.30),rgba(255,170,80,0.10) 42%,rgba(0,0,0,0) 68%);
  filter:blur(24px);"></div>
<div style="position:absolute;left:0;right:0;top:120px;height:900px;filter:url(#haze);
  opacity:0.15;mix-blend-mode:screen;background:#e8d3b0;"></div>
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;
  background:linear-gradient(180deg,#3a2418 0%,#21130a 45%,#120a04 100%);"></div>
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;filter:url(#wood);
  opacity:0.58;mix-blend-mode:multiply;background:#170c05;"></div>
<div style="position:absolute;left:0;right:0;top:{horizon-10}px;height:20px;
  background:linear-gradient(180deg,rgba(255,186,110,0.38),rgba(255,186,110,0));"></div>"""
    pal = dict(eyebrow="#d8a55f", head="#f6e9d6", sub="#d9c9b4", shadow="", grain="0.42")
    return bg, pal


def mood_bright(horizon=590):
    bg = f"""
<div style="position:absolute;inset:0;background:
  linear-gradient(172deg,#f4efe6 0%,#ece3d5 46%,#e0d4c0 58%,#cdbca3 100%);"></div>
<div style="position:absolute;left:-220px;top:-320px;width:1550px;height:1550px;
  background:radial-gradient(circle,rgba(255,255,255,0.85),rgba(255,255,255,0) 62%);"></div>
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;
  background:linear-gradient(180deg,#d6bc97 0%,#c2a479 48%,#a8875c 100%);"></div>
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;filter:url(#wood);
  opacity:0.32;mix-blend-mode:multiply;background:#7a5c36;"></div>"""
    pal = dict(eyebrow="#8a6f45", head="#141414", sub="#4a4034", shadow="", grain="0.3")
    return bg, pal


MOODS = {"patio": mood_patio, "bar": mood_bar, "bright": mood_bright}

SHADOW = {
    "patio":  "0 10px 22px rgba(0,0,0,0.42), 0 70px 110px -34px rgba(0,0,0,0.78)",
    "bar":    "0 10px 24px rgba(0,0,0,0.62), 0 80px 120px -36px rgba(0,0,0,0.92)",
    "bright": "0 8px 18px rgba(90,66,36,0.3), 0 62px 92px -32px rgba(90,66,36,0.55)",
}


def page(mood, name, ry=-4.0, rz=-1.0, w=1060, top=452):
    return f"""
<div style="position:absolute;left:50%;top:{top}px;transform:translateX(-50%) perspective(3400px)
     rotateX(7deg) rotateY({ry}deg) rotate({rz}deg);transform-origin:50% 0%;">
  <img src="{SRC}/{name}" style="width:{w}px;display:block;box-shadow:{SHADOW[mood]};">
</div>"""


def header(pal, eyebrow, head, sub):
    return f"""
<div style="position:absolute;left:120px;top:118px;max-width:1450px;{pal['shadow']}">
  <div style="font-size:36px;letter-spacing:0.15em;text-transform:uppercase;font-weight:700;
       color:{pal['eyebrow']};">{eyebrow}</div>
  <div style="font-weight:300;font-size:104px;line-height:1.0;margin-top:12px;color:{pal['head']};
       letter-spacing:-0.015em;">{head}</div>
  <div style="font-size:50px;line-height:1.32;margin-top:22px;color:{pal['sub']};max-width:1400px;
       font-weight:400;">{sub}</div>
</div>
<div style="position:absolute;right:120px;top:112px;"><div class="kb"><span class="l1">KINGB</span><span class="l2">KITS</span></div></div>"""


def write(name, mood_key, body_inner, horizon=None):
    fn = MOODS[mood_key]
    bg, pal = fn() if horizon is None else fn(horizon)
    html = f"""<!doctype html><html><head><meta charset='utf-8'><style>
{FONTS}
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:2000px;height:2000px;overflow:hidden;}}
body{{font-family:'Raleway',sans-serif;position:relative;}}
.kb{{display:inline-flex;flex-direction:column;align-items:center;justify-content:center;background:#000;
  border-radius:24px;padding:18px 30px 20px;font-family:'Archivo Black',sans-serif;line-height:0.92;
  text-align:center;width:fit-content;}}
.kb .l1{{font-size:40px;color:#f3c318;}}
.kb .l2{{font-size:28px;color:#fff;letter-spacing:0.02em;margin-top:2px;}}
.pill{{display:inline-flex;align-items:center;font-weight:700;font-size:34px;padding:14px 32px;
  border-radius:999px;color:#000;}}
.grain{{position:absolute;inset:0;filter:url(#grain);opacity:{pal['grain']};mix-blend-mode:overlay;background:#fff;}}
</style></head><body>{FILTERS}{bg}{body_inner(pal)}<div class="grain"></div></body></html>"""
    with open(os.path.join(BASE, name), "w") as f:
        f.write(html)


# ================= 1. HERO =================
def hero_body(pal):
    return f"""
<div style="position:absolute;left:120px;top:128px;max-width:1180px;">
  <div style="font-style:italic;font-size:40px;color:{pal['sub']};">The Agave Tasting Journey</div>
  <div style="font-weight:300;font-size:150px;line-height:0.96;color:{pal['head']};margin-top:26px;
       letter-spacing:-0.025em;">Tequila &amp;<br>Mezcal</div>
  <div style="font-weight:800;font-size:84px;color:{pal['head']};margin-top:20px;">Tasting Party Kit</div>
  <div style="font-size:50px;line-height:1.28;color:{pal['sub']};margin-top:28px;max-width:1080px;">
    A guided flight for six, with the bottles picked and the pours in order.</div>
  <div style="font-size:36px;color:{pal['sub']};margin-top:30px;letter-spacing:0.02em;">
    7 PDF Pages &middot; Instant Download &middot; Print at Home</div>
  <div style="display:flex;gap:22px;margin-top:34px;">
    <span class="pill" style="background:#87cb28;">Newbie</span>
    <span class="pill" style="background:#ffff00;">Casual</span>
    <span class="pill" style="background:#ffd230;">Aficionado</span>
  </div>
</div>
<div style="position:absolute;right:120px;top:120px;"><div class="kb"><span class="l1">KINGB</span><span class="l2">KITS</span></div></div>

<div style="position:absolute;left:20%;top:1090px;transform:translateX(-50%) perspective(3200px)
     rotateX(9deg) rotateY(7deg) rotate(-7deg);transform-origin:50% 0%;">
  <img src="{SRC}/page-2.png" style="width:700px;display:block;filter:brightness(0.88);box-shadow:{SHADOW['bar']};">
</div>
<div style="position:absolute;left:44%;top:1045px;transform:translateX(-50%) perspective(3200px)
     rotateX(9deg) rotateY(2deg) rotate(-2deg);transform-origin:50% 0%;">
  <img src="{SRC}/page-4.png" style="width:740px;display:block;filter:brightness(0.95);box-shadow:{SHADOW['bar']};">
</div>
<div style="position:absolute;left:70%;top:1075px;transform:translateX(-50%) perspective(3200px)
     rotateX(9deg) rotateY(-6deg) rotate(4deg);transform-origin:50% 0%;">
  <img src="{SRC}/page-1.png" style="width:720px;display:block;box-shadow:{SHADOW['bar']};">
</div>
"""

write("1-hero.html", "bar", hero_body, horizon=930)


# ============ 2. WHAT'S INCLUDED ============
def included_body(pal):
    items = [
        ("01", "Party Guide", "Setup, timing and pacing, plus why the lime and salt stay in the kitchen."),
        ("02", "Tequila &amp; Mezcal Primer", "Blue Weber vs wild agave, the age ladder, how to read a label."),
        ("03", "Agavebase Chart", "Real bottles at three budgets, with per-person cost math."),
        ("04", "Flavor Wheels", "Separate tequila and mezcal wheels for building vocabulary."),
        ("05", "Newbie Card", "The Age Ladder flight: blanco, reposado, a&ntilde;ejo."),
        ("06", "Casual Card", "Tequila Meets Mezcal: the smoke reveal."),
        ("07", "Aficionado Card", "Agave Terroir: three wild species, one producer."),
    ]
    rows = ""
    for n, t, d in items:
        rows += f"""
    <div style="display:flex;gap:38px;align-items:baseline;padding:30px 0;border-bottom:2px solid rgba(90,66,36,0.22);">
      <div style="font-family:'Archivo Black';font-size:44px;color:#a8875c;width:96px;flex:none;">{n}</div>
      <div>
        <div style="font-weight:700;font-size:50px;color:#141414;">{t}</div>
        <div style="font-size:38px;color:#4a4034;margin-top:8px;line-height:1.32;">{d}</div>
      </div>
    </div>"""
    return f"""
<div style="position:absolute;inset:0;padding:130px 120px;display:flex;flex-direction:column;justify-content:center;">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:44px;">
    <div style="font-weight:300;font-size:112px;color:#141414;">What's Included</div>
    <div class="kb"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  </div>
  {rows}
</div>"""

write("2-included.html", "bright", included_body, horizon=2100)


# ============ DETAIL SLIDES ============
def detail(eyebrow, head, sub, img, ry, rz):
    def body(pal):
        return header(pal, eyebrow, head, sub) + page(CUR[0], img, ry=ry, rz=rz)
    return body

CUR = ["bar"]

specs = [
    ("3-guide.html",     "patio",  "Piece 01", "Party Guide",
     "Setup, timing and pacing for a night that stays a tasting.", "page-1.png", -4, -1.1),
    ("4-primer.html",    "bar",    "Piece 02", "The Primer",
     "Blue Weber vs wild agave, and why only one of them tastes smoky.", "page-2.png", 3.5, 1.0),
    ("5-agavebase.html", "bright", "Piece 03", "Agavebase Chart",
     "Real bottles at three budgets, with the cost math already done.", "page-3.png", -3.5, -0.9),
    ("6-wheels.html",    "bar",    "Piece 04", "Flavor Wheels",
     "Put an actual word to what is in the glass.", "page-4.png", 3.0, 1.2),
    ("7-cards.html",     "patio",  "Piece 05-07", "A Card for Every Tier",
     "Three flights. Each one isolates a single variable.", "page-6.png", -3.0, -1.3),
]
for fname, mood, eb, hd, sb, img, ry, rz in specs:
    CUR[0] = mood
    write(fname, mood, detail(eb, hd, sb, img, ry, rz))


# ============ 8. WHY ============
def why_body(pal):
    return f"""
<div style="position:absolute;left:120px;top:230px;max-width:1500px;">
  <div style="font-weight:300;font-size:132px;line-height:1.04;color:{pal['head']};">Sip It.<br>Don't Shoot It.</div>
  <div style="font-size:52px;line-height:1.4;color:{pal['sub']};margin-top:52px;max-width:1420px;">
    The lime and salt ritual exists to hide cheap mixto. Good agave doesn't need hiding.
    This kit walks your table through three one-ounce pours, teaches the one label rule
    that filters out most bad bottles, and gives everyone the words for what they're tasting.
  </div>
</div>
<div style="position:absolute;right:120px;top:120px;"><div class="kb"><span class="l1">KINGB</span><span class="l2">KITS</span></div></div>
<div style="position:absolute;left:120px;right:120px;bottom:130px;display:flex;gap:90px;
     border-top:3px solid rgba(255,235,205,0.45);padding-top:44px;">
  <div><div style="font-weight:700;font-size:64px;color:{pal['head']};">3</div>
       <div style="font-size:34px;color:{pal['sub']};">experience tiers</div></div>
  <div><div style="font-weight:700;font-size:64px;color:{pal['head']};">3</div>
       <div style="font-size:34px;color:{pal['sub']};">bottles covers 6 guests</div></div>
  <div><div style="font-weight:700;font-size:64px;color:{pal['head']};">2</div>
       <div style="font-size:34px;color:{pal['sub']};">flavor wheels</div></div>
</div>"""

write("8-why.html", "bar", why_body, horizon=2100)


# ============ 9. HOW IT WORKS ============
def how_body(pal):
    steps = [
        ("Purchase &amp; Download", "Instant access to the 7-page PDF. Nothing ships."),
        ("Print at Home", "Standard US Letter, no bleed or special stock."),
        ("Pick Your Tier", "The Agavebase names the bottles for your budget."),
        ("Pour Three Ounces", "One flight, three pours, one evening."),
    ]
    rows = ""
    for i, (t, d) in enumerate(steps, 1):
        rows += f"""
    <div style="display:flex;gap:40px;align-items:baseline;padding:38px 0;border-bottom:2px solid rgba(90,66,36,0.22);">
      <div style="font-family:'Archivo Black';font-size:62px;color:#87a35f;width:110px;flex:none;">{i:02d}</div>
      <div><div style="font-weight:700;font-size:52px;color:#141414;">{t}</div>
           <div style="font-size:38px;color:#4a4034;margin-top:8px;">{d}</div></div>
    </div>"""
    return f"""
<div style="position:absolute;inset:0;padding:140px 120px;">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:50px;">
    <div style="font-weight:300;font-size:104px;color:#141414;line-height:1.05;">Instant Download,<br>How It Works</div>
    <div class="kb"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  </div>
  {rows}
  <div style="margin-top:56px;font-size:36px;color:#7a6647;">&#8252;&#65039; ALL DIGITAL. No physical items are shipped.</div>
</div>"""

write("9-howto.html", "bright", how_body, horizon=2100)

print("v2 slides written")
