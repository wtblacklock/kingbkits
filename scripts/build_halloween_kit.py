import re

BASE = "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad"

css = open(f"{BASE}/agave_css_base.txt").read()
css = css.replace("<title>Cigar &amp; Whisky Journey</title>",
                  "<title>Candy &amp; Whisky Pairing</title>")

ICON_DEFS = '''<svg style="display:none" aria-hidden="true">
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
'''

css = css.replace("  ::selection{background:var(--tier-aficionado); color:#000;}",
"""  @page{size:letter; margin:0;}
  .pcard .flight-q{background:var(--zone); border-radius:4px; padding:9px 14px; margin-bottom:12px; font-size:0.74rem; color:var(--ink-body);}
  .pcard .flight-q b{color:var(--ink);}
  .pcard .checkpoint .ck-order{font-size:0.62rem; font-weight:700; color:var(--ink-faint); letter-spacing:0.06em; text-transform:uppercase;}
  .pb-sub{font-size:0.68rem; color:var(--ink-faint); display:block; margin-top:3px;}
  .pr-warn{background:var(--zone); border-left:3px solid var(--ink); padding:12px 14px; margin-top:16px;}
  .pr-warn h5{font-weight:700; font-size:0.78rem; color:var(--ink); margin:0 0 6px;}
  .pr-warn p{font-size:0.74rem; color:var(--ink-body); margin:0 0 5px;}
  .pr-warn b{color:var(--ink);}
  ::selection{background:var(--tier-aficionado); color:#000;}""")

candy_wheel = open(f"{BASE}/candy_wheel.svg").read().strip()
whisky_wheel = open(f"{BASE}/whisky_wheel2.svg").read().strip()
def inner(svg):
    return re.match(r'<svg[^>]*>(.*)</svg>', svg, re.DOTALL).group(1)

CA = '<svg class="ico"><use href="#ico-candy"/></svg>'
GL = '<svg class="ico"><use href="#ico-glass"/></svg>'


def flight_card(tier_class, tier_name, flight_name, origin, question, pours):
    blocks = []
    for order, (label, hint) in enumerate(pours, start=1):
        blocks.append(f'''
              <div class="checkpoint">
                <div class="ck-head">
                  <div>
                    <div class="ck-order">Pairing {order}</div>
                    <div class="ck-name">{label}</div>
                  </div>
                  <div class="ck-hint">{hint}</div>
                </div>
                <div class="pour-line">{GL}Whisky poured<div class="fill-line"></div></div>
                <div class="note-lines">
                  <div class="ln"></div><div class="ln"></div><div class="ln"></div>
                </div>
              </div>''')
    return f'''
      <div class="pcard-page">
        <div class="pcard">
          <div class="bar">
            <div class="left">
              <span class="tier-pill {tier_class}">{tier_name}</span>
              <span class="cat">{flight_name}</span>
            </div>
            <span class="kb-badge sm"><span class="l1">KINGB</span><span class="l2">KITS</span></span>
          </div>
          <div class="body">
            <div class="origin">{origin}</div>
            <div class="flight-q">{question}</div>
            <div class="pairnames">
              <div><div class="role">{CA}Taster</div><div class="fill-line"></div></div>
              <div><div class="role">Date</div><div class="fill-line"></div></div>
            </div>
            <div class="checkpoints">{"".join(blocks)}
            </div>
            <div class="footer-row">
              <div><div class="role">Winner of the night</div><div class="fill-line"></div></div>
              <div><div class="role">Worst pairing (be honest)</div><div class="fill-line"></div></div>
            </div>
          </div>
        </div>
      </div>'''


SPF = "Sip &middot; bite &middot; sip again"

card_newbie = flight_card(
    "newbie", "Newbie", "The Sweet Match",
    "Three candies &middot; one bourbon &middot; like paired with like",
    "<b>The question:</b> what does it feel like when a pairing <i>agrees</i>? Every candy here shares a flavor compound with the whisky. Nothing fights. This is your baseline for everything after.",
    [("Snickers", SPF), ("Twix", SPF), ("Milky Way", SPF)])

