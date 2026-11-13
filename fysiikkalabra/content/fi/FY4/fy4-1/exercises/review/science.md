VERDICT: PASS
CONTENT-HASH: 56b462a120e44526
SCOPE: delta added-exercise from 6532dd8778633a6f base 7db0992d648a
## Blocking

## Polish
- content/fi/FY4/fy4-1/exercises/solutions.md:241 (L2-08) — keskivauhti gets the symbol $v_\text{k}$, which the lesson uses for keskinopeus (and L3-03 uses for the signed mean velocity); the Järkevyys line then compares two quantities that share one symbol — give the speed its own symbol, e.g. $v_\text{kv}$ or simply $s/\Delta t$.
- L2-09 Vastaus — the two figures are justified by "nopeudet $2{,}0\,\text{m/s}$ ... annettu"; the velocities are read from grid crossings rather than given; "kuvaajasta luetut kokonaisluvut ja $t = 6{,}0\,\text{s}$" would be more accurate.

## Checked
- Recomputed from figures.py data in one call: L2-08 s = 12 + 0 + 8 = 20 m, 20 m / 10 s = 2,0 m/s; L2-09 x_A(6) = 16 m, x_B(6) = 8 m, d = 8 m; crossing (4 s; 12 m). Both equal answers.py (2.0, 8.0) and exercises.json.
- ex-kolme-osaa: corners (0;4), (4;16), (6;16), (10;8) lie on tick crossings (xticks every 2 s, yticks every 4 m), so readable exactly; tolerance 0,02 fine.
- ex-kaksi-kappaletta: endpoints and the values at t = 6 s (16 m, 8 m, both y-ticks) and the crossing lie on grid lines; tolerance 0,04 fine.
- Descriptions give the same data as the drawings; neither marks the path length, the mean speed, the crossing or the distance.
- Physics: L2-08 defines keskivauhti in the task text as path / time, so it does not rely on an untaught term; solution correctly uses absolute values and contrasts mean velocity 0,4 m/s. L2-09 uses x = x₀ + vt and |x_A − x_B|; guardrail wording "ylempänä oleva viiva ... suurempaa paikkakoordinaattia" used.
- Not a repeat: L3-03 (three-part graph) asks the signed mean velocity from given text values, L3-01 mean speed from text; L2-06 asks a meeting time from a table. L2-08/L2-09 read figures and ask different quantities.
- Solutions complete (seven parts, symbolic before numbers, reasonableness checks are genuine independent checks).
- Hash 56b462a120e44526 at start and end.
