import re

BASE = "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad"

css = open(f"{BASE}/agave_css_base.txt").read()
css = css.replace("<title>Cigar &amp; Whisky Journey</title>",
                  "<title>24 Nights of Whisky</title>")

ICON_DEFS = '''<svg style="display:none" aria-hidden="true">
  <symbol id="ico-glass" viewBox="0 0 28 28">
    <path d="M7 6 H21 L18.5 20 Q18 23 14 23 Q10 23 9.5 20 Z" fill="none" stroke="#8a7663" stroke-width="1.6"/>
    <path d="M8.3 12.5 H19.7 L18.5 20 Q18 23 14 23 Q10 23 9.5 20 Z" fill="#c98a2c"/>
    <path d="M8.3 12.5 H19.7 L19.3 15 H8.7 Z" fill="#e0ab4e"/>
  </symbol>
</svg>
'''

# Kit-specific styles
css = css.replace("  ::selection{background:var(--tier-aficionado); color:#000;}",
"""  /* ============ ADVENT CARDS ============ */
  @page{size:letter; margin:0;}
  .sheet-flex{display:flex; flex-direction:column;}
  .adv-grid{display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr;
            gap:0.16in; flex:1; min-height:0;}
  .adv-card{border:1px dashed var(--rule); border-radius:3px; padding:0.17in 0.19in;
            display:flex; flex-direction:column; min-height:0;}
  .adv-top{display:flex; align-items:flex-start; justify-content:space-between; margin-bottom:7px;}
  .adv-num{font-family:'Archivo Black','Raleway',sans-serif; font-size:2.1rem; line-height:0.85;
           color:var(--ink); letter-spacing:-0.02em;}
  .adv-daylabel{font-size:0.55rem; letter-spacing:0.12em; text-transform:uppercase;
                color:var(--ink-faint); font-weight:700; margin-bottom:2px;}
  .adv-datebox{text-align:right;}
  .adv-datebox .lbl{font-size:0.52rem; letter-spacing:0.07em; text-transform:uppercase; color:var(--ink-faint);}
  .adv-datebox .ln{border-bottom:1px solid var(--rule); width:0.78in; height:12px;}
  .adv-guess{background:var(--zone); border-radius:3px; padding:5px 8px 6px; margin-bottom:6px;}
  .adv-guess .gh{font-size:0.5rem; font-weight:700; letter-spacing:0.08em; text-transform:uppercase;
                 color:var(--ink-faint); margin-bottom:2px;}
  .adv-guess .gr{display:grid; grid-template-columns:1fr 1fr; gap:8px;}
  .adv-guess .gl{font-size:0.5rem; text-transform:uppercase; letter-spacing:0.05em; color:var(--ink-faint);}
  .adv-guess .ln{border-bottom:1px solid var(--rule); height:12px;}
  .adv-name{margin-bottom:6px;}
  .adv-name .lbl{font-size:0.52rem; letter-spacing:0.07em; text-transform:uppercase; color:var(--ink-faint);}
  .adv-name .ln{border-bottom:1px solid var(--ink); height:15px;}
  .adv-meta{display:grid; grid-template-columns:1fr 1fr 1fr; gap:6px; margin-bottom:7px;}
  .adv-meta .lbl{font-size:0.5rem; letter-spacing:0.06em; text-transform:uppercase; color:var(--ink-faint);}
  .adv-meta .ln{border-bottom:1px solid var(--rule); height:12px;}
  .adv-notes{flex:1; display:flex; flex-direction:column; gap:5px; min-height:0;}
  .adv-note{flex:1; display:flex; flex-direction:column; min-height:0;}
  .adv-note .lbl{font-size:0.55rem; font-weight:700; color:var(--ink); margin-bottom:1px;}
  .adv-note .lines{flex:1; display:flex; flex-direction:column; min-height:0;}
  .adv-note .lines .l{flex:1; border-bottom:1px solid var(--rule); min-height:9px;}
  .adv-foot{display:flex; align-items:center; justify-content:space-between; margin-top:7px;}
  .adv-score{display:flex; align-items:center; gap:4px;}
  .adv-score .lbl{font-size:0.52rem; letter-spacing:0.06em; text-transform:uppercase; color:var(--ink-faint); margin-right:1px;}
  .adv-dot{width:11px; height:11px; border:1px solid var(--ink-faint); border-radius:50%;}
  .adv-again{font-size:0.55rem; color:var(--ink-faint);}
  .adv-again b{color:var(--ink);}

  /* ============ TRACKER ============ */
  .trk-grid{display:grid; grid-template-columns:repeat(4,1fr); grid-template-rows:repeat(6,1fr);
            gap:0.12in; flex:1; min-height:0; margin-top:0.14in;}
  .trk-cell{border:1px solid var(--rule); border-radius:3px; padding:6px 8px 7px;
            display:flex; flex-direction:column; min-height:0;}
  .trk-cell .n{font-family:'Archivo Black','Raleway',sans-serif; font-size:0.78rem;
               color:var(--ink-faint); line-height:1;}
  .trk-cell .wr{flex:1; display:flex; flex-direction:column; min-height:0; margin-top:3px;}
  .trk-cell .wr .l{flex:1; border-bottom:1px solid var(--rule); min-height:11px;}
  .trk-cell .sc{display:flex; gap:3px; margin-top:5px;}
  .trk-cell .sd{width:8px; height:8px; border:1px solid var(--ink-faint); border-radius:50%;}
  .trk-podium{display:grid; grid-template-columns:repeat(5,1fr); gap:0.13in; margin-top:0.09in;}
  .trk-slot{border-top:2px solid var(--ink); padding-top:6px;}
  .trk-slot .r{font-family:'Archivo Black','Raleway',sans-serif; font-size:0.85rem; color:var(--ink);}
  .trk-slot .ln{border-bottom:1px solid var(--rule); height:20px; margin-top:3px;}
  ::selection{background:var(--tier-aficionado); color:#000;}""")

