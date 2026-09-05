import os

BASE = "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad/listing_hw_v2"
os.makedirs(BASE, exist_ok=True)
SRC = "../listing_images_halloween"

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

def bokeh(spec, rgb="255,150,60"):
    out = ""
    for x, y, r, a, blur in spec:
        out += (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{r}px;height:{r}px;'
                f'border-radius:50%;background:radial-gradient(circle at 38% 34%,rgba({rgb},{a}),'
                f'rgba({rgb},{a*0.55}) 55%,rgba({rgb},0) 72%);filter:blur({blur}px);"></div>')
    return out

def confetti(spec):
    # small candy-colored dots, tasteful and sparse -- the "fun with the artifacts" touch
    out = ""
    for x, y, r, color, op in spec:
        out += (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{r}px;height:{r}px;'
                f'border-radius:50%;background:{color};opacity:{op};"></div>')
    return out


# ---------- MOODS ----------
def mood_dusk(horizon=560):
    bg = f"""
<div style="position:absolute;inset:0;background:
  linear-gradient(176deg,#2c1435 0%,#6a2650 18%,#a83a4a 36%,#d1622f 50%,#7a2f2a 64%,#2a1018 100%);"></div>
<div style="position:absolute;left:1150px;top:-140px;width:1200px;height:1200px;border-radius:50%;
  background:radial-gradient(circle,rgba(255,170,90,0.5),rgba(255,120,70,0.16) 45%,rgba(255,90,60,0) 70%);
  filter:blur(30px);"></div>
{bokeh([(150,250,150,0.4,26),(420,150,96,0.34,18),(1560,330,120,0.32,22),
        (1800,180,150,0.28,26),(940,120,84,0.24,16),(260,520,80,0.2,16)])}
{confetti([(180,640,10,'#ffb703',0.55),(1720,560,8,'#e0763a',0.5),(980,80,7,'#c94f7a',0.5),
           (1400,700,9,'#ffb703',0.4),(340,90,6,'#e0763a',0.45)])}
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;
  background:linear-gradient(180deg,#2e1a24 0%,#1c0f16 45%,#100810 100%);"></div>
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;filter:url(#wood);
  opacity:0.5;mix-blend-mode:multiply;background:#170a12;"></div>
<div style="position:absolute;left:0;right:0;top:{horizon-12}px;height:26px;
  background:linear-gradient(180deg,rgba(255,150,90,0.45),rgba(255,150,90,0));"></div>"""
    pal = dict(eyebrow="#ffb37a", head="#fbe9e2", sub="#f0d2c8",
               shadow="text-shadow:0 4px 26px rgba(30,10,20,0.55);", grain="0.5")
    return bg, pal


def mood_haunted(horizon=575):
    bg = f"""
<div style="position:absolute;inset:0;background:
  radial-gradient(ellipse 1600px 1300px at 66% 14%,#3a2836 0%,#241823 40%,#140c14 76%,#0a0509 100%);"></div>
<div style="position:absolute;left:760px;top:-320px;width:1560px;height:1750px;
  background:radial-gradient(ellipse at 50% 30%,rgba(255,140,60,0.30),rgba(255,110,60,0.10) 42%,rgba(0,0,0,0) 68%);
  filter:blur(24px);"></div>
<div style="position:absolute;left:0;right:0;top:120px;height:900px;filter:url(#haze);
  opacity:0.14;mix-blend-mode:screen;background:#d9b8e0;"></div>
{confetti([(120,760,9,'#ffb703',0.4),(1840,700,8,'#e0763a',0.35),(1700,140,7,'#c94f7a',0.4)])}
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;
  background:linear-gradient(180deg,#2e1c26 0%,#190f16 45%,#0d0709 100%);"></div>
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;filter:url(#wood);
  opacity:0.56;mix-blend-mode:multiply;background:#160b14;"></div>
<div style="position:absolute;left:0;right:0;top:{horizon-10}px;height:20px;
  background:linear-gradient(180deg,rgba(255,140,70,0.4),rgba(255,140,70,0));"></div>"""
    pal = dict(eyebrow="#e0a866", head="#f2e3da", sub="#d8c2be", shadow="", grain="0.42")
    return bg, pal


