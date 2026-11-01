VERDICT: PASS
CONTENT-HASH: c4613f28acbcb79a

## Blocking
(none)

## Polish
1. [Minor] `lessons/units/fy14-secret-fusion/figures.py`, figure `pinch` (Z-pinch panel). The green $\overline{B}$ rings have no direction, and in the theta-pinch panel "$I$ in the coil" has no arrow on the coil. A student cannot check "the field circles the current" with the right-hand rule. Fix: add one small arrowhead on each $\overline{B}$ ring (front side, the right-hand sense for $I$ to the right) and one copper arrowhead on a coil turn next to the label.
2. [Minor] `inquiry.json` `pred-secret`, correct option "Their neutrons could be used to make bomb fuel." "Their" has no antecedent in the prompt (governments? the countries?). Fix: "Fusion devices make neutrons that can make bomb fuel." (47 characters, still within ±30 % of the other options.)
3. [Minor] `unit.md` Summary, first bullet: "accelerator beams could never give more energy than they used" says more than the section, which only says that a beam "mostly loses its energy in collisions, and only a tiny fraction of the nuclei fuse". Fix: "but in accelerator beams only a tiny fraction of the nuclei fuse, so they use far more energy than they give". (For science, if "never" is meant.)
4. [Minor] Figure `neutrons` caption "Arrows show where neutrons fly." is grey on white and is the only key to the drawing. Fix: use the ink colour of the other labels.

## Checked
- Captures regenerated for this hash: contact-1 to -6; top-390, intro-390, intro-1280, stage-tutki-390-4 (pinch figure), stage-tutki-390-6 (ZETA text and `neutrons` figure), stage-sovella-390-2 (`zeta-temperature` solution open: Formula, Substitution, Answer, Reasonableness), selita and tarkista via contact sheets.
- Own Playwright captures of `hero`, `pinch`, `neutrons` at 390 and 1280. Smallest label is 16.7 px (`pinch`) and 15.5 px (`neutrons`) at 390. No `.katex-error`, no raw `$`, no console errors, no horizontal scroll.
- Components `fx-sf-order`, `fx-sf-sort` (match) and `fx-sf-french` (say) at 390 and 1280: options short, selects fit.
- Hero has no text and does not answer either prediction. Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4
