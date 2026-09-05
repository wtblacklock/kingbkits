import os

BASE = "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad/listing_images"

CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Archivo+Black&display=swap');
  *{box-sizing:border-box; margin:0; padding:0;}
  html,body{width:2000px; height:2000px; overflow:hidden;}
  body{
    background:#eaeae7;
    font-family:'Raleway', sans-serif;
    color:#454545;
    position:relative;
  }
  .kb-badge{
    display:inline-flex; flex-direction:column; align-items:center; justify-content:center;
    background:#000; border-radius:22px; padding:16px 26px 18px;
    font-family:'Archivo Black', sans-serif; line-height:0.92; text-align:center; width:fit-content;
  }
  .kb-badge .l1{font-size:34px; color:#f3c318; letter-spacing:-0.01em;}
  .kb-badge .l2{font-size:24px; color:#fff; letter-spacing:0.02em; margin-top:2px;}
  .tier-pill{display:inline-flex; align-items:center; gap:10px; font-weight:700; font-size:26px; padding:10px 24px; border-radius:999px; color:#000;}
  .tier-pill.newbie{background:#87cb28;}
  .tier-pill.casual{background:#ffff00;}
  .tier-pill.aficionado{background:#ffd230;}
  .ico{display:inline-block; vertical-align:middle;}
</style>
<svg style="display:none">
  <symbol id="ico-cigar" viewBox="0 0 48 28">
    <rect x="4" y="9" width="34" height="12" rx="6" fill="#a9764a"/>
    <rect x="4" y="15" width="34" height="6" rx="3" fill="#000" opacity="0.12"/>
    <rect x="15" y="7.5" width="8" height="15" rx="1.4" fill="#e5b85c"/>
    <rect x="15" y="7.5" width="8" height="3.2" fill="#b6862c"/>
    <ellipse cx="41" cy="15" rx="6.5" ry="6.8" fill="#ff7a3d"/>
    <ellipse cx="41.8" cy="15" rx="3.2" ry="3.4" fill="#ffcf94"/>
  </symbol>
  <symbol id="ico-glass" viewBox="0 0 28 28">
    <path d="M7 6 H21 L18.5 20 Q18 23 14 23 Q10 23 9.5 20 Z" fill="none" stroke="#8a7663" stroke-width="1.6"/>
    <path d="M8.3 12.5 H19.7 L18.5 20 Q18 23 14 23 Q10 23 9.5 20 Z" fill="#c98a2c"/>
    <path d="M8.3 12.5 H19.7 L19.3 15 H8.7 Z" fill="#e0ab4e"/>
  </symbol>
</svg>
"""

def write(name, body):
    with open(os.path.join(BASE, name), "w") as f:
        f.write(f"<!doctype html><html><head><meta charset='utf-8'>{CSS}</head><body>{body}</body></html>")

# ---------- SLIDE 1: COVER ----------
write("1-cover.html", """
<div style="position:absolute; inset:0; padding:160px 140px; display:flex; flex-direction:column; justify-content:space-between;">
  <div style="display:flex; justify-content:space-between; align-items:flex-start;">
    <div style="font-family:'Raleway'; font-style:italic; font-size:32px; color:#454545;">The Cigar &amp; Whisky Journey</div>
    <div class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  </div>
  <div>
    <div style="font-weight:300; font-size:150px; line-height:0.98; color:#000; letter-spacing:-0.02em;">Cigar &amp;<br>Whisky</div>
    <div style="font-weight:800; font-size:80px; color:#000; margin-top:18px;">Pairing Party Kit</div>
    <div style="font-size:36px; color:#454545; margin-top:28px; max-width:1300px;">Printable event planning kit &mdash; guide, primer, pairing chart &amp; tier cards</div>
    <div style="display:flex; gap:20px; margin-top:56px;">
      <span class="tier-pill newbie">Newbie</span>
      <span class="tier-pill casual">Casual</span>
      <span class="tier-pill aficionado">Aficionado</span>
    </div>
  </div>
  <div style="border-top:2px solid #000; padding-top:36px; display:flex; justify-content:space-between; align-items:center;">
    <div style="font-size:30px; color:#454545;">Instant Digital Download</div>
    <div style="font-size:30px; color:#454545;">7 PDF Pages &middot; Print at Home</div>
  </div>
</div>
""")

# ---------- SLIDE 2: WHAT'S INCLUDED ----------
items = [
    ("ico-glass", "01 &middot; Party Guide", "Setup, timing, supplies &mdash; realistic for one cigar per guest, not three."),
    ("ico-cigar", "02 &middot; Cigar &amp; Whisky Primer", "Wrapper types, whisky styles, and the leaf-to-ash process."),
    ("ico-glass", "03 &middot; Pairbase Chart", "17 curated pairings across all three tiers, with real cost math."),
    ("ico-cigar", "04 &middot; Flavor Wheels", "Dual cigar &amp; whisky wheels to build real tasting vocabulary."),
    ("ico-cigar", "05 &middot; Newbie Pairing Card", "Full-page tracking card for the mildest tier."),
    ("ico-cigar", "06 &middot; Casual Pairing Card", "Full-page tracking card for the middle tier."),
    ("ico-cigar", "07 &middot; Aficionado Pairing Card", "Full-page tracking card for the boldest tier."),
]
rows = ""
for i, (icon, title, desc) in enumerate(items):
    rows += f"""
    <div style="display:flex; gap:34px; align-items:flex-start; padding:34px 0; border-bottom:1px solid #d8d8d5;">
      <svg class="ico" viewBox="0 0 48 28" style="width:64px; height:38px; flex:none; margin-top:6px;"><use href="#{icon}"/></svg>
      <div>
        <div style="font-weight:700; font-size:38px; color:#000;">{title}</div>
        <div style="font-size:30px; color:#454545; margin-top:8px;">{desc}</div>
      </div>
    </div>"""
write("2-included.html", f"""
<div style="position:absolute; inset:0; padding:140px; display:flex; flex-direction:column; justify-content:center;">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:80px;">
    <div style="font-weight:300; font-size:100px; color:#000;">What's Included</div>
    <div class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  </div>
  {rows}
</div>
""")

# ---------- SLIDES 3-6: PAGE PREVIEWS ----------
def preview(name, label, sub, img, rot=0):
    write(name, f"""
    <div style="position:absolute; inset:0; padding:130px; display:flex; flex-direction:column;">
      <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:50px;">
        <div>
          <div style="font-size:28px; letter-spacing:0.08em; text-transform:uppercase; color:#8a7663; font-weight:700;">{label}</div>
          <div style="font-weight:300; font-size:76px; color:#000; margin-top:6px;">{sub}</div>
        </div>
        <div class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
      </div>
      <div style="flex:1; display:flex; align-items:center; justify-content:center;">
        <img src="{img}" style="max-width:1420px; max-height:1420px; box-shadow:0 40px 90px -30px rgba(0,0,0,0.35); border:1px solid #d8d8d5; transform:rotate({rot}deg);">
      </div>
    </div>
    """)

preview("3-guide.html", "Piece 01", "Party Guide", "page-1.png")
preview("4-primer.html", "Piece 02", "Cigar &amp; Whisky Primer", "page-2.png")
preview("5-pairbase.html", "Piece 03", "Pairbase Chart", "page-3.png")
preview("6-wheels.html", "Piece 04", "Flavor Wheels", "page-4.png")

# Slide 7: 3 cards fanned
write("7-cards.html", """
<div style="position:absolute; inset:0; padding:130px; display:flex; flex-direction:column;">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:40px;">
    <div>
      <div style="font-size:28px; letter-spacing:0.08em; text-transform:uppercase; color:#8a7663; font-weight:700;">Piece 05&ndash;07</div>
      <div style="font-weight:300; font-size:76px; color:#000; margin-top:6px;">Pairing Cards, All 3 Tiers</div>
    </div>
    <div class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  </div>
  <div style="flex:1; position:relative;">
    <img src="page-5.png" style="position:absolute; left:60px; top:60px; width:640px; box-shadow:0 30px 70px -20px rgba(0,0,0,0.35); border:1px solid #d8d8d5; transform:rotate(-6deg);">
    <img src="page-6.png" style="position:absolute; left:660px; top:0px; width:680px; box-shadow:0 30px 70px -20px rgba(0,0,0,0.4); border:1px solid #d8d8d5; z-index:2;">
    <img src="page-7.png" style="position:absolute; right:40px; top:80px; width:640px; box-shadow:0 30px 70px -20px rgba(0,0,0,0.35); border:1px solid #d8d8d5; transform:rotate(6deg);">
  </div>
</div>
""")

# ---------- SLIDE 8: WHY THIS KIT ----------
write("8-why.html", """
<div style="position:absolute; inset:0; padding:150px; display:flex; flex-direction:column; justify-content:space-between;">
  <div class="kb-badge" style="align-self:flex-end;"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  <div>
    <div style="font-weight:300; font-size:100px; color:#000; line-height:1.05;">One Cigar.<br>Three Whiskies.<br>Zero Guesswork.</div>
    <div style="font-size:38px; color:#454545; margin-top:44px; max-width:1400px; line-height:1.5;">
      Most kits have you smoking three full cigars in one night. This one doesn't &mdash;
      pick one cigar for the evening and taste three whisky pours against it as the flavor
      shifts through its three thirds. Realistic, affordable, and exactly how aficionados
      actually do it.
    </div>
  </div>
  <div style="display:flex; gap:60px; border-top:2px solid #000; padding-top:40px;">
    <div><div style="font-weight:700; font-size:40px; color:#000;">17</div><div style="font-size:26px; color:#454545;">curated pairings</div></div>
    <div><div style="font-weight:700; font-size:40px; color:#000;">3</div><div style="font-size:26px; color:#454545;">experience tiers</div></div>
    <div><div style="font-weight:700; font-size:40px; color:#000;">1</div><div style="font-size:26px; color:#454545;">bottle per tier, easily covers 6 guests</div></div>
  </div>
</div>
""")

# ---------- SLIDE 9: HOW IT WORKS ----------
steps = [
    ("Purchase &amp; Download", "Instant access to the full PDF, plus your editable Canva invitation template."),
    ("Print at Home or a Shop", "Staples, FedEx, or a service like Printify &mdash; or just use your own printer."),
    ("Pick Your Tier", "Newbie, Casual, or Aficionado &mdash; the Pairbase chart tells you what to buy."),
    ("Host Tonight", "Everything's ready. No physical items ship &mdash; this is an all-digital product."),
]
steps_html = ""
for i, (t, d) in enumerate(steps, 1):
    steps_html += f"""
    <div style="display:flex; gap:34px; align-items:flex-start; padding:32px 0; border-bottom:1px solid #d8d8d5;">
      <div style="font-family:'Archivo Black'; font-size:56px; color:#d9ab53; flex:none; width:90px;">{i:02d}</div>
      <div>
        <div style="font-weight:700; font-size:38px; color:#000;">{t}</div>
        <div style="font-size:30px; color:#454545; margin-top:8px;">{d}</div>
      </div>
    </div>"""
write("9-howto.html", f"""
<div style="position:absolute; inset:0; padding:140px;">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:60px;">
    <div style="font-weight:300; font-size:92px; color:#000;">Instant Download,<br>How It Works</div>
    <div class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  </div>
  {steps_html}
  <div style="margin-top:50px; font-size:28px; color:#8a7663;">&#8252;&#65039; This is an ALL DIGITAL product. No physical items will be shipped.</div>
</div>
""")

print("done")
