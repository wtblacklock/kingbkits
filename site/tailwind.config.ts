import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx,mdx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        paper: "oklch(99.4% 0.008 91.5)",
        "paper-2": "oklch(96.5% 0.013 87)",
        "paper-3": "oklch(93.2% 0.023 87)",
        ink: "oklch(15% 0.010 85)",
        "ink-2": "oklch(35% 0.010 85)",
        "ink-faint": "oklch(55% 0.010 85)",
        rule: "oklch(88% 0.012 85)",
        accent: "oklch(94% 0.200 106)",
        "accent-ink": "oklch(15% 0.010 85)",
        "accent-text": "oklch(54.8% 0.112 90.2)",
        pop: "oklch(68.5% 0.204 30.3)",
        "pop-dark": "oklch(62.4% 0.205 34.2)",
        "pop-ink": "oklch(99.4% 0.008 91.5)",
        focus: "oklch(62.4% 0.205 34.2)",
        tier: {
          newbie: "oklch(76.8% 0.196 130.6)",
          casual: "oklch(96.8% 0.211 109.8)",
          aficionado: "oklch(87.8% 0.169 91.9)",
        },
        // legacy aliases kept during the redesign so unmigrated markup doesn't break
        cover: "oklch(96.5% 0.013 87)",
        zone: "oklch(93.2% 0.023 87)",
        chip: "oklch(88% 0.012 85)",
        "ink-body": "oklch(35% 0.010 85)",
        gold: "oklch(94% 0.200 106)",
      },
      fontFamily: {
        sans: ["var(--font-raleway)", "ui-sans-serif", "system-ui", "sans-serif"],
        display: ["var(--font-archivo-black)", "var(--font-raleway)", "sans-serif"],
      },
      maxWidth: {
        content: "1200px",
      },
      borderRadius: {
        card: "12px",
      },
      transitionTimingFunction: {
        "hallmark-out": "cubic-bezier(0.16, 1, 0.3, 1)",
      },
    },
  },
  plugins: [],
};

export default config;
