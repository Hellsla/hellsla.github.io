VERDICT: PASS
CONTENT-HASH: 1908baceb1a28e91

## Blocking

## Polish
- solutions.md:155 (L2-06) — "kolme merkitsevää numeroa kuten massoissa": the limiting data are the times t₁₀ = 4,5 … 9,9 s (two figures), so the honest result is 20 N/m (answer box and tolerance 0,04 are fine either way) — give the reason from t₁₀ and round to 20 N/m, or say the third figure is kept only for comparison.
- solutions.md:177 (L3-04 Järkevyys) — "jousi on punnuksiin verrattuna kevyt, kuten pitääkin" is not a real check: m₀ = 21 g is not the spring's mass (the spring itself is heavier than m₀), and 21 g is not small next to the 50 g weight — replace with the check already given after it (k from the heaviest weight 23,6 N/m is closer to 25,1 N/m than k from the lightest, as the m₀ model predicts).
- solutions.md L3-05 (Järkevyys) / exercises.json:26 c) "miksi" — the solution explains only the size of the 0,13 % difference, not its direction — add: the harmonic model uses the restoring force mgα > mg sin α, so it gives slightly more work and a slightly larger speed (0,5988 > 0,5981 m/s).
- docs/exercise-bank/FY5.md:57,59 — the plan still lists a numeric pendulum task at level 1 and the clock-pendulum thermal-expansion task at level 3; the set has MC tasks on k and amplitude (L1-07, L1-08) and the clock task is the old L3-03, while new L3-05 is the energy-vs-harmonic model — update the plan lines to the set as built.

## Checked
- All answers recomputed in one script; new ones agree (9,772; 20,14; 7,175 %; 25,15 N/m; 0,5981 m/s).
- Least-squares fits agree with the hand readings (g 9,78; k 20,07; k 25,12 N/m, m₀ 20,8 g); slopes read from fitted lines.
- L2-07 data match the lesson's T : T₀ table; part b) correct.
- L3-04 k₁ 17,69 N/m, −29,6 %; L2-06 states its spring-mass assumption, no contradiction.
- L3-05: h 0,01823 m, T/4 0,549 s, harmonic 0,5988 m/s (0,127 %).
- MC L1-06..08: one correct option each, distractor feedback right.
- New tasks inside the slot and plan; "graph" only where a graph is asked.
- No duplicate of fy5-7, fy5-8, fy5-10 or old tasks; empty display-math boxes in shots also in old tasks (capture artefact).
- Hash identical at start and end.
