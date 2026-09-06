import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx,mdx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        paper: "oklch(15% 0.008 85)",
        "paper-2": "oklch(19% 0.010 85)",
        "paper-3": "oklch(24% 0.012 85)",
        ink: "oklch(95% 0.013 87)",
        "ink-2": "oklch(76% 0.024 87)",
        "ink-faint": "oklch(56% 0.018 87)",
        rule: "oklch(30% 0.014 85)",
        accent: "oklch(94% 0.200 106)",
        "accent-ink": "oklch(15% 0.008 85)",
        focus: "oklch(94% 0.200 106)",
        tier: {
          newbie: "oklch(76.8% 0.196 130.6)",
          casual: "oklch(96.8% 0.211 109.8)",
          aficionado: "oklch(87.8% 0.169 91.9)",
        },
        // legacy aliases kept during the redesign so unmigrated markup doesn't break
        cover: "oklch(19% 0.010 85)",
        zone: "oklch(24% 0.012 85)",
        chip: "oklch(30% 0.014 85)",
        "ink-body": "oklch(76% 0.024 87)",
        gold: "oklch(94% 0.200 106)",
      },
      fontFamily: {
        sans: ["var(--font-raleway)", "ui-sans-serif", "system-ui", "sans-serif"],
        display: ["var(--font-fraunces)", "var(--font-raleway)", "serif"],
        mono: ["var(--font-jetbrains-mono)", "ui-monospace", "SF Mono", "monospace"],
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
