VERDICT: PASS
CONTENT-HASH: bdef4444cc3b7d40
ROUND: 1

## Blocking

## Polish
- solutions.md:206 (L2-08) — "Pienin mahdollinen suhde" treats ±0,10 µm as a guaranteed limit (guardrail: an uncertainty is not a guaranteed limit) — "Pienin suhde epävarmuuden rajoissa saadaan, kun …".

## Checked
- New task L2-08 only (additions only since b032dcb83~1). Checked from the text only; no renders.
- Recomputed with b = 2,898·10⁻³ m·K: T = 707, 852, 865, 999 K; T₄ : T₁ = 1,41 (1,33–1,50 within ±0,10 µm); in Celsius 434 and 726 °C, ratio 1,67 → 1,7; T₃ − T₂ = 12,7 K → "noin 13 K", with intervals of 828–878 K and 840–892 K that overlap. All the numbers in the options, feedback and solution are right.
- Exactly one conclusion is supported. Each distractor has its own error: a difference inside the uncertainty (type 10), °C in Wien's law (the chapter's warned mistake) and the inverse dependence read the wrong way.
- Form: the four options are 92–95 characters and three share one sentence frame, so the right one is not identifiable by form.
- The black-body condition and the uncertainty are stated in the task. The guardrail wording holds: a difference "ei voi päätellä", not "values equal".
- Data caption short ("Spektrin huippu (esimerkkiaineisto)"); the unit is in the column header.
- answers.py: all 19 numeric answers agree with exercises.json.
- Hash bdef4444cc3b7d40 at start and end.
