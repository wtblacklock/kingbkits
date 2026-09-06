# Design — KingBKits

A locked design system for this app. Every page redesign reads this file before
emitting code. Extend or amend this file when the system needs to grow; do not
regenerate per page.

## Genre
editorial-playful: bold, exciting, party-planning energy, but set in serif display type
with generous prose rather than boxed SaaS cards. Mobile-first, high-accessibility,
fast-to-convert. This supersedes two earlier phases (a light gold/cream system, then a
dark + bright-yellow studied-DNA system with a monospace label voice) per explicit user
direction, then a follow-up refinement pass: drop all red/coral, don't state the kit
count in copy, make everything but the kit cards feel more editorial, move the marquee
banner above the nav, and swap the favicon for a text mark.

## Route
custom, complete redo, no external reference site. Built against one brief: **sell Etsy
listings fast**, on mobile, to someone who doesn't yet know they want a printable party
kit until the headline names their exact problem. Every section either builds desire
(hero photo, kit gallery, pull quote) or removes a purchase objection (value props, FAQ)
on the way to an Etsy click.

## Theme — light palette (OKLCH)

Anchor hue: **~85-87° (warm neutral)** for paper/ink, **106° (bright yellow)** for the
one accent (`#fff200`, the real printed brand yellow). **No red or coral anywhere** on
the site, including the wordmark; an earlier pass had a coral secondary accent and it's
gone, tokens and all.

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
- `--color-focus`        oklch(15% 0.010 85)    /* ink-black focus ring, visible on light paper */

**Tier system** (unrelated to the accent, kept exact, printed on real products):
- `--color-tier-newbie`      oklch(76.8% 0.196 130.6)  /* #87cb28 */
- `--color-tier-casual`      oklch(96.8% 0.211 109.8)  /* #ffff00 */
- `--color-tier-aficionado`  oklch(87.8% 0.169 91.9)   /* #ffd230 */

**Rule:** pure yellow (`--color-accent`) is a fill/badge color only (always paired with dark
text on top). For yellow used as text or a link color on the light paper, use
`--color-accent-text` (a darkened gold) so contrast actually holds up.

## Typography

- **Display (page headlines, h1/h2 everywhere):** Fraunces, weights 400/500/600, roman for
  section heads, **italic for statement-style headlines and pull quotes only** (the About
  page opener, the homepage pull-quote block) — a deliberate, consistent editorial device,
  not a single italicized word inside an otherwise-roman heading.
- **Wordmark + marquee only:** Archivo Black, weight 400, roman. Reserved for the logotype
  and the top marquee band so the "logo" reads as a distinct mark from body headlines. Not
  used for page content headings anymore (that's Fraunces' job).
- **Body:** Raleway, weights 300-700.
- No monospace label voice. No third face beyond the three above.
- **No logo image anywhere**, including the favicon. The wordmark is pure type, one solid
  word: "KingBKits" in Archivo Black, no space, no crown icon, no separate chip. "Kits"
  carries an animated yellow highlighter underline (`components/Badge.tsx` +
  `.wordmark__kits` in `globals.css`) that draws in left-to-right on mount instead of
  sitting there static, so the mark reads as one unit, not two stacked pieces. No coral,
  no colored letters. The favicon is a bold yellow "B" on a near-black square
  (`app/icon.png` / `app/apple-icon.png`), replacing the bee mark entirely, generated the
  same way as the rest of the type system (Archivo Black, rendered via headless Chrome,
  not a redrawn icon).

## Imagery
- **Kit/offering imagery**: the real Etsy listing images (hero + page-fan composites),
  used as-is. They're dark, richly composed product photography; on the light page they
  read as intentional contrast (dark product shot floating on a white/cream page).
- **Lifestyle/mood imagery**: sourced from Unsplash (`images.unsplash.com`, allowed via
  `next.config.mjs` remotePatterns), used for the homepage hero. Real photography, not
  fabricated.
- Never fabricate stock-photo-style content, invented metrics, or testimonials.

## Layout & structure
- **Marquee banner**: lives above `<SiteHeader>` at the very top of every page (in
  `app/layout.tsx`, via `components/MarqueeBar.tsx`), not in the footer anymore. Scrolls
  away with the page; the sticky nav takes over below it.
- **Home**: photo-led hero (headline + CTA left, Unsplash lifestyle photo right, stacks on
  mobile) → editorial value-prop row (typographic, no card borders, split by a rule not a
  box) → pull-quote statement section (real brand copy: "Party planning is the part people
  skip.") → kit gallery (Bento grid, kept exactly as the user asked, all kits shown, no
  "how many kits" copy anywhere) → FAQ (native `<details>`, feeds `FAQPage` JSON-LD) →
  final CTA: full-bleed accent-yellow band (not a boxed rounded card), a real "Shop all
  kits on Etsy" `EtsyButton`, full-opacity text throughout.
