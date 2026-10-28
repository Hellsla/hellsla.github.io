VERDICT: PASS
CONTENT-HASH: 65e8dbee4a6e41bb

## Blocking

## Polish
- exercises.json L3-02 — the interpretive question ("Mitä maankäyttö kertoo ...") is unchecked but not marked as a written part; begin it with "Perustele lyhyesti:" so the student knows it is answered in words.
- exercises.json L3-02 — the situation is still long (about 70 words); put the two yields as a two-item list or start the question on its own line.
- Still open from rounds 1-2: no `mistakes` feedback for the expected slips (GWh not converted, grams instead of kg or t), if the schema allows.

## Checked
- L3-02 now asks the ratio (50 kertaa, tolerance 0,02) so the student must compute both areas; answers.py A_bio / A_sol = 100 : 2,0 = 50 matches the solution; unit "kertaa" fits the question "kuinka moninkertaisen".
- L3-02 solution follows the new question: asked is the ratio, areas in km² by substitution of 1 ha = 0,01 km², ratio as a colon division, check that the area ratio equals the yield ratio, conclusion on land use kept.
- L3-01 and L3-03 solutions now name the symbols (e_b, h, N, V) in the formula before substituting; units appear in the substitution; answers (740, 4,1) unchanged.
- Added unit-conversion steps (g → kg, g → t) in the checks of L1-01, L1-02, L1-05, L2-01, L2-02, L2-03 make every step followable for a student who has met powers of ten in FY1; written division is a colon throughout, the symbolic fraction kept only in E/q and e = m/E.
- No task repeats the worked example (gas, 4800 kWh); levels 5 / 4 / 3 unchanged.
- Finnish and case endings in the diff are correct; decimal comma, LaTeX throughout.
- Hash at the end: 65e8dbee4a6e41bb (unchanged).
