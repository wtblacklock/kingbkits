import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx,mdx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        paper: "#ffffff",
        zone: "#f9f9f9",
        cover: "#eaeae7",
        chip: "#d2d2d2",
        ink: "#000000",
        "ink-body": "#454545",
        "ink-faint": "#8a8a8a",
        rule: "#d8d8d5",
        gold: "#f3c318",
        tier: {
          newbie: "#87cb28",
          casual: "#ffff00",
          aficionado: "#ffd230",
        },
      },
      fontFamily: {
        sans: ["var(--font-raleway)", "ui-sans-serif", "system-ui", "sans-serif"],
        display: ["var(--font-archivo-black)", "var(--font-raleway)", "sans-serif"],
      },
      maxWidth: {
        content: "1200px",
      },
    },
  },
  plugins: [],
};

export default config;
