import sys
sys.path.insert(0, "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad")
from gen_hero_gif import build_gif

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

CSS_BASE = f"""
{FONTS}
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:1100px;height:1100px;overflow:hidden;}}
body{{font-family:'Raleway',sans-serif;position:relative;}}
.kb{{display:inline-flex;flex-direction:column;align-items:center;justify-content:center;background:#000;
  border-radius:14px;padding:11px 18px 12px;font-family:'Archivo Black',sans-serif;line-height:0.92;
  text-align:center;width:fit-content;}}
.kb .l1{{font-size:24px;color:#f3c318;}}
.kb .l2{{font-size:17px;color:#fff;letter-spacing:0.02em;margin-top:1px;}}
.pill{{display:inline-flex;align-items:center;font-weight:700;font-size:20px;padding:8px 19px;
  border-radius:999px;color:#000;}}
"""

SCALE = 1100 / 2000  # slides were designed at 2000px canvas


# ================= AGAVE =================
def agave_bg(pages_html):
    bg = f"""
<div style="position:absolute;inset:0;background:
  radial-gradient(ellipse 880px 715px at 66% 14%,#4a3a2c 0%,#2b211a 40%,#17110d 76%,#0f0a07 100%);"></div>
<div style="position:absolute;left:418px;top:-176px;width:858px;height:962px;
  background:radial-gradient(ellipse at 50% 30%,rgba(255,198,120,0.30),rgba(255,170,80,0.10) 42%,rgba(0,0,0,0) 68%);
  filter:blur(13px);"></div>
<div style="position:absolute;left:0;right:0;top:66px;height:495px;filter:url(#haze);
  opacity:0.15;mix-blend-mode:screen;background:#e8d3b0;"></div>
{bokeh([(80,138,83,0.42,26),(231,83,53,0.36,18),(858,182,66,0.34,22),
        (990,99,83,0.30,26),(517,66,46,0.26,16),(143,286,44,0.22,16)])}
<div style="position:absolute;left:0;right:0;top:512px;bottom:0;
  background:linear-gradient(180deg,#3a2418 0%,#21130a 45%,#120a04 100%);"></div>
<div style="position:absolute;left:0;right:0;top:512px;bottom:0;filter:url(#wood);
  opacity:0.58;mix-blend-mode:multiply;background:#170c05;"></div>
<div style="position:absolute;left:0;right:0;top:507px;height:11px;
  background:linear-gradient(180deg,rgba(255,186,110,0.38),rgba(255,186,110,0));"></div>

<div style="position:absolute;left:66px;top:80px;max-width:650px;">
  <div style="font-size:19px;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;color:#d8a55f;">The Agave Tasting Journey</div>
  <div style="font-weight:300;font-size:73px;line-height:0.96;color:#f6e9d6;margin-top:12px;
       letter-spacing:-0.02em;">Tequila &amp; Mezcal</div>
  <div style="font-size:23px;color:#d9c9b4;margin-top:14px;">7-Page Printable Tasting Kit &middot; Instant Download</div>
  <div style="display:flex;gap:12px;margin-top:20px;">
    <span class="pill" style="background:#87cb28;">Newbie</span>
    <span class="pill" style="background:#ffff00;">Casual</span>
    <span class="pill" style="background:#ffd230;">Aficionado</span>
  </div>
</div>
<div style="position:absolute;right:66px;top:66px;"><div class="kb"><span class="l1">KINGB</span><span class="l2">KITS</span></div></div>
"""
    return f"""<!doctype html><html><head><meta charset='utf-8'><style>{CSS_BASE}</style></head>
<body>{FILTERS}{bg}{pages_html}</body></html>"""

SHADOW_BAR = "0 6px 13px rgba(0,0,0,0.62), 0 44px 66px -20px rgba(0,0,0,0.92)"
SRC_AGAVE = "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad/listing_images_agave"

