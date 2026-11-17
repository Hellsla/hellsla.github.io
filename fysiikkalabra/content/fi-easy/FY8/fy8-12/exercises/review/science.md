VERDICT: PASS
CONTENT-HASH: 727ba94e22099e77
SCOPE: delta added-exercise from 0afbb0e960a7159d base 5b3ca4f81c77

## Blocking

## Polish
- exercises.json (fy8-12-L2-09, text) — the task ends "Anna vastaus pulsseina minuutissa", while the unit field is 1/min. The two are physically the same because a pulse count has no dimension. For consistency with L1-07, the sentence could say "yksikössä $\tfrac{1}{\text{min}}$". This is optional.
- solutions.md (fy8-12-L2-09, Periaate) — "Gammasäteily vaimenee tasaisesti" could be misread as linear decay. The next clause states the right rule (each half-value layer halves the rate), so this is C, not an error. "vaimenee samassa suhteessa" would be clearer.

## Checked
- Hash 727ba94e22099e77 at the start and the end.
- The figure's data match the tasks: figures.py takes R0 = 800 and d½ = 12 mm from lesson-answers.py (CHK_R0, CHK_D). Readings of 400 at 12 mm, 200 at 24 mm and 50 at 48 mm are all correct values of the curve.
- I recomputed L2-09 myself: $800 \cdot 0{,}5^{2{,}5} = 800 \cdot 0{,}17678 = 141{,}42$ per minute, the same as answers.py and the stored 141,4. Tolerance 0,02 accepts 138,6–144,2, which includes the two-figure answer 140 (−1,0 %).
- L2-09 reasonableness check: 200 at 24 mm and 100 at 36 mm, and 141 lies between them. The check is correct, and it claims only "between", not linear interpolation.
- I recomputed L3-07: the allowed rate is $800/50 = 16$ per minute. $d = 12\,\text{mm}\cdot\ln 50/\ln 2 = 12 \cdot 3{,}9120/0{,}69315 = 67{,}73\,\text{mm}$, the same as answers.py. Every intermediate value is correct.
- L3-07 conclusion and rounding: 48 mm gives $800 \cdot (1/2)^4 = 50 > 16$, so 48 mm is not enough, as the solution says. Rounding up to 68 mm is right for an "enintään" limit on the rate (P7), and two figures follow the 12 mm read off the graph. Tolerance 0,02 accepts 66,6–69,4.
- L3-07 bracket check: $1/32 > 1/50 > 1/64$, so the thickness lies between 60 mm and 72 mm. This is a real check of the model.
- Model and conditions: the law is used only for gamma radiation and net rates, and the background is said to be removed. Extrapolating past the graph's 48 mm uses the exponential law the lesson states. The narrow-beam caveat is a level-appropriate simplification (C).
- Both solutions are complete. Each has all seven parts, with the formula solved in symbols before substitution and the graph reading shown.
