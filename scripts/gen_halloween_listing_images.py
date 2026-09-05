import os

BASE = "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad/listing_images_halloween"
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
  <symbol id="ico-candy" viewBox="0 0 28 28">
    <rect x="8.5" y="9" width="11" height="10" rx="2.2" fill="#c0563f"/>
    <rect x="8.5" y="9" width="11" height="4.6" rx="2.2" fill="#d97a5e"/>
    <path d="M8.5 11 L3.6 8.2 L4.8 14 L3.6 19.8 L8.5 17 Z" fill="#e0a24e"/>
    <path d="M19.5 11 L24.4 8.2 L23.2 14 L24.4 19.8 L19.5 17 Z" fill="#e0a24e"/>
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
    <div style="font-style:italic; font-size:32px; color:#454545;">The Candy &amp; Whisky Pairing Kit</div>
    <div class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  </div>
  <div>
    <div style="font-weight:300; font-size:150px; line-height:0.98; color:#000; letter-spacing:-0.02em;">Candy &amp;<br>Whisky</div>
    <div style="font-weight:800; font-size:80px; color:#000; margin-top:18px;">Halloween Pairing Kit</div>
    <div style="font-size:36px; color:#454545; margin-top:28px; max-width:1300px;">The cheapest tasting night you'll ever host &mdash; a $12 bag of candy and a bottle you already own</div>
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
    ("ico-candy", "01 &middot; Party Guide", "What to buy, how to set up, and how to actually taste a pairing."),
    ("ico-candy", "02 &middot; Candy Primer", "The real chemistry behind why chocolate and caramel pair so well with whisky."),
    ("ico-glass", "03 &middot; Pairbase Chart", "9 candies matched to real bottles, with the science for each pairing."),
    ("ico-glass", "04 &middot; Flavor Wheels", "Candy and whisky wheels side by side &mdash; find where they overlap."),
    ("ico-candy", "05 &middot; Newbie Card", "The Sweet Match &mdash; three candies that agree with one bourbon."),
    ("ico-candy", "06 &middot; Casual Card", "The Contrast &mdash; pairings that work by fighting instead of agreeing."),
    ("ico-candy", "07 &middot; Aficionado Card", "The Gauntlet &mdash; sour candy, licorice, and candy corn. Good luck."),
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

preview("3-guide.html",    "Piece 01", "Party Guide",   "page-1.png")
preview("4-primer.html",   "Piece 02", "Candy Primer",  "page-2.png")
preview("5-pairbase.html", "Piece 03", "Pairbase Chart","page-3.png")
preview("6-wheels.html",   "Piece 04", "Flavor Wheels", "page-4.png")

# ---------- SLIDE 7: CARDS FANNED ----------
write("7-cards.html", """
<div style="position:absolute; inset:0; padding:130px; display:flex; flex-direction:column;">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:40px;">
    <div>
      <div style="font-size:28px; letter-spacing:0.08em; text-transform:uppercase; color:#8a7663; font-weight:700;">Piece 05&ndash;07</div>
      <div style="font-weight:300; font-size:76px; color:#000; margin-top:6px;">Complement, Contrast, Collision</div>
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

# ---------- SLIDE 8: WHY THIS KIT ----------
write("8-why.html", """
<div style="position:absolute; inset:0; padding:150px; display:flex; flex-direction:column; justify-content:space-between;">
  <div class="kb-badge" style="align-self:flex-end;"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  <div>
    <div style="font-weight:300; font-size:110px; color:#000; line-height:1.05;">Your Leftover<br>Candy Deserves<br>Better.</div>
    <div style="font-size:38px; color:#454545; margin-top:44px; max-width:1400px; line-height:1.5;">
      Coconut in an Almond Joy shares the same compound class as American oak. Caramelized
      sugar and barrel char are the same chemical reaction. This isn't a party trick &mdash;
      candy and whisky actually agree, and this kit shows you exactly where.
    </div>
  </div>
  <div style="display:flex; gap:60px; border-top:2px solid #000; padding-top:40px;">
    <div><div style="font-weight:700; font-size:40px; color:#000;">9</div><div style="font-size:26px; color:#454545;">candy &amp; whisky pairings</div></div>
    <div><div style="font-weight:700; font-size:40px; color:#000;">$12</div><div style="font-size:26px; color:#454545;">covers a table of six</div></div>
    <div><div style="font-weight:700; font-size:40px; color:#000;">2</div><div style="font-size:26px; color:#454545;">selling windows &mdash; Oct &amp; Nov 1-7</div></div>
  </div>
</div>
""")

# ---------- SLIDE 9: HOW IT WORKS ----------
steps = [
    ("Purchase &amp; Download", "Instant access to the full PDF, plus your editable Canva invitation template."),
    ("Print at Home or a Shop", "Standard US Letter, no bleed or special stock needed."),
    ("Buy One Bag of Candy", "The Pairbase names exactly which fun-size bars to grab."),
    ("Half-Ounce Pours", "Sip, bite, sip again. Vote on a winner at the end."),
]
steps_html = ""
for i, (t, d) in enumerate(steps, 1):
    steps_html += f"""
    <div style="display:flex; gap:34px; align-items:flex-start; padding:32px 0; border-bottom:1px solid #d8d8d5;">
      <div style="font-family:'Archivo Black'; font-size:56px; color:#c0563f; flex:none; width:90px;">{i:02d}</div>
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
  <div style="margin-top:50px; font-size:28px; color:#8a7663;">&#8252;&#65039; This is an ALL DIGITAL product. No physical items will be shipped. No candy or bottles are included.</div>
</div>
""")

print("html written")
