VERDICT: PASS
CONTENT-HASH: b507f51d2917a3b7

## Blocking
(none)

## Polish
- [Minor, out of scope of this delta; shared-build defect for the coordinator] Example 1 title renders "The 3extdo2extp transition": the \t of \text and \to in the en example name (example-names.json) is lost when the build inserts the title. Pre-existing, not touched by the reflow; the same string appears in fi. It should be fixed in the shared title rendering before publication.
- [Minor] Stage 4 block E_3-E_2 sets the fractions small (\tfrac) in display; \dfrac, as in fy8-3, would read better.

## Checked
- batch delta review, en: opened example-390-1 (stages 3 and 4 blocks: rows broken before each + or -, first row left-hand side alone, = aligned, units whole, nothing clipped); the other changed blocks judged from the diff/source only. Verdict covers the lifted formulas only. Hash re-run at the end: unchanged.
