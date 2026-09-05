import { withUtm } from "@/lib/utm";
import { SITE } from "@/data/site";

export function EtsyButton({
  href,
  campaign,
  content,
  children,
  variant = "primary",
}: {
  href?: string;
  campaign: string;
  content?: string;
  children: React.ReactNode;
  variant?: "primary" | "ghost";
}) {
  const target = withUtm(href ?? SITE.etsyShopUrl, { campaign, content });
  const styles =
    variant === "primary"
      ? "bg-black text-white hover:bg-ink-body"
      : "border border-ink text-ink hover:bg-ink hover:text-white";
  return (
    <a
      href={target}
      target="_blank"
      rel="noopener noreferrer"
      className={`inline-flex items-center justify-center rounded-full px-6 py-3 text-sm font-semibold transition-colors ${styles}`}
    >
      {children}
    </a>
  );
}
