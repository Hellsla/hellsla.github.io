VERDICT: PASS
CONTENT-HASH: 35c3015164c2b5ea

## Blocking

## Polish
- exercises/solutions.md:108 — The Vastaus line leads with "2083 s" and then claims two significant figures. Give the answer as $2{,}1 \cdot 10^{3}\,\text{s}$ (≈ 35 min), and keep 2083 s only as the intermediate. The stored 2083.33 is fine: 2100 is within the tolerance.
- exercises/solutions.md:66, 86 — "30 % = 0,30", "5,0 % = 0,050" and "25 % = 0,25" are written without the substitution step that the other solutions show. Write them as $30\,\% = 30 \cdot 0{,}01 = 0{,}30$ (teacher's rule: conversions by substitution).
- exercises/solutions.md:9 (L1-01, Järkevyys) — 85 % is compared with the "typical 90 %" of an electric motor. That is fine, but small motors of this size (400 J) are often 70–85 %, so "sopii" holds either way and nothing needs to change.

## Checked
- One Python run recomputed all 12 answers from the task text with my own formulas: 85, 30, 3,0, 2000, 4,0, 96, 54, 0,228, 45, 1,5, 2083 and 180. All of them match answers.py and exercises.json.
- Each answers.py line computes the physics the task text describes: L2-02 holds light power equal, and L3-03 reads the Sankey bands as a ratio.
- Every solution states the principle and why it applies, solves symbolically before substituting, carries units and ends with a real check (sum to 100 %, inverse product, or a scale check).
- Students who round to 2 s.f. (0,23 kWh; 2,1·10³ s) stay inside the 2 % tolerance.
- Device efficiencies used (LED 30 %, bulb 5 %, motor 80–90 %, panel 20 %, petrol engine 25 %) are realistic typical values.
- Levels follow the rules: L1 needs one formula, L2 two steps or a conversion, L3 reasoning or an unfamiliar representation. None repeats the worked example (kettle losses).
- Nothing from FY3/FY4: no product of chain efficiencies (L2-02 compares two lamps; it is not a chain), no work, no Q = cmΔT, no heat-engine theory, and "liike-energia" is only named as an energy form.
- No ×, no slash division, and all mathematics is in LaTeX.