agave_pages = [
    dict(img=f"{SRC_AGAVE}/page-2.png", x_pct="20%", y_final=420, ry=7, rz=-7, w=470, delay=0.0,
         shadow=SHADOW_BAR, filter="brightness(0.88)"),
    dict(img=f"{SRC_AGAVE}/page-4.png", x_pct="44%", y_final=375, ry=2, rz=-2, w=510, delay=0.12,
         shadow=SHADOW_BAR, filter="brightness(0.95)"),
    dict(img=f"{SRC_AGAVE}/page-1.png", x_pct="70%", y_final=420, ry=-6, rz=4, w=470, delay=0.24,
         shadow=SHADOW_BAR),
]

build_gif("agave-hero", "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad",
           agave_bg, agave_pages, size=1100, n_frames=16)


# ================= HALLOWEEN =================
def hw_bg(pages_html):
    bg = f"""
<div style="position:absolute;inset:0;background:
  radial-gradient(ellipse 880px 715px at 66% 14%,#3a2836 0%,#241823 40%,#140c14 76%,#0a0509 100%);"></div>
<div style="position:absolute;left:418px;top:-176px;width:858px;height:962px;
  background:radial-gradient(ellipse at 50% 30%,rgba(255,140,60,0.30),rgba(255,110,60,0.10) 42%,rgba(0,0,0,0) 68%);
  filter:blur(13px);"></div>
<div style="position:absolute;left:0;right:0;top:66px;height:495px;filter:url(#haze);
  opacity:0.14;mix-blend-mode:screen;background:#d9b8e0;"></div>
{confetti([(66,418,5,'#ffb703',0.4),(1012,385,4,'#e0763a',0.35),(935,77,4,'#c94f7a',0.4)])}
<div style="position:absolute;left:0;right:0;top:512px;bottom:0;
  background:linear-gradient(180deg,#2e1c26 0%,#190f16 45%,#0d0709 100%);"></div>
<div style="position:absolute;left:0;right:0;top:512px;bottom:0;filter:url(#wood);
  opacity:0.56;mix-blend-mode:multiply;background:#160b14;"></div>
<div style="position:absolute;left:0;right:0;top:507px;height:11px;
  background:linear-gradient(180deg,rgba(255,140,70,0.4),rgba(255,140,70,0));"></div>

<div style="position:absolute;left:66px;top:80px;max-width:650px;">
  <div style="font-size:19px;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;color:#e0a866;">The Halloween Pairing Kit</div>
  <div style="font-weight:300;font-size:73px;line-height:0.96;color:#f2e3da;margin-top:12px;
       letter-spacing:-0.02em;">Candy &amp; Whisky</div>
  <div style="font-size:23px;color:#d8c2be;margin-top:14px;">7-Page Printable Tasting Kit &middot; Instant Download</div>
  <div style="display:flex;gap:12px;margin-top:20px;">
    <span class="pill" style="background:#87cb28;">Newbie</span>
    <span class="pill" style="background:#ffff00;">Casual</span>
    <span class="pill" style="background:#ffd230;">Aficionado</span>
  </div>
</div>
<div style="position:absolute;right:66px;top:66px;"><div class="kb"><span class="l1">KINGB</span><span class="l2">KITS</span></div></div>
"""
    return f"""<!doctype html><html><head><meta charset='utf-8'><style>{CSS_BASE}</style></head>
<body>{FILTERS}{bg}{pages_html}</body></html>"""

SHADOW_HAUNTED = "0 6px 13px rgba(0,0,0,0.65), 0 44px 66px -20px rgba(0,0,0,0.92)"
SRC_HW = "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad/listing_images_halloween"

hw_pages = [
    dict(img=f"{SRC_HW}/page-2.png", x_pct="20%", y_final=420, ry=7, rz=-7, w=470, delay=0.0,
         shadow=SHADOW_HAUNTED, filter="brightness(0.88)"),
    dict(img=f"{SRC_HW}/page-4.png", x_pct="44%", y_final=375, ry=2, rz=-2, w=510, delay=0.12,
         shadow=SHADOW_HAUNTED, filter="brightness(0.95)"),
    dict(img=f"{SRC_HW}/page-1.png", x_pct="70%", y_final=420, ry=-6, rz=4, w=470, delay=0.24,
         shadow=SHADOW_HAUNTED),
]

