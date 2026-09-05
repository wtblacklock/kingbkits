import os, sys, math
REPO = "/Users/BIGWilly/Projects/kingbkits"
sys.path.insert(0, os.path.join(REPO, "scripts"))
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


def smoke_wisps(t, base):
    """Three soft wisps that curl upward and fade, staggered so they never all peak at once.
    Keep base points inside open background, not under the page-mockup stack."""
    out = ""
    for i, (bx, by) in enumerate(base):
        local_t = max(0.0, min(1.0, t * 1.35 - i * 0.22))
        if local_t <= 0:
            continue
        drift_x = math.sin(local_t * math.pi * 1.6 + i * 1.7) * (14 + i * 5)
        y = by - local_t * 150 - i * 10
        x = bx + drift_x
        size = 30 + local_t * 66
        opacity = math.sin(min(local_t, 1.0) * math.pi) * 0.4
        blur = 6 + local_t * 16
        out += (f'<div style="position:absolute;left:{x:.0f}px;top:{y:.0f}px;width:{size:.0f}px;'
                f'height:{size*1.35:.0f}px;border-radius:50%;'
                f'background:radial-gradient(ellipse at 50% 60%,rgba(230,224,212,{opacity:.3f}),'
                f'rgba(230,224,212,0) 72%);filter:blur({blur:.0f}px);"></div>')
    return out


def ghost(t, x0, y0, drift=70, bob=22, cycles=1.4, scale=1.0, opacity=0.8):
    """A small friendly ghost that drifts sideways and bobs up and down."""
    x = x0 + t * drift
    y = y0 + math.sin(t * math.pi * 2 * cycles) * bob
    w = 118 * scale
    body_h = 92 * scale
    eye_w, eye_h = 13 * scale, 17 * scale
    scallop = w / 5
    scallops = "".join(
        f'<div style="width:{scallop:.0f}px;height:{scallop:.0f}px;background:rgba(255,255,255,0.94);'
        f'border-radius:0 0 {scallop:.0f}px {scallop:.0f}px;margin-right:-1px;"></div>'
        for _ in range(5)
    )
    return f"""
<div style="position:absolute;left:{x:.0f}px;top:{y:.0f}px;opacity:{opacity};
     filter:drop-shadow(0 8px 14px rgba(0,0,0,0.35));">
  <div style="width:{w:.0f}px;height:{body_h:.0f}px;background:rgba(255,255,255,0.94);
       border-radius:{w/2:.0f}px {w/2:.0f}px 0 0;position:relative;">
    <div style="position:absolute;bottom:-{scallop*0.7:.0f}px;left:0;display:flex;width:{w:.0f}px;">
      {scallops}
    </div>
    <div style="position:absolute;top:{body_h*0.38:.0f}px;left:{w*0.27:.0f}px;width:{eye_w:.0f}px;
         height:{eye_h:.0f}px;background:#241a2c;border-radius:50%;"></div>
    <div style="position:absolute;top:{body_h*0.38:.0f}px;left:{w*0.63:.0f}px;width:{eye_w:.0f}px;
         height:{eye_h:.0f}px;background:#241a2c;border-radius:50%;"></div>
  </div>
</div>"""


# ================= AGAVE (unchanged aside from the new t_global signature) =================
def agave_bg(pages_html, t=0):
    bg = f"""
<div style="position:absolute;inset:0;background:
  radial-gradient(ellipse 880px 715px at 66% 14%,#9a5230 0%,#6b3620 40%,#3c1f14 76%,#1e100a 100%);"></div>
<div style="position:absolute;left:418px;top:-176px;width:858px;height:962px;
  background:radial-gradient(ellipse at 50% 30%,rgba(90,205,185,0.30),rgba(255,150,70,0.14) 42%,rgba(0,0,0,0) 68%);
  filter:blur(13px);"></div>
<div style="position:absolute;left:0;right:0;top:66px;height:495px;filter:url(#haze);
  opacity:0.16;mix-blend-mode:screen;background:#f0d8ae;"></div>
{bokeh([(80,138,83,0.34,26),(990,99,83,0.30,26)])}
{bokeh([(231,83,53,0.4,18),(858,182,66,0.36,22),(517,66,46,0.34,16),(143,286,44,0.3,16)], rgb="90,210,190")}
<div style="position:absolute;left:0;right:0;top:512px;bottom:0;
  background:linear-gradient(180deg,#b06f45 0%,#7a4a2c 45%,#48301e 100%);"></div>
<div style="position:absolute;left:0;right:0;top:512px;bottom:0;filter:url(#wood);
  opacity:0.4;mix-blend-mode:multiply;background:#3e2818;"></div>

<div style="position:absolute;left:66px;top:80px;max-width:650px;">
  <div style="font-size:19px;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;color:#f0a860;">The Agave Tasting Journey</div>
  <div style="font-weight:300;font-size:73px;line-height:0.96;color:#fbeddb;margin-top:12px;
       letter-spacing:-0.02em;">Tequila &amp; Mezcal</div>
  <div style="font-size:23px;color:#e6c8a8;margin-top:14px;">8-Page Printable Tasting Kit &middot; Instant Download</div>
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
SRC_AGAVE = f"{REPO}/listing_images_raw/listing_images_agave"

agave_pages = [
    dict(img=f"{SRC_AGAVE}/page-2.png", x_pct="20%", y_final=420, ry=7, rz=-7, w=470, delay=0.0,
         shadow=SHADOW_BAR, filter="brightness(0.88)"),
    dict(img=f"{SRC_AGAVE}/page-4.png", x_pct="44%", y_final=375, ry=2, rz=-2, w=510, delay=0.12,
         shadow=SHADOW_BAR, filter="brightness(0.95)"),
    dict(img=f"{SRC_AGAVE}/page-1.png", x_pct="70%", y_final=420, ry=-6, rz=4, w=470, delay=0.24,
         shadow=SHADOW_BAR),
]

build_gif("agave-hero", REPO + "/source", agave_bg, agave_pages, size=1100, n_frames=16)


# ================= HALLOWEEN =================
def hw_bg(pages_html, t=0):
    bg = f"""
