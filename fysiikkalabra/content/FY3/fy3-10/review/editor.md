VERDICT: FAIL
CONTENT-HASH: 89cdb239b7f26e23

The lesson meets its goals. pV = nRT is built up from fy3-9's separate laws, and line 31 gets them back. The exercises solve for n, p, V, T, M and use the combined law. The sim treats pressure at particle level. The helium-versus-air hook is answered in line 10 and carries through to the example, the summary, L3-02 and exit ticket 2. The length (661 words) fits the FY3 series. Two weak points: L2-01 is the worked example with new numbers, and nothing outside the sim uses its main idea, p ∝ NT/V.

## Blocking
- exercises.json:48 (L2-01) — The task follows the same chain as the worked example (lesson.md:34–44): l → m³, °C → K, n = pV/(RT), m = nM. The bar conversion is the only new step. This breaks the house rule against repeating the worked example. — Reverse the direction, e.g. "the 10,0 l cylinder holds 2,40 kg of oxygen at 15 °C; what is the pressure in bar?" Then update answers.py and solutions.md.

## Polish
- lesson.md:12 — The text never points to the sim. It also says particles interact "vain törmätessään", but the sim leaves out particle–particle collisions. — Add one sentence: the sim ignores collisions between particles, and doubling N or T, or halving V, doubles the pressure (p ∝ NT/V).
- exit-ticket.json:3 — Q1 repeats L1-01. Nothing checks the ratio reasoning the sim teaches. — Ask instead: "V is halved and T goes from 300 K to 450 K; by what factor does p change?" (3).
- lesson.md:8 — L3-01 needs N = n·N_A, which appears only in prose. — Add $N = nN_\text{A}$ in display form and name the symbols.

## Checked
- Lint: 0 errors, 0 warnings. Hash was the same at the start and end of the review.
- meta.json goals match curriculum.json. The prerequisite fy3-9 holds the V/T and p/T laws.
- The hook question (line 3) is answered (line 10).
- Each quantity is solved for at least once: n, p, V, T, M.
- L3 tasks combine two ideas each. Gauge pressure is prepared at lesson.md:19.
- Example values are right: n ≈ 0,207 mol, m ≈ 0,83 g, air ≈ 6,0 g.
- Answers spot-checked and right: L2-02 27,9 g/mol (typpi), L2-03 555 °C, L3-03 0,72 kg, exit Q1 0,602 mol.
- Scope stays in FY3: no vectors and no kinetic-energy expression.
- Exercise counts are 5/4/3, and the exit ticket has 3 items.
