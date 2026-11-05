VERDICT: PASS
CONTENT-HASH: dac3457805b63750

## Blocking

## Polish
- exercises.json:146 (L2-05) — the example data are under-dispersed: the sample standard deviation is 4,4, but √N̄ = 7,0. 9 of 10 values lie inside ±√N̄, where about 7 would be expected. Widen a few values, e.g. 38 and 59 instead of 42 and 57.
- solutions.md:155 (L2-06 Kuvaajan lukeminen) — the solution calls the curve "kaareutuva" and then interpolates linearly between two raw points (5,6 mm). Say that the value is read from a smooth curve drawn through the points (≈ 5,5 mm), as the guardrail says ("A broken line through raw data is not a model").
- solutions.md:159 (L2-06) — "kaksi merkitsevää numeroa kuten tausta- ja paksuusarvoissa": a better reason is the scatter of the five estimates (5,4–5,6 mm).
- solutions.md:176 (L3-04 d) — "suhteellinen epävarmuus pienenee tekijällä 1/√N" should read "on verrannollinen lukuun 1/√N".
- exercises.json:252 (L2-07) — 3 mm of Al stops typical betas, but not the hardest ones (Y-90, 2,3 MeV, has a range of about 4 mm in Al). Within the lesson's model ("muutama millimetri alumiinia") this is a fair simplification. Adding "lähes" to the feedback, or "tavallisen beetalähteen", would make it exact.

## Checked
- Hash dac3457805b63750 at the start and at the end.
- All 17 numeric answers recomputed in one script (new tasks: 1530/min; 4,545 %; 5,499 mm; 11,99 mm; 2,997 kBq). All are within 1 % of exercises.json and answers.py.
- L2-06: the five d½ values (5,58; 5,46; 5,59; 5,44; 5,43) and the mean 5,50 mm match lead's 5,5 mm for 662 keV. A ln-fit gives 5,43, which is within tolerance.
- L3-04: the d½ values (12,32 … 11,93) give a mean of 11,99 mm, which identifies iron. NIST check: μ/ρ(Fe, 662 keV) = 0,074 cm²/g gives 11,9 mm. c) 79,6 mm and d) 4,9 % vs 2,0 % are correct.
- L3-05: R = 16,4 1/s, T = 0,3649, A = R/(Tη). In d), both assumptions make the estimate too low (GM gamma efficiency is small; Cs-137 has about 85 % gamma yield). Correct.
- MC L1-06, L1-08, L2-07: exactly one correct option in each. The feedback is right: alpha range tens of µm in tissue and a few cm in air, the GM pulse independent of radiation type, and gamma attenuation with no range.
- Levels fit. There is no duplicate of the existing tasks (L2-06 and L3-04 use background subtraction like L2-03, but with data tables and averaging).
