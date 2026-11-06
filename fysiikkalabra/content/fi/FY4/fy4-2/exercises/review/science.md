VERDICT: PASS
CONTENT-HASH: 8ae950d4924a8353

## Blocking

## Polish
- content/fi/FY4/fy4-2/exercises/exercises.json:281 (L2-08) — optional: no distractor touches this chapter's warned mistakes (a = 0 when v = 0; negative a always slowing); they test the s ∝ v₀²/|a| dependence, which suits this form. Keep as is or let the "Pysyy samana" feedback name the sign idea.

## Checked
- Round 2 (commit 684926b76, full packet regenerated): "Esimerkkiarvot:" dropped; Periaate now says the area equals the braking distance because v stays positive (correct condition); the check s₂ = v₀t + ½at² split into v₀t = 32 m, ½a = −1,0 m/s², ½at² = −16 m, s₂ = 16 m, all recomputed and right; answers.py adds an assert (ratio 2) and the string answer, equal to the correct choice text.
- L2-08 physics: s = v₀²/(2|a|) = 8,0 m and 16 m, t = 2,0 s and 4,0 s; sign choice consistent; magnitudes realistic for a bicycle. Exactly one correct option; each distractor's feedback says why it is wrong; the correct option is not identifiable by form and its feedback adds only times and distances.
- Scope: triangle area under (t,v) and x − x₀ = v₀t + ½at², both taught in this chapter.
- Solution complete, symbolic first, real check with the second formula; notation as in the lesson.
- All 21 answers: answers.py run once (python -I, exit 0, asserts pass) and compared: numeric answers within tolerance, string answers (L1-06, L1-08, L2-07, L2-08) equal their exercises.json answers; every MC task has exactly one correct choice.
- Inline formulas (text only, not rendered): after the split, the longest line is ½at² = −1,0 m/s² · (4,0 s)² (≈ 200 px), under 300 px at 390 px; the 360 px layout check passed.
- Hash identical at start and end.
