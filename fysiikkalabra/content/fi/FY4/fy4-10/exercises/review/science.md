VERDICT: FAIL
CONTENT-HASH: e7c9a7bc6c766e63

## Blocking
- exercises/solutions.md:114 (fy4-10-L3-03) — A: "Avaruudessa niihin ei vaikuta muita voimia" and "Heiton jälkeen astronauttiin ei vaikuta voimia" are false. Gravity at a station's orbit is about 90 % of g, so this teaches the "no gravity in space" misconception. — Write: "Painovoima vaikuttaa astronauttiin, työkaluun ja asemaan, mutta kaikki ovat samassa vapaassa putoamisessa, joten aseman suhteen ne liikkuvat (lyhyen ajan) kuin ilman ulkoisia voimia; heiton aikana kokonaisliikemäärä aseman suhteen säilyy, ja heiton jälkeen astronautti liikkuu aseman suhteen tasaisesti." Use the same wording in step (2).

## Polish
- exercises/solutions.md:69 (L2-02) — "muodonmuutoksiksi" is not a form of energy. — Write "energia muuttuu varusteiden ja kehon sisäenergiaksi (muodonmuutoksissa) ja ääneksi".
- exercises/solutions.md (L2-01) — the claim that compressed air pushes the bullet and the rifle with equal forces leaves out the air's own momentum. This is an acceptable simplification (C); a short "ilman massa jätetään huomiotta" would make it explicit.

## Checked
- I recomputed all 12 answers with my own formulas and they agree with answers.py: 0,050, 0,50, 0,90, 3,552, 0,20, 0,028125, 717,2 J, 70,83 %, 15 000 kg, 20,19 cm, −2,0 m/s and 120 s.
- Each rounded answer falls inside the 2 % tolerance (the largest gap is L1-04, 3,6 vs 3,552, at 1,35 %), and the significant figures follow the data.
- The signs and positive directions are consistent. L3-02 uses a nonzero initial momentum and gets −2,0 m/s, correctly downward.
- L3-01 has the right two-stage model: momentum only across the collision, then mechanical energy through the swing. The KE fraction 1/201 and the check 4 J/20 N ≈ 0,2 m are correct.
- L1-04 is physically possible (E_k 1,28 → 1,277 J), and L2-03 has e = 0,75, between the limiting cases.
- Every solution has all seven stages and is solved in symbols first. The conditions are stated in each task.
- Everything stays within FY4 scope, one-dimensional.
