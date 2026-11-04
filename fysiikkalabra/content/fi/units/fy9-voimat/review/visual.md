VERDICT: PASS
CONTENT-HASH: ebab1a0395bc447c

Round 2 (delta review of round 1 fixes; round 1 hash 85c6ce246c4dc32e). Round 1 had no Blocking visual findings; I verified the Polish fixes and the changed parts in the build.

## Verified
- Built with `python3 scripts/build.py fy9-voimat`; Playwright at 390 and 1280, all 34 details opened: scrollWidth = clientWidth (no horizontal scroll), 0 .katex-error, no raw $, no console errors.
- unit.md units in parentheses are LaTeX ($\text{N}$, $\text{kg}$, $\text{m/s}^2$).
- kartta at 390 px: "$\Sigma F_x = m_i a_x$" scalar form beside the hub's $\Sigma F_x = ma_x$; vector laws keep overlines; labels legible.
- kalteva at 390 px: v (blue) and a (orange) labels no longer overlap; forces red, components dashed.
- New exit ticket and kaksi-kappaletta at 390 px: LaTeX renders ($10{,}0\,\text{kg}$, $85{,}0\,\text{N}$, $19{,}6\,\text{N}$), Finnish correct.
- Not changed by the developer, accepted: hihna viewBox (labels 15 px, legible); fy4-14/vt small labels stay a shared issue.

## Polish (remaining)
- [Minor] kalteva force diagram at 390 px: the $\overline{G}_x$ label sits close to the box edge; a few px more offset would help.

## Scores
illustrations 4 · typography 5 · Finnish 4 · accessibility 4
