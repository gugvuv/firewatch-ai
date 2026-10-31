"use client";

import { useQuery } from "@tanstack/react-query";
import { healthSchema, fetchHealth } from "@/lib/api";
import { Button } from "@/components/ui/button";

export default function HomePage() {
  const { data, isLoading, isError, error } = useQuery({
    queryKey: ["health"],
    queryFn: fetchHealth,
  });

  return (
    <main className="min-h-screen p-8">
      <div className="mx-auto max-w-3xl space-y-6">
        <header>
          <h1 className="text-3xl font-bold text-primary">FireWatch AI</h1>
          <p className="text-muted-foreground">
            Wildfire monitoring &amp; risk platform on real NASA data.
          </p>
        </header>

        <section className="rounded-lg border border-border bg-card p-6">
          <h2 className="mb-2 text-xl font-semibold">Backend health</h2>
          {isLoading && <p className="text-muted-foreground">Loading…</p>}
          {isError && (
            <p className="text-red-400">Error: {(error as Error).message}</p>
          )}
          {data && (
            <pre className="text-sm text-muted-foreground">
              {JSON.stringify(data, null, 2)}
            </pre>
          )}
          <div className="mt-4">
            <Button onClick={() => window.location.reload()}>Refresh</Button>
          </div>
        </section>
      </div>
    </main>
  );
}
