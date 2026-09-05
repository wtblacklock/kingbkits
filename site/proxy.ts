import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { SITE } from "@/data/site";

const CANONICAL_HOSTS = new Set([SITE.domain, `www.${SITE.domain}`]);

export function proxy(request: NextRequest) {
  const host = request.headers.get("host") ?? "";
  const response = NextResponse.next();

  if (!CANONICAL_HOSTS.has(host)) {
    response.headers.set("X-Robots-Tag", "noindex, nofollow");
  }

  return response;
}

export const config = {
  matcher: ["/((?!_next/static|_next/image|favicon.ico).*)"],
};
