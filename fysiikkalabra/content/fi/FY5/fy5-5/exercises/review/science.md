VERDICT: PASS
CONTENT-HASH: d441cab8d0d7b4e9

## Blocking

## Polish
- exercises.json:344 (fy5-5-L3-05) — b) asks for the period that makes the scale read zero at the equator: 84,4 min. That is the same task and answer as the existing fy5-6-L3-03 (84,4 min). Weightlessness on the ground also belongs to fy5-6. — Keep a) and c) and replace b), for example: "Kuinka suuri olisi vaa'an lukema, jos vuorokausi olisi 2,0 h?" (a_n = 4π²R/T² = 1,94 m/s², N = 488 N). Or ask how many times faster the Earth would have to spin before the reading drops by 1 %.
- solutions.md:257 (L3-05 Vastaus, part c) — "gravitaatiovoimasta osa kuluu ympyräliikkeen keskeisvoimaksi" can be read as the centripetal force being a separate share of gravity. fy5-4 defines keskeisvoima as the resultant. — Write: "kokonaisvoiman mg − N on oltava m a_n kohti keskipistettä, joten N = mg − m a_n < mg". On line 234, also fix "keskipistä" → "keskipistettä" (three times). In Vastaus, "ei kierry" → "ei kierrä".
- solutions.md:206 (L2-07 Järkevyys) — "Tulot poikkeavat toisistaan alle 0,2 %": the spread from 3,9923 to 3,9840 is 0,21 %. — Write "noin 0,2 %". Also on line 183 (L2-06): "noin ±2 %" is really +2,4 % / −1,6 %. Write "enintään noin 2,5 %".
- solutions.md (L2-06 Vastaus) — "kolme merkitsevää numeroa kuten voimissa", but three of the four forces and every r have two significant figures. — Justify the third digit by averaging (the tolerance of 2 % already allows it), or give 6,7·10⁻¹¹.
- exercises.json:80 (L1-07 answer/choice) — "etäisyys neljännesosaa sen" is not Finnish. — Write "etäisyyden kaksinkertaistuminen pienentää sen neljäsosaan". This applies to both the answer and the correct choice. (Language only.)

## Checked
- The hash is the same at the start and the end (d441cab8d0d7b4e9).
- I recomputed all 20 answers in one script with my own formulas. All of them match exercises.json and answers.py: 1,2468; 6,72; 3,989·10¹⁴; 5508 kg/m³; 84,44 min, and the 12 old answers as before.
- L2-05: g = 11,18 / 9,006 / 11,23 m/s². In c), the Saturn/Neptune mass and R² factors (5,57 and 5,59) cancel to within 0,45 %, as stated. NASA data are real.
- L2-06: the γ values 6,88 / 6,67 / 6,72 / 6,61 are right. The slope γMm ≈ 2,0·10⁻¹² N·m² is right. A 1,5 kg and a 20 g lead sphere fit into r = 4,0 cm (radii 3,2 cm and 0,75 cm).
- L2-07: the data agree with GM = 3,986·10¹⁴. The 1/r² origin-line claim is right.
- L3-04: M = 5,966·10²⁴ kg and ρ = 5508 kg/m³. The rock-density argument is valid. Cavendish's 5,45 g/cm³ is right.
- L3-05 a): v = 463,8 m/s, a_n = 0,0337 m/s², N = 606 N against mg = 608 N. The force equation mg − N = m a_n has the right signs and direction.
- MC L1-06, L1-07 and L1-08: each has exactly one correct option, and every feedback is right. In L1-08, 17² ≈ 290 is right.
- Scope: everything stays inside the gravitation law and g = γM/r², plus the fy5-4 prerequisite (normal acceleration) in L3-05. No ω is used.
- The plan is met: the MC on the inverse square and the third law, the planet table, Cavendish data and the 1/r² graph, and Earth's mass from g and R.
- Every new solution solves the unknown symbolically first and has a real reasonableness check.
