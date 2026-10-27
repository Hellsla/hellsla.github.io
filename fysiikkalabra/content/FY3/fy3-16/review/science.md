VERDICT: PASS
CONTENT-HASH: da634386ef4f18f0

## Blocking

## Polish
- solutions.md:233 (L3-03 Järkevyys) — the task asks for the *minimum* mass; 1,5 kg is 0,7 % below the computed 1,511 kg, so strictly it falls short. Calling it "pienin sopiva massa" to two figures is a convention, not physics. — "1,51 kg; kahdella numerolla noin 1,5 kg, käytännössä hieman yli".
- solutions.md:118 (L1-01 Vastaus) — the two figures rest on "20 kg", which is ambiguous; the difference 280 K (300 °C − 20 °C) is the cleaner justification. — name ΔT = 280 K and the two-figure masses together.
- solutions.md:159 (L1-05 Järkevyys) — "Arvio: 3500 · 0,5 · 8 = 14 000" repeats the substitution; only the tens-of-kW comparison checks anything. — drop the repeated product.

## Checked
- Round-1 Blocking fixed: inquiry.json löyly Vastaus now justifies two figures by ΔT = 90 K (100 °C − 10 °C) and says m cancels; consistent with its Järkevyys (2260/2640 ≈ 86 %).
- One script recomputed all 12 exercises and 4 inquiry numerics with my own formulas: all match answers.py; stated answers within 1,4 % of exact (tolerances 2–4 %); mistake values (14,3 %, 6,0; 8,4 s, 56,5 s; 92,5, 5,55; 200, 12,6 kJ) are what the named errors give.
- Every solution has the seven parts; principles apply for the stated reasons (constant T during phase change, constant wall power while ice remains, Q = cmΔT/t for flow); symbolic first; conversions (h→s, kJ→J, °C differences = K) right.
- Rounding: L3-02 two figures from the difference 84 400 J (NOTES §2) correct; L1-03 from 28 K difference; kayra 3,3·10² kJ from the read 3,7 h; exit ticket now 1,8·10² kJ.
- Worked example: 292 100 J / 33,6 W = 8,69·10³ s = 2,4 h; checks 2,76 h × 0,87 and initial rise 19,2 K/h are real and correct.
- Tutki graph: plateau ends at x = 282,7 px = 3,68 h; exponential rise τ = C/(UA) = 1,29 h matches the path; the kayra solution now reads t₀ between the 3 h and 4 h lines.
- Table t = sm/(UAΔT): 8,59 / 5,73 / 4,30 / 3,44 / 2,86 h, Pt = 334 kJ every row; pred-2 2,9 h and the 2,2 h distractor right.
- Etsi virhe 62,9 kJ < 267 kJ, 0,19 kg melts; misconception 126 kJ < 334 kJ; check-3 model 67/452 kJ, "esimerkiksi" now given.
- Formulas inside FY3 central contents; L3-01, L3-03 assumptions (no steam heating, constant wall power) stated.
- Content hash identical at start and end.
