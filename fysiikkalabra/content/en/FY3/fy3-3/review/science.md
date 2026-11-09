VERDICT: PASS
CONTENT-HASH: 52d033ece91afb31

## Blocking
- none

## Polish
- none

## Checked
- delta review 2026-11-10 (measurement window reset, teacher's FY3 brief): a change of T or V empties hist before the steps of the frame, so the 1,5 s window holds only hits of the new state; the piston fix maps x > right−R to BOX.x+R+(x−BOX.x−R)·V/V_old ≤ right−R, so compression adds no clamp hits and keeps speeds (T slider fixed, as the model says); expansion untouched. Node port: long-run measured/theory 0,99–1,00 at (300, 1), (300, 2), (600, 0,5), (150, 1), so p ∝ T/V is not faked; window scatter ±5 % (1 dm³) to ±12 % (2 dm³, 150 K) is pre-existing. Settling text keeps the theory value, which is the model, not a measurement; t = 0 guard gives 0 only while hidden. 'odota pari sekuntia' (≥ 1,5 s) still valid. Hashes equal at start and end.
- delta review 2026-11-07 round 2 (follow-up consistency edits): summary bullet and kelvin-scale figure label (figures.py w=300, x=72, centred on 222) now the numerical-value equation T/K = θ/°C + 273.15, identical to the teacher's Formula (lesson.md:231); 0 K = −273.15 °C unchanged and consistent. Hashes equal at start and end.
- delta review 2026-11-07 (teacher's proofread replacement texts): kelvin formula as numerical-value equation T/K = θ/°C + 273,15, example 20 °C = 293,15 K and temperature difference 10 K = 10 °C are correct; inquiry changes are typesetting only (128 kPa = 120 kPa·313,15/293,15 rechecked). English text carries the same meaning as fi.
- delta review 2026-11-06 (teacher's correction): Ennuste 3 title no longer says a warm gas "painaa enemmän" (reads as 'weighs more'; heating a closed gas does not change its mass or weight) but asks why the pressure of a warm gas is higher; the hook question and two feedback texts now speak of the air's pressure increasing. Physics consistent with the micro model (same particles, faster, more frequent and harder wall collisions → higher pressure). No numbers, symbols, answers or correct options changed.
- Translation review against the reviewed Finnish (teacher's procedure 2026-10-28): lesson text, formulas, worked example, inquiry.json (predictions, experiments, solutions, checks) and exit ticket compared with content/fi; every number, inline-math value with unit, formula, symbol and answer matches (automatic math/number diff clean; only language and subscript words differ).
- Physics unchanged from the Finnish: conditions stated (dilute gas, constant V and n; rigid container; extrapolation as model), recomputed key results (k = 1/3 per degC, theta_0 = -273 degC; 101 kPa * 353.15/293.15 = 121.67 kPa; slope 0.37 kPa/degC giving -270 degC) agree.
- English: natural, no Finnish words left, units and symbols (F_avg, A_rectangle, etc.) translated.
- Latest change: inquiry transfer-task solution substitution re-typeset (100·3 °C); matches the Finnish exactly.
- check_i18n.py: 0 errors for en.