- **Kit detail**: headline + CTA left, the kit's own Etsy hero image shown whole
  (`object-contain`, never cropped) → Bento stats/included grid → "Pick your tier" as a
  short paragraph, not a table (the full per-tier shopping chart is paid content inside
  the PDF, not given away on the marketing page) → "Inside the PDF" gallery (cropped in
  tight via `scale-[1.35] object-cover object-top` and right-click/drag disabled via
  `components/ProtectedGalleryImage.tsx` — a deterrent against casual image theft, not
  DRM) → how-it-works (step numbers as filled yellow circles with dark ink text, never
  yellow text directly on paper — fails contrast) → final CTA.
- **About**: restructured editorially (What we do / What we don't do / How we build it /
  How we make money / Who's behind it), modeled on the same honest, structured voice used
  on the operator's other sites (wblacklock.com, trailsteadguide.com) rather than a single
  paragraph.
- **Guides**: now spans two kinds of content: per-spirit primers (unchanged) plus a new
  "Party Planning" topic covering logistics that apply across every kit: pour math, tasting
  station setup, running a blind tasting, and printable invitations.
- Mobile-first: nav collapses to a hamburger sheet under `sm:`; kit-card images use a fixed
  `aspect-[4/3]` below `sm:` (they collapsed to zero height before, since they depended on a
  `sm:`-only grid row height that doesn't exist on a single-column mobile grid).

## Motion
- Easings: `--ease-out: cubic-bezier(0.16, 1, 0.3, 1)`.
- **Scroll-triggered section reveals**, sitewide: every major section on every page
  (home, kit detail, about, guides index, guide detail) is wrapped in
  `components/Reveal.tsx`, a client component that fades + rises a section in once
  (`IntersectionObserver`, 12% threshold, disconnects after first fire) via the `.reveal`
  / `.reveal.is-visible` classes in `globals.css`. Repeated elements (value props, kit
  cards, topic groups) stagger with a `delay` prop. Honors
  `prefers-reduced-motion: reduce` (shows content at full opacity, no transition).
- The wordmark's yellow underline animates in on mount (`wordmark-underline` keyframe,
  background-size 0%→100%), also reduced-motion-aware.
- The marquee is the only continuous, looping motion and also honors
  `prefers-reduced-motion: reduce`.
- FAQ disclosure uses the native `<details>` toggle, no JS animation.

## CTA voice
- Primary CTA ("Buy on Etsy" / "Shop all kits on Etsy"): filled black pill, turns yellow on
  hover, direct verb copy.
- Secondary CTA: outlined black pill.
- Never state the total kit count in marketing copy ("See the kits", not "See the 4 kits").
- Never reduce opacity on CTA-band body text below `/80`; body copy on a solid band stays
  at least at 80% of the heading's contrast (paper-on-ink, ink-on-paper, or
  accent-ink-on-accent).
- Never a boxed button inside Long Document prose; use an underlined text link there instead.

## Copy discipline
No em dashes anywhere on the site (explicit standing rule). Use a period, colon, comma, or a
restructured sentence. Don't state the number of kits in copy (kits get added over time; the
gallery speaks for itself).

## Accessibility & mobile non-negotiables
- Hamburger nav on mobile with a real toggle button (`aria-expanded`, `aria-label`), not a
  hover-only menu.
- Focus rings always visible, ink-black, never transitioned.
- No horizontal scroll except an intentionally-scrollable table (the tier chart).
- Card images never depend on a breakpoint-scoped ancestor height; use `aspect-*` so they
  render correctly with no JS and no matching breakpoint upstream.

## What pages MUST share
- The wordmark type treatment: one solid word "KingBKits" in Archivo Black, animated
  yellow underline on "Kits", no crown icon, no separate chip, no other color.
- The accent yellow, fills/badges only, never as body text color.
- Fraunces (display) + Raleway (body) + Archivo Black (wordmark/marquee only).
- No em dashes. No kit-count statements.

## What pages MAY differ on
- Hero composition: home uses a photo; kit pages use the kit's own product image.
- Enrichment: guides keep their existing real-asset imagery (flavor-wheel crops, kit
  previews) plus small hand-built SVG diagrams. No fabricated stock photography anywhere.

## Superseded
Three earlier system revisions are fully replaced, not just the palette:
1. The original light gold/cream "custom (tuned)" system.
2. A dark + bright-yellow system with a monospace label voice studied from an external
   reference site (usehallmark.com).
3. A light + yellow + **coral** system with Archivo Black on every headline and the
   marquee in the footer. The coral accent, the footer marquee placement, and the
   all-Archivo-Black type scale are all gone; this file describes what actually ships now.
