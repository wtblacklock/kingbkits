import os

BASE = "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad/listing_images_advent"
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
  .ico{display:inline-block; vertical-align:middle;}
</style>
<svg style="display:none">
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
    <div style="font-style:italic; font-size:32px; color:#454545;">The Whisky Advent Companion</div>
    <div class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  </div>
  <div>
    <div style="font-weight:300; font-size:150px; line-height:0.98; color:#000; letter-spacing:-0.02em;">24 Nights<br>of Whisky</div>
    <div style="font-weight:800; font-size:80px; color:#000; margin-top:18px;">Advent Calendar Companion</div>
    <div style="font-size:36px; color:#454545; margin-top:28px; max-width:1300px;">A tasting card for every night, a month tracker, and a flavor wheel &mdash; built for the calendar you already bought</div>
  </div>
  <div style="border-top:2px solid #000; padding-top:36px; display:flex; justify-content:space-between; align-items:center;">
    <div style="font-size:30px; color:#454545;">Instant Digital Download</div>
    <div style="font-size:30px; color:#454545;">9 PDF Pages &middot; Print at Home</div>
  </div>
</div>
""")

# ---------- SLIDE 2: WHAT'S INCLUDED ----------
items = [
    ("01", "How to Use", "Setup, blind-tasting method, and what to do each night."),
    ("02–07", "24 Tasting Cards", "One numbered card per night, 4 per sheet, dashed cut lines."),
    ("08", "Month Tracker", "Every night at a glance, plus your top five of the month."),
    ("09", "Flavor Wheel", "Put a real word to what's in the glass."),
]
rows = ""
for n, title, desc in items:
    rows += f"""
    <div style="display:flex; gap:34px; align-items:flex-start; padding:34px 0; border-bottom:1px solid #d8d8d5;">
      <div style="font-family:'Archivo Black'; font-size:44px; color:#87a35f; flex:none; width:150px;">{n}</div>
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

# ---------- SLIDE 3: GUIDE PREVIEW ----------
def preview(name, label, sub, img, w=1420):
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
        <img src="{img}" style="max-width:{w}px; max-height:1420px; box-shadow:0 40px 90px -30px rgba(0,0,0,0.35); border:1px solid #d8d8d5;">
      </div>
    </div>
    """)

preview("3-guide.html", "Piece 01", "How to Use", "page-1.png")

# ---------- SLIDE 4: CARDS FANNED ----------
write("4-cards.html", """
<div style="position:absolute; inset:0; padding:130px; display:flex; flex-direction:column;">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:40px;">
    <div>
      <div style="font-size:28px; letter-spacing:0.08em; text-transform:uppercase; color:#8a7663; font-weight:700;">Piece 02&ndash;07</div>
      <div style="font-weight:300; font-size:76px; color:#000; margin-top:6px;">A Card for Every Night</div>
    </div>
    <div class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  </div>
  <div style="flex:1; display:flex; align-items:center; justify-content:center;">
    <img src="page-2.png" style="max-width:1350px; max-height:1420px; box-shadow:0 40px 90px -30px rgba(0,0,0,0.35); border:1px solid #d8d8d5;">
  </div>
</div>
""")

# ---------- SLIDE 5: BLIND TASTING CALLOUT ----------
write("5-blind.html", """
<div style="position:absolute; inset:0; padding:150px; display:flex; flex-direction:column; justify-content:space-between;">
  <div class="kb-badge" style="align-self:flex-end;"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  <div>
    <div style="font-weight:300; font-size:110px; color:#000; line-height:1.05;">Guess First.<br>Reveal Second.</div>
    <div style="font-size:38px; color:#454545; margin-top:44px; max-width:1400px; line-height:1.5;">
      Real whisky advent calendars keep the dram a mystery until you open the door. So every
      card starts with a blind guess &mdash; region and age &mdash; before you ever see the
      label. Then the reveal. That's the part a blank notebook can't do.
    </div>
  </div>
  <div style="display:flex; gap:60px; border-top:2px solid #000; padding-top:40px;">
    <div><div style="font-weight:700; font-size:40px; color:#000;">24</div><div style="font-size:26px; color:#454545;">numbered nights</div></div>
    <div><div style="font-weight:700; font-size:40px; color:#000;">30ml</div><div style="font-size:26px; color:#454545;">standard dram format</div></div>
    <div><div style="font-weight:700; font-size:40px; color:#000;">1</div><div style="font-size:26px; color:#454545;">tracker for the whole month</div></div>
  </div>
</div>
""")

# ---------- SLIDE 6: TRACKER PREVIEW ----------
preview("6-tracker.html", "Piece 08", "Month Tracker", "page-8.png")

# ---------- SLIDE 7: WHEEL PREVIEW ----------
preview("7-wheel.html", "Piece 09", "Flavor Wheel", "page-9.png", w=1100)

# ---------- SLIDE 8: COMPATIBLE CALENDARS ----------
write("8-compat.html", """
<div style="position:absolute; inset:0; padding:150px; display:flex; flex-direction:column; justify-content:center;">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:70px;">
    <div style="font-weight:300; font-size:96px; color:#000; line-height:1.05;">Works With<br>Any 24-Dram<br>Calendar</div>
    <div class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></div>
  </div>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:24px; max-width:1500px;">
    <div style="background:#fff; border-radius:10px; padding:32px 40px; font-size:36px; font-weight:700; color:#000;">Drinks by the Dram</div>
    <div style="background:#fff; border-radius:10px; padding:32px 40px; font-size:36px; font-weight:700; color:#000;">Secret Spirits</div>
    <div style="background:#fff; border-radius:10px; padding:32px 40px; font-size:36px; font-weight:700; color:#000;">Flaviar</div>
    <div style="background:#fff; border-radius:10px; padding:32px 40px; font-size:36px; font-weight:700; color:#000;">The Whisky Exchange</div>
  </div>
  <div style="font-size:32px; color:#454545; margin-top:50px; max-width:1300px;">
    Any standard 24 &times; 30ml calendar, plus supermarket sets. Also works for 12-day
    calendars &mdash; just use cards 01&ndash;12.
  </div>
</div>
""")

# ---------- SLIDE 9: HOW IT WORKS ----------
steps = [
    ("Purchase &amp; Download", "Instant access to the full 9-page PDF. Nothing ships."),
    ("Print at Home", "Standard US Letter, no bleed or special stock."),
    ("Grab the Card First", "Before you open the door. That's the whole trick."),
    ("Guess, Then Reveal", "Fill in the blind guess, taste, then check the label."),
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
  <div style="margin-top:50px; font-size:28px; color:#8a7663;">&#8252;&#65039; This is an ALL DIGITAL product. No physical items will be shipped. No advent calendar is included.</div>
</div>
""")

print("html written")
