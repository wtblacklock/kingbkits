"use client";

import Image from "next/image";

/**
 * Gallery preview of a paid PDF page: cropped in tighter than the real page
 * (so the full page is never handed over) and blocked from right-click-save
 * or drag-out. Deterrent, not DRM — a screenshot always gets through — but it
 * stops the one-click "Save image as" theft path.
 */
export function ProtectedGalleryImage({
  src,
  alt,
  sizes,
}: {
  src: string;
  alt: string;
  sizes: string;
}) {
  return (
    <div
      className="relative aspect-[4/5] select-none overflow-hidden [-webkit-touch-callout:none]"
      onContextMenu={(e) => e.preventDefault()}
    >
      <Image
        src={src}
        alt={alt}
        fill
        draggable={false}
        sizes={sizes}
        className="scale-[1.35] object-cover object-top"
      />
      <div className="absolute inset-0" aria-hidden="true" />
    </div>
  );
}
