import Image from "next/image";
import Link from "next/link";
import type { Kit } from "@/data/kits";

export function KitCard({
  kit,
  featured = false,
  contain = false,
}: {
  kit: Kit;
  featured?: boolean;
  contain?: boolean;
}) {
  return (
    <Link
      href={`/kits/${kit.slug}`}
      className="group flex h-full flex-col overflow-hidden rounded-card border border-rule bg-paper transition-all duration-200 hover:-translate-y-0.5 hover:border-ink"
    >
      <div className={`relative flex-1 overflow-hidden bg-paper-2 ${contain ? "p-4" : ""}`}>
        <Image
          src={kit.images.hero}
          alt={kit.name}
          fill
          sizes={featured ? "(min-width: 768px) 50vw, 100vw" : "(min-width: 768px) 25vw, 50vw"}
          className={contain ? "object-contain" : "object-cover"}
        />
      </div>
      <div className="flex flex-col gap-1 p-4">
        <div className="text-xs font-bold uppercase tracking-[0.06em] text-ink-faint">{kit.subtitle}</div>
        <h3 className={`font-display text-ink ${featured ? "text-2xl" : "text-lg"}`}>{kit.name}</h3>
        {featured && <p className="text-sm text-ink-2">{kit.shortDescription}</p>}
        <span className="mt-1 text-sm font-semibold text-ink underline decoration-accent decoration-2 underline-offset-4 group-hover:decoration-4">
          See the kit
        </span>
      </div>
    </Link>
  );
}
