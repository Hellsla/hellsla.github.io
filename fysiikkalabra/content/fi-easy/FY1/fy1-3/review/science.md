VERDICT: PASS
CONTENT-HASH: 8e0939a59d68304b

## Blocking

## Polish
- content/fi-easy/FY1/fy1-3/lesson.md:412 — "Hajonta on sama asia kuin satunnaisvirheen suuruus." equates two different things (guardrails: hajonta = how widely repeated results spread; satunnaisvirhe = one reading's random deviation). Category C at this level, but sharper wording would be: "Hajonta kertoo, kuinka suuri satunnaisvirhe on."
- content/fi-easy/FY1/fy1-3/inquiry.json:check-2 — answer key 2.08 with relative tolerance 0.1 accepts both the typed $2\,\%$ (shown answer) and $2{,}1\,\%$; fine. Keep fi, en and fi-easy on the same tolerance.

## Checked
- Hash 8e0939a59d68304b at the start and the end.
- Round-2 Blocking item resolved: check-2 Vastaus is again "$2\,\%$ … yksi merkitsevä numero, kuten virhearviossa $0{,}05\,\text{s}$ (laskimen arvo $2{,}08\,\%$)", consistent with the rounding rule and the worked example; tolerance widened to 0.1 (relative, docs/inquiry.md) so 2 passes; mistakes 4,2 / 0,05 / 0,021 stay outside the tolerance.
- Recomputed in one Python call from the sim's G series: exp-1 n=1 error $-0{,}22\,\text{s}$, n=40 error $-0{,}0005\,\text{s}$, half-range 0,25 to 0,26 s; exp-2 n=40 mean 2,6995 s, difference 0,30 s; exp-3 half-ranges 0,085 s and 0,525 s, ratio 6,18 → 6,2 (mistake 6 outside 3 % tolerance).
- Worked example: sum 19,09 s, mean 3,1817 s → 3,18 s, Δt 0,12 s, ε 3,77 % → 3,8 %; interval 3,06–3,30 s covers five of six, correct.
- Karkea: outlier 4,31 s shifts mean by 0,17 s ("noin 0,2 s"), Δt 0,09 s → 0,62 s (about sevenfold); correct.
- Siirto: (28,0 g − 0,8 g)/5 = 5,44 g; mistakes 5,6 / 27,2 / 4,8 / 28 correct.
- Exit ticket: 20,4 g − 0,5 g = 19,9 g; 0,09/4,52 = 1,99 % → 2 %.
- sim.js reading model $t_i = T + \Delta t_\text{sys} + \Delta t_\text{sat} g_i$ rounded to 0,01 s matches lesson-answers.py and the model box.
- Error types, outlier handling, resolution vs uncertainty, half-range as a course-level scatter estimate (not the mean's uncertainty) follow the guardrails' wording.
- Ice-water data: mean 1,5 °C, half-range 0,1 °C, systematic error identified only by the known reference; distractor feedback correct.
