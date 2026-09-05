import os

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
body{{font-family:'Raleway',sans-serif;position:relative;}}
.kb{{display:inline-flex;flex-direction:column;align-items:center;justify-content:center;background:#000;
  border-radius:24px;padding:18px 30px 20px;font-family:'Archivo Black',sans-serif;line-height:0.92;
  text-align:center;width:fit-content;}}
.kb .l1{{font-size:40px;color:#f3c318;}}
.kb .l2{{font-size:28px;color:#fff;letter-spacing:0.02em;margin-top:2px;}}
.pill{{display:inline-flex;align-items:center;font-weight:700;font-size:32px;padding:12px 30px;
  border-radius:999px;color:#000;}}
.cap{{font-size:32px;letter-spacing:0.1em;text-transform:uppercase;font-weight:700;}}
.grain{{position:absolute;inset:0;filter:url(#grain);opacity:{pal['grain']};mix-blend-mode:overlay;background:#fff;}}
</style></head><body>{FILTERS}{mood_bg_fn}{body_inner}<div class="grain"></div></body></html>"""
    with open(os.path.join(base, name), "w") as f:
        f.write(html)


def badge():
    return '<div style="position:absolute;right:100px;top:100px;"><div class="kb"><span class="l1">KINGB</span><span class="l2">KITS</span></div></div>'


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
def hero_slide(eyebrow, title_html, sub, pal, pages_html, tiers=True):
    tiers_html = ""
    if tiers:
        tiers_html = """
  <div style="display:flex;gap:22px;margin-top:36px;">
    <span class="pill" style="background:#87cb28;">Newbie</span>
    <span class="pill" style="background:#ffff00;">Casual</span>
    <span class="pill" style="background:#ffd230;">Aficionado</span>
  </div>"""
    return f"""
<div style="position:absolute;left:100px;top:100px;max-width:1500px;{pal.get('shadow','')}">
  <div style="font-size:34px;letter-spacing:0.14em;text-transform:uppercase;font-weight:700;
       color:{pal['eyebrow']};">{eyebrow}</div>
  <div style="font-weight:300;font-size:132px;line-height:0.98;color:{pal['head']};margin-top:16px;
       letter-spacing:-0.02em;">{title_html}</div>
  <div style="font-size:42px;color:{pal['sub']};margin-top:20px;">{sub}</div>
  {tiers_html}
</div>
{badge()}
{pages_html}"""
