import Image from "next/image";

const SIZES = {
  sm: { h: 32 },
  md: { h: 48 },
  lg: { h: 96 },
} as const;

export function Badge({ size = "md" }: { size?: keyof typeof SIZES }) {
  const { h } = SIZES[size];
  return (
    <Image
      src="/logo.png"
      alt="KingBKits"
      width={h}
      height={h}
      className="w-auto flex-none"
      style={{ height: h }}
      priority
    />
  );
}