whisky_wheel = open(f"{BASE}/whisky_wheel.svg").read().strip()
wheel_inner = re.match(r'<svg[^>]*>(.*)</svg>', whisky_wheel, re.DOTALL).group(1)

GL = '<svg class="ico"><use href="#ico-glass"/></svg>'


def card(n):
    dots = '<span class="adv-dot"></span>' * 5
    return f'''
        <div class="adv-card">
          <div class="adv-top">
            <div>
              <div class="adv-daylabel">Night</div>
              <div class="adv-num">{n:02d}</div>
            </div>
            <div class="adv-datebox">
              <div class="lbl">Date</div>
              <div class="ln"></div>
            </div>
          </div>
          <div class="adv-guess">
            <div class="gh">Blind guess &mdash; before the reveal</div>
            <div class="gr">
              <div><div class="gl">Region / style</div><div class="ln"></div></div>
              <div><div class="gl">Age</div><div class="ln"></div></div>
            </div>
          </div>
          <div class="adv-name">
            <div class="lbl">The reveal &middot; distillery &amp; expression</div>
            <div class="ln"></div>
          </div>
          <div class="adv-meta">
            <div><div class="lbl">Region</div><div class="ln"></div></div>
            <div><div class="lbl">Age</div><div class="ln"></div></div>
            <div><div class="lbl">ABV</div><div class="ln"></div></div>
          </div>
          <div class="adv-notes">
            <div class="adv-note"><div class="lbl">Nose</div>
              <div class="lines"><div class="l"></div><div class="l"></div></div></div>
            <div class="adv-note"><div class="lbl">Palate</div>
              <div class="lines"><div class="l"></div><div class="l"></div></div></div>
            <div class="adv-note"><div class="lbl">Finish</div>
              <div class="lines"><div class="l"></div></div></div>
          </div>
          <div class="adv-foot">
            <div class="adv-score"><span class="lbl">Score</span>{dots}</div>
            <div class="adv-again">Full bottle? <b>Y / N</b></div>
          </div>
        </div>'''


card_pages = ""
for page in range(6):
    nums = [page * 4 + i + 1 for i in range(4)]
    cards = "".join(card(n) for n in nums)
    first, last = nums[0], nums[-1]
    card_pages += f'''
  <div id="cards-{page+1}">
    <div class="sheet-label"><span class="n">{page+2:02d}</span><h2>Tasting Cards &middot; Nights {first}&ndash;{last}</h2><span class="fmt">8.5 &times; 11 in &middot; 1 page</span></div>
    <div class="sheet sheet-flex">
      <div class="adv-grid">{cards}
      </div>
    </div>
  </div>
'''

