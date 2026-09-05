import math, re

BASE = "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad"

def polar(cx, cy, r, angle_deg):
    a = math.radians(angle_deg - 90)  # start at top
    return (cx + r * math.cos(a), cy + r * math.sin(a))

def wedge_path(cx, cy, r1, r2, a1, a2):
    x1, y1 = polar(cx, cy, r1, a1)
    x2, y2 = polar(cx, cy, r1, a2)
    x3, y3 = polar(cx, cy, r2, a2)
    x4, y4 = polar(cx, cy, r2, a1)
    large = 1 if (a2 - a1) > 180 else 0
    return (f"M {x1:.2f} {y1:.2f} "
            f"A {r1:.2f} {r1:.2f} 0 {large} 1 {x2:.2f} {y2:.2f} "
            f"L {x3:.2f} {y3:.2f} "
            f"A {r2:.2f} {r2:.2f} 0 {large} 0 {x4:.2f} {y4:.2f} Z")

def radial_text(cx, cy, r, angle_deg, text, size, weight="500", fill="#2a221a", extra="", anchor_mode=None):
    x, y = polar(cx, cy, r, angle_deg)
    norm = angle_deg % 360
    if 180 < norm < 360:
        rot = angle_deg + 90
        anchor = "end"
    else:
        rot = angle_deg - 90
        anchor = "start"
    if anchor_mode == "middle":
        anchor = "middle"
    words = text.split(" ")
    if len(words) > 1:
        mid = (len(words) + 1) // 2
        line1 = " ".join(words[:mid])
        line2 = " ".join(words[mid:])
        content = (f'<tspan x="{x:.2f}" dy="-0.5em">{line1}</tspan>'
                   f'<tspan x="{x:.2f}" dy="1.05em">{line2}</tspan>')
    else:
        content = text
    return (f'<text x="{x:.2f}" y="{y:.2f}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" transform="rotate({rot:.2f} {x:.2f} {y:.2f})" '
            f'font-family="Raleway, sans-serif" {extra}>{content}</text>')

def build_wheel(cx, cy, categories, center_label, r0=64, r1=176, r2=272):
    n = len(categories)
    seg = 360 / n
    out = []
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r0}" fill="#17130f"/>')
    out.append(f'<text x="{cx}" y="{cy}" font-size="17" font-weight="700" fill="#f3c318" '
                f'text-anchor="middle" dominant-baseline="central" font-family=\'Raleway, sans-serif\'>{center_label}</text>')
    for i, cat in enumerate(categories):
        a1 = i * seg
        a2 = (i + 1) * seg
        mid = (a1 + a2) / 2
        out.append(f'<path d="{wedge_path(cx, cy, r0, r1, a1, a2)}" fill="{cat["color"]}" stroke="#fdf9ef" stroke-width="2"/>')
        out.append(radial_text(cx, cy, r0 + (r1 - r0) * 0.32, mid, cat["name"], 17, "700", "#241b10"))
        notes = cat["notes"]
        m = len(notes)
        nseg = seg / m
        for j, note in enumerate(notes):
            b1 = a1 + j * nseg
            b2 = a1 + (j + 1) * nseg
            bmid = (b1 + b2) / 2
            out.append(f'<path d="{wedge_path(cx, cy, r1, r2, b1, b2)}" fill="{cat["light"]}" stroke="#fdf9ef" stroke-width="1.5"/>')
            note_r = (r1 + r2) / 2 + 4
            out.append(radial_text(cx, cy, note_r, bmid, note, 14, "600", "#3a2f22", anchor_mode="middle"))
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r2}" fill="none" stroke="#d8d8d5" stroke-width="1.5"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r1}" fill="none" stroke="#fdf9ef" stroke-width="1.5"/>')
    return "\n".join(out)

tequila_categories = [
    {"name": "Agave", "color": "#c9cc57", "light": "#e6e8b0",
     "notes": ["Roasted Agave", "Sweet Potato", "Squash"]},
    {"name": "Citrus", "color": "#e3c34a", "light": "#f2e3a9",
     "notes": ["Lime", "Grapefruit", "Orange Peel"]},
    {"name": "Pepper", "color": "#d4653f", "light": "#eda98d",
     "notes": ["White Pepper", "Black Pepper", "Jalapeno"]},
    {"name": "Sweet", "color": "#e2bd6a", "light": "#f2e0b4",
     "notes": ["Vanilla", "Caramel", "Honey", "Butterscotch"]},
    {"name": "Oak", "color": "#a98a53", "light": "#d3bd8e",
     "notes": ["Toasted Oak", "Coconut", "Cinnamon"]},
    {"name": "Earth", "color": "#8a6a4f", "light": "#c2a889",
     "notes": ["Wet Stone", "Clay", "Mineral"]},
]

mezcal_categories = [
    {"name": "Smoke", "color": "#6b6259", "light": "#a8a099",
     "notes": ["Campfire", "Mesquite", "Charcoal", "Ash"]},
    {"name": "Earth", "color": "#9c6b4f", "light": "#cba894",
     "notes": ["Wet Clay", "Wet Stone", "Leather"]},
    {"name": "Green", "color": "#7d9457", "light": "#b8c894",
     "notes": ["Green Agave", "Herbs", "Grass", "Eucalyptus"]},
    {"name": "Fruit", "color": "#b98aa3", "light": "#dcbecc",
     "notes": ["Green Apple", "Tropical", "Banana"]},
    {"name": "Floral", "color": "#c39bb8", "light": "#e2cbdc",
     "notes": ["Rose", "Jasmine", "Honeysuckle"]},
    {"name": "Mineral", "color": "#7e93a1", "light": "#b6c5ce",
     "notes": ["Salt", "Flint", "Brine"]},
]

tequila_svg = build_wheel(290, 290, tequila_categories, "TEQUILA")
mezcal_svg = build_wheel(290, 290, mezcal_categories, "MEZCAL")

with open(f"{BASE}/tequila_wheel.svg", "w") as f:
    f.write(f'<svg viewBox="0 0 580 580" xmlns="http://www.w3.org/2000/svg">{tequila_svg}</svg>')

with open(f"{BASE}/mezcal_wheel.svg", "w") as f:
    f.write(f'<svg viewBox="0 0 580 580" xmlns="http://www.w3.org/2000/svg">{mezcal_svg}</svg>')

print("wheels written")
