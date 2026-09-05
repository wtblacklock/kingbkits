import os

BASE = "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad/listing_images_agave"
os.makedirs(BASE, exist_ok=True)

CSS = """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=Archivo+Black&display=swap');
  *{box-sizing:border-box; margin:0; padding:0;}
  html,body{width:2000px; height:2000px; overflow:hidden;}
  body{background:#eaeae7; font-family:'Raleway', sans-serif; color:#454545; position:relative;}
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
  <symbol id="ico-agave" viewBox="0 0 28 28">
    <ellipse cx="14" cy="13" rx="2.7" ry="10.5" fill="#6f8a4c" transform="rotate(-42 14 23)"/>
    <ellipse cx="14" cy="13" rx="2.7" ry="10.5" fill="#6f8a4c" transform="rotate(42 14 23)"/>
    <ellipse cx="14" cy="12.5" rx="2.7" ry="11" fill="#87a35f" transform="rotate(-21 14 23)"/>
    <ellipse cx="14" cy="12.5" rx="2.7" ry="11" fill="#87a35f" transform="rotate(21 14 23)"/>
    <ellipse cx="14" cy="12" rx="2.8" ry="11.5" fill="#9db977"/>
  </symbol>
  <symbol id="ico-copita" viewBox="0 0 28 28">
    <path d="M8.4 6 H19.6 L18.3 14.6 Q17.8 18.2 14 18.2 Q10.2 18.2 9.7 14.6 Z"
          fill="none" stroke="#8a7663" stroke-width="1.6"/>
    <path d="M9.5 12 H18.5 L18.3 14.6 Q17.8 18.2 14 18.2 Q10.2 18.2 9.7 14.6 Z" fill="#e6dcae"/>
    <rect x="13.2" y="18.2" width="1.6" height="4" fill="#8a7663"/>
    <rect x="9.8" y="22.2" width="8.4" height="1.7" rx="0.85" fill="#8a7663"/>
  </symbol>
</svg>
"""

def write(name, body):
    with open(os.path.join(BASE, name), "w") as f:
        f.write(f"<!doctype html><html><head><meta charset='utf-8'>{CSS}</head><body>{body}</body></html>")

