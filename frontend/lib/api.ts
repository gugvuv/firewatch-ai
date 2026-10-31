import { z } from "zod";

const apiBase =
  process.env.NEXT_PUBLIC_API_BASE_URL ?? "http://localhost:8000";

export const healthSchema = z.object({
  status: z.string(),
  timestamp: z.string(),
});

export type Health = z.infer<typeof healthSchema>;

export async function fetchHealth(): Promise<Health> {
  const res = await fetch(`${apiBase}/api/v1/health`, { cache: "no-store" });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const json = await res.json();
  return healthSchema.parse(json);
}
