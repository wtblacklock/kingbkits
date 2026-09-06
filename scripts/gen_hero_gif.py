import os, sys, subprocess, shutil
from PIL import Image

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def ease_out_back(t, overshoot=1.4):
    c1 = overshoot
    c3 = c1 + 1
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2

def ease_out_cubic(t):
    return 1 - (1 - t) ** 3


def build_gif(name, out_dir, bg_html_fn, pages, size=1100, n_frames=40, entrance_frac=0.4,
              frame_ms=90, hold_ms=300):
    """
    pages: list of dicts: {img, x_pct, y_final, ry, rz, w, delay}
      delay in [0,1): fraction of the ENTRANCE window (see entrance_frac) before this
      page starts animating - unaffected by total clip length.
    bg_html_fn: function(pages_html, t_global) -> full <body> inner HTML for this frame.
                t_global runs 0..1 across the WHOLE clip, uninterrupted - there's no
                separate frozen "hold" phase. Use it to drive continuous, looping
                background animation (smoke, floating characters, sparkles, etc) so the
                clip stays alive for its full length instead of settling into a static
                frame after the page-mockup entrance finishes. Motif helpers should treat
                t as a repeating cycle (e.g. `(t * cycles) % 1.0`), not a one-shot ramp.
    entrance_frac: fraction of the total clip during which pages fan in (default 0.4 -
                   e.g. clip is n_frames*frame_ms long, pages finish settling at that
                   fraction of the way through, then hold position for the remainder
                   while the background keeps animating).
    """
    frames_dir = os.path.join(out_dir, f"_frames_{name}")
    os.makedirs(frames_dir, exist_ok=True)

    frame_paths = []
    for i in range(n_frames):
        t_global = i / (n_frames - 1)
        entrance_t = min(t_global / entrance_frac, 1.0)
        pages_html = ""
        for p in pages:
            local_t = max(0.0, min(1.0, (entrance_t - p["delay"]) / (1 - p["delay"])))
            eased = ease_out_back(local_t) if local_t > 0 else 0
            y_off = (1 - eased) * 260  # slides up from +260px
            opacity = min(1.0, ease_out_cubic(local_t) * 1.15) if local_t > 0 else 0
            y = p["y_final"] + y_off
            pages_html += f"""
<div style="position:absolute;left:{p['x_pct']};top:{y}px;opacity:{opacity:.3f};
     transform:translateX(-50%) perspective(3200px) rotateX(9deg) rotateY({p['ry']}deg) rotate({p['rz']}deg);
     transform-origin:50% 0%;">
  <img src="{p['img']}" style="width:{p['w']}px;display:block;box-shadow:{p['shadow']};filter:{p.get('filter','none')};">
</div>"""
        html = bg_html_fn(pages_html, t_global)
        fpath = os.path.join(frames_dir, f"f{i:03d}.html")
        with open(fpath, "w") as f:
            f.write(html)
        ppath = os.path.join(frames_dir, f"f{i:03d}.png")
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--virtual-time-budget=6000",
                         f"--window-size={size},{size}", f"--screenshot={ppath}",
                         f"file://{fpath}"], capture_output=True)
        frame_paths.append(ppath)

    imgs = [Image.open(p).convert("RGB") for p in frame_paths]
    durations = [frame_ms] * n_frames
    durations[-1] = hold_ms
    total_s = (sum(durations)) / 1000
    out_path = os.path.join(out_dir, f"{name}.gif")
    imgs[0].save(out_path, save_all=True, append_images=imgs[1:], duration=durations,
                 loop=0, optimize=True)
    shutil.rmtree(frames_dir)
    print(f"wrote {out_path} ({os.path.getsize(out_path)/1024:.0f} KB, {n_frames} frames, {total_s:.2f}s)")
    return out_path
