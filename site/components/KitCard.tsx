import Image from "next/image";
import Link from "next/link";
import type { Kit } from "@/data/kits";

export function KitCard({ kit }: { kit: Kit }) {
  return (
    <Link
      href={`/kits/${kit.slug}`}
      className="group flex flex-col overflow-hidden rounded-2xl border border-rule bg-paper transition-shadow hover:shadow-lg"
    >
      <div className="relative aspect-square overflow-hidden bg-cover">
        <Image
          src={kit.images.hero}
          alt={kit.name}
          fill
          sizes="(min-width: 768px) 25vw, 50vw"
          className="object-cover transition-transform duration-300 group-hover:scale-105"
        />
      </div>
      <div className="flex flex-1 flex-col gap-2 p-5">
        <div className="text-xs font-bold uppercase tracking-wide text-ink-faint">{kit.subtitle}</div>
        <h3 className="text-lg font-semibold text-ink">{kit.name}</h3>
        <p className="text-sm text-ink-body">{kit.shortDescription}</p>
        <span className="mt-auto pt-3 text-sm font-semibold text-ink underline decoration-gold decoration-2 underline-offset-4">
          See the kit →
        </span>
      </div>
    </Link>
  );
}
