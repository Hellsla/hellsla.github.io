VERDICT: PASS
CONTENT-HASH: 73f0ca12470c1103

## Blocking

## Polish
- inquiry.json:713 (data, mistakes value 10) — 10 is 2,0 % from 9,8, inside the 3 % tolerance, so the page accepts it before the mistake can fire — drop this mistake entry (or lower the tolerance to 0,015 if a reading of 5,0 m/s should be corrected).
- inquiry.json:713 — the feedback sentence "Laskit nopeuden viimeisestä pisteestä viivan ruudukkoviivaan pyöristäen" is garbled — e.g. "Pyöristit suoran arvon ruudukkoviivaan 5 m/s; suora on hetkellä 0,50 s hieman sen alapuolella."
- answers.py:1173 — t_d/v_d (1.1, 1.9, 3.0, 3.9, 5.0) do not match the table (1,0, 2,0, 2,9, 3,9, 4,9) and are unused — remove them or copy the table.
- solutions.md L3-03 Vastaus — g·t with t = 3,0 s (2 sf) is 29 ± 0,5 m/s, so the difference is about 4 m/s; "4,4 m/s" with a decimal-places argument overstates precision — say the time limits it, or give t as 3,00 s.

## Checked
- All 12 exercise answers and 6 inquiry/example answers recomputed independently: identical to answers.py; every mistake value (19,6; 29,4; 22,2; 3,7; 11,0; 0,327; 30; 0,1) is the error it names.
- Worked example: v = gt = 14,7 m/s ≈ 15 m/s = 53 km/h from the unrounded value; 2 sf justified; check real.
- Solutions: all seven parts present, symbolic first, conversions (ms, km/h) right; L2-03 Δv = gΔt correctly stated for a body not starting from rest.
- Figures to scale: free-fall positions 0/4,9/19,6/44,1 m, arrows 1:2:3; same-fall heights and equal arrows; vt-graph points 9,81/19,6/29,4/39,2 and slope 9,81 m/s²; data-graph points match the table, fitted line slope 9,81 (LSQ through origin 9,78).
- Sim: v = gt in vacuum, v = v_T tanh(gt/v_T) with K = ½ρC_dA for air; ruler 0–80 m holds the 78,5 m 4-s fall; limits stated under Mallin oletukset; values called model values.
- Model answer air values recomputed: 0,1 kg → 10,5 m/s, 10 kg → 37,5 m/s at 4,0 s (correct).
- Experiments: exp-1 locks environment and masses, varies t; exp-2/3 lock environment, t, m_A and vary m_B; simState gives vA, vB; correct options and feedback consistent with the model.
- Predictions, Etsi virhe, checks and exit ticket: correct options and physics right; Apollo 15 hammer–feather correct.
- Scope: v = gt as a linear (t,v) model inside FY1 notes; mass-independence taken as an experimental result, forces deferred.
