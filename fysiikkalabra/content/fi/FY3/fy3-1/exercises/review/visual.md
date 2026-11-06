VERDICT: PASS
CONTENT-HASH: e2152bc8e282da0b
ROUND: 1

## Blocking
(none)

## Polish
- [Minor] fy3-1-L1-09 option names — the choices are shuffled, so the labels appear as C, B, D, A while the text and solution refer to "Voimakuvio B" etc.; works, but reads scrambled — optional: name the options by a non-ordinal tag or keep figure options in A–D order.
- [Minor] pick-extra (D) — F_k starts at the lower face although the force acts on the meter; intended as the misconception, the feedback explains it — no change needed, optional note in the solution that F_k is drawn only to be rejected.
- [Minor] aria-labels of the four figures state the arrow lengths and give "F_k" as plain text (allowed in aria-label); they also describe the answer — acceptable for a screen reader.

## Checked
- Rendered myself at 390 px (Playwright, feedback and solution open) and at 2x zoom: fy3-1-L1-09 and all four figures pick-rest, pick-long-pull, pick-extra, pick-weight-only.
- Figures: forces red (#c92a2a), G and F and F_k as KaTeX italic with subscript, labels about 22 px at phone width, body and arrows clear; wrong options differ plainly (C: F twice G; D: third arrow; A: only G) and share the scale with B. No clipping, no horizontal overflow at 390 and 360 (measured scrollWidth).
- Solution text, Sijoitus chain (three short display rows), quantities all in LaTeX, case endings ($4{,}9\,\text{N}$:n) read from the render.
- Text only: the rest of the set (unchanged since PASS). The correct option is not identifiable by form; distractors catch the chapter's warned mistakes (missing meter force, F larger than G, F_k on the body).

## Scores
illustrations 5 · typography 5 · Finnish 4 · accessibility 4
