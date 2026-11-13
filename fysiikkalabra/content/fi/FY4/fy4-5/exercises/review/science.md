VERDICT: PASS
CONTENT-HASH: b109d86dc61f2dd3
SCOPE: delta added-exercise from efb48162357b8d03 base 7db0992d648a
## Blocking

## Polish
- content/fi/FY4/fy4-5/exercises/exercises.json:285 (L2-08) — a $2{,}5\,\text{kg}$ "kiekko" is about 15 times an ice-hockey puck's mass; harmless, but "kiekko" makes a reader picture one — "curlingkivi" style object or "jääkiekkoa raskaampi kiekko"/"metallikiekko" would read as realistic. The figure description also says "Jääkiekko".
- L2-08 — the forces have no named causes (two ropes or two players' sticks); adding one would match the chapter's rule that every force has an aiheuttaja.

## Checked
- Recomputed from figures.py: F_1 = (10, 12) N, F_2 = (−4, −4) N at sq/2,0 px per N, i.e. (5, 6) and (−2, −2) squares; ΣF = (6, 8) N, |ΣF| = 10 N, a = 10 N / 2,5 kg = 4,0 m/s² at 53,1°; equals answers.py and exercises.json. Voimakuvio fence magnitudes 15,62 N at 50,19° and 5,657 N at 225° correct.
- Readable to tolerance: body centre P on a grid crossing, corners at P ± sq, so both tails and both tips (6 and −7 squares; −3 and +3) fall on drawn crossings inside the grid; scale bar 4,0 N = 2 squares consistent with 2,0 N per square.
- FBD(a_dir=(3, 4)) is only a check (net force along (3,4)), no acceleration or net-force arrow is drawn; description gives the same squares and gives nothing away.
- Physics: frictionless horizontal ice, weight and normal force cancel vertically (stated in Periaate), ΣF = ma in components; Järkevyys correct (10 N < 21,3 N, 6-8-10 triangle).
- Two significant figures justified by m = 2,5 kg and 2,0 N per square.
- Not a repeat: L1-02 collinear forces on a 10 N grid, L2-04 perpendicular pulls given as numbers, L2-07 measured oblique forces with angles; L2-08 reads oblique components from a grid.
- Hash b109d86dc61f2dd3 at start and end.
