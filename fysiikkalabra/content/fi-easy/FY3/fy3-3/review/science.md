VERDICT: PASS
CONTENT-HASH: 2ac81e9fbe169b33

## Blocking
- none

## Polish
- none

## Checked
- delta review 2026-11-10 (measurement window reset, teacher's FY3 brief): a change of T or V empties hist before the steps of the frame, so the 1,5 s window holds only hits of the new state; the piston fix maps x > right−R to BOX.x+R+(x−BOX.x−R)·V/V_old ≤ right−R, so compression adds no clamp hits and keeps speeds (T slider fixed, as the model says); expansion untouched. Node port: long-run measured/theory 0,99–1,00 at (300, 1), (300, 2), (600, 0,5), (150, 1), so p ∝ T/V is not faked; window scatter ±5 % (1 dm³) to ±12 % (2 dm³, 150 K) is pre-existing. Settling text keeps the theory value, which is the model, not a measurement; t = 0 guard gives 0 only while hidden. 'odota pari sekuntia' (≥ 1,5 s) still valid. Hashes equal at start and end.
- delta review 2026-11-07 round 2 (follow-up consistency edits): summary bullet and kelvin-scale figure label (figures.py w=300, x=72, centred on 222) now the numerical-value equation T/K = θ/°C + 273{,}15, identical to the teacher's Kaava (lesson.md:231); 0 K = −273{,}15 °C unchanged and consistent. Hashes equal at start and end.
- delta review 2026-11-07 (teacher's proofread replacement texts): kelvin formula as numerical-value equation T/K = θ/°C + 273,15, example 20 °C = 293,15 K and temperature difference 10 K = 10 °C are correct; inquiry changes are typesetting only (128 kPa = 120 kPa·313,15/293,15 rechecked). Selkokieli text carries the same meaning as fi.
- delta review 2026-11-06 (teacher's correction): Ennuste 3 title no longer says a warm gas "painaa enemmän" (reads as 'weighs more'; heating a closed gas does not change its mass or weight) but asks why the pressure of a warm gas is higher; the hook question and two feedback texts now speak of the air's pressure increasing. Physics consistent with the micro model (same particles, faster, more frequent and harder wall collisions → higher pressure). No numbers, symbols, answers or correct options changed.
- batch delta review: key_concepts, reworded sentences, photo captions, objective-form and level-policy edits, chapter-reference titles judged against the guardrails and the lesson text; restyled figure lines are styling only.