card_casual = flight_card(
    "casual", "Casual", "The Contrast",
    "Three candies &middot; two whiskies &middot; opposites on purpose",
    "<b>The question:</b> can a pairing work by <i>fighting</i>? Dark chocolate against peat smoke should be a train wreck and isn't. Salt against sweet should be too much and isn't. Find out where the line is.",
    [("Dark Chocolate + Peated Scotch", SPF), ("Reese's + Wheated Bourbon", SPF), ("Almond Joy + Rye", SPF)])

card_aficionado = flight_card(
    "aficionado", "Aficionado", "The Gauntlet",
    "The difficult candy &middot; the ones nobody pairs on purpose",
    "<b>The question:</b> what actually survives? Acid, anise and pure sugar are the three things whisky handles worst. Something here will surprise you and something will be genuinely unpleasant. Both are the point.",
    [("Sour Patch Kids", "Acid vs oak"), ("Black Licorice", "Anise vs peat"), ("Candy Corn", "Pure sugar vs everything")])


body = f'''
{ICON_DEFS}
<div class="topbar">
  <div class="brand"><span class="kb-badge sm"><span class="l1">KINGB</span><span class="l2">KITS</span></span><span class="word">Candy &amp; Whisky</span></div>
  <div class="nav-tabs">
    <a href="#guide">Guide</a>
    <a href="#primer">Primer</a>
    <a href="#pairbase">Pairbase</a>
    <a href="#wheels">Flavor Wheels</a>
    <a href="#cards">Tasting Cards</a>
  </div>
  <div class="print-hint">Print each sheet at Letter, no scaling &mdash; <kbd>Cmd/Ctrl+P</kbd></div>
</div>

<div class="intro">
  <div class="eyebrow">Product Master &middot; v1</div>
  <h1>The cheapest way into a tasting night</h1>
  <p>Same system as the other kits, but the shopping list is a $12 bag of fun-size candy and one bottle you probably already own. Seven pages, print at home.</p>
  <p class="fit-note">Two selling windows on purpose: <b>October</b> for Halloween parties, and <b>November 1&ndash;7</b> for the leftover candy bowl, which is a nearly uncontested week.</p>
</div>

<div class="deck">

  <!-- PIECE 1: GUIDE -->
  <div id="guide">
    <div class="sheet-label"><span class="n">01</span><h2>Party Guide</h2><span class="fmt">8.5 &times; 11 in &middot; 1 page</span></div>
    <div class="sheet">
      <div class="g-top" style="display:flex; justify-content:space-between; align-items:flex-start;">
        <div>
          <div class="breadcrumb">Start Here</div>
          <div class="arrow">&darr;</div>
          <h3>The Candy Bowl Tasting</h3>
          <div class="sub">Your leftovers deserve better</div>
        </div>
        <span class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></span>
      </div>

      <div class="g-cols">
        <div>
          <div class="g-block">
            <h4>WHAT TO BUY</h4>
            <ul>
              <li><b>One bag of fun-size variety candy.</b> That's roughly $12 and it covers the whole table. The Pairbase names the specific bars that matter.</li>
              <li><b>One bottle</b> for Newbie, two for Casual and Aficionado. Check the Pairbase for your tier before you shop.</li>
              <li>You almost certainly already own a workable bottle. Start there before buying anything.</li>
            </ul>
            <h4 style="margin-top:14px;">SET UP</h4>
            <ul>
              <li>Unwrap everything and put each candy on its own plate or napkin. Wrappers are loud and they give away the answer.</li>
              <li>Half-ounce pours, not full ones. You're taking three or four sips per pairing, not drinking a glass.</li>
              <li>Water and plain crackers on the table. You'll need the reset more than you expect.</li>
            </ul>
          </div>
        </div>
        <div>
          <div class="g-block">
            <h4>HOW TO TASTE A PAIRING</h4>
            <ul>
              <li><b>Sip, bite, sip again.</b> The second sip is the one that matters &mdash; that's the pairing talking. The first is just the whisky.</li>
              <li>Let the chocolate melt rather than chewing it. Fat coats the palate, which is exactly what tames a high-proof pour.</li>
              <li>Rinse with water between pairings. Sugar builds up fast and by pairing four everything tastes the same.</li>
              <li>Vote on a winner at the end, and be honest about the worst one. The disasters are the fun part.</li>
            </ul>
          </div>
          <hr class="g-rule">
          <div class="g-block">
            <h4>IF THERE ARE KIDS AROUND</h4>
            <p>Run the same cards with cold brew, root beer, or apple cider instead of whisky. The candy side of the pairing works identically and the flavor wheel doesn't care what's in the glass.</p>
          </div>
        </div>
      </div>

      <div class="g-toc">
        <h4>WHAT'S IN THIS KIT</h4>
        <div class="g-toc-grid">
          <a href="#guide"><span class="tn">01</span><span class="tt">Party Guide</span><span class="tp">This page</span></a>
          <a href="#primer"><span class="tn">02</span><span class="tt">Candy Primer</span><span class="tp">Page 2</span></a>
          <a href="#pairbase"><span class="tn">03</span><span class="tt">Pairbase</span><span class="tp">Page 3</span></a>
          <a href="#wheels"><span class="tn">04</span><span class="tt">Flavor Wheels</span><span class="tp">Page 4</span></a>
          <a href="#cards"><span class="tn">05</span><span class="tt">Tasting Cards</span><span class="tp">Pages 5-7</span></a>
        </div>
      </div>

    </div>
  </div>

  <!-- PIECE 2: PRIMER -->
  <div id="primer">
    <div class="sheet-label"><span class="n">02</span><h2>Candy Primer</h2><span class="fmt">8.5 &times; 11 in &middot; 1 page</span></div>
    <div class="sheet">
      <div class="pr-head" style="display:flex; justify-content:space-between; align-items:flex-start;">
        <div>
          <div class="eyebrow">Primer</div>
          <h3>Why Candy and Whisky Agree</h3>
          <div class="sub">The overlap is real chemistry, not a party trick.</div>
        </div>
        <span class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></span>
      </div>

      <div class="pr-cols">
        <div>
          <div class="pr-section">
            <h4>{CA}What's Actually In There</h4>
            <div class="lede">Five ingredients do almost all the work.</div>
            <div class="pr-item">
              <div class="name">Milk chocolate</div>
              <p>Cocoa butter, milk solids and sugar. The fat physically coats your palate, which blunts alcohol burn. This is why chocolate makes a cask-strength pour suddenly drinkable.</p>
            </div>
            <div class="pr-item">
              <div class="name">Caramel</div>
              <p>Cooked sugar produces the same browning compounds that form when a barrel is charred. Caramel candy and bourbon are, in a real sense, tasting of the same reaction.</p>
            </div>
            <div class="pr-item">
              <div class="name">Coconut</div>
              <p>Rich in lactones &mdash; the exact compound class American oak gives bourbon. An Almond Joy against a bourbon is a straight compound match, which is why it lands so hard.</p>
            </div>
            <div class="pr-item">
              <div class="name">Malt and nougat</div>
              <p>Malted barley in nougat and malted-milk candy shares its base ingredient with single malt. Same grain, different end of the process.</p>
            </div>
            <div class="pr-item">
              <div class="name">Salt</div>
              <p>Suppresses bitterness and boosts perceived sweetness. It's why salted peanut candy flatters oak tannin instead of fighting it.</p>
            </div>
          </div>
        </div>

        <div>
          <div class="pr-section">
            <h4>{GL}The Two Kinds of Pairing</h4>
            <div class="pr-timeline">
              <div class="pr-step">
                <div class="name">Complement</div>
                <p>Shared compounds. Caramel candy with a caramel-forward bourbon. Comfortable, obvious, and the right place to start. This is the Newbie card.</p>
              </div>
              <div class="pr-step">
                <div class="name">Contrast</div>
                <p>Opposing forces that hold each other up. Bitter dark chocolate against peat smoke. Salt against sweet. Riskier, and far more interesting when it lands. This is the Casual card.</p>
              </div>
              <div class="pr-step">
                <div class="name">Collision</div>
                <p>Acid, anise and raw sugar &mdash; the three things whisky handles worst. Mostly bad, occasionally astonishing. This is the Aficionado card.</p>
              </div>
            </div>
          </div>

          <div class="pr-warn">
            <h5>THE THREE DIFFICULT ONES</h5>
            <p><b>Sour candy.</b> Citric and malic acid strip the palate and clash hard with oak tannin. Genuinely useful as a reset between pairings; rarely good as a pairing itself.</p>
            <p><b>Black licorice.</b> Anethole, the anise compound. Fights almost everything, then works unreasonably well with heavily peated Islay.</p>
            <p><b>Candy corn.</b> Effectively sugar, honey and vanilla with no fat to carry it. Nothing tames it. Expect an argument at the table, which is the whole reason it's on the card.</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- PIECE 3: PAIRBASE -->
  <div id="pairbase">
    <div class="sheet-label"><span class="n">03</span><h2>Pairbase</h2><span class="fmt">8.5 &times; 11 in &middot; 1 page</span></div>
    <div class="sheet">
      <div class="pb-head" style="display:flex; justify-content:space-between; align-items:flex-start;">
        <div>
          <div class="eyebrow">Pairbase</div>
          <h3>What to Pour Against What</h3>
          <div class="sub">Every bottle here is common and under $70.</div>
        </div>
        <span class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></span>
      </div>

      <table class="pairbase">
        <colgroup>
          <col style="width:17%"><col style="width:20%"><col style="width:19%">
          <col style="width:26%"><col style="width:18%">
        </colgroup>
        <thead>
          <tr>
            <th>{CA}Candy</th>
            <th>Why It Works</th>
            <th>{GL}Whisky Style</th>
            <th>Try These Bottles</th>
            <th>Pairing Type</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>Snickers</b></td>
            <td>Caramel and roasted peanut meet barrel char head-on.</td>
            <td>Caramel-forward bourbon</td>
            <td>Evan Williams Bottled-in-Bond<span class="pb-sub">Four Roses Small Batch</span></td>
            <td>Complement</td>
          </tr>
          <tr>
            <td><b>Twix</b></td>
            <td>Cookie and caramel echo oak and vanilla almost exactly.</td>
            <td>Standard bourbon</td>
            <td>Buffalo Trace<span class="pb-sub">Eagle Rare 10</span></td>
            <td>Complement</td>
          </tr>
          <tr>
            <td><b>Milky Way</b></td>
            <td>Malted nougat shares its base grain with the whisky.</td>
            <td>Sweeter bourbon or Speyside</td>
            <td>Jim Beam Black<span class="pb-sub">Glenlivet 12</span></td>
            <td>Complement</td>
          </tr>
          <tr>
            <td><b>Almond Joy</b></td>
            <td>Coconut lactones are the same compounds American oak donates.</td>
            <td>Rye, or a rum-cask finish</td>
            <td>Rittenhouse Rye<span class="pb-sub">Wild Turkey 101</span></td>
            <td>Complement</td>
          </tr>
          <tr>
            <td><b>Reese's</b></td>
            <td>Salt suppresses bitterness and lifts the sweetness underneath.</td>
            <td>Wheated bourbon</td>
            <td>Maker's Mark<span class="pb-sub">Larceny</span></td>
            <td>Contrast</td>
          </tr>
          <tr>
            <td><b>Dark chocolate</b></td>
            <td>Cocoa bitterness and peat smoke cancel each other's edges.</td>
            <td>Peated Islay</td>
            <td>Highland Park 12<span class="pb-sub">Laphroaig 10</span></td>
            <td>Contrast</td>
          </tr>
          <tr>
            <td><b>Sour Patch Kids</b></td>
            <td>Acid strips the palate. Best used as a reset, not a pairing.</td>
            <td>Anything, briefly</td>
            <td>Use between pairings<span class="pb-sub">not as one</span></td>
            <td>Collision</td>
          </tr>
          <tr>
            <td><b>Black licorice</b></td>
            <td>Anise fights everything except heavy peat, where it sings.</td>
            <td>Heavily peated scotch</td>
            <td>Ardbeg 10<span class="pb-sub">Laphroaig 10</span></td>
            <td>Collision</td>
          </tr>
          <tr>
            <td><b>Candy corn</b></td>
            <td>Pure sugar with no fat to carry it. Nothing tames it.</td>
            <td>Irish, if anything</td>
            <td>Jameson<span class="pb-sub">good luck</span></td>
            <td>Collision</td>
          </tr>
        </tbody>
      </table>

      <div class="pb-note">
        <b>Shopping math.</b> One $12 bag of fun-size variety candy plus one bottle you likely already own covers a table of six. <b>This is the cheapest tasting night you will ever host</b>, which makes it the easiest one to actually schedule.
      </div>
    </div>
  </div>

  <!-- PIECE 4: FLAVOR WHEELS -->
  <div id="wheels">
    <div class="sheet-label"><span class="n">04</span><h2>Flavor Wheels</h2><span class="fmt">8.5 &times; 11 in &middot; 1 page</span></div>
    <div class="sheet">
      <div class="fw-head" style="display:flex; justify-content:space-between; align-items:flex-start;">
        <div>
          <div class="eyebrow">Flavor Wheels</div>
          <h3>Find the Overlap</h3>
          <div class="sub">Where the two wheels share a word, the pairing usually works.</div>
        </div>
        <span class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></span>
      </div>

      <div class="fw-pair">
        <figure>
          <svg viewBox="0 0 580 580">{inner(candy_wheel)}</svg>
          <figcaption>Candy</figcaption>
        </figure>
        <figure>
          <svg viewBox="0 0 580 580">{inner(whisky_wheel)}</svg>
          <figcaption>Whisky</figcaption>
        </figure>
      </div>

      <div class="fw-how"><b>Using the wheels:</b> name what's in the candy, then name what's in the glass. <b>Caramel, Nutty and Malt appear on both wheels</b> &mdash; those overlaps are your safe pairings. Sour appears on only one, which tells you everything about why sour candy is so hard to pair.</div>
    </div>
  </div>

  <!-- PIECE 5: TASTING CARDS -->
  <div id="cards">
    <div class="sheet-label"><span class="n">05a</span><h2>Tasting Card &middot; Newbie</h2><span class="fmt">8.5 &times; 11 in &middot; 1 page</span></div>
    <div class="sheet">{card_newbie}
    </div>
  </div>

  <div id="cards-casual">
    <div class="sheet-label"><span class="n">05b</span><h2>Tasting Card &middot; Casual</h2><span class="fmt">8.5 &times; 11 in &middot; 1 page</span></div>
    <div class="sheet">{card_casual}
    </div>
  </div>

  <div id="cards-aficionado">
    <div class="sheet-label"><span class="n">05c</span><h2>Tasting Card &middot; Aficionado</h2><span class="fmt">8.5 &times; 11 in &middot; 1 page</span></div>
    <div class="sheet">{card_aficionado}
    </div>
  </div>

</div>
'''

with open(f"{BASE}/kingbkits-halloween-kit.html", "w") as f:
    f.write(css + body)

print("built:", len(css + body), "chars")
