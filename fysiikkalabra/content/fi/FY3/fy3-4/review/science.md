VERDICT: PASS
CONTENT-HASH: 35ef1dd72b43d7e8

## Blocking

## Polish
- meta.json — still has no `"solutions": "all"`, which CLAUDE.md Lesson form 7 asks for. — Add it.
- solutions.md:71 (L2-02, Vastaus) — "350 kPa = 3,50·10² kPa" says the data has three figures, but 350 kPa as written has two or three. — Say that the result is given to three figures by convention, or write the datum as 350 kPa and give 36 m. Either is within tolerance.
- lesson.md (Esimerkki, Tulos) — "150 cm² on annettu kahdella numerolla" has the same ambiguity (it could have two or three figures); 1,8 kN is still a defensible answer.

## Checked
- Round-2 fix: exp-1's solution now gives 9,8 kPa/m with two figures, limited by Δh = 5,0 m. The figures follow sim.js (readouts 150,1 and 199,1 kPa at 5 and 10 m; 49,0/5,0 = 9,80). The comparison with ρg = 9,81 kPa/m is kept, and the stored 9.81 with tolerance 0,02 accepts 9,8. The mistakes 9810 and 19,9 are right.
- L3-03: now gives 19,0 kPa only. The justification (sum limited by the oil term 3,3 kPa, known to 0,1 kPa) is right, and the stored 19 with tolerance 2 % accepts it.
- I recomputed all 12 answers.py lines independently in one script. They all match exercises.json within tolerance. Each solution's principle applies for the reason it states, the unknown is solved symbolically first, and the cm², kPa, bar and MPa conversions are right.
- Reasonableness checks recomputed: L2-01 ≈ 40 atm and ×133 versus a bare foot; L2-04 ≈ 330 kg; L3-01 25 × 56 cm and 28 kPa for a shoe; L3-02 hose cross-section 1 cm² and ratio 2500; L3-03 19 620 − 588,6 Pa; L1-04 6 cm² per leg.
- Worked example: 117 720 Pa, 219 kPa, 1765,8 N → 1,8 kN, ratio 2,2, ≈ 180 kg.
- siirto: 0,757 m; its mistakes 10,3 and 0,000757 are right. check-2: 891,9 → 890 kg/m³ (two figures from 70 kPa and 8,0 m); the mistakes 2180 and 0,892 are right.
- pred-1 and pred-2: 150/199 kPa, 49 → 98 kPa, 122 kPa and 223 kPa (+12 %). Each option's feedback is right. virhe 29 kPa, check-3 ≈ 1,8 N, dam ≈ 290 kPa and the exit ticket's 49/150 kPa are right.
- sim.js implements p₀ + ρgh and states its limits. exp-1 locks ρ and exp-2 locks h, and simState carries pOver and pTotal.
- Scope stays inside FY3 (p = F/A and hydrostatic pressure, with force as a scalar normal to the surface).
