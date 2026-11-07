VERDICT: PASS
CONTENT-HASH: 628b35522ef3610a

## Blocking
- (none)

## Polish
- solutions.md:214 and :218 fy7-3-L2-08 — the inline $B_1 = 4\pi \cdot 10^{-7}\,\tfrac{\text{Vs}}{\text{Am}} \cdot \dfrac{240 \cdot 0{,}60\,\text{A}}{0{,}12\,\text{m}}$ (and the B₂ line) are near 300 px at 390 px width (estimate from text, not rendered); split after the constant if the visual check finds overflow.

## Checked
- Round 1, full mode; only L2-08 is new (type 6, prediction of change). Hash identical start and end.
- Recomputed: B₁ = μ₀ · 240 · 0,60 A / 0,12 m = 1,51 mT, B₂ = μ₀ · 240 · 1,8 A / 0,24 m = 2,26 mT, ratio 1,50; answer, correct feedback ("1,5 mT → 2,3 mT") and answers.py comment agree.
- Conditions stated in the task: long coil compared with its thickness, air inside, field at the middle; same wire on an equally thick tube, so N stays 240. Long-coil formula applies.
- Distractors: 3× is the chapter's own warned mistake (total turns instead of N : l), 6× reads the length the wrong way, ½ forgets the current; each feedback gives the right dependence. No option identifiable by form.
- Solution complete, ratio solved symbolically before numbers, check by absolute values.
- All numeric answers of the chapter recomputed in one script: all within tolerance.
