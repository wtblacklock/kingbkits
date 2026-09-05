import math

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
    # center circle
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r0}" fill="#17130f"/>')
    out.append(f'<text x="{cx}" y="{cy}" font-size="18" font-weight="700" fill="#f3c318" '
                f'text-anchor="middle" dominant-baseline="central" font-family=\'Raleway, sans-serif\'>{center_label}</text>')
    for i, cat in enumerate(categories):
        a1 = i * seg
        a2 = (i + 1) * seg
        mid = (a1 + a2) / 2
        # inner ring wedge
        out.append(f'<path d="{wedge_path(cx, cy, r0, r1, a1, a2)}" fill="{cat["color"]}" stroke="#fdf9ef" stroke-width="2"/>')
        out.append(radial_text(cx, cy, r0 + (r1 - r0) * 0.32, mid, cat["name"], 17, "700", "#241b10"))
        # outer ring: subdivide by notes
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
    # outer boundary
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r2}" fill="none" stroke="#d8d8d5" stroke-width="1.5"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r1}" fill="none" stroke="#fdf9ef" stroke-width="1.5"/>')
    return "\n".join(out)

cigar_categories = [
    {"name": "Sweet", "color": "#eecb5f", "light": "#f6e4a8",
     "notes": ["Honey", "Caramel", "Vanilla", "Molasses"]},
    {"name": "Spicy", "color": "#e0793c", "light": "#f0b98d",
     "notes": ["Black Pepper", "Cinnamon", "Clove", "Nutmeg"]},
    {"name": "Earthy", "color": "#8a6a4f", "light": "#c2a889",
     "notes": ["Leather", "Barnyard", "Char", "Damp Soil"]},
    {"name": "Woody", "color": "#a98a53", "light": "#d3bd8e",
     "notes": ["Cedar", "Oak", "Toasted"]},
    {"name": "Nutty", "color": "#d9c08a", "light": "#ecdfc0",
     "notes": ["Almond", "Walnut", "Roasted"]},
    {"name": "Fruity", "color": "#b98aa3", "light": "#dcbecc",
     "notes": ["Raisin", "Fig", "Dried Cherry"]},
]

whisky_categories = [
    {"name": "Sweet", "color": "#eecb5f", "light": "#f6e4a8",
     "notes": ["Vanilla", "Caramel", "Honey", "Maple"]},
    {"name": "Spicy", "color": "#e0793c", "light": "#f0b98d",
     "notes": ["Pepper", "Cinnamon", "Clove"]},
    {"name": "Smoky", "color": "#6b5a45", "light": "#a5907a",
     "notes": ["Peat", "Smoke", "Tar", "Iodine"]},
    {"name": "Woody", "color": "#a98a53", "light": "#d3bd8e",
     "notes": ["Oak", "Cedar", "Sawdust"]},
    {"name": "Grainy", "color": "#d9c08a", "light": "#ecdfc0",
     "notes": ["Malt", "Cereal", "Bread"]},
    {"name": "Fruity", "color": "#b98aa3", "light": "#dcbecc",
     "notes": ["Apple", "Citrus", "Berry", "Dried Fruit"]},
]

cigar_svg = build_wheel(290, 290, cigar_categories, "PUFF")
whisky_svg = build_wheel(290, 290, whisky_categories, "SIP")

with open("/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad/cigar_wheel.svg", "w") as f:
    f.write(f'<svg viewBox="0 0 580 580" xmlns="http://www.w3.org/2000/svg">{cigar_svg}</svg>')

with open("/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad/whisky_wheel.svg", "w") as f:
    f.write(f'<svg viewBox="0 0 580 580" xmlns="http://www.w3.org/2000/svg">{whisky_svg}</svg>')

print("CIGAR_SVG_INNER:")
print(cigar_svg)
print("\n\nWHISKY_SVG_INNER:")
print(whisky_svg)