# ---------- 1: COVER ----------
write("1-cover.html", """
<div style="position:absolute; inset:0; padding:160px 140px; display:flex; flex-direction:column; justify-content:space-between;">
  <div style="display:flex; justify-content:space-between; align-items:flex-start;">
    <div style="font-style:italic; font-size:32px; color:#454545;">The Agave Tasting Journey</div>
    <div class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  </div>
  <div>
    <div style="font-weight:300; font-size:150px; line-height:0.98; color:#000; letter-spacing:-0.02em;">Tequila &amp;<br>Mezcal</div>
    <div style="font-weight:800; font-size:80px; color:#000; margin-top:18px;">Tasting Party Kit</div>
    <div style="font-size:36px; color:#454545; margin-top:28px; max-width:1300px;">Printable tasting kit &mdash; guide, primer, bottle chart, flavor wheels &amp; tier cards</div>
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

# ---------- 2: WHAT'S INCLUDED ----------
items = [
    ("ico-agave",  "01 &middot; Party Guide", "Setup, timing, supplies &mdash; and why the lime and salt stay in the kitchen."),
    ("ico-copita", "02 &middot; Tequila &amp; Mezcal Primer", "Blue Weber vs wild agave, the age ladder, and how to read a label."),
    ("ico-agave",  "03 &middot; Agavebase Chart", "Real bottles at three budgets, with per-person cost math."),
    ("ico-copita", "04 &middot; Flavor Wheels", "Separate tequila and mezcal wheels to build tasting vocabulary."),
    ("ico-agave",  "05 &middot; Newbie Tasting Card", "The Age Ladder flight &mdash; blanco, reposado, a&ntilde;ejo."),
    ("ico-agave",  "06 &middot; Casual Tasting Card", "Tequila Meets Mezcal &mdash; the smoke reveal flight."),
    ("ico-agave",  "07 &middot; Aficionado Tasting Card", "Agave Terroir &mdash; three wild species, one producer."),
]
rows = ""
for icon, title, desc in items:
    rows += f"""
    <div style="display:flex; gap:34px; align-items:flex-start; padding:34px 0; border-bottom:1px solid #d8d8d5;">
      <svg class="ico" viewBox="0 0 28 28" style="width:52px; height:52px; flex:none; margin-top:2px;"><use href="#{icon}"/></svg>
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

# ---------- 3-6: PAGE PREVIEWS ----------
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

preview("3-guide.html",     "Piece 01", "Party Guide",              "page-1.png")
preview("4-primer.html",    "Piece 02", "Tequila &amp; Mezcal Primer", "page-2.png")
preview("5-agavebase.html", "Piece 03", "Agavebase Chart",          "page-3.png")
preview("6-wheels.html",    "Piece 04", "Flavor Wheels",            "page-4.png")

# ---------- 7: CARDS FANNED ----------
write("7-cards.html", """
<div style="position:absolute; inset:0; padding:130px; display:flex; flex-direction:column;">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:40px;">
    <div>
      <div style="font-size:28px; letter-spacing:0.08em; text-transform:uppercase; color:#8a7663; font-weight:700;">Piece 05&ndash;07</div>
      <div style="font-weight:300; font-size:76px; color:#000; margin-top:6px;">A Flight Card for Every Tier</div>
    </div>
    <div class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  </div>
  <div style="flex:1; position:relative;">
    <img src="page-5.png" style="position:absolute; left:130px; top:70px; width:590px; box-shadow:0 30px 70px -20px rgba(0,0,0,0.35); border:1px solid #d8d8d5; transform:rotate(-5deg);">
    <img src="page-6.png" style="position:absolute; left:575px; top:10px; width:620px; box-shadow:0 30px 70px -20px rgba(0,0,0,0.4); border:1px solid #d8d8d5; z-index:2;">
    <img src="page-7.png" style="position:absolute; left:1030px; top:70px; width:590px; box-shadow:0 30px 70px -20px rgba(0,0,0,0.35); border:1px solid #d8d8d5; transform:rotate(5deg);">
  </div>
</div>
""")

# ---------- 8: WHY THIS KIT ----------
write("8-why.html", """
<div style="position:absolute; inset:0; padding:150px; display:flex; flex-direction:column; justify-content:space-between;">
  <div class="kb-badge" style="align-self:flex-end;"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  <div>
    <div style="font-weight:300; font-size:110px; color:#000; line-height:1.05;">Sip It.<br>Don't Shoot It.</div>
    <div style="font-size:38px; color:#454545; margin-top:44px; max-width:1400px; line-height:1.5;">
      The lime and salt ritual exists to hide cheap mixto tequila. Good agave doesn't need
      hiding. This kit walks your table through three one-ounce pours, teaches the one
      label rule that filters out most bad bottles, and gives everyone the words for what
      they're actually tasting.
    </div>
  </div>
  <div style="display:flex; gap:60px; border-top:2px solid #000; padding-top:40px;">
    <div><div style="font-weight:700; font-size:40px; color:#000;">3</div><div style="font-size:26px; color:#454545;">experience tiers</div></div>
    <div><div style="font-weight:700; font-size:40px; color:#000;">3</div><div style="font-size:26px; color:#454545;">bottles covers 6 guests</div></div>
    <div><div style="font-weight:700; font-size:40px; color:#000;">2</div><div style="font-size:26px; color:#454545;">flavor wheels, tequila &amp; mezcal</div></div>
  </div>
</div>
""")

# ---------- 9: HOW IT WORKS ----------
steps = [
    ("Purchase &amp; Download", "Instant access to the 7-page PDF. Nothing ships."),
    ("Print at Home or a Shop", "Standard US Letter, no bleed or special stock needed."),
    ("Pick Your Tier", "Newbie, Casual, or Aficionado &mdash; the Agavebase names the bottles."),
    ("Pour Three Ounces", "One flight, three pours, one evening. Cards track the rest."),
]
steps_html = ""
for i, (t, d) in enumerate(steps, 1):
    steps_html += f"""
    <div style="display:flex; gap:34px; align-items:flex-start; padding:32px 0; border-bottom:1px solid #d8d8d5;">
      <div style="font-family:'Archivo Black'; font-size:56px; color:#87a35f; flex:none; width:90px;">{i:02d}</div>
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

print("html written")
