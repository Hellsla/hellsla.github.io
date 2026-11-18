VERDICT: PASS
CONTENT-HASH: 15261a26498e83ce
SCOPE: delta unit 1/min -> min⁻¹ (L1-07, L2-09) and solutions.md reflow

## Blocking

## Polish

- solutions.md:462-478 (L2-09) — the solution writes the rate as `pulssia/min` while the `unit` field is now `min⁻¹` (L1-07 and L2-03 use `min^{-1}`). A student who types "min⁻¹" sees a different form in the model answer. Fix (optional): use `\text{min}^{-1}` in the L2-09 solution, as in L1-07.

## Checked

- L1-07 text now asks for the answer in `$\text{min}^{-1}$`; unit field `min⁻¹`, answer 1530 and the solution (which already used `min^{-1}`) agree.
- L2-09 unit `min⁻¹`, answer 141,4 unchanged and consistent with the solution; the change is language-neutral and the level and task unchanged.
- The notation `min⁻¹` matches the other count-rate exercises (L2-03 and others) and the lesson's rate notation; no task misleads a student about the unit.
- solutions.md diff is blank-line reflow only (stage paragraphs separated); all seven stages remain, symbolic before numeric, reasonableness checks intact.
- Hash unchanged at start and end (15261a26498e83ce).
