VERDICT: PASS
CONTENT-HASH: 129dcdd5c074199d

## Blocking

## Polish
- lesson.md "Mistä paine syntyy?" — "Nesteen paine syntyy nesteen omasta painosta" leaves out p₀, which comes two paragraphs later (C) — clearer: "Nesteen paine kasvaa syvyyden mukana nesteen oman painon vuoksi".
- inquiry.json pred-1 wrong options — "Mittauksesi näyttävät" — use "Mallin arvot", as the correct option does (the sim gives model values).
- inquiry.json exp-1 solution, Vastaus — the two figures are blamed on "syvyysero 5,0 m", but the slider sets depth exactly; rounding of the readout is what limits the answer (ρgh readout gives 9,81).

## Checked
- One script: 300 kPa (pysähdy); 294 ≈ 290 kPa at the 30 m dam; example 117 720 Pa, 218,7 ≈ 219 kPa, 1765,8 N ≈ 1,77 kN ≈ 180 kg; exit ticket 49/150 kPa; G = 29 430 N, mistakes 3000 N and 306 N.
- pred-1/pred-2: 150,1 → 199,1 kPa (×1,33); ρ = 1240: ρgh 98,1 → 121,6 kPa (+24 %), p 199,1 → 222,6 kPa (+12 %). One correct option each, every distractor's feedback right. The sim's toFixed values (49,1/150,1/199,1) match the quoted numbers.
- exp-1: 9,81 kPa/m, tolerance 2 %; mistakes 9810 and 19,9 right. exp-1 and exp-2 lock the right variable; simState has pOver and pTotal; slider steps reach 720/1000/1025/1240.
- Siirto: h = p₀/(ρg) = 0,757 m, mistakes 10,3 and 0,000757 right; check-2: 891,9 → 890 kg/m³, mistakes 2180 and 0,892 right.
- check-1, check-c2, virhe (h = 3,0 m → 29 kPa), check-3 model (29 kPa; 0,6 cm² → 1,8 N, an estimate): right physics, one correct option.
- Figures: pressure-depth is to scale (101 and 199,1 kPa within 1 px); in pressure-area, A₂ = 3A₁ with equal arrows; the water-column derivation is right.
- sim.js implements p = p₀ + ρgh. The arrows from four sides show that pressure acts in every direction. The over-pressure mode draws the line through the origin. Mallin oletukset states the limits; the conclusion calls the values model values.
- Example: the window force uses only the overpressure, which is right because the room is at normal pressure. The diver remark is correct.
- Scope: FY3 "paine ja hydrostaattinen paine". Force is used as a scalar perpendicular to the surface, as the slot says, and no Newton's laws appear. The formula name is the teacher-approved exception.
