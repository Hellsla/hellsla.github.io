VERDICT: PASS
CONTENT-HASH: 8ea29c696463591e

## Blocking

## Polish
- exercises.json:50,55 (L1-06) — "Villan varaus on positiivinen ja yhtä suuri kuin sauvan varaus": +Q and −Q are not equal; write "itseisarvoltaan yhtä suuri".
- exercises.json:291 (L3-05 c) — "langat ovat edelleen yhtä suuressa kulmassa" can be read as "still 10°", which is false (the angle grows); write "langat ovat edelleen keskenään yhtä suuressa kulmassa pystysuoraan nähden (vaikka kulma kasvaa)".
- solutions.md:145 (L2-05) — the slope 5,50·10⁻⁶ N·m² is the least-squares value, not read from two points of the drawn line (guardrail "Fits"), and the reason for forcing the line through the origin (1 : r² → 0 when r → ∞, so F → 0) is not given; add both. solutions.md:150: the F r² values differ by 7,1 %, not "alle 7 %" — "noin 7 %".
- solutions.md:156 (L2-06) — headed "Kuvaajan lukeminen" and "voimakäyrät", but the task gives a table and asks for ratios; no graph is drawn. Rename to the table, or ask for the two curves; kind "graph" likewise.
- docs/exercise-bank/FY6.md (fy6-10) — plan items not delivered: L1 calc "etäisyys, jolla voima on annettu" (L1-08 is Q = It instead), L2 experiment on humid days (L2-07 error task instead), L3 qualitative comb and paper (L3-05 pendulum instead). Update the plan or note the swap. Round-2 Polish still open: solutions.md:108 "Tarkista selityksesi" inside the answer.

## Checked
- All 20 answers recomputed in one script with my own formulas (k = 8,988·10⁹), and answers.py re-run: every pair agrees (< 0,05 %).
- L1-06, L1-07: exactly one correct option, distractor feedback right.
- L2-05: F r² = 5,44–5,82·10⁻⁶ N·m², origin fit 24,7 nC (per-row mean 25,0 nC, within 5 %); data consistent with Coulomb's law at 25 nC.
- L2-06: ratios 3,41/3,69/3,30/3,50/3,55, mean 3,49 → 69,8 nC ; F_A matches 20 nC theory, F_B 70 nC within 3 %.
- L2-07: the student's k q₁q₂ : r = 0,0288 mN, i.e. 0,029 as stated; correct 0,959 mN, factor 1 : 0,030 = 33.
- L3-04: region analysis right (between: both forces +x; x < 0: q₁ always dominates); x = 33,85 cm.
- L3-05: F = mg tan θ = 1,384 mN, r = 2L sin θ = 0,104 m, q = 40,9 nC; part c (third law → equal angles) correct.
- Levels fit; no duplicate of an existing task (L3-04 outside unlike charges vs L3-03 between like ones); notation as in the brief; point-charge assumption stated where needed.
