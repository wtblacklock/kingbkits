import os, re, glob, sys
from PIL import Image

REPO = "/Users/BIGWilly/Projects/kingbkits"


def _scene_num(path):
    m = re.match(r"^(\d+)-", os.path.basename(path))
    return int(m.group(1)) if m else 999


def build_slideshow(kit_name, listing_dir, out_dir, size=1100, hold_ms=850,
                     trans_ms=360, trans_steps=6):
    """Crossfade through a kit's existing listing images (hero, guide, primer,
    pairbase, wheels, cards, bundle) - each already has its own distinct
    background from the listing-image build, so this is a proper multi-scene
    product tour, not one static hero repeated. Pure PIL compositing, no
    re-rendering, so it's fast even though the result runs much longer."""
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
    ]
    for name, listing_dir in kits:
        build_slideshow(name, listing_dir, f"{REPO}/source")
