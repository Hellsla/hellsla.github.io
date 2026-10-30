VERDICT: PASS
CONTENT-HASH: 051efb6706e3999f

## Blocking

## Polish
- exercises.json:98 (L3-03) — "Astronautin massa avaruuspukuineen on 120 kg" can be read as including the tool he holds (117 kg → 117 s). Rounded to two significant figures, 117 s is still 1,2·10² s and inside the tolerance, so this is not blocking. — Write "ilman työkalua" to make it explicit.
- solutions.md L2-02 Järkevyys — "muuttuu … muodonmuutoksiksi, sisäenergiaksi ja ääneksi": a deformation is not a form of energy. — Write "muuttuu muodonmuutoksissa sisäenergiaksi ja ääneksi".

## Checked
- I recomputed all 12 answers with my own formulas in one script, and all agree with answers.py: 0,050; 0,50; 0,90; 3,552; 0,20; 0,028125; 717,2 J; 70,8 %; 15 000 kg; 20,19 cm; −2,0 m/s; 120 s.
- L1-04 is physically possible: E_k is 1,28 J before and 1,277 J after, which does not exceed the elastic limit (elastic v_A' = −0,444 m/s).
- L2-03 lies between the perfectly inelastic case (33 %) and the elastic case (100 %), and the solution says so correctly.
- L3-01 uses momentum across the capture and mechanical energy across the swing. The tension does no work, and the solution states that.
- L3-02 uses the non-zero initial momentum Mv correctly. L3-03 justifies the free-fall frame of the station correctly.
- Each solution states the condition for conservation: the negligible impulse of the external forces, or friction neglected.
- Each answer rounded to the data's two significant figures stays inside its tolerance. Units and conversions (g → kg, m → cm) are correct.
- Notation matches the lesson: signed v before and v' after. Nothing uses fy4-9's v₀/F_ka, and there is no need for it.
- The scope is FY4, one-dimensional; only the ballistic pendulum combines this chapter with energy conservation from fy4-8.
