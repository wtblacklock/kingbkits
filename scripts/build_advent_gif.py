import os, sys, math
REPO = "/Users/BIGWilly/Projects/kingbkits"
sys.path.insert(0, os.path.join(REPO, "scripts"))
from gen_hero_gif import build_gif

FONTS = ("@import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,300;0,400;"
         "0,500;0,600;0,700;0,800;1,400&family=Fraunces:opsz,wght@9..144,400;9..144,500;"
         "9..144,600&display=swap');")

PAPER = "#f3efe6"
PINE = "#2f4a3a"
INK = "#211c14"
INK_MUTED = "#6b6155"
LOGO = f"{REPO}/branding/logo/kingbkits-logo.png"

CSS_BASE = f"""
{FONTS}
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{width:1100px;height:1100px;overflow:hidden;}}
body{{font-family:'Raleway',sans-serif;position:relative;background:{PAPER};}}
.pill{{display:inline-flex;align-items:center;font-weight:700;font-size:20px;padding:8px 19px;
  border-radius:999px;color:#000;}}
"""


def check_glints(t):
    """A few small pine-green ring accents that fade in, echoing the scoring circles."""
    out = ""
    spots = [(910, 860, 0.0), (960, 190, 0.12), (140, 940, 0.2)]
    for x, y, delay in spots:
        local_t = max(0.0, min(1.0, (t - delay) / (1 - delay)))
        if local_t <= 0:
            continue
        op = math.sin(min(local_t, 1.0) * math.pi) * 0.5
        out += (f'<div style="position:absolute;left:{x}px;top:{y}px;width:14px;height:14px;'
                f'border-radius:50%;border:2px solid rgba(47,74,58,{op:.2f});"></div>')
    return out


def advent_bg(pages_html, t=0):
    grid = ("background-image:linear-gradient(rgba(47,74,58,0.08) 1px,transparent 1px),"
            "linear-gradient(90deg,rgba(47,74,58,0.08) 1px,transparent 1px);"
            "background-size:46px 46px;")
    bg = f"""
<div style="position:absolute;inset:0;{grid}"></div>
<div style="position:absolute;left:55%;top:-180px;width:820px;height:820px;
  background:radial-gradient(ellipse at 50% 30%,rgba(255,196,90,0.28),rgba(255,196,90,0) 62%);
  filter:blur(14px);"></div>
{check_glints(t)}

<div style="position:absolute;left:66px;top:80px;max-width:650px;">
  <div style="font-size:19px;letter-spacing:0.12em;text-transform:uppercase;font-weight:700;color:{PINE};">The Whisky Advent Companion</div>
  <div style="font-family:'Fraunces',serif;font-weight:500;font-size:70px;line-height:0.98;color:{INK};margin-top:12px;
       letter-spacing:-0.01em;">Track Every Night</div>
  <div style="font-size:22px;color:{INK_MUTED};margin-top:14px;">The printable sheet for a calendar you already own</div>
</div>
<div style="position:absolute;right:66px;top:66px;"><img src="{LOGO}" style="height:96px;display:block;"></div>
"""
    return f"""<!doctype html><html><head><meta charset='utf-8'><style>{CSS_BASE}</style></head>
<body>{bg}{pages_html}</body></html>"""


SHADOW = "0 8px 18px rgba(40,32,18,0.18), 0 44px 66px -24px rgba(40,32,18,0.3)"
SRC = f"{REPO}/listing_images_raw/listing_images_advent"

pages = [
    dict(img=f"{SRC}/page-9.png", x_pct="52%", y_final=430, ry=0, rz=-1, w=460, delay=0.0,
         shadow=SHADOW),
    dict(img=f"{SRC}/page-2.png", x_pct="20%", y_final=560, ry=6, rz=-8, w=280, delay=0.14,
         shadow=SHADOW),
    dict(img=f"{SRC}/page-8.png", x_pct="83%", y_final=570, ry=-6, rz=7, w=290, delay=0.24,
         shadow=SHADOW),
]

build_gif("advent-hero", REPO + "/source", advent_bg, pages, size=1100, n_frames=16)
print("done")
