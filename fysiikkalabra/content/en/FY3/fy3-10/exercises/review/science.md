VERDICT: PASS
CONTENT-HASH: 999b960b9ada8a99
SCOPE: delta added-exercise from ec42002a596881a5 base 81db4a6fd727

## Blocking
(none)

## Polish
- content/en/FY3/fy3-10/exercises/exercises.json (fy3-10-L2-09) — the same figure pt-suorat serves fy3-10-L2-04, where vessel A is 2.00 l (0.0602 mol), while here A holds 0.0500 mol and comes out 1.66 l; each task is self-contained and correct, but a student doing both may wonder. Optional: one clause "(a different pair of vessels than in the earlier task)" in both languages; same in the Finnish.

## Checked
- fy3-10-L2-09 (new question: vessel A's volume): rigid closed vessel, ideal gas assumed in the task; read (400 K; 100 kPa) on the grid lines; V = nRT/p = 0.0500 mol * 8.31 J/(mol K) * 400 K / 100 000 Pa = 1.662e-3 m3 = 1.66 l; answer, three figures from n, tolerance 3 % fits grid-line reading.
- L2-09 consistency: the other point (200 K; 50 kPa) gives the same p/T = 0.25 kPa/K and the same V; the line goes through the origin as p proportional to T at constant V and n requires.
- L2-09 reasonableness: RT/p = 33.2 l/mol at 400 K and 100 kPa, times 0.0500 mol = 1.7 l; a real check.
- fy3-10-L1-09: n = 500 g / 39.95 g/mol = 12.52 mol, p = nRT/V = 3.047 MPa, answer 3.05 MPa; ideal gas stated; 30 times atmospheric pressure is realistic for a welding cylinder; 4 % tolerance covers other table values of M.
- Both solutions complete: given, principle and why, symbolic solution first, conversions (kPa to Pa, m3 to l, kg to g), substitution with units, rounding reason, check.
- Scripted comparison with the Finnish exercises.json: all 23 exercises have the same answers, units, tolerances, figures and numbers in the task texts. Every answers.py value is within its tolerance.
- Hash identical at start and end.