def mood_candy(horizon=590):
    bg = f"""
<div style="position:absolute;inset:0;background:
  linear-gradient(172deg,#f7ece0 0%,#f0ddc9 46%,#e8cba9 58%,#d1a97d 100%);"></div>
<div style="position:absolute;left:-220px;top:-320px;width:1550px;height:1550px;
  background:radial-gradient(circle,rgba(255,255,255,0.85),rgba(255,255,255,0) 62%);"></div>
{confetti([(1780,120,10,'#c0563f',0.28),(1850,300,7,'#7b5544',0.3),(60,700,8,'#d99a3f',0.28)])}
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;
  background:linear-gradient(180deg,#c88a52 0%,#a86a3a 48%,#7a4a28 100%);"></div>
<div style="position:absolute;left:0;right:0;top:{horizon}px;bottom:0;filter:url(#wood);
  opacity:0.32;mix-blend-mode:multiply;background:#5a3a20;"></div>"""
    pal = dict(eyebrow="#9a5a2e", head="#241408", sub="#5a3a24", shadow="", grain="0.3")
    return bg, pal


MOODS = {"dusk": mood_dusk, "haunted": mood_haunted, "candy": mood_candy}

SHADOW = {
    "dusk":    "0 10px 22px rgba(0,0,0,0.5), 0 70px 110px -34px rgba(20,0,10,0.8)",
    "haunted": "0 10px 24px rgba(0,0,0,0.65), 0 80px 120px -36px rgba(0,0,0,0.92)",
    "candy":   "0 8px 18px rgba(90,50,20,0.32), 0 62px 92px -32px rgba(90,50,20,0.55)",
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
  <div style="font-style:italic;font-size:40px;color:{pal['sub']};">The Halloween Pairing Kit</div>
  <div style="font-weight:300;font-size:150px;line-height:0.96;color:{pal['head']};margin-top:26px;
       letter-spacing:-0.025em;">Candy &amp;<br>Whisky</div>
  <div style="font-weight:800;font-size:84px;color:{pal['head']};margin-top:20px;">Halloween Pairing Kit</div>
  <div style="font-size:50px;line-height:1.28;color:{pal['sub']};margin-top:28px;max-width:1080px;">
    The cheapest tasting night you'll ever host &mdash; a $12 bag of candy and a bottle you already own.</div>
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
  <img src="{SRC}/page-2.png" style="width:700px;display:block;filter:brightness(0.88);box-shadow:{SHADOW['haunted']};">
</div>
<div style="position:absolute;left:44%;top:1045px;transform:translateX(-50%) perspective(3200px)
     rotateX(9deg) rotateY(2deg) rotate(-2deg);transform-origin:50% 0%;">
  <img src="{SRC}/page-4.png" style="width:740px;display:block;filter:brightness(0.95);box-shadow:{SHADOW['haunted']};">
</div>
<div style="position:absolute;left:70%;top:1075px;transform:translateX(-50%) perspective(3200px)
     rotateX(9deg) rotateY(-6deg) rotate(4deg);transform-origin:50% 0%;">
  <img src="{SRC}/page-1.png" style="width:720px;display:block;box-shadow:{SHADOW['haunted']};">
</div>
"""

write("1-hero.html", "haunted", hero_body, horizon=930)


# ============ 2. WHAT'S INCLUDED ============
def included_body(pal):
    items = [
        ("01", "Party Guide", "What to buy, how to set up, and how to actually taste a pairing."),
        ("02", "Candy Primer", "The real chemistry behind why chocolate and caramel pair so well with whisky."),
        ("03", "Pairbase Chart", "9 candy-to-whisky pairings with real bottles, and why each one works."),
        ("04", "Flavor Wheels", "A candy wheel and a whisky wheel side by side."),
        ("05", "Newbie Card", "The Sweet Match: three candies that agree with one bourbon."),
        ("06", "Casual Card", "The Contrast: pairings that work by fighting instead of agreeing."),
        ("07", "Aficionado Card", "The Gauntlet: sour candy, licorice, and candy corn."),
    ]
    rows = ""
    for n, t, d in items:
        rows += f"""
    <div style="display:flex;gap:38px;align-items:baseline;padding:30px 0;border-bottom:2px solid rgba(90,50,20,0.22);">
      <div style="font-family:'Archivo Black';font-size:44px;color:#a86a3a;width:96px;flex:none;">{n}</div>
      <div>
        <div style="font-weight:700;font-size:50px;color:#241408;">{t}</div>
        <div style="font-size:38px;color:#5a3a24;margin-top:8px;line-height:1.32;">{d}</div>
      </div>
    </div>"""
    return f"""
<div style="position:absolute;inset:0;padding:130px 120px;display:flex;flex-direction:column;justify-content:center;">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:44px;">
    <div style="font-weight:300;font-size:112px;color:#241408;">What's Included</div>
    <div class="kb"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  </div>
  {rows}
</div>"""

write("2-included.html", "candy", included_body, horizon=2100)


# ============ DETAIL SLIDES ============
def detail(eyebrow, head, sub, img, ry, rz):
    def body(pal):
        return header(pal, eyebrow, head, sub) + page(CUR[0], img, ry=ry, rz=rz)
    return body

CUR = ["haunted"]

specs = [
    ("3-guide.html",    "dusk",    "Piece 01", "Party Guide",
     "What to buy and how to actually taste a pairing.", "page-1.png", -4, -1.1),
    ("4-primer.html",   "haunted", "Piece 02", "Candy Primer",
     "Why coconut, caramel and cocoa agree with whisky. Real chemistry.", "page-2.png", 3.5, 1.0),
    ("5-pairbase.html", "candy",   "Piece 03", "Pairbase Chart",
     "Nine pairings, real bottles, the reason each one works.", "page-3.png", -3.5, -0.9),
    ("6-wheels.html",   "haunted", "Piece 04", "Flavor Wheels",
     "Candy and whisky, side by side. Find the overlap.", "page-4.png", 3.0, 1.2),
    ("7-cards.html",    "dusk",    "Piece 05-07", "Complement, Contrast, Collision",
     "Three flights. One of them is a genuine gauntlet.", "page-6.png", -3.0, -1.3),
]
for fname, mood, eb, hd, sb, img, ry, rz in specs:
    CUR[0] = mood
    write(fname, mood, detail(eb, hd, sb, img, ry, rz))


# ============ 8. WHY ============
def why_body(pal):
    return f"""
<div style="position:absolute;left:120px;top:230px;max-width:1500px;">
  <div style="font-weight:300;font-size:132px;line-height:1.04;color:{pal['head']};">Your Leftover<br>Candy Deserves<br>Better.</div>
  <div style="font-size:52px;line-height:1.4;color:{pal['sub']};margin-top:52px;max-width:1420px;">
    Coconut in an Almond Joy shares the same compound class as American oak. Caramelized
    sugar and barrel char are the same chemical reaction. This isn't a party trick &mdash;
    candy and whisky actually agree, and this kit shows you exactly where.
  </div>
</div>
<div style="position:absolute;right:120px;top:120px;"><div class="kb"><span class="l1">KINGB</span><span class="l2">KITS</span></div></div>
<div style="position:absolute;left:120px;right:120px;bottom:130px;display:flex;gap:90px;
     border-top:3px solid rgba(255,200,150,0.4);padding-top:44px;">
  <div><div style="font-weight:700;font-size:64px;color:{pal['head']};">9</div>
       <div style="font-size:34px;color:{pal['sub']};">candy &amp; whisky pairings</div></div>
  <div><div style="font-weight:700;font-size:64px;color:{pal['head']};">$12</div>
       <div style="font-size:34px;color:{pal['sub']};">covers a table of six</div></div>
  <div><div style="font-weight:700;font-size:64px;color:{pal['head']};">2</div>
       <div style="font-size:34px;color:{pal['sub']};">selling windows &mdash; Oct &amp; Nov 1-7</div></div>
</div>"""

write("8-why.html", "haunted", why_body, horizon=2100)


# ============ 9. HOW IT WORKS ============
def how_body(pal):
    steps = [
        ("Purchase &amp; Download", "Instant access to the full PDF. Nothing ships."),
        ("Print at Home", "Standard US Letter, no bleed or special stock."),
        ("Buy One Bag of Candy", "The Pairbase names exactly which bars to grab."),
        ("Half-Ounce Pours", "Sip, bite, sip again. Vote on a winner at the end."),
    ]
    rows = ""
    for i, (t, d) in enumerate(steps, 1):
        rows += f"""
    <div style="display:flex;gap:40px;align-items:baseline;padding:38px 0;border-bottom:2px solid rgba(90,50,20,0.22);">
      <div style="font-family:'Archivo Black';font-size:62px;color:#c0563f;width:110px;flex:none;">{i:02d}</div>
      <div><div style="font-weight:700;font-size:52px;color:#241408;">{t}</div>
           <div style="font-size:38px;color:#5a3a24;margin-top:8px;">{d}</div></div>
    </div>"""
    return f"""
<div style="position:absolute;inset:0;padding:140px 120px;">
  <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:50px;">
    <div style="font-weight:300;font-size:104px;color:#241408;line-height:1.05;">Instant Download,<br>How It Works</div>
    <div class="kb"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  </div>
  {rows}
  <div style="margin-top:56px;font-size:36px;color:#8a5a34;">&#8252;&#65039; ALL DIGITAL. No physical items are shipped. No candy or bottles are included.</div>
</div>"""

write("9-howto.html", "candy", how_body, horizon=2100)

print("halloween v2 slides written")
