VERDICT: PASS
CONTENT-HASH: 2af3ee47b4394d1d

## Blocking

## Polish

## Checked
- Round 2 (commit 684926b76, full packet regenerated): "Esimerkkiarvot:" dropped; the row-3 feedback now ends "Tarkista muut rivit samalla tavalla." and no longer points at the error; the solution's row-3 chain split into G = 18 kg · 9,81 m/s², eli G = 176,58 N ≈ 177 N; answers.py asserts a = 36 N / 18 kg = 2,0 m/s² (passes).
- L2-08 physics recomputed: ΣF = 45 − 9,0 = 36 N; G = 176,58 ≈ 177 N; a = 2,0 m/s²; the shown 36/177 ≈ 0,20 is the only wrong line, so exactly one correct option. Rows 1–3 really correct.
- The error is this chapter's warned mistake (massa vs. paino on a horizontal track); the "ei virhettä" feedback uses the lesson's words. Options parallel ("Rivi n: …"), not identifiable by form; the unit check N : N ≠ m/s² is a real check.
- Data plausible (μ ≈ 0,05 for a cart); F_μ as elsewhere in this set; air resistance left out is stated. Scope: signed ΣF = ma from this chapter.
- Solution complete, symbolic a = ΣF/m first, direction and significant figures stated.
- All 21 answers: answers.py run once (python -I, exit 0) and compared: 19 numeric answers within tolerance; L1-06 and L2-08 one correct choice each.
- Inline formulas (text only, not rendered): the longest is row 4's \dfrac chain (≈ 170 px), under 300 px at 390 px; the 360 px layout check passed.
- Hash identical at start and end.
