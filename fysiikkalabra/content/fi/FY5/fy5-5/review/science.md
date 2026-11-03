VERDICT: PASS
CONTENT-HASH: 1fa0e4e20ea43329

## Blocking

## Polish
- inquiry.json ennuste-1 — the reworded distractor "Suurempaan, koska suurempi massa vetää enemmän" now uses almost the same reasoning as "Pienempään, koska suurempi lohkare vetää voimakkaammin". Both are wrong and the feedback fits, but the two options are less distinct than before. The pedagogy reviewer may want to look at it.
- lesson.md "Gravitaatio maailmankaikkeudessa" — the structure-formation story leaves out dark matter. That is a fair simplification (C) at FY5 level. No change needed.

## Checked
- Round-1 polish items are fixed. The apple force is now 1,96 N, so 9,8 m/s² checks out. The g table says it leaves out the Earth's rotation and that 9,81 is used in the book. The lesson-answers.py comment is 2,702e-3. The kuvaaja caption now states the 10 t masses.
- Recomputed in one script: the g table (1,62 / 3,71 / 9,80 / 24,8 / 274), 0,28 µN, 686 N, 3·10⁻²⁵ m/s², the worked example 1,99·10²⁰ N, the Moon's acceleration 2,7·10⁻³ m/s², and 8,9 m/s² at 300 km.
- Inquiry numbers are right:
  - koe-1: 83,4 / 250 µN, 8,34 / 41,7 nm/s²
  - koe-2: 742 / 185 / 82,4 / 66,7 µN, F·r² = 6674
  - the numeric answers and their mistake values
  - kuukoe: 2,724 vs 2,698 mm/s²
  - siirto: 2640 km
  - etsi-virhe: 4427 / 8,93
  - tarkistus-1: 130 / 785 N; tarkistus-2: 9,0 N
- Exactly one correct option in every choice item. Every distractor is wrong, and its feedback gives the right reason.
- koe-1 locks m1 and r; koe-2 locks both masses. simState gives the measured keys.
- sim.js: F = γm1m2/r², a = F/m and F1 = F2, with the arrows on shared scales. The spheres (R = 0,93 m) do not overlap at 2 m, and the box's 0,3 mm per minute checks out.
- Figures: kuvaaja and planeetat are to scale (checked coordinates), and the third-law pairs are drawn equal.
- Conditions are stated: point masses or spherical symmetry, r measured between centres, air resistance left out.
- Causal account of structure formation: gravity always attracts, charges cancel out, and its range is long.
- The exit ticket and the model answers agree with the theory. Simulation numbers are called model values.
- Scope is FY5: no ω, γ is used, and orbital speeds are deferred to the next chapter.
