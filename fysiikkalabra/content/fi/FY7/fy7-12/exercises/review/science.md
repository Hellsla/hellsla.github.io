VERDICT: FAIL
CONTENT-HASH: 81597b11751cc4cb

## Blocking
- exercises.json:183–189 and solutions.md:164 (fy7-12-L2-06) — A, data contradicts the model the task asks students to check: the axial (fastest) ray arrives at t₀ = n s : c = 49,33 µs, yet the table shows light at 49,0 µs (1 %) and 49,2 µs (4 %). Nothing can arrive before t₀, and b) asks when the pulse starts to arrive; the solution says the pulse "alkaa saapua hetkien 49,2 µs (4 %) ja 49,4 µs (52 %) välillä", which its own 4 % row contradicts. — Fix: set I = 0 at 49,0 µs and 49,2 µs (width stays 800 ns), and at solutions.md:164 write "pulssi alkaa saapua hetkien 49,2 µs (0 %) ja 49,4 µs (52 %) välillä, mikä sopii kulkuaikaan 49,33 µs: aiemmin valoa ei voi tulla, koska akselin suuntainen reitti on lyhin."

## Polish
- solutions.md:154 (fy7-12-L2-05) — sin⁻¹(1,00 : 1,59) = 38,97°, so write 39,0°, not 38,9°.
- solutions.md:143 (fy7-12-L1-08) — the limiting datum is t = 0,50 ms (two significant figures), not n = 1,45: answer "1,0 · 10² km (noin 100 km), kaksi merkitsevää numeroa kuten aika 0,50 ms".
- solutions.md:184 and :194 (L3-04, L3-05) — "kolme merkitsevää numeroa kuten taitekertoimet" ignores that the results hinge on n₁ − n₂ (0,03 / 0,09, one or two significant figures) and a = 0,50 mm: say the precision is limited by the difference: R_min ≈ 16 mm, θ_max ≈ 17°.
- solutions.md:160 (L2-06) — "Kuvaajan lukeminen" for a table: "Taulukon lukeminen".
- exercises.json fy7-12-L1-07 vs L1-03 and plan — L1-07 (acrylic→water) has the same structure as L1-03 (glass→water); the plan's Taso 3 "timantin hionta (kuva diamond)" was replaced by the bent-fibre L3-05. Update the plan or note the swap.

## Checked
- All 20 answers recomputed in one script; all match answers.py and exercises.json; units and tolerances fit.
- L1-06: exactly one correct option.
- L2-05: mean 42,04°, n = 1,4933; extremes 1,477 / 1,509; "todennäköisesti" wording follows the guardrails; acrylic identification right.
- L2-07: error explained correctly (no critical angle from air to glass); α₂ = 38,79°.
- L3-04: α_r, φ_max, θ_max for A/B/C = 14,03° / 17,37° / 9,82°; √(n₁² − n₂²) identity correct; delay ratios 0,0137 / 0,0204 / 0,0069.
- L3-05: geometry sin α = (R − a) : (R + a) is the minimum over the core, R_min = a(n₁ + n₂) : (n₁ − n₂) = 16,06 mm, check angle 70,0°.
- Notation matches the lesson brief; within FY7 scope.
- Hash unchanged start to end.
