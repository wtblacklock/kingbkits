/**
 * Appends UTM params to an outbound Etsy link so click-throughs are
 * attributable in Etsy's own traffic-source stats and in site analytics.
 */
export function withUtm(url: string, opts: { campaign: string; content?: string }): string {
  const target = new URL(url);
  target.searchParams.set("utm_source", "kingbkits.com");
  target.searchParams.set("utm_medium", "referral");
  target.searchParams.set("utm_campaign", opts.campaign);
  if (opts.content) target.searchParams.set("utm_content", opts.content);
  return target.toString();
}
