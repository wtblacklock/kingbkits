import os

REPO = "/Users/BIGWilly/Projects/kingbkits"
LOGO_PATH = f"{REPO}/branding/logo/kingbkits-logo.png"

# Unified brand system: warm near-black (never literal #000), the exact yellow
# from the logo as the one accent, warm paper/muted tones instead of white/grey.
YELLOW = "#fff200"
PAPER = "#f3efe6"
MUTED = "#b7b0a0"
NEAR_BLACK = "#0d0b08"

FONTS = ("@import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,300;0,400;"
         "0,500;0,600;0,700;0,800;1,400&family=Fraunces:opsz,wght@9..144,400;9..144,500;"
         "9..144,600&display=swap');")

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
  <filter id="stone">
    <feTurbulence type="fractalNoise" baseFrequency="0.014" numOctaves="5" seed="9"/>
    <feColorMatrix type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.38"/></feComponentTransfer>
  </filter>
  <filter id="stone-fine">
    <feTurbulence type="fractalNoise" baseFrequency="0.045" numOctaves="4" seed="14"/>
    <feColorMatrix type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.16"/></feComponentTransfer>
  </filter>
  <filter id="haze">
    <feTurbulence type="fractalNoise" baseFrequency="0.004 0.011" numOctaves="5" seed="11"/>
    <feColorMatrix type="saturate" values="0"/>
    <feComponentTransfer><feFuncA type="linear" slope="0.5"/></feComponentTransfer>
  </filter>
