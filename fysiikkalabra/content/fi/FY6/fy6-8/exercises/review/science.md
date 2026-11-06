VERDICT: FAIL
CONTENT-HASH: bbc9cb838c12abd5
Round: 1. One new YO-skill task, fy6-8-L2-08 (type 10, Mittausdata); the rest of the set was PASS before and is unchanged.

## Blocking
- exercises.json:321–334 (fy6-8-L2-08 choices) — the correct option can be found by form: 1,55 V is in three of the four options and 0,40 Ω in two, and only the correct option holds both majority values. A student who knows nothing can guess it. — Balance the values, for example make option 3 "noin 1,51 V ja noin 1,3 Ω" (the two errors together) and keep the others. Then 1,51 V and 1,55 V each appear twice and 0,40 Ω twice. Update that feedback and the solution's last paragraph to match.

## Polish
- solutions.md:208–211 — "Kulmakerroin luetaan kahdesta kaukana toisistaan olevasta pisteestä" reads the slope from raw end points. The guardrail says to read it from two points on the fitted line. Here the end points lie within 0,002 V of the least-squares line (0,400 Ω; 1,552 V), so the number holds. Write "suoralta, esimerkiksi ääripisteiden kohdalta, jotka ovat suoralla" or say so.
- exercises.json:286 — "(esimerkkiaineisto)" is in both the task text and the caption; keep it in the caption only.
- exercises.json:334 feedback — the difference of two successive drops depends on three readings, so its uncertainty is up to 0,04 V, not "kahden lukeman" 0,02 V. The conclusion holds either way, but "mahtuu lukemien epävarmuuteen" would be exact.

## Checked
- Hash bbc9cb838c12abd5 at start and end.
- All answers.py values rerun in one call: no mismatch.
- L2-08 recomputed: least squares slope −0,400 Ω, intercept 1,552 V; end points give 0,40 Ω and 1,55 V; drops 0,08/0,07/0,09/0,08 V; U : I = 15,1…1,32 Ω, so 1,3 Ω is the last point's load resistance; the ±0,01 V spread 0,38–0,43 Ω is right.
- Distractors: 1,51 V as source voltage is the lesson's warned mistake (napajännite ≠ lähdejännite); U : I is load resistance; "varies" is a difference inside the uncertainty. The option that mentions the uncertainty is a distractor, not the key.
- Notation E, R_s, U = E − R_s I as in the brief.
- Formulas measured with KaTeX in Chrome at 390 px (formula widths only, not a page render): widest inline 203 px, widest display row 236 px.
