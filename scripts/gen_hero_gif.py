import os, sys, subprocess, shutil
from PIL import Image

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def ease_out_back(t, overshoot=1.4):
    c1 = overshoot
    c3 = c1 + 1
    return 1 + c3 * (t - 1) ** 3 + c1 * (t - 1) ** 2

def ease_out_cubic(t):
    return 1 - (1 - t) ** 3


def build_gif(name, out_dir, bg_html_fn, pages, size=1100, n_frames=16, hold_ms=1400, frame_ms=55):
    """
    pages: list of dicts: {img, x_pct, y_final, ry, rz, w, delay}
      delay in [0,1): fraction of the entrance timeline before this page starts animating
    bg_html_fn: function(pages_html, t_global) -> full <body> inner HTML for this frame.
                t_global is 0..1 across the entrance timeline (held at 1.0 during hold_ms).
                Use it to drive any continuous background animation (smoke, floating
                characters, etc) independent of the page-mockup entrance.
    """
    frames_dir = os.path.join(out_dir, f"_frames_{name}")
    os.makedirs(frames_dir, exist_ok=True)

    frame_paths = []
    for i in range(n_frames):
        t_global = i / (n_frames - 1)
        pages_html = ""
        for p in pages:
            local_t = max(0.0, min(1.0, (t_global - p["delay"]) / (1 - p["delay"])))
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
    out_path = os.path.join(out_dir, f"{name}.gif")
    imgs[0].save(out_path, save_all=True, append_images=imgs[1:], duration=durations,
                 loop=0, optimize=True)
    shutil.rmtree(frames_dir)
    print(f"wrote {out_path} ({os.path.getsize(out_path)/1024:.0f} KB, {n_frames} frames)")
    return out_path
