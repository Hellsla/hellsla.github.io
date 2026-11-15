VERDICT: FAIL
CONTENT-HASH: b507f51d2917a3b7

## Blocking
- [Major] example title (stage heading of Example 1, example-390-1) — the name `The $3\text{d} \to 2\text{p}$ transition` renders as "The 3extdo2extp transition": the `\t` of `\text` and `\to` is eaten when the title is built, so the notation is broken — a student reads garbage in the box heading — fix the shared title rendering (the string in example-names.json is correct JSON; escape backslashes when the name is inserted, e.g. `re.sub` with a function, not a template string), then recapture. Not caused by the reflow, but visible in the current capture.

## Polish
- [Minor] stage 4 block, `E_3-E_2 = -\tfrac{..}{9}+\tfrac{..}{4}` is set with small fractions in display; \dfrac as in fy8-3 would read better.

## Checked
- batch delta review, en: opened example-390-1 (stages 3 and 4: blocks); the other changed blocks judged from the diff/source only (rows broken before each + or -, first row left-hand side alone, no clipping seen in the capture sampled). Hash re-run at the end: unchanged.
