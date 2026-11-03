VERDICT: FAIL
CONTENT-HASH: 3e396d934e202161

## Blocking
- exercises/solutions.md:39 (fy7-3-L1-04, Järkevyys) — B: "toisen johtimen vastakkaissuuntainen virta heikentää kenttää, joten johdon kenttä on vielä pienempi" holds only at points that are not beside the other conductor. Counterexample: the conductors 3 mm apart and the point on the line beyond the second conductor, 5 mm from the first. There the return conductor's field (2 mm away, opposite current) points the same way, and the net field is 0,15 mT, more than 0,10 mT. — Fix: "useimmissa kohdissa ja varsinkin kauempana johdosta kenttä on vielä pienempi".

## Polish
- solutions.md L3-02 — "Arvio on karkea, koska todellinen käämi ei ole pitkä" is fine. Adding the direction would help: for l/d = 1,6 the centre field is about 85 % of μ₀NI/l, so more wire is needed.

## Checked
- Recomputed all 12 answers in one script with my own formulas; all within tolerance: 80 µT, 3,016 mT, 10 µT, 0,10 mT, 1,005 mT, 3,979 A, 8,57 cm, 2,50 mT, 80 µT, 2,02 A, 15,0 km, 4,0 cm.
- answers.py implements the same physics: straight long wire, long coil, N = L/(πd), vector addition with signs.
- L2-04: opposite currents add at the midpoint. L3-03: parallel currents cancel between the wires, and the zero point lies nearer the weaker current.
- L3-01: the wire's field below an N–S wire is horizontal and E–W, so tan α = B_j / B_h. The 14 µT horizontal component is plausible for Finland.
- Every solution has the full structure (symbolic first, conversions, significant figures from the limiting datum, a real reasonableness check). Scope: FY7 central contents only.
