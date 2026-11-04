VERDICT: FAIL
CONTENT-HASH: 666a811032b40963

## Blocking
- solutions.md:150 (fy6-6-L2-05 Periaate) — **B**: "lämpötilaero kasvaa, ja samalla sen mukana kasvaa ympäristöön siirtyvä teho. Siksi ΔT on suoraan verrannollinen tehoon" — the balance gives a steady state, not proportionality; ΔT ∝ P holds only if the heat flow to the air is about proportional to the temperature difference (moderate ΔT). Fix: "Jos ympäristöön siirtyvä teho on likimain verrannollinen lämpötilaeroon, kuten pienillä lämpötilaeroilla, vakiintunut ΔT on verrannollinen tehoon; P = 0 antaa ΔT = 0, joten suora kulkee origon kautta."

## Polish
- exercises.json:75 vs :115 (fy6-6-L1-07 vs L2-03) — the same model (0,25 W rating, square root) sits at level 1 and at level 2. L1-07 even adds an mA conversion. Move L1-07 to level 2 or simplify it.
- solutions.md:195 (fy6-6-L3-05 Vastaus) — "ei pääse jäähtymään" overstates it: a rolled cord cools poorly. Write "jäähtyy huonosti", and since this is a safety situation, add one clause: a heavily loaded cord drum is unrolled, and its rated current must not be exceeded.
- solutions.md:127 ff. (fy6-6-L1-07) — the Vastaus says "34 mA", but the answer box holds 33,7. Use one value.

## Checked
- Hash 666a811032b40963 at start and end.
- All eight new answers recomputed in one script with my own formulas and compared with exercises.json and answers.py: L1-07 33,7 mA; L1-08 7,2 W; L2-05 12,1 K/W; L2-06 172 %; L2-07 3,0 W; L3-04 822 W; L3-05 152,5 W. All agree within tolerance.
- L2-05: R = U/I ≈ 47 Ω constant; 5 % tolerance matches the accepted 11,5–12,7 K/W.
- L2-06: R grows from 5,1 Ω to 17,3 Ω, which is realistic for a small bulb. "+300 % with constant R" is correct (×4).
- L3-04: R₁ = 48,1 Ω, R₂ = 77,9 Ω, parallel check 1779 W ≈ 1780 W. At 253 V, R₁ gives 1331 W < 1400 W and R₂ gives 822 W > 750 W. c) right: both ×1,21, R₂ already at 91 %.
- L3-05: the cord resistances match copper (100 m of conductor: 2,24 Ω at 0,75 mm² and 0,67 Ω at 2,5 mm²).
- L2-07: one series current of 0,50 A; the correction says that current is not used up and that P = UI decides.
- L1-06: exactly one correct option.
- Notation (P = UI = RI² = U² : R, E = Pt) and the series/parallel choice of formula match the lesson; scope and plan fit.
