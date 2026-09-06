# Design — KingBKits

A locked design system for this app. Every page redesign reads this file before
emitting code. Extend or amend this file when the system needs to grow; do not
regenerate per page.

## Genre
playful (bold end of the register: mono labels, pill buttons, badge energy, not soft pastel onboarding)

## Route
studied-DNA (source: url, https://www.usehallmark.com/) — structure adopted, palette overridden
with the brand's own colors per explicit user instruction ("adopt the structure, keep our own
colors"). The studied page supplied the macrostructure family, hero archetype, nav/footer
archetypes, type-pairing logic (display+body family plus a distinct mono label face), and pill/
hairline component language. The paper, ink, and accent values below are **not** from the studied
source — they come from the same dark + bright-yellow identity already shipped across every Etsy
listing image, itself anchored on the real crowned-bee logo and its printed yellow (`#fff200`).

Prior system (superseded 2026-09): a light cream/gold custom palette anchored on `#f3c318`. That
palette is gone site-wide, not just on hero sections — see Theme below.

## Macrostructure family
- Marketing pages (home, 4 kit pages): **Bento Grid** for the kit gallery and stat/included-item
  blocks — unchanged, the user explicitly asked to keep the gallery layout as-is.
- Home hero: **H2 Split Diptych** (studied from usehallmark.com's hero) — eyebrow + display
  headline + lede + CTAs on the left, a hand-built `aria-hidden` decorative shape cluster (Tier A
  pure CSS art: blob, ring, pill, dot, the real logo mark) on the right. Replaces the old centered
  typographic hero — centered-symmetric hero is the anti-pattern the split fixes.
- Kit detail hero: **H6 Photographic Fold**, unchanged in archetype, but the hero image is now
  pure atmosphere (background gradient + accent glow + logo badge, no baked-in text, no product
  pages) because the section overlays its own heading/CTA on top — baking text into the image
  duplicated it. A separate `images.card` asset (same background, WITH the fanned product pages,
  no text) feeds the homepage gallery cards instead, since that context has no overlaid heading to
  collide with.
- Content pages (guides index + detail, about): **Long Document** — unchanged.

## Theme — dark palette (OKLCH), our own colors on the studied structure

Anchor hue: **~85-87° (warm neutral)** for surfaces/text, **106° (bright yellow)** for the accent —
taken directly from the brand mark's printed yellow `#fff200`.

- `--color-paper`      oklch(15% 0.008 85)
- `--color-paper-2`    oklch(19% 0.010 85)
- `--color-paper-3`    oklch(24% 0.012 85)
- `--color-ink`         oklch(95% 0.013 87)
- `--color-ink-2`       oklch(76% 0.024 87)
- `--color-ink-faint`   oklch(56% 0.018 87)
- `--color-rule`        oklch(30% 0.014 85)
- `--color-accent`      oklch(94% 0.200 106)   /* brand yellow, #fff200 */
- `--color-accent-ink`  oklch(15% 0.008 85)
- `--color-focus`       oklch(94% 0.200 106)

**Documented exception:** none anymore — the real logo image now renders everywhere (nav, footer,
favicon), replacing the old placeholder text badge and its "stays literal #000" carve-out.

**Tier system** (unrelated to the accent, kept exact, printed on real products):
- `--color-tier-newbie`      oklch(76.8% 0.196 130.6)  /* #87cb28 */
- `--color-tier-casual`      oklch(96.8% 0.211 109.8)  /* #ffff00 */
- `--color-tier-aficionado`  oklch(87.8% 0.169 91.9)   /* #ffd230 */

**Diversification axes:** dark / roman-serif-display+mono-label / chromatic-yellow (~106°)

## Typography

- Display: **Fraunces**, weights 500/600, roman only — matches the Etsy listing redesign's
  headline face.
- Body: **Raleway**, weights 300-700 — unchanged, real shipped brand choice across every physical
  product and Etsy listing.
- Label role (new, studied from usehallmark.com): **JetBrains Mono**, weights 400/500 — nav links,
  hero eyebrow, footer nav/copyright, the Shop pill. This is the type-pairing DNA adopted from the
  study: a distinct monospace voice for labels/chips/nav, separate from the display+body pairing.
- Type scale anchor: `--text-display: clamp(2.75rem, 5vw + 1rem, 5.25rem)`

## Spacing
4-point named scale (`--space-3xs` through `--space-3xl`), values in `tokens.css`. Pages use named
tokens only, never raw pixel values.

## Motion
- Easings: `--ease-out: cubic-bezier(0.16, 1, 0.3, 1)`
- Reveal pattern: none by default. One optional one-shot fade on Bento tile entry, never a
  scroll-triggered fade on every section.
- Marquee footer honors `prefers-reduced-motion: reduce` (animation removed entirely).
- Reduced-motion fallback everywhere else: opacity-only, at most 150ms.

## Microinteractions stance
- Silent success, no celebratory toasts.
- Hover delay 800ms, focus delay 0ms on any tooltip.
- Card hover: a 1px lift plus border color shift, nothing else.
- Focus rings appear instantly, never transitioned.

## CTA voice
- Primary CTA (Etsy buy buttons): filled pill, brand yellow, direct verb copy ("Buy on Etsy", never "Click here" or "Learn more").
- Secondary CTA: outlined pill, same shape family.
- Long Document (guides/about) CTAs: typographic link inside the paragraph flow (C3), never a boxed button mid-paragraph.

## Copy discipline (site-specific override)
Hallmark's own copy.md defaults to em dashes for interruption. This project overrides that
default at the user's explicit request: **no em dashes anywhere on the site.** Use a period, a
colon, a comma, or a restructured sentence instead. This override applies to every page, every
data file, and every guide.

## Nav / footer (shared across every page)
- Nav: **sticky translucent masthead** (studied from usehallmark.com) — `bg-paper/90 backdrop-blur`,
  hairline bottom border, mono-label nav links, a filled yellow pill CTA. Replaces the old N7 Brutal
  slab (heavy border, filled-black CTA) — the old pattern doesn't carry over well onto a dark
  surface where the "slab" contrast device stops reading as bold and just reads as heavy.
- Footer: **Ft8 Marquee scroll** kept (the scrolling tagline band), with a studied colophon touch
  added underneath: mono-label nav links and a "Back to top" link alongside the copyright line,
  echoing usehallmark.com's dense colophon footer without fully replacing the marquee.

## What pages MUST share
- The real logo image (nav, footer, homepage hero shape cluster, favicon).
- The accent yellow and its restrained placement (CTAs, focus rings, small accents, never a large fill).
- Fraunces + Raleway + JetBrains Mono (labels only).
- The nav and footer archetypes above.
- No em dashes.

## What pages MAY differ on
- Macrostructure within their family (a kit page could vary its Bento tile arrangement from another kit page; both stay Bento).
- Hero archetype: kit pages use H6 Photographic Fold (pure atmosphere, no baked text). Home uses the H2 Split hero with the CSS shape cluster.
- Enrichment: guides get real-asset imagery (existing flavor-wheel crops, kit preview shots) plus small hand-built SVG diagrams where they clarify something. No fabricated stock photography anywhere.

## Per-page allowances
- Marketing pages (Bento family) MAY use photographic enrichment and the stat-strip archetype.
- Content pages (Long Document family) stay typography-plus-real-imagery only. No enrichment tiers beyond that.
