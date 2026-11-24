VERDICT: PASS
CONTENT-HASH: 30e17fdff0b41bba

## Blocking

## Polish
- assets/sims/fy4/fy4-1/sim.js:1005 (lang `sims.fy4-1.nopeus_toisto` = "Nopeus") — the playback-pace select is labelled "Nopeus", the same word as the physical quantity this lesson defines. A student may think "nopea" changes the carts' velocity. — label it "Toistonopeus" or "Toiston tahti".
- inquiry.json check-3 criteria[3] — "paikka ja siirtymä metreinä" does not fit the task: the cyclist's data and the model answer are in km. — "paikka ja siirtymä pituuden yksikössä (m tai km)".
- inquiry.json check-3 model — the hook says the cyclist stops at the shop, so the graph also has a horizontal part (v = 0). The model answer names only the rising and falling parts. — add the stop.
- inquiry.json pred-2 choices[0].feedback — "kumpikin kärry siirtyy saman matkan … 20 m" mixes matka and siirtymä in a chapter that keeps them apart. — "kummankin siirtymä on 20 m".
- lesson.md:339 — "Kappale voi olla edellä ja liikkua silti hitaammin" uses "edellä" without a direction. The claim is true, but the guardrail asks for the direction to be stated. — "…edellä positiiviseen suuntaan…".

## Checked
- I recomputed every lesson-answers.py number and every inquiry number in one script with my own formulas: 4,0; −3,0; 1,49 (least squares, intercept 4,10 m, SE 0,029, so "1,49 ± 0,03" holds); mistakes 1,91, 1,3 and 0,67; 39 m with mistakes 50, 74 and 5,0; 13 m; 2,5 m/s and 170 m; 16 m; 15, 7,5 and 0,25 km/h; exit Δx = −8 m. All agree.
- Pred-3: D and A meet at t = 6 s, x = 12 m. Exactly one option is correct in every prediction, check, Etsi virhe and experiment choice, and each distractor's feedback gives the right reason.
- The figures are to scale where they say so. Displacement (40 px/m): +6 m and −5 m. Jogger: 20→120→170 m at 0/40/60 s. Robot data: every point is placed correctly and the fitted line runs 4,1→19,1 m. Case E: 0→8→8→0 m. The round-trip figure says it is not to scale.
- sim.js implements x = x₀ + vt for cases 1–3 and, for case 4, out, stop and back with path 16 m and Δx = 0. This matches the Mallin oletukset box, which states the limits (cart at full speed at once, no friction).
- Experiments: `tapaus` is locked, `t` is varied, and the measured keys `xA` and `x2` exist in simState. The setup isolates the varied parameter.
- Worked example: solved in symbols first; x = x₁ + vt is justified by t₁ = 0; the reasonableness check is a real one (proportional step, 9 km/h).
- Definitions (paikka, siirtymä, matka, nopeus, vauhti, keskinopeus) agree with the glossary. Vectors are written with overlines. Scope fits FY4 tasainen liike and graph reading.
- Line fitting follows the guardrails: the slope is read from points far apart on the fitted line, never from neighbouring raw points.
