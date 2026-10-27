VERDICT: PASS
CONTENT-HASH: 824a4d20f0370c33

## Blocking

## Polish
- solutions.md:126 (L3-03 Järkevyys) — the task asks for the *minimum* mass; 1,5 kg is 0,7 % below the computed 1,511 kg, so calling it "pienin sopiva massa" is a rounding convention, not physics. — "1,51 kg; kahdella numerolla noin 1,5 kg, käytännössä hieman yli".
- solutions.md:8 (L1-01 Vastaus) — "20 kg" is an ambiguous two-figure datum; the difference 280 K (300 °C − 20 °C) is the clearer justification. — name ΔT = 280 K together with the mass.
- solutions.md:49 (L1-05 Järkevyys) — "Arvio: 3500 · 0,5 · 8 = 14 000" repeats the substitution; only the tens-of-kW comparison checks anything. — drop the repeated product.

## Checked
- Round-3 split, L3-02 (solutions.md:107): numerator 4190·2,00·30,0 − 334 000·0,500 = 251 400 − 167 000 = 84 400 J, denominator 4190·2,50 = 10 475 J/K, T = 8,057 °C → 8,1 °C; energy balance 183 880 J both sides; the intermediate values carry the units right.
- Round-3 split, inquiry siirto: bracket 335 200 + 2 260 000 = 2 595 200 J/kg, Q = 0,15·2 595 200 = 389 280 J, t = 64,88 s → 65 s; vaporization share 339/389 = 87 %, 8,4 s without it; mistakes 8,4 s and 56,5 s correct.
- L3-02 rounding: two figures because the subtraction 251 400 − 167 000 loses a figure (NOTES §2): correct.
- One script recomputed all 12 exercises and 4 inquiry numerics with my own formulas: all match answers.py and the stated answers (within 1,4 %, tolerances 2–4 %).
- Worked example: 292 100 J / 33,6 W = 8,69·10³ s = 2,4 h; checks 2,76 h × 0,87 and initial rise 19,2 K/h real and correct; figure t₀ = 2,41 h matches.
- Tutki: kayra 333 kJ vs sm = 334 kJ (plateau 3,68 h); table rows 8,59/5,73/4,30/3,44/2,86 h; pred-2 2,87 h; löyly 85,7 % with mistakes 14,3 % and 6,0.
- check-2 213 kJ → 210 kJ; exit ticket 175,5 kJ; Etsi virhe 62,9 kJ < 267 kJ, 0,19 kg melts; misconception 126 kJ < 334 kJ.
- Principles, symbolic-first forms and conversions unchanged from round 2 and still correct; formulas inside FY3 central contents.
- Content hash identical at start and end.
