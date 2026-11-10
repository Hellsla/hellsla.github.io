VERDICT: PASS
CONTENT-HASH: d97ae414b55734f2

## Blocking
- none

## Polish
- none

## Checked
- delta review 2026-11-10 (measurement window reset, teacher's FY3 brief): a change of T or V empties hist before the steps of the frame, so the 1,5 s window holds only hits of the new state; the piston fix maps x > right−R to BOX.x+R+(x−BOX.x−R)·V/V_old ≤ right−R, so compression adds no clamp hits and keeps speeds (T slider fixed, as the model says); expansion untouched. Node port: long-run measured/theory 0,99–1,00 at (300, 1), (300, 2), (600, 0,5), (150, 1), so p ∝ T/V is not faked; window scatter ±5 % (1 dm³) to ±12 % (2 dm³, 150 K) is pre-existing. Settling text keeps the theory value, which is the model, not a measurement; t = 0 guard gives 0 only while hidden. 'odota pari sekuntia' (≥ 1,5 s) still valid. Hashes equal at start and end.
- delta review 2026-11-07 round 2 (follow-up consistency edits): summary bullet and kelvin-scale figure label (figures.py w=300, x=72, centred on 222) now the numerical-value equation T/K = θ/°C + 273{,}15, identical to the teacher's Kaava (lesson.md:231); 0 K = −273{,}15 °C unchanged and consistent. Hashes equal at start and end.
- delta review 2026-11-07 (teacher's proofread replacement texts): kelvin formula as numerical-value equation T/K = θ/°C + 273,15, example 20 °C = 293,15 K and temperature difference 10 K = 10 °C are correct; inquiry changes are typesetting only (128 kPa = 120 kPa·313,15/293,15 rechecked).
- delta review 2026-11-06 (teacher's correction): Ennuste 3 title no longer says a warm gas "painaa enemmän" (reads as 'weighs more'; heating a closed gas does not change its mass or weight) but asks why the pressure of a warm gas is higher; the hook question and two feedback texts now speak of the air's pressure increasing. Physics consistent with the micro model (same particles, faster, more frequent and harder wall collisions → higher pressure). No numbers, symbols, answers or correct options changed.
Re-review after typesetting round (word-level diff against the passed versions). Only change: inquiry.json activity 17 solution, Sijoitus line. Old nested fraction 100 / (1/3 1/°C) replaced by 100 · 3 °C: 100 ÷ (1/3 per °C) = 300 °C, so θ0 = 27 °C − 300 °C = −273 °C unchanged; k = 1/3 1/°C, answer, Järkevyys chain and absolute-zero remark untouched and correct (linear extrapolation, p ∝ T; −273,15 °C stated). Unit is correct (°C), \cdot used, valid LaTeX. Learning-goal verb changes (-maan/-mään) carry no physics.
