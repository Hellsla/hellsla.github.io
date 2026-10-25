VERDICT: PASS
CONTENT-HASH: 8fb367b0d6fd83e0

Round 3 (final). Hash checked at start and at end: 8fb367b0d6fd83e0 (unchanged). `check_latex.py content/FY3/fy3-1`: all LaTeX ok (7 fragments).

Verification done
- All 12 solutions recomputed in Python (`python3 -I`): 39,24; 6,0; 48,6; 1,5; 62,0; 4,995; 0,5886; 1187,55; 5,886; 6,807; 133,22; 0,9908. Every intermediate and final value in solutions.md matches.
- Every exercises.json `answer` equals the solutions.md final answer. Significant figures follow the data in every case: 2 sf for L1-01, 02, 03, 04, 05, L2-01, 02, 04, L3-01, L3-03; 3 sf for L2-03 (145 kg, 1,62: 1190 N) and L3-02 (22,0 kg: 133 kg).
- Tolerance 0,02: the relative error of each stored answer against the unrounded value is at most 0,0082 (L1-03: 49 against 48,6). A student who rounds correctly, or who gives the unrounded value, stays inside the tolerance. Alternative routes also stay inside: rounded intermediates in L3-01 (1,83 · 3,71 = 6,79), the difference 1185 N in L2-03, and 1,19 kN.
- Rearrangements are correct (m = G/g; m_Kuu = F/g_Kuu; L3-01 via m = G_Maa/g_Maa; L3-03 reading = G/9,81). Proportional-stretch ratios are correct (L1-02, L1-04, L2-04). Rounding happens only at the end.
- Exit ticket: 3,0 · 9,81 = 29,43, so 29 N; 3,0 · 1,62 = 4,86, so 4,9 N; the ratio 0,165 is about 1/6. 20/8,0 = 2,5, so 2,5 · 3,0 = 7,5 cm. 70 · 9,81 = 686,7, so about 690 N. All correct.
- Lesson numbers: 120 · 9,81 = 1177,2, so 1180 N or 1,18 kN. 120 · 3,71 = 445,2, so 445 N. The ratios 5,0 N : 2,0 cm give 10 N : 4,0 cm and 2,5 N : 1,0 cm. 100 g · 9,81 = 0,981 N, so "noin 1 N" is correct. 1,62/9,81 = 0,165, about 1/6. The g table (1,62; 3,71; 9,81; 24,8) is correct and the Jupiter note is accurate.
- SVG: the geometry is consistent (spring polyline from 34 to 166, box 166 to 246, arrow shaft 170 to 258 and head 250 to 272). The labels are plain text without LaTeX, as NOTES.md requires. G = mg and the notation in lesson.md match solutions.md (G, m, g in N/kg).

Findings (all non-blocking, no change required)
1. solutions.md:120 — L2-03 sanity check says "noin 83 %". It is correct (1187,55/1422,45 = 0,835) — no change needed.
2. solutions.md:80 — L1-03 sanity check uses "noin 294 N" (30 · 9,81 = 294,3). It is correct as an approximate check — no change needed.
3. solutions.md:151 — L3-03 sanity check, "noin kuudesosa" of 6,0 kg is about 1,0 kg, and the exact reading 0,991 kg agrees with the rounded 0,99 kg. This is fine — no change needed.
