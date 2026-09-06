import os, sys, math
REPO = "/Users/BIGWilly/Projects/kingbkits"
sys.path.insert(0, os.path.join(REPO, "scripts"))
from gen_hero_gif import build_gif

LOGO_PATH = f"{REPO}/branding/logo/kingbkits-logo.png"
YELLOW = "#fff200"
PAPER = "#f3efe6"
MUTED = "#b7b0a0"
NEAR_BLACK = "#0d0b08"

FONTS = ("@import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,300;0,400;"
         "0,500;0,600;0,700;0,800;1,400&family=Fraunces:opsz,wght@9..144,400;9..144,500;"
         "9..144,600&display=swap');")

FILTERS = """
<svg style="position:absolute;width:0;height:0"><defs>
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
body{{font-family:'Raleway',sans-serif;position:relative;background:{NEAR_BLACK};}}
.pill{{display:inline-flex;align-items:center;font-weight:700;font-size:20px;padding:8px 19px;
  border-radius:999px;}}
"""


def badge_img():
    return (f'<div style="position:absolute;right:60px;top:58px;">'
            f'<img src="{LOGO_PATH}" style="height:104px;display:block;'
            f'filter:drop-shadow(0 6px 14px rgba(0,0,0,0.55));"></div>')


def midnight_bg(tint, glow_rgb, glow2_rgb=None, motif=""):
    glow2 = ""
    if glow2_rgb:
        glow2 = (f'<div style="position:absolute;left:-140px;top:230px;width:660px;height:660px;'
                 f'background:radial-gradient(ellipse at 50% 50%,rgba({glow2_rgb},0.16),'
                 f'rgba({glow2_rgb},0) 65%);filter:blur(18px);"></div>')
    return f"""
<div style="position:absolute;inset:0;background:
  radial-gradient(ellipse 935px 715px at 66% 9%,{tint} 0%,#15120d 38%,#0a0806 70%,{NEAR_BLACK} 100%);"></div>
<div style="position:absolute;left:30%;top:-154px;width:825px;height:825px;
  background:radial-gradient(ellipse at 50% 30%,rgba({glow_rgb},0.22),rgba({glow_rgb},0) 62%);
  filter:blur(12px);"></div>
{glow2}
{motif}
<div style="position:absolute;left:0;right:0;bottom:0;height:310px;
  background:linear-gradient(180deg,rgba(0,0,0,0) 0%,rgba(0,0,0,0.5) 100%);"></div>"""


def headline(eyebrow, title_html, sub, tiers=True):
    tiers_html = ""
    if tiers:
        tiers_html = f"""
  <div style="display:flex;gap:12px;margin-top:20px;">
    <span class="pill" style="color:#000;background:{YELLOW};">Newbie</span>
    <span class="pill" style="color:{PAPER};background:rgba(255,255,255,0.07);
      border:1.5px solid rgba(255,242,0,0.5);">Casual</span>
    <span class="pill" style="color:{PAPER};background:rgba(255,255,255,0.07);
      border:1.5px solid rgba(255,242,0,0.5);">Aficionado</span>
  </div>"""
    return f"""
<div style="position:absolute;left:66px;top:70px;max-width:650px;">
  <div style="font-size:19px;letter-spacing:0.14em;text-transform:uppercase;font-weight:700;color:{YELLOW};">{eyebrow}</div>
  <div style="font-family:'Fraunces',serif;font-optical-sizing:auto;font-weight:500;font-style:normal;
       font-size:68px;line-height:0.98;color:{PAPER};margin-top:12px;
       letter-spacing:-0.01em;">{title_html}</div>
  <div style="font-size:22px;color:{MUTED};margin-top:14px;">{sub}</div>
  {tiers_html}
</div>
{badge_img()}"""


def smoke_wisps(t, base):
    """Wisps that continuously rise and fade, looping through several cycles across
    the whole clip so the scene keeps breathing after the pages settle. Keep base
    points inside open background, not under the page-mockup stack."""
    out = ""
    for i, (bx, by) in enumerate(base):
        cycle_t = (t * 3.0 - i * 0.3) % 1.0
        drift_x = math.sin(cycle_t * math.pi * 1.6 + i * 1.7) * (14 + i * 5)
        y = by - cycle_t * 150
        x = bx + drift_x
        size = 30 + cycle_t * 66
        opacity = math.sin(cycle_t * math.pi) * 0.4
        blur = 6 + cycle_t * 16
        out += (f'<div style="position:absolute;left:{x:.0f}px;top:{y:.0f}px;width:{size:.0f}px;'
                f'height:{size*1.35:.0f}px;border-radius:50%;'
                f'background:radial-gradient(ellipse at 50% 60%,rgba(230,224,212,{opacity:.3f}),'
                f'rgba(230,224,212,0) 72%);filter:blur({blur:.0f}px);"></div>')
    return out


def ghost(t, x0, y0, drift=90, bob=26, cycles=3.0, drift_cycles=1.0, scale=1.0, opacity=0.8):
    """A small friendly ghost that floats in a smooth continuous loop - bobbing and
    drifting side to side for the whole clip, never just flying off in one direction."""
    x = x0 + math.sin(t * math.pi * 2 * drift_cycles) * drift
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


