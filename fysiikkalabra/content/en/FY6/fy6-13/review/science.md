VERDICT: PASS
CONTENT-HASH: d3bbbfc30db75858

## Blocking

## Polish
- assets/sims/fy6/fy6-13/sim.js:81 — the code comment still says "the ideal model's values before it". It is not shown to students and is optional to update. This is C-level.

## Checked
- batch delta review: the packet's wording diff is empty. The only change is lang/en.json:2014 `sims.fy6-13.lukemat_lap` (it is outside the content hash, which is unchanged) and now reads "Values of the ideal model at this voltage, as if no breakdown occurred". sim.js:62–64 confirms that, connected and in breakdown, U = U0 (the voltage shown on the line above), Q = C·U0 and W = ½·Q·U0. "At this voltage" is therefore exact, and last round's Polish item is resolved. Example: d = 1.0 mm in air, C = 177 pF, U0 = 3.1 kV gives 549 nC and 851 µJ. The label and the mallirajaus note agree; the label is used only when S.lap && !S.burnt; no simState key or calculation changed; it says the same as fi. Hash identical at start and end.
