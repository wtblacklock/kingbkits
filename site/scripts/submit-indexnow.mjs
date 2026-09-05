#!/usr/bin/env node
// Pings IndexNow (Bing, Yandex, and other participating search engines) with the
// site's current URLs after each production build, so new/changed pages get
// picked up faster than waiting for the next crawl. Runs as a `postbuild` step.
//
// Docs: https://www.indexnow.org/documentation

import { readFileSync } from "node:fs";
import path from "node:path";

const SITE_URL = "https://kingbkits.com";
const HOST = "kingbkits.com";
const KEY = "ad90dd5dc8c311f377e0dfde6850f63f";

if (process.env.VERCEL_ENV !== "production") {
  console.log("[indexnow] Skipping: not a production build.");
  process.exit(0);
}

const sitemapPath = path.join(process.cwd(), ".next/server/app/sitemap.xml.body");

let urls;
try {
  const xml = readFileSync(sitemapPath, "utf8");
  urls = [...xml.matchAll(/<loc>(.*?)<\/loc>/g)].map((m) => m[1]);
} catch (err) {
  console.warn(`[indexnow] Could not read generated sitemap at ${sitemapPath}, skipping.`, err.message);
  process.exit(0);
}

if (urls.length === 0) {
  console.warn("[indexnow] Sitemap had no URLs, skipping.");
  process.exit(0);
}

try {
  const res = await fetch("https://api.indexnow.org/indexnow", {
    method: "POST",
    headers: { "Content-Type": "application/json; charset=utf-8" },
    body: JSON.stringify({
      host: HOST,
      key: KEY,
      keyLocation: `${SITE_URL}/${KEY}.txt`,
      urlList: urls,
    }),
  });
  console.log(`[indexnow] Submitted ${urls.length} URLs, status ${res.status}`);
} catch (err) {
  console.warn("[indexnow] Submission failed (non-fatal):", err.message);
}
