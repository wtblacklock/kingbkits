# Design — KingBKits

A locked design system for this app. Every page redesign reads this file before
emitting code. Extend or amend this file when the system needs to grow; do not
regenerate per page.

## Genre
playful (bold end of the register: heavy uppercase nav, badge energy, not soft pastel onboarding)

## Route
custom (tuned) — anchored on the real, already-printed brand rather than an invented vibe. The
gold, black, and cream come from the KingBKits wordmark badge and the new crowned-bee-in-mask
mascot, already shipped across dozens of real Etsy product PDFs. The tier colors (Newbie green,
Casual yellow, Aficionado gold) are preserved exactly as-is, they are printed on real products and
must match across every channel.

## Macrostructure family
- Marketing pages (home, 4 kit pages): **Bento Grid** — modular blocks of varying size. Fits
  stat rows, included-item lists, tier tables, and galleries far better than stacked full-width
  sections.
- Content pages (guides index + detail, about): **Long Document** — continuous prose with inline
  section heads. The guides already read like reference essays; this macrostructure stops fighting
  that instead of forcing marketing-page furniture onto them.

## Theme — custom palette (OKLCH)

Anchor hue: **90° (gold)**, taken directly from the brand mark `#f3c318`.

- `--color-paper`      oklch(97% 0.010 88)
- `--color-paper-2`    oklch(94% 0.012 88)
- `--color-paper-3`    oklch(90% 0.014 88)
- `--color-ink`         oklch(18% 0.010 88)
- `--color-ink-2`       oklch(38% 0.008 88)
- `--color-ink-faint`   oklch(56% 0.008 88)
- `--color-rule`        oklch(84% 0.012 88)
- `--color-accent`      oklch(84% 0.167 90)   /* brand gold, #f3c318 */
- `--color-accent-ink`  oklch(18% 0.010 88)
- `--color-focus`       oklch(78% 0.200 90)

**Documented exception:** the KINGBKITS wordmark badge chip stays literal `#000` / pure black, not
the tinted ink token. It is a fixed, already-printed brand mark (matches the physical Etsy
products and the new logo's linework); tinting it would make the site badge mismatch every
printed and Etsy-listed version of the same mark.

**Tier system** (unrelated to the accent, kept exact, printed on real products):
- `--color-tier-newbie`      oklch(76.8% 0.196 130.6)  /* #87cb28 */
- `--color-tier-casual`      oklch(96.8% 0.211 109.8)  /* #ffff00 */
- `--color-tier-aficionado`  oklch(87.8% 0.169 91.9)   /* #ffd230 */

**Diversification axes:** light / display-heavy / chromatic-gold (~90°)

## Typography

- Display: **Archivo Black**, weight 400 (single-weight black face), roman only
- Body: **Raleway**, weights 300/400/500/600/700
- Documented exception: Raleway sits on Hallmark's generic banned-defaults list. It is kept anyway
  because it is a real, deliberate, already-shipped brand choice across every physical product and
  Etsy listing, not a lazy model default. Switching it here would break brand consistency between
  the site and the product line for no real gain.
- No outlier third face. The badge/wordmark carries its own register already (Archivo Black); a
  mono or serif outlier would be a fourth voice for no reason.
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
- Primary CTA (Etsy buy buttons): filled black pill, gold hover state, direct verb copy ("Buy on Etsy", never "Click here" or "Learn more").
- Secondary CTA: outlined pill, same shape family.
- Long Document (guides/about) CTAs: typographic link inside the paragraph flow (C3), never a boxed button mid-paragraph.

## Copy discipline (site-specific override)
Hallmark's own copy.md defaults to em dashes for interruption. This project overrides that
default at the user's explicit request: **no em dashes anywhere on the site.** Use a period, a
colon, a comma, or a restructured sentence instead. This override applies to every page, every
data file, and every guide.

## Nav / footer (shared across every page)
- Nav: **N7 Brutal slab** — heavy uppercase wordmark, 2px border-bottom, tracked uppercase links, filled CTA. Matches the mascot's bold badge energy better than a soft floating pill.
- Footer: **Ft8 Marquee scroll** — a moving brand tagline band, honoring reduced-motion, with a slim functional link row underneath it so kit/guide navigation still works. This also fixes the outgoing footer, which was a textbook Ft3 four-column AI-footer pattern.

## What pages MUST share
- The wordmark/logo (once the real asset lands, currently a placeholder text badge).
- The accent gold and its restrained placement (CTAs, focus rings, small accents, never a large fill).
- Archivo Black + Raleway.
- The nav and footer archetypes above.
- No em dashes.

## What pages MAY differ on
- Macrostructure within their family (a kit page could vary its Bento tile arrangement from another kit page; both stay Bento).
- Hero archetype: kit pages use **H6 Photographic Fold** (real owned product photography, full-bleed). Home uses a typographic Bento hero, no photograph, since there's no single product to lead with.
- Enrichment: guides get real-asset imagery (existing flavor-wheel crops, kit preview shots) plus small hand-built SVG diagrams where they clarify something. No fabricated stock photography anywhere.

## Per-page allowances
- Marketing pages (Bento family) MAY use photographic enrichment and the stat-strip archetype.
- Content pages (Long Document family) stay typography-plus-real-imagery only. No enrichment tiers beyond that.

## Pending
- Real logo asset (crowned bee in mask, black/white/gold) not yet attached to the session. Site
  ships with the existing text badge as a placeholder until the file is provided, then every nav,
  footer, and favicon usage gets swapped in one pass.
