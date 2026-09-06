import os, re, glob, sys, math
from PIL import Image, ImageDraw

REPO = "/Users/BIGWilly/Projects/kingbkits"


def _scene_num(path):
    m = re.match(r"^(\d+)-", os.path.basename(path))
    return int(m.group(1)) if m else 999


def tiki_buddy_overlay(frame, phase):
    """A small bobbing tiki mug with a straw, umbrella, and rising bubbles,
    drawn straight onto the frame with PIL so it can animate continuously
    through the whole clip regardless of which background scene is showing -
    the 'have fun with it' layer on top of the scene-to-scene tour."""
    frame = frame.copy()
    draw = ImageDraw.Draw(frame, "RGBA")
    w, h = frame.size
    cx, cy = int(w * 0.14), int(h * 0.86)
    bob = math.sin(phase * math.pi * 2 * 3) * 10
    tilt = math.sin(phase * math.pi * 2 * 3 + 0.6) * 4
    cy += bob

    mug_w, mug_h = 74, 92
    top = cy - mug_h / 2
    bottom = cy + mug_h / 2
    # mug body (tapered)
    draw.polygon([
        (cx - mug_w * 0.42 + tilt, top), (cx + mug_w * 0.42 + tilt, top),
        (cx + mug_w * 0.5, bottom), (cx - mug_w * 0.5, bottom),
    ], fill=(120, 84, 52, 235))
    # carved face
    eye_y = top + mug_h * 0.32
    draw.ellipse([cx - 18 + tilt, eye_y, cx - 8 + tilt, eye_y + 13], fill=(30, 20, 12, 255))
    draw.ellipse([cx + 8 + tilt, eye_y, cx + 18 + tilt, eye_y + 13], fill=(30, 20, 12, 255))
    draw.arc([cx - 16 + tilt, eye_y + 16, cx + 16 + tilt, eye_y + 34], 20, 160,
              fill=(30, 20, 12, 255), width=3)
    # straw
    draw.line([(cx + 16 + tilt, top - 2), (cx + 26 + tilt, top - 34)], fill=(255, 90, 130, 255), width=6)
    # umbrella
    ux, uy = cx - 4 + tilt, top - 44
    draw.line([(ux, uy), (ux, top - 6)], fill=(230, 230, 230, 255), width=3)
    draw.pieslice([ux - 26, uy - 26, ux + 26, uy + 10], 180, 360, fill=(255, 210, 60, 235))

    # rising bubbles - three, staggered, looping
    for i in range(3):
        bt = (phase * 2.2 + i * 0.33) % 1.0
        bx = cx + math.sin(bt * math.pi * 2 + i) * 20
        by = top - 10 - bt * 130
        r = 5 + bt * 4
        op = int(200 * math.sin(bt * math.pi))
        draw.ellipse([bx - r, by - r, bx + r, by + r], outline=(255, 255, 255, op), width=2)
    return frame


def build_slideshow(kit_name, listing_dir, out_dir, size=1100, hold_ms=850,
                     trans_ms=360, trans_steps=6, overlay_fn=None):
    """Crossfade through a kit's existing listing images (hero, guide, primer,
    pairbase, wheels, cards, bundle) - each already has its own distinct
    background from the listing-image build, so this is a proper multi-scene
    product tour, not one static hero repeated. Pure PIL compositing, no
    re-rendering, so it's fast even though the result runs much longer.
    overlay_fn(frame, phase) -> frame, if given, is applied to every output
    frame with phase running 0..1 continuously across the WHOLE clip (holds
    and transitions alike), for a fun animated character independent of
    which scene is currently showing."""
    pngs = sorted(glob.glob(os.path.join(listing_dir, "[0-9]-*.png")), key=_scene_num)
    pngs = [p for p in pngs if _scene_num(p) <= 7]
    if not pngs:
        raise SystemExit(f"no numbered scene pngs found in {listing_dir}")

    imgs = [Image.open(p).convert("RGB").resize((size, size), Image.LANCZOS) for p in pngs]

    frames, durations = [], []
    for idx, img in enumerate(imgs):
        frames.append(img)
        durations.append(hold_ms)
        if idx < len(imgs) - 1:
            nxt = imgs[idx + 1]
            for step in range(1, trans_steps + 1):
                alpha = step / (trans_steps + 1)
                frames.append(Image.blend(img, nxt, alpha))
                durations.append(max(30, trans_ms // trans_steps))

    if overlay_fn:
        n = len(frames)
        frames = [overlay_fn(f, i / (n - 1)) for i, f in enumerate(frames)]

    out_path = os.path.join(out_dir, f"{kit_name}-hero.gif")
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=durations,
                   loop=0, optimize=True)
    total_s = sum(durations) / 1000
    print(f"wrote {out_path} ({len(frames)} frames, {total_s:.2f}s, {len(pngs)} scenes)")
    return out_path


if __name__ == "__main__":
    kits = [
        ("cigar", f"{REPO}/listing_marketing/listing_clean_cigar"),
        ("agave", f"{REPO}/listing_marketing/listing_clean_agave"),
        ("halloween", f"{REPO}/listing_marketing/listing_clean_halloween"),
        ("advent", f"{REPO}/listing_marketing/listing_clean_advent"),
        ("rum", f"{REPO}/listing_marketing/listing_clean_rum"),
    ]
    for name, listing_dir in kits:
        build_slideshow(name, listing_dir, f"{REPO}/source")
