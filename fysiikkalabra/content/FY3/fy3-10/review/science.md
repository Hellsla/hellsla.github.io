VERDICT: PASS
CONTENT-HASH: e390340fc253a339

## Blocking

## Polish
- (Reused, round 3; file lines unchanged) solutions.md L1-03 Järkevyys — "18 g, mikä on tavallisen patruunan koko": common automatic-lifejacket cartridges hold about 24–38 g CO₂, so 18 g is on the small side; "pienen patruunan koko" or drop the claim.
- (Reused, round 3) solutions.md L2-01 Järkevyys — at 288 K and about 180 bar attraction dominates (Z < 1); an optional "vetovoima on tässä hallitseva" would make the direction self-explanatory. Not an error.

## Checked
- Hash e390340fc253a339 at start and end (round-3 PASS was 69d12376298ae428).
- New, sim.js ~L231: the only change wraps the "asteikko mukautuu" label in `if (k <= 1.5)`. Inside, it measures 'p/p' at the current ts(13) size and sets ts(10) only for this label; the bar loop that follows sets its own text sizes. No state, measurement, scaling or particle variable is touched, so the physics cannot change.
- New, screenshot fy3-10-sim-1280.png: label "asteikko mukautuu" present beside p/p_ref; bars 0,99 / 1,00, ticks 0–2,5, dashed reference at 1, ratio strip 0,99.
- New, screenshot fy3-10-sim-360.png: label absent, p/p_ref no longer collides with the tank; bars, ticks, reference line, gauge, ratio strip and legend otherwise as at 1280.
- Reused (round 2, files unchanged): all 12 answers recomputed with independent formulas; answers.py, exercises.json and mine agree within 0,5 % (tolerance 2 %).
- Reused: exit ticket (0,601 mol), worked example (0,2073 mol, 0,829 g, air 6,01 g, 24,1 l/mol), SVG numbers, solution side-checks, formulas, conditions and FY3 scope.
- Reused: sim.js physics p = NkT/A, P_REF from it; Playwright 8 slider states ratio 0,95–1,05; 300-window statistics (N = 20 sd 5,5 %, N = 100 sd 2,5 %).
- Reused (round 3): lesson.md reference state N = 100, T = 300 K, V = 100 % matches sim.js; volume change isothermal in code (velocities never scaled); L2-01 real-gas comment (Z ≈ 0,94–0,95, ~6 % high) defensible; sim note text correct, including the adaptive-scale sentence that now carries the message on phones.