</defs></svg>
"""

def bokeh(spec, rgb="255,225,160"):
    out = ""
    for x, y, r, a, blur in spec:
        out += (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{r}px;height:{r}px;'
                f'border-radius:50%;background:radial-gradient(circle at 38% 34%,rgba({rgb},{a}),'
                f'rgba({rgb},{a*0.55}) 55%,rgba({rgb},0) 72%);filter:blur({blur}px);"></div>')
    return out

def confetti(spec):
    out = ""
    for x, y, r, color, op in spec:
        out += (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{r}px;height:{r}px;'
                f'border-radius:50%;background:{color};opacity:{op};"></div>')
    return out


def write(base, name, mood_bg_fn, pal, body_inner):
    html = f"""<!doctype html><html><head><meta charset='utf-8'><style>
{FONTS}
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:2000px;height:2000px;overflow:hidden;}}
body{{font-family:'Raleway',sans-serif;position:relative;background:{NEAR_BLACK};}}
.pill{{display:inline-flex;align-items:center;font-weight:700;font-size:32px;padding:12px 30px;
  border-radius:999px;color:#000;}}
.cap{{font-size:32px;letter-spacing:0.1em;text-transform:uppercase;font-weight:700;}}
.grain{{position:absolute;inset:0;filter:url(#grain);opacity:{pal['grain']};mix-blend-mode:overlay;background:#fff;}}
</style></head><body>{FILTERS}{mood_bg_fn}{body_inner}<div class="grain"></div></body></html>"""
    with open(os.path.join(base, name), "w") as f:
        f.write(html)


def badge():
    return (f'<div style="position:absolute;right:90px;top:90px;">'
            f'<img src="{LOGO_PATH}" style="height:172px;display:block;'
            f'filter:drop-shadow(0 10px 22px rgba(0,0,0,0.55));"></div>')


# ---- unified dark background: warm near-black base + one or two accent glows
#      + an optional per-kit motif (embers, dust, haze, string-lights...) ----
def midnight_bg(tint, glow_rgb, glow2_rgb=None, motif=""):
    glow2 = ""
    if glow2_rgb:
        glow2 = (f'<div style="position:absolute;left:-260px;top:420px;width:1200px;height:1200px;'
                 f'background:radial-gradient(ellipse at 50% 50%,rgba({glow2_rgb},0.16),'
                 f'rgba({glow2_rgb},0) 65%);filter:blur(30px);"></div>')
    return f"""
<div style="position:absolute;inset:0;background:
  radial-gradient(ellipse 1700px 1300px at 66% 9%,{tint} 0%,#15120d 38%,#0a0806 70%,{NEAR_BLACK} 100%);"></div>
<div style="position:absolute;left:55%;top:-280px;width:1500px;height:1500px;
  background:radial-gradient(ellipse at 50% 30%,rgba({glow_rgb},0.22),rgba({glow_rgb},0) 62%);
  filter:blur(20px);"></div>
{glow2}
{motif}
<div style="position:absolute;left:0;right:0;bottom:0;height:560px;
  background:linear-gradient(180deg,rgba(0,0,0,0) 0%,rgba(0,0,0,0.5) 100%);"></div>"""


def midnight_pal(grain="0.3"):
    return dict(eyebrow=YELLOW, head=PAPER, sub=MUTED, grain=grain)


# ---- bundle/"what's inside" slide: left-aligned itemized list + fanned pages ----
def bundle_slide(pal, count_label, items, pages_html):
    items_html = "".join(
        f'<div style="display:flex;gap:20px;align-items:baseline;margin-top:24px;">'
        f'<span style="font-family:\'Fraunces\',serif;font-weight:500;font-size:30px;'
        f'color:{pal["eyebrow"]};min-width:50px;">{i:02d}</span>'
        f'<span style="font-size:30px;color:{pal["head"]};">{label}</span></div>'
        for i, label in enumerate(items, 1)
    )
    return f"""
<div style="position:absolute;left:100px;top:150px;max-width:840px;">
  <div style="font-size:30px;letter-spacing:0.16em;text-transform:uppercase;font-weight:700;
       color:{pal['eyebrow']};">What&rsquo;s Inside</div>
  <div style="font-family:'Fraunces',serif;font-weight:500;font-style:normal;font-size:100px;
       line-height:1.0;color:{pal['head']};margin-top:16px;">{count_label}</div>
  <div style="font-size:32px;color:{pal['sub']};margin-top:16px;">Instant Digital Download &middot; Print at Home</div>
  <div style="margin-top:8px;">{items_html}</div>
</div>
{badge()}
{pages_html}"""


# ---- text-free hero background: badge + fanned pages only, no headline block.
#      For contexts (like the marketing site) that overlay their own heading text
#      on top of the hero image - baking our own text in there would duplicate it. ----
def hero_bg_only(pages_html):
    return f"{badge()}{pages_html}"


# ---- photo slide: a real lifestyle photo (not a page mockup) inset with a frame ----
def photo_slide(cap, img, cap_color, size=1600, top=300):
    return f"""
<div style="position:absolute;left:100px;top:90px;">
  <div class="cap" style="color:{cap_color};">{cap}</div>
</div>
{badge()}
<div style="position:absolute;left:50%;top:{top}px;transform:translateX(-50%);">
  <img src="{img}" style="width:{size}px;display:block;border-radius:10px;
       box-shadow:0 20px 40px rgba(0,0,0,0.6), 0 90px 130px -40px rgba(0,0,0,0.95);">
</div>"""


# ---- single big-image slide: tiny caption, one large product shot ----
def single_image_slide(cap, img, cap_color, w=1560, top=340, shadow="", rot=0):
    return f"""
<div style="position:absolute;left:100px;top:90px;">
  <div class="cap" style="color:{cap_color};">{cap}</div>
</div>
{badge()}
<div style="position:absolute;left:50%;top:{top}px;transform:translateX(-50%) rotate({rot}deg);">
  <img src="{img}" style="width:{w}px;display:block;box-shadow:{shadow};">
</div>"""


# ---- hero: headline, one line, tier pills, big fanned pages ----
def hero_slide(eyebrow, title_html, sub, pal, pages_html, tiers=True, tier_labels=("Newbie", "Casual", "Aficionado")):
    tiers_html = ""
    if tiers:
        solid, o1, o2 = tier_labels
        tiers_html = f"""
  <div style="display:flex;gap:20px;margin-top:38px;">
    <span class="pill" style="background:{YELLOW};">{solid}</span>
    <span class="pill" style="color:{PAPER};background:rgba(255,255,255,0.07);
      border:1.5px solid rgba(255,242,0,0.5);">{o1}</span>
    <span class="pill" style="color:{PAPER};background:rgba(255,255,255,0.07);
      border:1.5px solid rgba(255,242,0,0.5);">{o2}</span>
  </div>"""
    return f"""
<div style="position:absolute;left:100px;top:100px;max-width:1500px;{pal.get('shadow','')}">
  <div style="font-size:32px;letter-spacing:0.16em;text-transform:uppercase;font-weight:700;
       color:{pal['eyebrow']};">{eyebrow}</div>
  <div style="font-family:'Fraunces',serif;font-optical-sizing:auto;font-weight:500;font-style:normal;
       font-size:126px;line-height:0.98;color:{pal['head']};margin-top:18px;
       letter-spacing:-0.01em;">{title_html}</div>
  <div style="font-size:40px;color:{pal['sub']};margin-top:22px;">{sub}</div>
  {tiers_html}
</div>
{badge()}
{pages_html}"""
