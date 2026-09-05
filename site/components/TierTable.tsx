import type { Kit } from "@/data/kits";
import { TierPill } from "./TierPill";

export function TierTable({ kit }: { kit: Kit }) {
  if (!kit.tiers) return null;
  const labels = kit.tierLabels ?? { primary: "Pick", secondary: undefined };

  return (
    <div className="overflow-x-auto rounded-lg border border-rule">
      <table className="w-full min-w-[640px] border-collapse text-sm">
        <thead>
          <tr className="border-b-2 border-ink text-left text-xs font-bold uppercase tracking-wide text-ink-faint">
            <th className="px-4 py-3">Tier</th>
            <th className="px-4 py-3">{labels.primary}</th>
            {labels.secondary && <th className="px-4 py-3">{labels.secondary}</th>}
            <th className="px-4 py-3">Notes</th>
            {kit.tiers.some((t) => t.cost) && <th className="px-4 py-3">Cost</th>}
          </tr>
        </thead>
        <tbody>
          {kit.tiers.map((row) => (
            <tr key={row.tier} className="border-b border-rule align-top last:border-b-0">
              <td className="px-4 py-4">
                <TierPill tier={row.tier} tierClass={row.tierClass} />
                {row.flightName && <div className="mt-1 text-xs text-ink-faint">{row.flightName}</div>}
              </td>
              <td className="px-4 py-4">
                {row.primaryPicks.map((pick) => (
                  <div key={pick} className="text-ink-body">
                    {pick}
                  </div>
                ))}
              </td>
              {labels.secondary && (
                <td className="px-4 py-4">
                  {row.secondaryPicks?.map((pick) => (
                    <div key={pick} className="text-ink-body">
                      {pick}
                    </div>
                  ))}
                </td>
              )}
              <td className="px-4 py-4 text-ink-body">{row.notes}</td>
              {kit.tiers?.some((t) => t.cost) && (
                <td className="px-4 py-4 whitespace-nowrap text-ink-body">{row.cost}</td>
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
