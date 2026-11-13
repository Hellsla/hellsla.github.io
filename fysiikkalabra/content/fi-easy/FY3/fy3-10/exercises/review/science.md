VERDICT: PASS
CONTENT-HASH: f73ec8a5700e70a3
SCOPE: delta added-exercise from 2d45d7f23d815a16 base 81db4a6fd727

## Blocking
(none)

## Polish
- content/fi-easy/FY3/fy3-10/exercises/exercises.json (fy3-10-L2-09): L2-04 uses the same figure pt-suorat and states that both vessels are 2,00 l (n_A = 0,0602 mol). L2-09 gives n_A = 0,0500 mol and asks for A's volume (1,66 l). Each task holds on its own, but a student who does both meets two volumes for "vessel A" in the same graph. A phrase such as "Toisessa kokeessa ..." in L2-09 would remove the clash. Same in the Finnish.

## Checked
- L2-09 now asks for vessel A's volume. The ideal-gas law and a rigid closed vessel are stated, so pV = nRT applies and V = nRT/p.
- Recomputed: V = 0,0500 · 8,31 · 400 / 100 000 = 1,662·10⁻³ m³ = 1,66 l. The point (200 K; 50 kPa) gives the same value, because p/T = 0,25 kPa/K. answers.py gives 1,662.
- The conversions are right (100 kPa = 10⁵ Pa, 1 m³ = 1000 l). 3 s.f. follow from n = 0,0500 mol. Tolerance 3 %.
- The reasonableness check is a real one: the molar volume at 400 K and 100 kPa is RT/p = 33,2 l, so 0,05 mol takes about 1,7 l.
- Figure pt-suorat: A's line passes the grid crossings (200; 50) and (400; 100). The description lists them and does not give n or V.
- L1-09 unchanged: n = 500/39,95 = 12,52 mol and p = 3,047 MPa, so 3,05 MPa.
- The script compared fi-easy with the Finnish: answers, units, tolerances, figure ids and numbers are identical. The only extra figure, "1", comes from the gloss in L3-04's solution.
- Hash the same at start and end.
