VERDICT: FAIL
CONTENT-HASH: 8fe84e3602f89d3f

## Blocking
- inquiry.json:180 (exp-1 question solution, Vastaus) — "9,80 kPa/m, kolme merkitsevää numeroa, koska paine-ero 49,0 kPa" names the wrong limiting datum: the quotient is 49,0 kPa / 5,0 m, and the depth difference Δh = 10,0 m − 5,0 m = 5,0 m (the sim shows h to 0,1 m) has two figures, so the result has two. (My round-1 fix asked for 9,80 and overlooked Δh; that was wrong.) — Fix: answer 9,8 kPa/m, "kaksi merkitsevää numeroa, koska syvyysero 5,0 m on kahden numeron tarkkuudella", and keep the comparison with ρg = 9,81 kPa/m. (The stored answer 9.81 with tolerance 0.02 still accepts 9,8.)

## Polish
- solutions.md:118 (L3-03) — "19,0 kPa eli 19 kPa": the justification supports 19,0 kPa, then a second, unexplained rounding follows. — Give 19,0 kPa only (it is inside the tolerance of 19), or say why 19 is given.
- solutions.md (L1-03) — 98,5 kPa + 176,58 kPa by the addition rule gives 275,1 kPa; "three figures like 18,0 m and 98,5 kPa" follows the product rule. Not wrong for the house three-figure rule, but different from how L3-03 justifies a sum.
- meta.json — has no `"solutions": "all"`, which CLAUDE.md Lesson form 7 asks for (a developer matter; the checks did not flag it).

## Checked
- Round-1 fixes: check-2 now 890 kg/m³ with two figures from Δp = 70 kPa and Δh = 8,0 m; it matches the stored answer 890 (891,9 is 0,2 % off; tolerance 2 %), hint 3 (8,75 kPa/m), the mistakes 2180 and 0,892, and the back-substitution 890·9,81·8,0 ≈ 70 000 Pa.
- Worked example fixed: depth 12,0 m gives ρgh = 117,72 kPa and p = 218,72 → 219 kPa (three figures, from 12,0 m and 101 kPa); F = 1765,8 N → 1,8 kN (two figures, from 150 cm² = 0,015 m²); the 2,2 ratio and the ≈ 180 kg check are right.
- All 12 answers.py lines recomputed independently in one script; all match exercises.json within tolerance.
- Each solution's principle applies and the reason given is right; symbolic first; the cm², kPa, bar and MPa conversions are right; the reasonableness checks are real (back-substitution, 10 kPa/m estimates, the L3-02 area ratio 2500).
- exp-1 arithmetic: sim readouts 150,1 and 199,1 kPa (toFixed checked), 49,0 kPa / 5,0 m = 9,8 kPa/m.
- siirto 0,757 m and its mistakes 10,3 and 0,000757; virhe 29 kPa; check-3 ≈ 1,8 N; exit ticket 49/150 kPa; the dam at 30 m ≈ 290 kPa.
- pred-1 and pred-2 numbers (150/199, 98 → 122, 199 → 223, about 12 %) and every option's feedback.
- sim.js implements p₀ + ρgh with its limits stated; exp-1 locks ρ, exp-2 locks h; simState carries pOver and pTotal.
- Scope inside FY3 (p = F/A, hydrostatic pressure, force as a scalar normal to the surface).