trk_cells = ""
for n in range(1, 25):
    dots = '<span class="sd"></span>' * 5
    trk_cells += f'''
          <div class="trk-cell">
            <div class="n">{n:02d}</div>
            <div class="wr"><div class="l"></div><div class="l"></div></div>
            <div class="sc">{dots}</div>
          </div>'''

podium = ""
for i in range(1, 6):
    podium += f'''
          <div class="trk-slot">
            <div class="r">{i:02d}</div>
            <div class="ln"></div>
          </div>'''

body = f'''
{ICON_DEFS}
<div class="topbar">
  <div class="brand"><span class="kb-badge sm"><span class="l1">KINGB</span><span class="l2">KITS</span></span><span class="word">24 Nights of Whisky</span></div>
  <div class="nav-tabs">
    <a href="#guide">Guide</a>
    <a href="#cards-1">Tasting Cards</a>
    <a href="#tracker">Tracker</a>
    <a href="#wheel">Flavor Wheel</a>
  </div>
  <div class="print-hint">Print each sheet at Letter, no scaling &mdash; <kbd>Cmd/Ctrl+P</kbd></div>
</div>

<div class="intro">
  <div class="eyebrow">Product Master &middot; v1</div>
  <h1>The advent calendar companion</h1>
  <p>Built for the person who already bought a 24-dram whisky advent calendar and has nowhere to write anything down. Twenty-four numbered cards, a month-at-a-glance tracker, and a flavor wheel &mdash; same system as the other kits.</p>
  <p class="fit-note">This one deliberately ships <b>no bottle recommendations</b>. The buyer's calendar already picked the whiskies; the job here is to capture them, not to shop. That is what makes it a companion product rather than a competing one.</p>
</div>

<div class="deck">

  <!-- PIECE 1: GUIDE -->
  <div id="guide">
    <div class="sheet-label"><span class="n">01</span><h2>How to Use</h2><span class="fmt">8.5 &times; 11 in &middot; 1 page</span></div>
    <div class="sheet">
      <div class="g-top" style="display:flex; justify-content:space-between; align-items:flex-start;">
        <div>
          <div class="breadcrumb">Start Here</div>
          <div class="arrow">&darr;</div>
          <h3>24 Nights of Whisky</h3>
          <div class="sub">One dram a night, written down properly</div>
        </div>
        <span class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></span>
      </div>

      <div class="g-cols">
        <div>
          <div class="g-block">
            <h4>BEFORE NIGHT ONE</h4>
            <ul>
              <li>Print the six card sheets and cut along the dashed lines. Twenty-four cards, four per page.</li>
              <li>Print the tracker once and put it somewhere you'll actually see it &mdash; the whole point is watching the month fill in.</li>
              <li>Keep the flavor wheel next to the glass, not in a drawer.</li>
            </ul>
            <h4 style="margin-top:14px;">EACH NIGHT</h4>
            <ul>
              <li>Grab that night's numbered card <b>before</b> you open the door. Most calendars keep the dram a mystery, so the guess only works if the card comes first.</li>
              <li><b>Guess blind.</b> Pour, nose, taste, then commit to a region and an age on the card. Only then read the label and fill in the reveal.</li>
              <li>Nose it with your mouth slightly open. Most calendar drams run cask strength or close to it.</li>
              <li>Add a few drops of water partway through and note whether it opened up. On a 30ml dram you get exactly one chance at this.</li>
            </ul>
          </div>
        </div>
        <div>
          <div class="g-block">
            <h4>SCORING</h4>
            <ul>
              <li>Five circles, fill as many as it earns. Resist scoring everything a four &mdash; the spread is what makes the tracker worth reading in January.</li>
              <li>"Full bottle? Y / N" is the only question that really matters. Circle it honestly.</li>
            </ul>
            <h4 style="margin-top:14px;">AT THE END</h4>
            <ul>
              <li>Transfer each night's name and score to the tracker as you go, not all at once on the 24th.</li>
              <li>Fill in your top five on the tracker. That list is your buying list for next year.</li>
              <li>Keep the cards. Next December you'll want to know what past-you thought.</li>
            </ul>
          </div>
          <hr class="g-rule">
          <div class="g-block">
            <h4>WHICH CALENDARS THIS FITS</h4>
            <p>Built around the standard <b>24 &times; 30ml</b> format, so it works with Drinks by the Dram, Secret Spirits, Flaviar, The Whisky Exchange, and the supermarket calendars. Scotch, bourbon, Irish, Japanese or world whisky &mdash; the cards don't assume a category.</p>
            <p style="margin-top:6px;">Also fine for a 12-day calendar: use cards 01&ndash;12 and ignore the rest.</p>
          </div>
          <hr class="g-rule">
          <div class="g-block">
            <h4>IF YOU'RE SHARING</h4>
            <p>Print a second set per person and compare before the reveal. Two people rarely guess the same region, and that argument is the best part of the night.</p>
          </div>
        </div>
      </div>

      <div class="g-toc">
        <h4>WHAT'S IN THIS KIT</h4>
        <div class="g-toc-grid">
          <a href="#guide"><span class="tn">01</span><span class="tt">How to Use</span><span class="tp">This page</span></a>
          <a href="#cards-1"><span class="tn">02&ndash;07</span><span class="tt">Tasting Cards</span><span class="tp">Pages 2-7</span></a>
          <a href="#tracker"><span class="tn">08</span><span class="tt">Month Tracker</span><span class="tp">Page 8</span></a>
          <a href="#wheel"><span class="tn">09</span><span class="tt">Flavor Wheel</span><span class="tp">Page 9</span></a>
          <a href="#cards-1"><span class="tn">24</span><span class="tt">Numbered Cards</span><span class="tp">4 per sheet</span></a>
        </div>
      </div>

    </div>
  </div>
{card_pages}
  <!-- TRACKER -->
  <div id="tracker">
    <div class="sheet-label"><span class="n">08</span><h2>Month Tracker</h2><span class="fmt">8.5 &times; 11 in &middot; 1 page</span></div>
    <div class="sheet sheet-flex">
      <div class="pb-head" style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0;">
        <div>
          <div class="eyebrow">Tracker</div>
          <h3>The Whole Month at a Glance</h3>
          <div class="sub">Name and score each night as you go, not all at once on the 24th.</div>
        </div>
        <span class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></span>
      </div>

      <div class="trk-grid">{trk_cells}
      </div>

      <div style="margin-top:0.22in;">
        <h4 style="font-weight:700; font-size:0.86rem; color:var(--ink); margin:0 0 2px;">TOP FIVE OF THE MONTH</h4>
        <div style="font-size:0.72rem; color:var(--ink-faint);">Your buying list for next year. Start from the nights you circled <b style="color:var(--ink-body)">Y</b>.</div>
        <div class="trk-podium">{podium}
        </div>
      </div>
    </div>
  </div>

  <!-- FLAVOR WHEEL -->
  <div id="wheel">
    <div class="sheet-label"><span class="n">09</span><h2>Flavor Wheel</h2><span class="fmt">8.5 &times; 11 in &middot; 1 page</span></div>
    <div class="sheet">
      <div class="fw-head" style="display:flex; justify-content:space-between; align-items:flex-start;">
        <div>
          <div class="eyebrow">Flavor Wheel</div>
          <h3>Put a Word to It</h3>
          <div class="sub">Start at the center tier, work outward for something more specific.</div>
        </div>
        <span class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></span>
      </div>

      <div style="display:flex; justify-content:center; margin-top:0.3in;">
        <svg viewBox="0 0 580 580" style="width:100%; max-width:5.6in; height:auto;">{wheel_inner}</svg>
      </div>

      <div class="fw-how" style="margin-top:0.28in;"><b>Using the wheel:</b> taste first, then find the inner-ring category that fits &mdash; Sweet, Smoky, Fruity, and so on. From there work outward to the specific note. Two words per card is plenty; you are building a vocabulary over twenty-four nights, not writing a review.</div>
    </div>
  </div>

</div>
'''

with open(f"{BASE}/kingbkits-advent-kit.html", "w") as f:
    f.write(css + body)

print("built:", len(css + body), "chars")
