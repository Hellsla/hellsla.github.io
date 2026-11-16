VERDICT: PASS
CONTENT-HASH: 22126cca58c08cf9
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- C: s4 d still says "johdon lämpöteho" in Kysytty and Vastaus while c and the task text now say "sisäenergiaksi muuttuva teho"; both are correct physics, one wording would be tidier.

## Checked
- solutions.md and tasks.json, 5 hunks: "Lähtökitka eli täysin kehittynyt lepokitka on μ0N = μ0mg" agrees with the model answer's "suurin mahdollinen lepokitka" and the condition ma ≤ μ0mg; the cable power is now energy becoming the conductor's internal energy, in agreement with the Periaate line. Recomputed: I = 14,27 A, P = 0,560 Ω · I² = 114,0 W, thicker cable 70,35 W (answer 70.4 within rounding, unchanged).
- No task was added to this unit (item 19 touches other units); `python scripts/practice.py check units/fy9-harjoituskoe` OK; hash the same at start and end.
