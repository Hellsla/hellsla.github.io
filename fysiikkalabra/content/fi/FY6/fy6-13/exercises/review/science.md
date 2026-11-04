VERDICT: PASS
CONTENT-HASH: f5fcd47fe45cc762

## Blocking

## Polish
- solutions.md:140 (L1-08): the Vastaus says "noin 1,4·10² mJ, kaksi merkitsevää numeroa", but 140 is 2,8 % from 144. The checker would mark it "Lähellä", not correct. Fix: give the answer as $144\,\text{mJ}$ only (1000 µF and 18 V carry enough digits), or set `tolerance` to 0.03.
- solutions.md:147 (L2-05) and :175 (L3-04): the slope is read from the origin and the last raw point (567/12 and 1201/12), but the Muunnokset then use the least-squares 47,2 µF without saying where it comes from. Fix: read the slope from two points far apart on the drawn fitted line, and say that 47,2 is that line's slope (guardrail "Fits").
- exercises.json L2-06, option 2: "jännite on silloin noin puolet lähteen jännitteestä" is false for 2–3 s (5,5–6,9 V of 9,0 V). Fix: move this distractor to 1–2 s (3,5–5,5 V) and change its feedback number to 2,0 V.
- Plan deviation (not physics): the plan's error-analysis task was "nettovaraus on Q". L2-07 tests the QU vs ½QU error instead, and L2-06 has only a charging curve, no discharging curve. Both are fine as physics; the planning side should decide whether they are acceptable.

## Checked
- One script recomputed every new answer: L1-08 144 mJ; L2-05 fit 47,21 µF → 3,40 mJ (raw triangle 3,40); L2-07 63,4 mJ, QU = 127 mJ; L3-04 k = 100,0 V/s → C = 150 µF, W = 243 J, P = 48,6 kW, charging time 18 s; L3-05 teflon 1500 V, 3,72 nF, 4,18 mJ; glass 350 V, 9,92 nF, 0,607 mJ; ratio 6,89. All match answers.py.
- L2-06 data follow an RC charge (τ ≈ 2 s, U → 9 V). The steps 3,5/2,0/1,4/0,8/0,5/0,3 V match the solution and every feedback.
- L3-05 c: W = ⅛ε₀ε_r E_max² A d is right, and the ratio (2,1·60²)/(5,6·14²) = 6,89 agrees.
- L3-04: constant-current charging (U ∝ t) is linear and stays within the scope note (no exponential). The model assumes full discharge in 5,0 ms. The safety reasoning is correct and exact.
- L1-06 and L1-07: exactly one correct option each, and every distractor's feedback is right. L1-07 option 4 has the right outcome for the wrong reason, which is acceptable.
- L2-07: the solution says what the lesson says (half of QU goes to internal energy of wires and resistors).
- Levels 8/7/5, tolerances, symbols as in the lesson; no duplicate of an existing task.
- Hash identical at start and end.
