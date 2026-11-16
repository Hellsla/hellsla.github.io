VERDICT: FAIL
CONTENT-HASH: 7b8809a307253ebd

## Blocking
- content/fi/FY5/fy5-17/exercises/solutions.md:240 (L2-10, Kohta a) — A (a claim about the source with no basis): "Taulukon uusimmat rivit ovat alustavia, joten arvot voivat vielä tarkentua" presents a property of the Institute's tables as fact, but the fetched page says nothing about preliminary rows. It notes only that F marks a fixed depth. — Delete the sentence, or replace it with what the page says (for example that the location is uncertain by a few hundred metres to 2 km).

## Polish
- content/fi/FY5/fy5-17/exercises/exercises.json:348 (L2-10) — the answer is stored as 11.905, five figures, but the solution gives Δt ≈ 12 s with two figures (from the speeds). Store 11.9 or 12. The tolerance of 3 % already accepts 12.
- content/fi/FY5/fy5-17/exercises/exercises.json (L2-10 text) — "Sivun lopussa on linkki alasivulle": the source notes confirm that the subpage exists, but not where its link is. Write "Sivulta on linkki alasivulle".

## Checked
- The hash was the same at the start and at the end.
- I recomputed all 23 numeric answers in one script. All of them are inside their tolerances. The largest differences come from two-significant-figure rounding, as the solutions explain: L2-04 is 20 s against 19,6 s (2,0 %, tolerance 3 %), and L2-03 is 3,9 kHz against 3,85 kHz.
- L2-10 c: Δt = 100/3,5 − 100/6,0 = 11,905 s, which is 12 s with two figures. The check 100 km : 8,4 km/s = 11,9 s and the claim that 2 km equals 0,24 s are right.
- L2-10 a against the source notes: row no. 149 (10.11.2026 01:34 UTC, 61,754° N 24,361° E, 18,3 km, M 1,0, Orivesi) and the magnitude range 0–4 are as the page gave them. More than 40 stations and an uncertainty from a few hundred metres to 2 km are in d). The example says that another earthquake or a later reading gives other values, so no number depends on the source alone.
- L2-10 b, d: P is longitudinal and S transverse, S does not travel in liquids (no restoring force against shear), and the third station resolves the two intersections. The limits of the model (depth, varying speeds) are stated.
- L3-04: d = 84,0; 63,0; 49,6 km, the point is (72,9; ±41,8), and C gives 49,9 km against 132,4 km, so y = 42 km.