<div style="position:absolute;inset:0;background:
  radial-gradient(ellipse 880px 715px at 66% 14%,#5a2f6e 0%,#341b42 40%,#1a0e22 76%,#0a0510 100%);"></div>
<div style="position:absolute;left:418px;top:-176px;width:858px;height:962px;
  background:radial-gradient(ellipse at 50% 30%,rgba(255,140,60,0.24),rgba(255,110,60,0.08) 42%,rgba(0,0,0,0) 68%);
  filter:blur(13px);"></div>
<div style="position:absolute;left:0;right:0;top:66px;height:495px;filter:url(#haze);
  opacity:0.2;mix-blend-mode:screen;background:#c98be0;"></div>
{ghost(t, x0=760, y0=140, drift=90, bob=26, cycles=1.3, scale=0.62, opacity=0.85)}
<div style="position:absolute;left:0;right:0;top:512px;bottom:0;
  background:linear-gradient(180deg,#2c2a2f 0%,#19171b 45%,#0a090b 100%);"></div>

<div style="position:absolute;left:66px;top:80px;max-width:650px;">
  <div style="font-size:19px;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;color:#e0a866;">The Halloween Pairing Kit</div>
  <div style="font-weight:300;font-size:73px;line-height:0.96;color:#f2e3da;margin-top:12px;
       letter-spacing:-0.02em;">Candy &amp; Whisky</div>
  <div style="font-size:23px;color:#d8c2be;margin-top:14px;">8-Page Printable Tasting Kit &middot; Instant Download</div>
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
SRC_HW = f"{REPO}/listing_images_raw/listing_images_halloween"

hw_pages = [
    dict(img=f"{SRC_HW}/page-2.png", x_pct="20%", y_final=420, ry=7, rz=-7, w=470, delay=0.0,
         shadow=SHADOW_HAUNTED, filter="brightness(0.88)"),
    dict(img=f"{SRC_HW}/page-4.png", x_pct="44%", y_final=375, ry=2, rz=-2, w=510, delay=0.12,
         shadow=SHADOW_HAUNTED, filter="brightness(0.95)"),
    dict(img=f"{SRC_HW}/page-1.png", x_pct="70%", y_final=420, ry=-6, rz=4, w=470, delay=0.24,
         shadow=SHADOW_HAUNTED),
]

build_gif("halloween-hero", REPO + "/source", hw_bg, hw_pages, size=1100, n_frames=16)


# ================= CIGAR =================
def cigar_bg(pages_html, t=0):
    bg = f"""
<div style="position:absolute;inset:0;background:
  radial-gradient(ellipse 880px 715px at 66% 14%,#4e3628 0%,#2c1e16 40%,#180f0a 76%,#0f0906 100%);"></div>
<div style="position:absolute;left:418px;top:-176px;width:858px;height:962px;
  background:radial-gradient(ellipse at 50% 30%,rgba(255,198,120,0.30),rgba(255,170,80,0.10) 42%,rgba(0,0,0,0) 68%);
  filter:blur(13px);"></div>
<div style="position:absolute;left:0;right:0;top:66px;height:495px;filter:url(#haze);
  opacity:0.15;mix-blend-mode:screen;background:#e8d3b0;"></div>
{bokeh([(80,138,83,0.42,26),(231,83,53,0.36,18),(858,182,66,0.34,22),
        (990,99,83,0.30,26),(517,66,46,0.26,16),(143,286,44,0.22,16)])}
{smoke_wisps(t, base=[(800, 330), (830, 350), (770, 310)])}
<div style="position:absolute;left:0;right:0;top:512px;bottom:0;
  background:linear-gradient(180deg,#48261a 0%,#2c150c 45%,#160a05 100%);"></div>
<div style="position:absolute;left:0;right:0;top:512px;bottom:0;filter:url(#wood);
  opacity:0.5;mix-blend-mode:multiply;background:#1a0d06;"></div>

<div style="position:absolute;left:66px;top:80px;max-width:650px;">
  <div style="font-size:19px;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;color:#d8a55f;">The Cigar &amp; Whisky Journey</div>
  <div style="font-weight:300;font-size:73px;line-height:0.96;color:#f6e9d6;margin-top:12px;
       letter-spacing:-0.02em;">Cigar &amp; Whisky</div>
  <div style="font-size:23px;color:#d9c9b4;margin-top:14px;">8-Page Printable Pairing Kit &middot; Instant Download</div>
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
SRC_CIGAR = f"{REPO}/listing_images_raw/listing_images"

cigar_pages = [
    dict(img=f"{SRC_CIGAR}/page-2.png", x_pct="20%", y_final=420, ry=7, rz=-7, w=470, delay=0.0,
         shadow=SHADOW_CIGAR, filter="brightness(0.88)"),
    dict(img=f"{SRC_CIGAR}/page-4.png", x_pct="44%", y_final=375, ry=2, rz=-2, w=510, delay=0.12,
         shadow=SHADOW_CIGAR, filter="brightness(0.95)"),
    dict(img=f"{SRC_CIGAR}/page-1.png", x_pct="70%", y_final=420, ry=-6, rz=4, w=470, delay=0.24,
         shadow=SHADOW_CIGAR),
]

build_gif("cigar-hero", REPO + "/source", cigar_bg, cigar_pages, size=1100, n_frames=16)

print("done")
