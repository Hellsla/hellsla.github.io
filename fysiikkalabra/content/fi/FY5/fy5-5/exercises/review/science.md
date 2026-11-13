VERDICT: FAIL
CONTENT-HASH: f407d72330d297fb
SCOPE: delta added-exercise from 0712046380ca6300 base 81db4a6fd727

## Blocking
- exercises.json:342, solutions.md:295 (L2-09) — A: the data do not belong together. The figure's 24,8 m/s² is Jupiter's field strength at the 1-bar level on the equator, R ≈ 7,15·10⁷ m (γ·1,898·10²⁷ kg / (7,149·10⁷ m)² = 24,8 m/s²). The task combines it with the mean radius 6,99·10⁷ m. The result 1,82·10²⁷ kg is 4 % below Jupiter's mass (1,90·10²⁷ kg) and is given to 3 sf as Jupiter's mass. The check "noin 300-kertainen … tunnettu suuruusluokka" hides the gap. — Fix: give "päiväntasaajan säde $7{,}15\cdot 10^{7}\,\text{m}$". Then M = 24,8 · (7,15·10⁷)² / γ = 1,90·10²⁷ kg. Update the answer, answers.py and the check (about 318 times the Earth's mass).
- solutions.md:284 (L1-09) — A: the rounding reason is wrong. The mass 85 kg has 2 sf and limits the answer, so the answer is 3,2·10² N, not "315 N, kolme merkitsevää numeroa kuten kiihtyvyydessä". — Fix: answer $3{,}2\cdot 10^{2}\,\text{N}$, limited by the mass 85 kg, or give the mass as 85,0 kg.

## Polish
- The figure labels Earth with 9,80 m/s², but the course uses 9,81 m/s² (the L1-09 check uses 9,81). Neither added task uses Earth's value, so nothing needs to change now.

## Checked
- The hash was the same at the start and at the end. Only L1-09 and L2-09 were judged.
- Recomputed: L1-09 gives 85 · 3,71 = 315,35 N; L2-09 gives 24,8 · (6,99·10⁷)² / 6,674·10⁻¹¹ = 1,816·10²⁷ kg. Both equal answers.py and exercises.json.
- The figure's labelled values are 1,62, 3,71, 9,80 and 24,8 m/s², the arrows are drawn at 7 px per m/s², and the description gives the same numbers. Each task reads its own planet. Neither task gives the other away or repeats the fy5-5 tasks that have no figure.
- Mars: γ · 6,417·10²³ kg / (3,39·10⁶ m)² = 3,73 m/s², so the value 3,71 is consistent.
- Physics: $F = mg$ with $g = \gamma M/R^2$, and the cancelling of m in L2-09, are the brief's model. Notation γ, M, R matches the brief.
