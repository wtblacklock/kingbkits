export interface KitStat {
  value: string;
  label: string;
}

export interface KitIncludedItem {
  number: string;
  title: string;
  description: string;
}

export interface KitStep {
  title: string;
  description: string;
}

export type TierName = "Newbie" | "Casual" | "Aficionado";

export interface KitTierRow {
  tier: TierName;
  tierClass: "newbie" | "casual" | "aficionado";
  flightName?: string;
  primaryPicks: string[];
  secondaryPicks?: string[];
  notes: string;
  cost?: string;
}

export interface KitGalleryImage {
  src: string;
  label: string;
}

export interface Kit {
  slug: string;
  name: string;
  subtitle: string;
  shortDescription: string;
  pageCount: number;
  heroHeadline: string;
  heroBody: string;
  stats: KitStat[];
  included: KitIncludedItem[];
  tiers?: KitTierRow[];
  tierLabels?: { primary: string; secondary?: string };
  compatibleWith?: string[];
  howItWorks: KitStep[];
  images: {
    hero: string;
    heroGif?: string;
    card: string;
    gallery: KitGalleryImage[];
  };
  seasonalNote?: string;
  /** Set to override the shop-wide Etsy URL once this kit has its own listing. */
  etsyUrl?: string;
}

export const KITS: Kit[] = [
  {
    slug: "cigar-whisky",
    etsyUrl: "https://kingbkits.etsy.com/listing/4566632986",
    name: "Cigar & Whisky Journey",
    subtitle: "Pairing Party Kit",
    shortDescription:
      "Printable event planning kit: guide, primer, pairing chart, and tier cards.",
    pageCount: 8,
    heroHeadline: "One Cigar. Three Whiskies. Zero Guesswork.",
    heroBody:
      "Most kits have you smoking three full cigars in one night. This one doesn't. Pick one cigar for the evening and taste three whisky pours against it as the flavor shifts through its three thirds. Realistic, affordable, and exactly how aficionados actually do it.",
    stats: [
      { value: "17", label: "curated pairings" },
      { value: "3", label: "experience tiers" },
      { value: "1", label: "bottle per tier, easily covers 6 guests" },
    ],
    included: [
      { number: "01", title: "Party Guide", description: "Setup, timing, supplies: realistic for one cigar per guest, not three." },
      { number: "02", title: "Cigar & Whisky Primer", description: "Wrapper types, whisky styles, and the leaf-to-ash process." },
      { number: "03", title: "Pairbase Chart", description: "17 curated pairings across all three tiers, with real cost math." },
      { number: "04", title: "Flavor Wheels", description: "Dual cigar & whisky wheels to build real tasting vocabulary." },
      { number: "05–07", title: "Pairing Cards", description: "One full-page tracking card per tier: Newbie, Casual, Aficionado." },
      { number: "08", title: "Checklist & Scorecard", description: "Shopping checklist and a scorecard to close out the night." },
    ],
    tierLabels: { primary: "Cigar", secondary: "Whisky" },
    tiers: [
      {
        tier: "Newbie",
        tierClass: "newbie",
        primaryPicks: ["Macanudo Café", "Ashton Classic", "Romeo y Julieta 1875", "Arturo Fuente Chateau Fuente"],
        secondaryPicks: ["Jameson", "Buffalo Trace", "Four Roses Yellow Label", "Evan Williams Black"],
        notes: "Creamy, vanilla, light spice, subtle wood.",
        cost: "$8–12 / cigar · $25–35 / bottle",
      },
      {
        tier: "Casual",
        tierClass: "casual",
        primaryPicks: ["Padrón 3000", "Camacho Ecuador", "Rocky Patel Vintage 1990", "Arturo Fuente Hemingway"],
        secondaryPicks: ["Glenlivet 12", "Woodford Reserve", "Glenfiddich 12", "Four Roses Small Batch"],
        notes: "Honey, oak, caramel, light dried fruit.",
        cost: "$10–16 / cigar · $35–55 / bottle",
      },
      {
        tier: "Aficionado",
        tierClass: "aficionado",
        primaryPicks: ["Padrón 1964 Maduro", "My Father Le Bijou 1922", "Liga Privada No. 9", "Oliva Serie V Maduro"],
        secondaryPicks: ["Laphroaig 10", "Ardbeg 10", "Lagavulin 16", "Wild Turkey Rare Breed"],
        notes: "Smoke, leather, dark fruit, black pepper.",
        cost: "$14–22 / cigar · $50–80+ / bottle",
      },
    ],
    howItWorks: [
      { title: "Purchase & Download", description: "Instant access to the full PDF, plus your editable Canva invitation template." },
      { title: "Print at Home or a Shop", description: "Staples, FedEx, or a service like Printify, or just use your own printer." },
      { title: "Pick Your Tier", description: "Newbie, Casual, or Aficionado: the Pairbase chart tells you what to buy." },
      { title: "Host Tonight", description: "Everything's ready. No physical items ship. This is an all-digital product." },
    ],
    images: {
      hero: "/kits/cigar/hero.png",
      card: "/kits/cigar/card.png",
      heroGif: "/kits/cigar/hero.gif",
      gallery: [
        { src: "/kits/cigar/preview-guide.png", label: "Party Guide" },
        { src: "/kits/cigar/preview-primer.png", label: "Cigar & Whisky Primer" },
        { src: "/kits/cigar/preview-pairbase.png", label: "Pairbase Chart" },
        { src: "/kits/cigar/preview-wheels.png", label: "Flavor Wheels" },
        { src: "/kits/cigar/preview-cards.png", label: "Pairing Cards" },
      ],
    },
  },
  {
    slug: "tequila-mezcal",
    etsyUrl: "https://kingbkits.etsy.com/listing/4566840538",
    name: "Tequila & Mezcal",
    subtitle: "Tasting Party Kit",
    shortDescription:
      "Printable tasting kit: guide, primer, bottle chart, flavor wheels, and tier cards.",
    pageCount: 8,
    heroHeadline: "Sip It. Don't Shoot It.",
    heroBody:
      "The lime and salt ritual exists to hide cheap mixto tequila. Good agave doesn't need hiding. This kit walks your table through three one-ounce pours, teaches the one label rule that filters out most bad bottles, and gives everyone the words for what they're actually tasting.",
    stats: [
      { value: "3", label: "experience tiers" },
      { value: "3", label: "bottles covers 6 guests" },
      { value: "2", label: "flavor wheels, tequila & mezcal" },
    ],
    included: [
      { number: "01", title: "Party Guide", description: "Setup, timing, supplies, and why the lime and salt stay in the kitchen." },
      { number: "02", title: "Tequila & Mezcal Primer", description: "Blue Weber vs wild agave, the age ladder, and how to read a label." },
      { number: "03", title: "Agavebase Chart", description: "Real bottles at three budgets, with per-person cost math." },
      { number: "04", title: "Flavor Wheels", description: "Separate tequila and mezcal wheels to build tasting vocabulary." },
      { number: "05–07", title: "Tasting Cards", description: "The Age Ladder, Tequila Meets Mezcal, and Agave Terroir flights." },
      { number: "08", title: "Checklist & Scorecard", description: "Shopping checklist and a scorecard to close out the night." },
    ],
    tierLabels: { primary: "Tequila", secondary: "Mezcal" },
    tiers: [
      {
        tier: "Newbie",
        tierClass: "newbie",
        flightName: "The Age Ladder",
        primaryPicks: ["Espolòn Blanco", "Olmeca Altos Plata", "Cimarrón Blanco", "Milagro Silver"],
        secondaryPicks: ["Del Maguey Vida", "Montelobos Espadín", "400 Conejos Espadín"],
        notes: "Clean cooked agave, white pepper, lime zest. The mezcal picks add a gentle campfire edge without overwhelming anyone.",
        cost: "$25–35 / bottle · ~$9 / person",
      },
      {
        tier: "Casual",
        tierClass: "casual",
        flightName: "Tequila Meets Mezcal",
        primaryPicks: ["Fortaleza Blanco", "Tapatío Blanco", "Siete Leguas Blanco", "G4 Blanco"],
        secondaryPicks: ["Banhez Espadín", "Del Maguey Chichicapa", "Bozal Ensamble", "Real de Xalisco"],
        notes: "Tahona texture, olive brine, deeper roast, real minerality. This is where people stop thinking of tequila as a shot.",
        cost: "$45–70 / bottle · ~$18 / person",
      },
      {
        tier: "Aficionado",
        tierClass: "aficionado",
        flightName: "Agave Terroir",
        primaryPicks: ["Tequila Ocho Plata", "Fortaleza Añejo", "El Tesoro Añejo", "Siete Leguas D'Antano"],
        secondaryPicks: ["Del Maguey Tobalá", "Rey Campero Tepeztate", "Mezcal Vago Elote", "El Jolgorio Madrecuixe"],
        notes: "Single-varietal wild agave. Tropical fruit, hard minerality, florals. Plants that grew twenty years before anyone cut them.",
        cost: "$90–160 / bottle · ~$38 / person",
      },
    ],
    howItWorks: [
      { title: "Purchase & Download", description: "Instant access to the 8-page PDF. Nothing ships." },
      { title: "Print at Home or a Shop", description: "Standard US Letter, no bleed or special stock needed." },
      { title: "Pick Your Tier", description: "Newbie, Casual, or Aficionado: the Agavebase names the bottles." },
      { title: "Host Tonight", description: "Everything's ready. This is an all-digital product." },
    ],
    images: {
      hero: "/kits/agave/hero.png",
      card: "/kits/agave/card.png",
      heroGif: "/kits/agave/hero.gif",
      gallery: [
        { src: "/kits/agave/preview-guide.png", label: "Party Guide" },
        { src: "/kits/agave/preview-primer.png", label: "Tequila & Mezcal Primer" },
        { src: "/kits/agave/preview-pairbase.png", label: "Agavebase Chart" },
        { src: "/kits/agave/preview-wheels.png", label: "Flavor Wheels" },
        { src: "/kits/agave/preview-cards.png", label: "Tasting Cards" },
      ],
    },
  },
  {
    slug: "candy-whisky",
    etsyUrl: "https://kingbkits.etsy.com/listing/4567609487",
    name: "Candy & Whisky",
    subtitle: "Halloween Pairing Kit",
    shortDescription:
      "The cheapest tasting night you'll ever host: a $12 bag of candy and a bottle you already own.",
    pageCount: 7,
    heroHeadline: "Your Leftover Candy Deserves Better.",
    heroBody:
      "Coconut in an Almond Joy shares the same compound class as American oak. Caramelized sugar and barrel char are the same chemical reaction. This isn't a party trick. Candy and whisky actually agree, and this kit shows you exactly where.",
    stats: [
      { value: "9", label: "candy & whisky pairings" },
      { value: "$12", label: "covers a table of six" },
      { value: "2", label: "selling windows: Oct & Nov 1–7" },
    ],
    included: [
      { number: "01", title: "Party Guide", description: "What to buy, how to set up, and how to actually taste a pairing." },
      { number: "02", title: "Candy Primer", description: "The real chemistry behind why chocolate and caramel pair so well with whisky." },
      { number: "03", title: "Pairbase Chart", description: "9 candies matched to real bottles, with the science for each pairing." },
      { number: "04", title: "Flavor Wheels", description: "Candy and whisky wheels side by side. Find where they overlap." },
      { number: "05", title: "Newbie Card", description: "The Sweet Match: three candies that agree with one bourbon." },
      { number: "06", title: "Casual Card", description: "The Contrast: pairings that work by fighting instead of agreeing." },
      { number: "07", title: "Aficionado Card", description: "The Gauntlet: sour candy, licorice, and candy corn. Good luck." },
    ],
    tierLabels: { primary: "Candy", secondary: "Whisky style" },
    tiers: [
      {
        tier: "Newbie",
        tierClass: "newbie",
        flightName: "The Sweet Match",
        primaryPicks: ["Snickers", "Twix", "Milky Way"],
        secondaryPicks: ["Caramel-forward bourbon"],
        notes: "Every candy here shares a flavor compound with the whisky. Nothing fights. This is your baseline for everything after.",
      },
      {
        tier: "Casual",
        tierClass: "casual",
        flightName: "The Contrast",
        primaryPicks: ["Dark Chocolate + Peated Scotch", "Reese's + Wheated Bourbon", "Almond Joy + Rye"],
        notes: "Opposites on purpose. Dark chocolate against peat smoke should be a train wreck and isn't. Find out where the line is.",
      },
      {
        tier: "Aficionado",
        tierClass: "aficionado",
        flightName: "The Gauntlet",
        primaryPicks: ["Sour Patch Kids", "Black Licorice", "Candy Corn"],
        notes: "Acid, anise, and pure sugar: the three things whisky handles worst. Something here will surprise you.",
      },
    ],
    howItWorks: [
      { title: "Purchase & Download", description: "Instant access to the full PDF, plus your editable Canva invitation template." },
      { title: "Print at Home or a Shop", description: "Standard US Letter, no bleed or special stock needed." },
      { title: "Buy One Bag of Candy", description: "The Pairbase names exactly which fun-size bars to grab." },
      { title: "Half-Ounce Pours", description: "Sip, bite, sip again. Vote on a winner at the end." },
    ],
    seasonalNote:
      "Two selling windows on purpose: October for Halloween parties, and November 1–7 for the leftover candy bowl.",
    images: {
      hero: "/kits/halloween/hero.png",
      card: "/kits/halloween/card.png",
      heroGif: "/kits/halloween/hero.gif",
      gallery: [
        { src: "/kits/halloween/preview-guide.png", label: "Party Guide" },
        { src: "/kits/halloween/preview-primer.png", label: "Candy Primer" },
        { src: "/kits/halloween/preview-pairbase.png", label: "Pairbase Chart" },
        { src: "/kits/halloween/preview-wheels.png", label: "Flavor Wheels" },
        { src: "/kits/halloween/preview-cards.png", label: "Tasting Cards" },
      ],
    },
  },
  {
    slug: "whisky-advent",
    name: "24 Nights of Whisky",
    subtitle: "Advent Calendar Companion",
    shortDescription:
      "A tasting card for every night, a month tracker, and a flavor wheel, built for the calendar you already bought.",
    pageCount: 9,
    heroHeadline: "Guess First. Reveal Second.",
    heroBody:
      "Real whisky advent calendars keep the dram a mystery until you open the door. So every card starts with a blind guess (region and age) before you ever see the label. Then the reveal. That's the part a blank notebook can't do.",
    stats: [
      { value: "24", label: "numbered nights" },
      { value: "30ml", label: "standard dram format" },
      { value: "1", label: "tracker for the whole month" },
    ],
    included: [
      { number: "01", title: "How to Use", description: "Setup, blind-tasting method, and what to do each night." },
      { number: "02–07", title: "24 Tasting Cards", description: "One numbered card per night, 4 per sheet, dashed cut lines." },
      { number: "08", title: "Month Tracker", description: "Every night at a glance, plus your top five of the month." },
      { number: "09", title: "Flavor Wheel", description: "Put a real word to what's in the glass." },
    ],
    compatibleWith: ["Drinks by the Dram", "Secret Spirits", "Flaviar", "The Whisky Exchange"],
    howItWorks: [
      { title: "Purchase & Download", description: "Instant access to the full 9-page PDF. Nothing ships." },
      { title: "Print at Home", description: "Standard US Letter, no bleed or special stock." },
      { title: "Grab the Card First", description: "Before you open the door. That's the whole trick." },
      { title: "Guess, Then Reveal", description: "Fill in the blind guess, taste, then check the label." },
    ],
    seasonalNote:
      "Works with any standard 24 × 30ml calendar, plus supermarket sets. Also works for 12-day calendars: just use cards 01–12.",
    images: {
      hero: "/kits/advent/hero.png",
      card: "/kits/advent/card.png",
      heroGif: "/kits/advent/hero.gif",
      gallery: [
        { src: "/kits/advent/preview-guide.png", label: "How to Use" },
        { src: "/kits/advent/preview-cards.png", label: "Tasting Cards" },
        { src: "/kits/advent/preview-tracker.png", label: "Month Tracker" },
        { src: "/kits/advent/preview-wheel.png", label: "Flavor Wheel" },
      ],
    },
  },
];

export function getKit(slug: string): Kit | undefined {
  return KITS.find((k) => k.slug === slug);
}
