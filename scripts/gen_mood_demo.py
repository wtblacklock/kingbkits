import os

BASE = "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad/mood_demo"
os.makedirs(BASE, exist_ok=True)

# page previews to composite live next to these files
SRC = "../listing_images_agave"

FONTS = "@import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,300;0,400;0,600;0,700;0,800;1,400&family=Archivo+Black&display=swap');"

FILTERS = """
<svg style="position:absolute;width:0;height:0">
  <defs>
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
  </defs>
</svg>
"""

def bokeh(spec):
    out = ""
    for x, y, r, a, blur in spec:
        out += (f'<div style="position:absolute; left:{x}px; top:{y}px; width:{r}px; height:{r}px;'
                f'border-radius:50%; background:radial-gradient(circle at 38% 34%, rgba(255,225,160,{a}),'
                f'rgba(255,196,110,{a*0.55}) 55%, rgba(255,170,80,0) 72%);'
                f'filter:blur({blur}px); pointer-events:none;"></div>')
    return out


def sheets(back, front, shadow_back, shadow_front):
    """Two overlapping sheets on the surface: reads as a kit, not one page."""
    return f"""
<div style="position:absolute;left:34%;top:700px;transform:translateX(-50%) perspective(3000px)
     rotateX(10deg) rotateY(6deg) rotate(-6deg);transform-origin:50% 0%;">
  <img src="{back}" style="width:660px;display:block;filter:brightness(0.9);
    box-shadow:{shadow_back};">
</div>
<div style="position:absolute;left:57%;top:748px;transform:translateX(-50%) perspective(3000px)
     rotateX(10deg) rotateY(-5deg) rotate(2.4deg);transform-origin:50% 0%;">
  <img src="{front}" style="width:760px;display:block;
    box-shadow:{shadow_front};">
</div>"""


def write(name, body, extra_css=""):
    html = f"""<!doctype html><html><head><meta charset='utf-8'>
<style>
{FONTS}
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:2000px;height:2000px;overflow:hidden;}}
body{{font-family:'Raleway',sans-serif; position:relative;}}
.kb-badge{{display:inline-flex;flex-direction:column;align-items:center;justify-content:center;
  background:#000;border-radius:22px;padding:16px 26px 18px;font-family:'Archivo Black',sans-serif;
  line-height:0.92;text-align:center;width:fit-content;}}
.kb-badge .l1{{font-size:34px;color:#f3c318;}}
.kb-badge .l2{{font-size:24px;color:#fff;letter-spacing:0.02em;margin-top:2px;}}
.eyebrow{{font-size:28px;letter-spacing:0.14em;text-transform:uppercase;font-weight:700;}}
.headline{{font-weight:300;font-size:104px;line-height:1.02;margin-top:10px;}}
.sub{{font-size:34px;margin-top:20px;max-width:1050px;line-height:1.45;}}
.grainlayer{{position:absolute;inset:0;filter:url(#grain);opacity:0.5;mix-blend-mode:overlay;
  pointer-events:none;background:#fff;}}
{extra_css}
</style></head><body>{FILTERS}{body}</body></html>"""
    with open(os.path.join(BASE, name), "w") as f:
        f.write(html)


# ---------------- A: GOLDEN HOUR PATIO ----------------
write("A-golden-patio.html", f"""
<div style="position:absolute;inset:0;background:
   linear-gradient(176deg,#6d2f16 0%,#a34f28 22%,#cf7a41 42%,#e0975a 54%,#b56a38 62%,#6b3a1e 100%);">
</div>

<!-- warm sun glow -->
<div style="position:absolute;left:1150px;top:60px;width:1100px;height:1100px;border-radius:50%;
  background:radial-gradient(circle,rgba(255,214,140,0.62),rgba(255,180,90,0.20) 45%,rgba(255,160,70,0) 70%);
  filter:blur(30px);"></div>

{bokeh([(180,300,150,0.50,26),(400,180,96,0.42,18),(620,340,120,0.34,22),
        (1500,430,110,0.40,20),(1720,250,150,0.34,26),(980,150,84,0.30,16),
        (300,620,76,0.26,16),(1850,600,96,0.24,18)])}

<!-- table surface -->
<div style="position:absolute;left:0;right:0;top:760px;bottom:0;
  background:linear-gradient(180deg,#6b3a1f 0%,#4a2614 40%,#331a0d 100%);"></div>
<div style="position:absolute;left:0;right:0;top:760px;bottom:0;filter:url(#wood);
  opacity:0.55;mix-blend-mode:multiply;background:#2a150a;"></div>
<div style="position:absolute;left:0;right:0;top:748px;height:26px;
  background:linear-gradient(180deg,rgba(255,196,120,0.55),rgba(255,196,120,0));"></div>

<!-- copy -->
<div style="position:absolute;left:130px;top:150px;color:#fff5e6;text-shadow:0 4px 26px rgba(60,20,0,0.55);">
  <div class="eyebrow" style="color:#ffd9a0;">Piece 01</div>
  <div class="headline">Party Guide</div>
  <div class="sub" style="color:#ffeeda;">Setup, timing and pacing for a night that stays a tasting.</div>
</div>
<div style="position:absolute;right:130px;top:140px;"><div class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></div></div>

{sheets(f"{SRC}/page-2.png", f"{SRC}/page-1.png", "0 6px 14px rgba(0,0,0,0.4), 0 50px 80px -28px rgba(0,0,0,0.7)", "0 8px 18px rgba(0,0,0,0.45), 0 62px 95px -30px rgba(0,0,0,0.8)")}
<div class="grainlayer"></div>
""")


