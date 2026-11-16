VERDICT: PASS
CONTENT-HASH: 799fb4d8eefe224d

## Blocking
(none)

## Polish
- none.

## Checked
- Delta: fy5-4-L3-06 task text (exercises.json:367) and its solution principle (solutions.md:317) now say "maximum static friction $\mu_0 N$" instead of "greatest static friction". The new wording is the English term in docs/physics-guardrails.md (Friction, P8: maximum (fully developed) static friction). The physics, the condition and the limiting case $F = \mu_0 N$ are unchanged.
- The remaining uses of "greatest" in the set (greatest speed, greatest tension, greatest rotation frequency) name kinematic or string limits, not the static-friction quantity, so the term is used the same way everywhere.
- Recomputed: $\mu_0 = 8000/(1200 \cdot 9.81) = 0.680$, which matches answer 0.68. The figure kuvaaja-b (F = 1.2 kN · v²/60) still gives 8.0 kN at 20 m/s.
- The diff changes no number, symbol, unit or tolerance. The earlier full checks (ground-frame model, no centrifugal force, significant figures, figures) still hold.
- Hash 799fb4d8eefe224d (with --lang en) is the same at the start and at the end.