def shimmer(t, base, rgb="120,225,205"):
    """Slow-pulsing accent dots - agave's answer to cigar's smoke and Halloween's ghost,
    since agave otherwise has zero motion once the pages settle."""
    out = ""
    for i, (x, y) in enumerate(base):
        phase = (t * 2.2 + i * 0.4) % 1.0
        a = 0.25 + 0.35 * (0.5 + 0.5 * math.sin(phase * math.pi * 2))
        out += (f'<div style="position:absolute;left:{x}px;top:{y}px;width:9px;height:9px;'
                f'border-radius:50%;background:radial-gradient(circle at 38% 34%,rgba({rgb},{a:.2f}),'
                f'rgba({rgb},{a*0.5:.2f}) 55%,rgba({rgb},0) 72%);filter:blur(4px);"></div>')
    return out


def page(img, x_pct, y_final, ry, rz, w, delay, shadow, filt="none"):
    return dict(img=img, x_pct=x_pct, y_final=y_final, ry=ry, rz=rz, w=w, delay=delay,
                shadow=shadow, filter=filt)


SHADOW = "0 6px 13px rgba(0,0,0,0.65), 0 44px 66px -20px rgba(0,0,0,0.92)"

# ================= AGAVE — patio dust: terracotta + agave-turquoise =================
SRC_AGAVE = f"{REPO}/listing_images_raw/listing_images_agave"

def agave_bg(pages_html, t=0):
    dust = bokeh([(80, 138, 42, 0.4, 12), (495, 33, 33, 0.36, 10), (429, 91, 23, 0.34, 8),
                  (72, 143, 22, 0.3, 8)], rgb="90,210,190")
    glints = shimmer(t, base=[(150, 60), (560, 95), (860, 50), (960, 190)])
    bg = midnight_bg("#241811", "255,150,70", glow2_rgb="90,210,190", motif=dust + glints)
    head = headline("The Agave Tasting Journey", "Tequila &amp; Mezcal",
                     "Six pairings, three tiers &middot; Instant Download")
    return f"""<!doctype html><html><head><meta charset='utf-8'><style>{CSS_BASE}</style></head>
<body>{FILTERS}{bg}{head}{pages_html}</body></html>"""

agave_pages = [
    page(f"{SRC_AGAVE}/page-2.png", "20%", 420, 7, -7, 470, 0.0, SHADOW, "brightness(0.9)"),
    page(f"{SRC_AGAVE}/page-4.png", "44%", 375, 2, -2, 510, 0.12, SHADOW, "brightness(0.96)"),
    page(f"{SRC_AGAVE}/page-1.png", "70%", 420, -6, 4, 470, 0.24, SHADOW),
]
build_gif("agave-hero", REPO + "/source", agave_bg, agave_pages, size=1100)


# ================= HALLOWEEN — violet haunt + pumpkin glow, a drifting ghost =================
SRC_HW = f"{REPO}/listing_images_raw/listing_images_halloween"

def hw_bg(pages_html, t=0):
    bg = midnight_bg("#1c1420", "170,110,220", glow2_rgb="255,140,60",
                      motif=ghost(t, x0=760, y0=140, drift=90, bob=26, cycles=3.0, drift_cycles=1.0,
                                   scale=0.62, opacity=0.85))
    head = headline("The Halloween Pairing Kit", "Candy &amp; Whisky",
                     "Six pairings, three tiers &middot; Instant Download")
    return f"""<!doctype html><html><head><meta charset='utf-8'><style>{CSS_BASE}</style></head>
<body>{FILTERS}{bg}{head}{pages_html}</body></html>"""

hw_pages = [
    page(f"{SRC_HW}/page-2.png", "20%", 420, 7, -7, 470, 0.0, SHADOW, "brightness(0.9)"),
    page(f"{SRC_HW}/page-4.png", "44%", 375, 2, -2, 510, 0.12, SHADOW, "brightness(0.96)"),
    page(f"{SRC_HW}/page-1.png", "70%", 420, -6, 4, 470, 0.24, SHADOW),
]
build_gif("halloween-hero", REPO + "/source", hw_bg, hw_pages, size=1100)


# ================= CIGAR — ember glow + curling smoke =================
SRC_CIGAR = f"{REPO}/listing_images_raw/listing_images"

def cigar_bg(pages_html, t=0):
    embers = bokeh([(80, 138, 10, 0.55, 6), (500, 60, 8, 0.45, 5), (462, 293, 9, 0.4, 6),
                    (65, 288, 7, 0.35, 5)], rgb="255,175,90")
    bg = midnight_bg("#241a12", "255,175,90", motif=embers + smoke_wisps(t, base=[(800, 330), (830, 350), (770, 310)]))
    head = headline("The Cigar &amp; Whisky Journey", "Cigar &amp; Whisky",
                     "Six pairings, three tiers &middot; Instant Download")
    return f"""<!doctype html><html><head><meta charset='utf-8'><style>{CSS_BASE}</style></head>
<body>{FILTERS}{bg}{head}{pages_html}</body></html>"""

cigar_pages = [
    page(f"{SRC_CIGAR}/page-2.png", "20%", 420, 7, -7, 470, 0.0, SHADOW, "brightness(0.9)"),
    page(f"{SRC_CIGAR}/page-4.png", "44%", 375, 2, -2, 510, 0.12, SHADOW, "brightness(0.96)"),
    page(f"{SRC_CIGAR}/page-1.png", "70%", 420, -6, 4, 470, 0.24, SHADOW),
]
build_gif("cigar-hero", REPO + "/source", cigar_bg, cigar_pages, size=1100)

# Advent has its own light "tracking desk" look now (paper_bg, not this file's
# midnight system) - see build_advent_gif.py.

print("done")
