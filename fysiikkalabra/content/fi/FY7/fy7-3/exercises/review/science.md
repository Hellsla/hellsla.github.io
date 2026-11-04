VERDICT: PASS
CONTENT-HASH: 22c488369ee7ef37

## Blocking
- (none)

## Polish
- solutions.md:137 fy7-3-L2-06 d) — 0,50 cm lies outside the measured range 1,0–4,0 cm, so the 1/r law is extrapolated; add "oletetaan, että johdin on paljon ohuempi kuin 0,50 cm ja 1/r-riippuvuus jatkuu mittausalueen ulkopuolelle".
- solutions.md:123–124 fy7-3-L2-05 — the read-off slope 2,51 mT/A gives 1,255 µVs/(Am), and the Sijoitus jumps to 1,26; write "= 1,255 · 10⁻⁶ ≈ 1,26 · 10⁻⁶" (or read 2,512 from the fit) so the rounding is visible.
- docs/exercise-bank/FY7.md:21 (carried over from round 1) — Taso 3 still names the two-wire compass task and the "kenttä ulkopuolella" misconception task; record what was made: L3-04 (one wire, tan α against I, fit) and L3-05 d) (wire length doubled, single layer).

## Checked
- Round 2. Round 1 had no Blocking items; all four round-1 Polish items are fixed: l = 0,300 m (three figures, tolerance range 1,21–1,31 = ±4 %), offset "samaa suuruusluokkaa kuin Maan kenttä … loput anturin nollakohtaa", "poikkeavat keskiarvostaan alle 2 %" (161/158/164 → −1,9 %/+1,9 %), Earth-field sentence added to L2-07.
- Recomputed all 18 numeric answers in one script with my own formulas; all equal answers.py and exercises.json within tolerance (L2-05 LSQ slope 2,512 mT/A, intercept 0,059 mT; two-point slope (7,59 − 0,06)/3,0 = 2,51; check value at 1,5 A 3,83 mT).
- L2-06 new d): B·r = 161 µT cm → 322 µT ≈ 320 µT; answers.py comment agrees; not in the answer box.
- L1-06 and L2-07 choices reordered and reworded: still exactly one correct option each, every distractor wrong and its feedback right.
- L1-07, L1-08: "pitkä paksuuteensa verrattuna" moved before the question; physics unchanged.
- L3-04 a) now asks the student to find the linearising quantity (tan α); Periaate gives the reason; fits level 3 (YO-style data interpretation). Free-fit intercept 0,003, so the line through the origin is justified; B_h = 15,99 µT.
- L3-05 d): added two-layer remark correct (N doubles, l same, I halves → B unchanged); task now states "Käämi pysyy yksikerroksisena", so the single-layer answer 2,6 mT is determined.
- Levels 8/7/5; all new tasks inside fy7-3 scope; notation matches the brief; every changed solution complete and symbolic first.
- Hash identical at start and end.
