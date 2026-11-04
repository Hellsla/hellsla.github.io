VERDICT: PASS
CONTENT-HASH: 005b36e1c19fdf68

## Blocking
- (none)

## Polish
- solutions.md fy7-3-L2-05 Vastaus — "kolme merkitsevää numeroa kuten mittaustulokset", but l = 0,30 m and the currents have two; the tolerance (±4 %) already accepts 1,3 — round to 1,3 or give l as 0,300 m in the task.
- solutions.md fy7-3-L2-05 Järkevyys (B) — "Vakiotermi 0,06 mT on lähellä Maan kentän suuruutta 0,05 mT, kuten pitääkin": the offset is the Earth field's component along the coil axis plus the sensor's zero, not the full field — "on samaa suuruusluokkaa kuin Maan kenttä, joka on osa vakiotermiä".
- solutions.md fy7-3-L2-06 Kuvaajan lukeminen — "poikkeavat toisistaan alle 2 %, mikä on mittausepävarmuuden sisällä": they differ from the mean by under 2 % (from each other by up to 3,8 %), and no uncertainty is given — "poikkeavat keskiarvosta alle 2 %, joten tulo on käytännössä vakio".
- solutions.md fy7-3-L2-07 Mallivastaus — the plan asks also what Earth's field does; add one sentence: Earth's field adds a constant term, removed by zeroing the sensor with the current off (it does not change the slope).
- exercises.json fy7-3-L3-04 — same compass setup as L3-01 (one wire, not the plan's two wires); acceptable as its data/fit version, but update docs/exercise-bank/FY7.md to say what was made (also L3-05 d) instead of the "kenttä ulkopuolella" misconception task).

## Checked
- Recomputed all 18 numeric answers in one script with my own formulas; all equal answers.py: new ones 4,712 mT, 314, 1,256 µVs/(Am) (LSQ slope 2,512 mT/A, intercept 0,059 mT), 53,7 µT (I = 8,05 A), 15,99 µT, 5,28 mT.
- L1-06: current up, seen from above, counter-clockwise; exactly one correct option, every distractor's feedback right.
- L2-07: sensor reads B cos 60° = 0,50 B; one correct option, option 4 (right sign, wrong cause) correctly rejected.
- L3-04: tan α/I constant to 2 %; free fit intercept 0,003, so a line through the origin is justified; tabulated angles agree with B_h = 16 µT within 0,3°; c) reasoning (arctan saturates at 90°) correct.
- L3-05: N = 318, l = 0,175 m (l/d = 5,8, long-coil formula stated as assumed), R = 2,60 Ω, I = 2,31 A, B = μ₀I/d_e check; d) halving (2,64 mT) correct.
- Levels 8/7/5; new tasks inside fy7-3 scope (FY6 R = ρl/A, I = U/R allowed at level 3); notation matches the brief; every new solution complete, symbolic first, real reasonableness check.
