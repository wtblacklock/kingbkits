import re

BASE = "/private/tmp/claude-503/-Users-BIGWilly-Projects-trailsteadguide/87d4370e-7294-4ec3-abfe-3d9c94e0cb41/scratchpad"

css = open(f"{BASE}/agave_css_base.txt").read()

# Retitle
css = css.replace("<title>Cigar &amp; Whisky Journey</title>",
                  "<title>Agave Tasting Journey</title>")

# Agave-appropriate icon symbols (the CSS slice ends at </style>, so these get
# prepended to the body rather than swapped in)
ICON_DEFS = '''<svg style="display:none" aria-hidden="true">
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
'''

# Extra styles this kit needs on top of the shared system
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

tequila_wheel = open(f"{BASE}/tequila_wheel.svg").read().strip()
mezcal_wheel = open(f"{BASE}/mezcal_wheel.svg").read().strip()
def inner(svg):
    return re.match(r'<svg[^>]*>(.*)</svg>', svg, re.DOTALL).group(1)

AG = '<svg class="ico"><use href="#ico-agave"/></svg>'
CO = '<svg class="ico"><use href="#ico-copita"/></svg>'


def flight_card(tier_class, tier_name, flight_name, origin, question, pours):
    blocks = []
    for order, (label, hint) in enumerate(pours, start=1):
        blocks.append(f'''
              <div class="checkpoint">
                <div class="ck-head">
                  <div>
                    <div class="ck-order">Pour {order}</div>
                    <div class="ck-name">{label}</div>
                  </div>
                  <div class="ck-hint">{hint}</div>
                </div>
                <div class="pour-line">{CO}What I poured<div class="fill-line"></div></div>
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
              <div><div class="role">{AG}Taster</div><div class="fill-line"></div></div>
              <div><div class="role">Date</div><div class="fill-line"></div></div>
            </div>
            <div class="checkpoints">{"".join(blocks)}
            </div>
            <div class="footer-row">
              <div><div class="role">Best of the night</div><div class="fill-line"></div></div>
              <div><div class="role">Would buy again</div><div class="fill-line"></div></div>
            </div>
          </div>
        </div>
      </div>'''


NOSE = "Nose &middot; palate &middot; finish"

card_newbie = flight_card(
    "newbie", "Newbie", "The Age Ladder",
    "Three tequilas &middot; same distillery if you can &middot; lightest to darkest",
    "<b>The question:</b> what did the barrel actually do? Same agave, same distillery, three different amounts of oak. Everything you taste that changes is the wood.",
    [("Blanco", NOSE), ("Reposado", NOSE), ("A&ntilde;ejo", NOSE)])

card_casual = flight_card(
    "casual", "Casual", "Tequila Meets Mezcal",
    "Two tequilas and one mezcal &middot; the smoke reveal sits in the middle",
    "<b>The question:</b> where does the smoke actually come from? Pour 2 is the same plant family as Pour 1, cooked in a fire pit instead of a steam oven. That is the only real difference.",
    [("Tequila Blanco", NOSE), ("Mezcal Espad&iacute;n", NOSE), ("Tequila Reposado", NOSE)])

card_aficionado = flight_card(
    "aficionado", "Aficionado", "Agave Terroir",
    "Three mezcals &middot; three different agave species &middot; same producer if possible",
    "<b>The question:</b> forget the process, taste the plant. Hold the producer and method steady and the only variable left is which agave went in the pit, and how long it grew.",
    [("Espad&iacute;n", "The baseline"), ("Tobal&aacute; or Cuishe", "Wild &middot; 12-15 yrs"), ("Tepeztate or Arroque&ntilde;o", "Wild &middot; 20-25 yrs")])


body = f'''
{ICON_DEFS}
<div class="topbar">
  <div class="brand"><span class="kb-badge sm"><span class="l1">KINGB</span><span class="l2">KITS</span></span><span class="word">The Agave Tasting Journey</span></div>
  <div class="nav-tabs">
    <a href="#guide">Guide</a>
    <a href="#primer">Primer</a>
    <a href="#agavebase">Agavebase</a>
    <a href="#wheels">Flavor Wheels</a>
    <a href="#cards">Tasting Cards</a>
  </div>
  <div class="print-hint">Print each sheet at Letter, no scaling &mdash; <kbd>Cmd/Ctrl+P</kbd></div>
</div>

<div class="intro">
  <div class="eyebrow">Product Master &middot; v1</div>
  <h1>Tequila &amp; Mezcal, built on the same system</h1>
  <p>Same Raleway type, same grey/white content zones, same tier colors as the Whisky and Cigar kits (Newbie <b style="color:#6b9c1c">&#9679;</b> Casual <b style="color:#c7c700">&#9679;</b> Aficionado <b style="color:#c99a1a">&#9679;</b>). Seven pages, print at home.</p>
  <p class="fit-note">The structural difference from the cigar kit: a cigar burns in three stages, so those cards tracked one pairing over time. Agave has no burn, so these cards track a <b>flight of three pours</b> instead, and each tier changes which variable is being isolated.</p>
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
          <h3>Agave Night</h3>
          <div class="sub">Sip it, don't shoot it</div>
        </div>
        <span class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></span>
      </div>

      <div class="g-cols">
        <div>
          <div class="g-block">
            <h4>PRE-PARTY PLANNING</h4>
            <ul>
              <li><b>Three one-ounce pours per guest</b> &mdash; that's the whole night. A 750ml bottle holds about 25 tastes, so one bottle per spirit covers six to eight people comfortably.</li>
              <li>Pick <b>one tier</b> from the Agavebase and stay in it. Pouring a $25 blanco against a $120 wild-agave mezcal just makes the cheap one taste broken.</li>
              <li>Buying or BYO both work &mdash; three bottles total is the whole shopping list.</li>
            </ul>
            <h4 style="margin-top:14px;">SET A DATE AND SEND INVITES</h4>
            <ul>
              <li>Say the word "tasting" in the invite. It sets expectations away from shots and toward a seated hour.</li>
              <li>Tell everyone to eat beforehand. This is high proof on a slow schedule.</li>
            </ul>
            <h4 style="margin-top:14px;">GATHER SUPPLIES</h4>
            <ul>
              <li>Copitas, veladoras, or small wine glasses &mdash; anything that holds aroma. Never shot glasses.</li>
              <li>Water and plain crackers between pours.</li>
              <li>Orange slices, and chili salt or sal de gusano if you can find it.</li>
            </ul>
          </div>
        </div>
        <div>
          <div class="g-block">
            <h4>PARTY SETUP</h4>
            <ul>
              <li>Three glasses per guest if you have them, so pours can sit side by side and be revisited.</li>
              <li>Bag or hide the bottles for a blind round &mdash; labels change what people think they taste.</li>
              <li>Pour one ounce, no more. Everyone gets a tasting card before the first pour.</li>
            </ul>
            <h4 style="margin-top:14px;">DURING THE PARTY</h4>
            <ul>
              <li><b>No ice, no lime, no salt.</b> That ritual exists to cover cheap mixto. Good agave doesn't need hiding.</li>
              <li>Nose it with your mouth slightly open. A hard sniff at 40%+ ABV just numbs you.</li>
              <li>Small sip, let it coat, then swallow. The second sip always reads differently than the first &mdash; that one is the honest one.</li>
              <li>Five to ten minutes and a sip of water between pours. Close with a vote.</li>
            </ul>
          </div>
          <hr class="g-rule">
          <div class="g-block">
            <h4>SNACK PAIRINGS</h4>
            <p>Orange slices with chili salt, dark chocolate, salted nuts, aged cheese, grilled pineapple. Skip anything sugary or lime-forward &mdash; both flatten the agave.</p>
          </div>
        </div>
      </div>

      <div class="g-toc">
        <h4>WHAT'S IN THIS KIT</h4>
        <div class="g-toc-grid">
          <a href="#guide"><span class="tn">01</span><span class="tt">Party Guide</span><span class="tp">This page</span></a>
          <a href="#primer"><span class="tn">02</span><span class="tt">Primer</span><span class="tp">Page 2</span></a>
          <a href="#agavebase"><span class="tn">03</span><span class="tt">Agavebase</span><span class="tp">Page 3</span></a>
          <a href="#wheels"><span class="tn">04</span><span class="tt">Flavor Wheels</span><span class="tp">Page 4</span></a>
          <a href="#cards"><span class="tn">05</span><span class="tt">Tasting Cards</span><span class="tp">Pages 5-7</span></a>
        </div>
      </div>

    </div>
  </div>

  <!-- PIECE 2: PRIMER -->
  <div id="primer">
    <div class="sheet-label"><span class="n">02</span><h2>Tequila &amp; Mezcal Primer</h2><span class="fmt">8.5 &times; 11 in &middot; 1 page</span></div>
    <div class="sheet">
      <div class="pr-head" style="display:flex; justify-content:space-between; align-items:flex-start;">
        <div>
          <div class="eyebrow">Primer</div>
          <h3>Know Your Agave</h3>
          <div class="sub">Enough to order well and host without bluffing.</div>
        </div>
        <span class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></span>
      </div>

      <div class="pr-cols">
        <div>
          <div class="pr-section">
            <h4>{AG}Tequila vs Mezcal</h4>
            <div class="lede">All tequila is technically a mezcal. Almost no mezcal is tequila.</div>
            <div class="pr-item">
              <div class="name">Tequila</div>
              <p>One agave only: blue Weber. Made in Jalisco and four bordering states. The agave is steamed in brick ovens or autoclaves, which is why tequila reads clean, peppery, and vegetal rather than smoky.</p>
            </div>
            <div class="pr-item">
              <div class="name">Mezcal</div>
              <p>Thirty-plus agave species, centered on Oaxaca. The agave is roasted in an underground pit over hot rocks and hardwood. That pit is the entire source of the smoke &mdash; nothing is added.</p>
            </div>
            <div class="pr-item">
              <div class="name">The cousins</div>
              <p>Raicilla and bacanora are regional agave spirits under their own rules. Sotol gets shelved next to them but isn't agave at all.</p>
            </div>
          </div>

          <hr class="pr-dash">

          <div class="pr-section">
            <h4>{CO}The Age Ladder</h4>
            <div class="lede">Same spirit, different time in oak. This is the Newbie flight.</div>
            <div class="pr-item">
              <div class="name">Blanco / Plata</div>
              <p>Unaged, or under two months. The clearest read on the agave itself. Pepper, lime, cooked vegetable.</p>
            </div>
            <div class="pr-item">
              <div class="name">Reposado</div>
              <p>"Rested" two to twelve months. Oak rounds off the pepper and brings in vanilla and caramel.</p>
            </div>
            <div class="pr-item">
              <div class="name">A&ntilde;ejo</div>
              <p>One to three years. Darker and rounder. This is the one whisky drinkers convert on.</p>
            </div>
            <div class="pr-item">
              <div class="name">Extra A&ntilde;ejo</div>
              <p>Three years and up. Dessert territory, and the point where you start paying for the barrel more than the plant.</p>
            </div>
          </div>
        </div>

        <div>
          <div class="pr-section">
            <h4>From Plant to Bottle</h4>
            <div class="pr-timeline">
              <div class="pr-step">
                <div class="name">Jima</div>
                <p>A jimador strips the leaves with a coa, leaving the pi&ntilde;a &mdash; the heart. Blue Weber needs six to eight years. Wild agaves can need twenty-five.</p>
              </div>
              <div class="pr-step">
                <div class="name">Cooking</div>
                <p>Steamed in ovens, or roasted in an earth pit. Starch becomes sugar here, and this single step is the biggest fork in the whole flavor road.</p>
              </div>
              <div class="pr-step">
                <div class="name">Crushing</div>
                <p>A roller mill, a tahona stone wheel, or a wooden mallet by hand. Tahona-crushed spirits carry noticeably more texture.</p>
              </div>
              <div class="pr-step">
                <div class="name">Fermentation</div>
                <p>Open-air vats, often on wild yeast that drifts in. Days, not hours.</p>
              </div>
              <div class="pr-step">
                <div class="name">Distillation</div>
                <p>Usually twice. Copper pot stills for tequila; traditional mezcal often runs through clay.</p>
              </div>
            </div>
          </div>

          <div class="pr-warn">
            <h5>READ THE LABEL</h5>
            <p><b>"100% de Agave."</b> If the bottle doesn't say it, it's a mixto &mdash; up to 49% cane sugar. That is the source of nearly every bad tequila story anyone tells.</p>
            <p><b>NOM number.</b> Identifies the distillery. Two brands sharing a NOM came out of the same house.</p>
            <p><b>Additive-free.</b> Producers may add glycerin, vanilla, and coloring up to 1% without disclosing it. The best bottles skip it entirely.</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- PIECE 3: AGAVEBASE -->
  <div id="agavebase">
    <div class="sheet-label"><span class="n">03</span><h2>Agavebase</h2><span class="fmt">8.5 &times; 11 in &middot; 1 page</span></div>
    <div class="sheet">
      <div class="pb-head" style="display:flex; justify-content:space-between; align-items:flex-start;">
        <div>
          <div class="eyebrow">Agavebase</div>
          <h3>Pick a Tier, Buy Three Bottles</h3>
          <div class="sub">Every bottle here is widely available and additive-free or close to it.</div>
        </div>
        <span class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></span>
      </div>

      <table class="pairbase">
        <colgroup>
          <col style="width:11%"><col style="width:21%"><col style="width:21%">
          <col style="width:33%"><col style="width:14%">
        </colgroup>
        <thead>
          <tr>
            <th>Tier</th>
            <th>{AG}Tequila</th>
            <th>{CO}Mezcal</th>
            <th>What You'll Taste</th>
            <th>Per Bottle</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><span class="tier-pill newbie">Newbie</span></td>
            <td>Espol&ograve;n Blanco<span class="pb-sub">Olmeca Altos Plata</span><span class="pb-sub">Cimarr&oacute;n Blanco</span></td>
            <td>Del Maguey Vida<span class="pb-sub">the standard first mezcal</span></td>
            <td>Clean cooked agave, white pepper, lime zest. Vida adds a gentle campfire edge without overwhelming anyone.</td>
            <td>$25&ndash;35<span class="pb-sub">~$9 / person</span></td>
          </tr>
          <tr>
            <td><span class="tier-pill casual">Casual</span></td>
            <td>Fortaleza Blanco<span class="pb-sub">Tapat&iacute;o Blanco</span><span class="pb-sub">Siete Leguas &middot; G4</span></td>
            <td>Banhez Espad&iacute;n<span class="pb-sub">Del Maguey Chichicapa</span><span class="pb-sub">Bozal Ensamble</span></td>
            <td>Tahona texture, olive brine, deeper roast, real minerality. This is where people stop thinking of tequila as a shot.</td>
            <td>$45&ndash;70<span class="pb-sub">~$18 / person</span></td>
          </tr>
          <tr>
            <td><span class="tier-pill aficionado">Aficionado</span></td>
            <td>Tequila Ocho<span class="pb-sub">single estate, vintage dated</span><span class="pb-sub">Fortaleza A&ntilde;ejo &middot; El Tesoro</span></td>
            <td>Del Maguey Tobal&aacute;<span class="pb-sub">Rey Campero Tepeztate</span><span class="pb-sub">Mezcal Vago &middot; El Jolgorio</span></td>
            <td>Single-varietal wild agave. Tropical fruit, hard minerality, florals. Plants that grew twenty years before anyone cut them.</td>
            <td>$90&ndash;160<span class="pb-sub">~$38 / person</span></td>
          </tr>
        </tbody>
      </table>

      <div class="pb-note">
        <b>Bottle math.</b> A 750ml bottle pours roughly 25 one-ounce tastes. Three pours each for six guests is 18 ounces total, so <b>one bottle per spirit covers the night with room left over</b>. Buy one tier across three bottles &mdash; not one bottle from each tier.
      </div>

      <div class="pb-note" style="margin-top:12px;">
        <b>Shopping shortcut.</b> If a bottle doesn't say "100% de Agave" on the front, put it back. That one rule filters out most of what goes wrong at this price range.
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
          <h3>Put a Word to It</h3>
          <div class="sub">Start at the center tier, work outward for something more specific.</div>
        </div>
        <span class="kb-badge"><span class="l1">KINGB</span><span class="l2">KITS</span></span>
      </div>

      <div class="fw-pair">
        <figure>
          <svg viewBox="0 0 580 580">{inner(tequila_wheel)}</svg>
          <figcaption>Tequila</figcaption>
        </figure>
        <figure>
          <svg viewBox="0 0 580 580">{inner(mezcal_wheel)}</svg>
          <figcaption>Mezcal</figcaption>
        </figure>
      </div>

      <div class="fw-how"><b>Using the wheels:</b> taste first, then find the inner-ring category that fits, then work outward to the specific note. The two wheels barely overlap on purpose &mdash; that gap is exactly what the fire pit does to the same plant.</div>
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

with open(f"{BASE}/kingbkits-agave-kit.html", "w") as f:
    f.write(css + body)

print("built:", len(css + body), "chars")
