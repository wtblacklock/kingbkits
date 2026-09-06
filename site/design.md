# Design — KingBKits

A locked design system for this app. Every page redesign reads this file before
emitting code. Extend or amend this file when the system needs to grow; do not
regenerate per page.

## Genre
playful (bold, exciting, party-planning energy) — mobile-first, high-accessibility,
fast-to-convert. This supersedes two earlier phases (a light gold/cream system, then a
dark + bright-yellow studied-DNA system) per explicit user direction: "the dark isn't
working... ignore my hallmark example and just have fun... reimagine this whole site."

## Route
custom, complete redo — no external reference site, no studied macrostructure. Built from
first principles against one brief: **sell Etsy listings fast**, on mobile, to someone who
doesn't yet know they want a printable party kit until the headline names their exact
problem. Every section exists to either build desire (hero photo, kit gallery) or remove a
purchase objection (value props, FAQ) on the way to an Etsy click.

## Theme — light palette (OKLCH)

Anchor hue: **~85-87° (warm neutral)** for paper/ink, **106° (bright yellow)** for the
primary accent (`#fff200`, the real printed brand yellow), **~30-34° (coral)** for a second,
more energetic accent used sparingly.

- `--color-paper`       oklch(99.4% 0.008 91.5)  /* warm near-white, not stark #fff, not beige */
- `--color-paper-2`     oklch(96.5% 0.013 87)
- `--color-paper-3`     oklch(93.2% 0.023 87)
- `--color-ink`          oklch(15% 0.010 85)
- `--color-ink-2`        oklch(35% 0.010 85)
- `--color-ink-faint`    oklch(55% 0.010 85)
- `--color-rule`         oklch(88% 0.012 85)
- `--color-accent`       oklch(94% 0.200 106)   /* brand yellow, #fff200 - fills/badges only */
- `--color-accent-ink`   oklch(15% 0.010 85)    /* text ON accent fills */
- `--color-accent-text`  oklch(54.8% 0.112 90.2) /* darkened gold, for yellow-as-text on paper */
- `--color-pop`          oklch(68.5% 0.204 30.3) /* coral - secondary energy accent, sparingly */
- `--color-pop-dark`     oklch(62.4% 0.205 34.2)
- `--color-focus`        oklch(62.4% 0.205 34.2) /* coral focus ring - visible on light paper */

**Tier system** (unrelated to the accent, kept exact, printed on real products):
- `--color-tier-newbie`      oklch(76.8% 0.196 130.6)  /* #87cb28 */
- `--color-tier-casual`      oklch(96.8% 0.211 109.8)  /* #ffff00 */
- `--color-tier-aficionado`  oklch(87.8% 0.169 91.9)   /* #ffd230 */

**Rule:** pure yellow (`--color-accent`) is a fill/badge color only (always paired with dark
text on top). For yellow used as text or a link color on the light paper, use
`--color-accent-text` (a darkened gold) so contrast actually holds up.

## Typography

- Display + wordmark: **Archivo Black**, weight 400, roman only. The real, already-printed
  brand face across every physical product; also the site's logotype ("KingB Kits" set in
  Archivo Black, "B" in coral, "Kits" on a rotated yellow highlighter chip).
- Body: **Raleway**, weights 300-700.
- No third face. No monospace label voice — that was a studied-DNA device from a discarded
  direction and doesn't fit a "have fun, exciting" party brand.
- No logo image anywhere on the site. The mascot (crowned bee) didn't read at web sizes /
  in this context; a hand-drawn SVG crown accent stands in for it next to the wordmark. The
  bee mark still lives on the favicon only, where a tiny simplified mark works fine.

## Imagery
- **Kit/offering imagery**: the real Etsy listing images (hero + page-fan composites),
  used as-is. They're dark, richly composed product photography; on the new light page they
  read as intentional contrast (dark product shot floating on a white/cream page), not as
  leftover dark-theme styling.
- **Lifestyle/mood imagery**: sourced from Unsplash (`images.unsplash.com`, allowed via
  `next.config.mjs` remotePatterns), used for the homepage hero and any future mood sections.
  Real photography, not fabricated. Attribution isn't required for Unsplash's license but
  credit the photographer in a code comment near the URL if one is ever added to a new spot.
- Never fabricate stock-photo-style content or invented metrics/testimonials.

## Layout & structure
- **Home**: photo-led hero (headline + CTA left, Unsplash lifestyle photo right, stacks on
  mobile) → value-prop strip (3 cards) → kit gallery (Bento grid, kept exactly as the user
  asked) → FAQ (native `<details>`, also feeds `FAQPage` JSON-LD) → final CTA band.
- **Kit detail**: headline + CTA left, the kit's own Etsy hero image shown whole
  (`object-contain`, never cropped, since it's already a finished product photo) → Bento
  stats/included grid → tier table → "Inside the PDF" gallery → how-it-works → final CTA.
- **Content pages** (guides, about): unchanged Long Document prose layout, recolored.
- Mobile-first: nav collapses to a hamburger sheet under `sm:`; kit-card images use a fixed
  `aspect-[4/3]` below `sm:` (they collapsed to zero height before, since they depended on a
  `sm:`-only grid row height that doesn't exist on a single-column mobile grid).

## Motion
- Easings: `--ease-out: cubic-bezier(0.16, 1, 0.3, 1)`.
- No scroll-triggered reveals. The footer marquee is the only continuous motion and honors
  `prefers-reduced-motion: reduce`.
- FAQ disclosure uses the native `<details>` toggle, no JS animation.

## CTA voice
- Primary CTA ("Buy on Etsy" / "Shop all kits on Etsy"): filled black pill, turns yellow on
  hover, direct verb copy.
- Secondary CTA: outlined black pill.
- Never a boxed button inside Long Document prose; use an underlined text link there instead.

## Copy discipline
No em dashes anywhere on the site (explicit standing rule). Use a period, colon, comma, or a
restructured sentence.

## Accessibility & mobile non-negotiables
- Hamburger nav on mobile with a real toggle button (`aria-expanded`, `aria-label`), not a
  hover-only menu.
- Focus rings always visible, coral, never transitioned.
- No horizontal scroll except an intentionally-scrollable table (the tier chart).
- Card images never depend on a breakpoint-scoped ancestor height; use `aspect-*` so they
  render correctly with no JS and no matching breakpoint upstream.

## What pages MUST share
- The wordmark type treatment (Archivo Black + coral "B" + yellow "Kits" chip + SVG crown).
- The accent yellow (fills/badges only) and the coral secondary accent (sparing use: focus
  rings, one highlight per section at most).
- Archivo Black + Raleway, nothing else.
- No em dashes.

## What pages MAY differ on
- Hero composition: home uses a photo; kit pages use the kit's own product image.
- Enrichment: guides keep their existing real-asset imagery (flavor-wheel crops, kit
  previews) plus small hand-built SVG diagrams. No fabricated stock photography anywhere.

## Superseded
Two earlier system revisions are fully replaced, not just the palette:
1. The original light gold/cream "custom (tuned)" system.
2. A dark + bright-yellow system with a monospace label voice studied from an external
   reference site (usehallmark.com). Both are gone site-wide; this file describes what
   actually ships now.