# ---------------- B: DARK BAR ----------------
write("B-dark-bar.html", f"""
<div style="position:absolute;inset:0;background:
  radial-gradient(ellipse 1500px 1200px at 68% 18%, #4a3a2c 0%, #2b211a 42%, #17110d 78%, #100b08 100%);"></div>

<!-- spotlight -->
<div style="position:absolute;left:780px;top:-260px;width:1500px;height:1700px;
  background:radial-gradient(ellipse at 50% 30%, rgba(255,198,120,0.30), rgba(255,170,80,0.10) 42%, rgba(0,0,0,0) 68%);
  filter:blur(24px);"></div>

<!-- smoke haze -->
<div style="position:absolute;left:0;right:0;top:200px;height:1000px;filter:url(#haze);
  opacity:0.16;mix-blend-mode:screen;background:#e8d3b0;"></div>

<!-- bar top -->
<div style="position:absolute;left:0;right:0;top:775px;bottom:0;
  background:linear-gradient(180deg,#3a2418 0%,#241509 45%,#140b05 100%);"></div>
<div style="position:absolute;left:0;right:0;top:775px;bottom:0;filter:url(#wood);
  opacity:0.6;mix-blend-mode:multiply;background:#170c05;"></div>
<div style="position:absolute;left:0;right:0;top:765px;height:20px;
  background:linear-gradient(180deg,rgba(255,186,110,0.40),rgba(255,186,110,0));"></div>

<div style="position:absolute;left:130px;top:160px;color:#f6e9d6;">
  <div class="eyebrow" style="color:#d8a55f;">Piece 04</div>
  <div class="headline">Flavor Wheels</div>
  <div class="sub" style="color:#d9c9b4;">Put an actual word to what is in the glass.</div>
</div>
<div style="position:absolute;right:130px;top:150px;"><div class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></div></div>

{sheets(f"{SRC}/page-3.png", f"{SRC}/page-4.png", "0 6px 14px rgba(0,0,0,0.6), 0 55px 85px -30px rgba(0,0,0,0.85)", "0 8px 18px rgba(0,0,0,0.65), 0 70px 100px -32px rgba(0,0,0,0.92)")}
<div class="grainlayer" style="opacity:0.42;"></div>
""")


# ---------------- C: BRIGHT MODERN ----------------
write("C-bright-modern.html", f"""
<div style="position:absolute;inset:0;background:
  linear-gradient(172deg,#f2ede3 0%,#e8dfd0 44%,#ddd0bc 56%,#cbbaa1 100%);"></div>

<div style="position:absolute;left:-200px;top:-300px;width:1500px;height:1500px;
  background:radial-gradient(circle,rgba(255,255,255,0.85),rgba(255,255,255,0) 62%);"></div>

<!-- light oak surface -->
<div style="position:absolute;left:0;right:0;top:790px;bottom:0;
  background:linear-gradient(180deg,#d3b892 0%,#c2a479 46%,#ab8b60 100%);"></div>
<div style="position:absolute;left:0;right:0;top:790px;bottom:0;filter:url(#wood);
  opacity:0.34;mix-blend-mode:multiply;background:#7a5c36;"></div>

<div style="position:absolute;left:130px;top:165px;color:#241b10;">
  <div class="eyebrow" style="color:#8a6f45;">Piece 03</div>
  <div class="headline" style="color:#141414;">Agavebase Chart</div>
  <div class="sub" style="color:#4a4034;">Real bottles at three budgets, with the cost math done for you.</div>
</div>
<div style="position:absolute;right:130px;top:150px;"><div class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></div></div>

{sheets(f"{SRC}/page-2.png", f"{SRC}/page-3.png", "0 5px 12px rgba(90,66,36,0.3), 0 46px 70px -28px rgba(90,66,36,0.5)", "0 7px 16px rgba(90,66,36,0.36), 0 56px 84px -30px rgba(90,66,36,0.58)")}
<div class="grainlayer" style="opacity:0.34;"></div>
""")

print("mood demos written")