build_gif("halloween-hero", "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad",
           hw_bg, hw_pages, size=1100, n_frames=16)

# ================= CIGAR =================
def cigar_bg(pages_html):
    bg = f"""
<div style="position:absolute;inset:0;background:
  radial-gradient(ellipse 880px 715px at 66% 14%,#4a3a2c 0%,#2b211a 40%,#17110d 76%,#0f0a07 100%);"></div>
<div style="position:absolute;left:418px;top:-176px;width:858px;height:962px;
  background:radial-gradient(ellipse at 50% 30%,rgba(255,198,120,0.30),rgba(255,170,80,0.10) 42%,rgba(0,0,0,0) 68%);
  filter:blur(13px);"></div>
<div style="position:absolute;left:0;right:0;top:66px;height:495px;filter:url(#haze);
  opacity:0.15;mix-blend-mode:screen;background:#e8d3b0;"></div>
{bokeh([(80,138,83,0.42,26),(231,83,53,0.36,18),(858,182,66,0.34,22),
        (990,99,83,0.30,26),(517,66,46,0.26,16),(143,286,44,0.22,16)])}
<div style="position:absolute;left:0;right:0;top:512px;bottom:0;
  background:linear-gradient(180deg,#3a2418 0%,#21130a 45%,#120a04 100%);"></div>
<div style="position:absolute;left:0;right:0;top:512px;bottom:0;filter:url(#wood);
  opacity:0.58;mix-blend-mode:multiply;background:#170c05;"></div>
<div style="position:absolute;left:0;right:0;top:507px;height:11px;
  background:linear-gradient(180deg,rgba(255,186,110,0.38),rgba(255,186,110,0));"></div>

<div style="position:absolute;left:66px;top:80px;max-width:650px;">
  <div style="font-size:19px;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;color:#d8a55f;">The Cigar &amp; Whisky Journey</div>
  <div style="font-weight:300;font-size:73px;line-height:0.96;color:#f6e9d6;margin-top:12px;
       letter-spacing:-0.02em;">Cigar &amp; Whisky</div>
  <div style="font-size:23px;color:#d9c9b4;margin-top:14px;">7-Page Printable Pairing Kit &middot; Instant Download</div>
  <div style="display:flex;gap:12px;margin-top:20px;">
    <span class="pill" style="background:#87cb28;">Newbie</span>
    <span class="pill" style="background:#ffff00;">Casual</span>
    <span class="pill" style="background:#ffd230;">Aficionado</span>
  </div>
</div>
<div style="position:absolute;right:66px;top:66px;"><div class="kb"><span class="l1">KINGB</span><span class="l2">KITS</span></div></div>
"""
    return f"""<!doctype html><html><head><meta charset='utf-8'><style>{CSS_BASE}</style></head>
<body>{FILTERS}{bg}{pages_html}</body></html>"""

SHADOW_CIGAR = "0 6px 13px rgba(0,0,0,0.62), 0 44px 66px -20px rgba(0,0,0,0.92)"
SRC_CIGAR = "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad/listing_images"

cigar_pages = [
    dict(img=f"{SRC_CIGAR}/page-2.png", x_pct="20%", y_final=420, ry=7, rz=-7, w=470, delay=0.0,
         shadow=SHADOW_CIGAR, filter="brightness(0.88)"),
    dict(img=f"{SRC_CIGAR}/page-4.png", x_pct="44%", y_final=375, ry=2, rz=-2, w=510, delay=0.12,
         shadow=SHADOW_CIGAR, filter="brightness(0.95)"),
    dict(img=f"{SRC_CIGAR}/page-1.png", x_pct="70%", y_final=420, ry=-6, rz=4, w=470, delay=0.24,
         shadow=SHADOW_CIGAR),
]

build_gif("cigar-hero", "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad",
           cigar_bg, cigar_pages, size=1100, n_frames=16)

print("done")
