VERDICT: PASS
CONTENT-HASH: d0da9c07714a7ca0
ROUND: 1

## Blocking
- none

## Polish
- [Minor] fy3-3-L1-09 — the distractors are all unit-algebra slips; none touches the chapter's warned mistake (Celsius instead of kelvin, or an unscaled proportionality). Acceptable for a level-1 units item; for pedagogy to judge.
- [Minor] Inline \tfrac units in the options ($\tfrac{\text{kPa}}{\text{K}}$) are small at 390 px but legible; the display rows in the solution are clear.
- [Minor] solutions.md fy3-3-L1-04 Sijoitus — untouched $\Delta T = 45 - 20 = 25\,\text{K}$ still has bare inputs, unlike L2-01 now — $\Delta T = (45 - 20)\,\text{K} = 25\,\text{K}$.

## Checked
- delta review 2026-11-07 round 3 (fixes to round 2 findings): L2-01 now $T_2 = (288 + 45)\,\text{K} = 333\,\text{K}$ (round-2 Minor fixed); L1-04 Kaava shows the constant cancelling in slash form, L2-04 ratio has $\theta/{}^\circ\text{C} + 273{,}15$ above and below. Opened fy3-3-fi-l3a-390 and -l3b-390: inline Kaava wraps at sensible points, the ratio display fits the card, no clipping.
- delta review 2026-11-07 round 2 (follow-up consistency edits): every Kaava now $\tfrac{T}{\text{K}} = \tfrac{\theta}{{}^\circ\text{C}} + 273{,}15$ (and its solved forms), every substitution $T = (\ldots + 273{,}15)\,\text{K}$ / $\theta = (\ldots - 273{,}15)\,{}^\circ\text{C}$; read all hunks in the diff and opened fy3-3-fi-l2sol-390: aligned display, brackets and unit render cleanly, results unchanged.
- Rendered fy3-3-L1-09 at 390 px with feedback and solution open (two tiles): $p = c\,T$, option fractions, K²/kPa in feedback, display chain $c = \dfrac{p}{T}$ and $[c] = \dfrac{\text{kPa}}{\text{K}}$, all KaTeX, upright units, decimal comma. No clipping, no horizontal overflow at 390 and 360 (measured).
- The correct option is not identifiable by form (similar length, first of two fraction forms, wrong ones phrased alike); the Tarkistus line and the example values $120\,\text{kPa} : 300\,\text{K}$ fit the width.
- Text only: the rest of the set (unchanged).

## Scores
illustrations 5 · typography 5 · Finnish 4 · accessibility 4
