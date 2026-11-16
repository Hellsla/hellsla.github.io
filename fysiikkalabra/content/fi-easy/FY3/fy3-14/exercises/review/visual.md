VERDICT: FAIL
CONTENT-HASH: 601ac54fb208a3c4

## Blocking
- [Major] fy3-14-L3-04 Kaava (`josta s = \dfrac{c_\text{v} m_\text{v}(T_\text{v}-T) - c_\text{v} m_\text{j}T - c_\text{j} m_\text{j}\Delta T_\text{j}}{m_\text{j}}`) and fy3-14-L3-05 Järkevyys (`T = \dfrac{4190\cdot0{,}300\cdot30-36\,704{,}4}{1676}\,{}^\circ\text{C}` and its next row) — at 360 px the eq-chain is 292 px wide in a 272 px box, so `\Delta T_\text{j}` is cut in half (capture clip-14-L3-04-360); both are still listed in docs/clipped-formulas.tsv — a formula that has to be scrolled to is clipped (rule 2026-11-15); the work item 5d was meant to remove exactly these — lift the inline `josta s = …` onto its own aligned rows (`&s = \dfrac{…}{m_\text{j}}` with the numerator split after `-`) and split the L3-05 fraction chain, then delete the two tsv rows. Fine at 390 px and 1280 px.

## Polish
- [Minor] Open-solution captures were read mainly at 390 px; the 360 px check is by check_layout.py and my own DOM measurement.

## Checked
- Own 390 px captures of the opened solutions (preview/fi-easy/fy3-14, scratchpad), plus a DOM measurement of every opened formula at 360, 390 and 1280 px (clipping, off-screen, row breaking inside a katex); check_layout.py --width 360 run.
- Reflowed rows read: aligned equals signs in one column, continuation rows begin with an operator, closing comma or full stop stays in the aligned row (fy3-15-L2-05, fy3-10-L1-07 at 1280, fy3-12-L2-02, fy3-13-L2-06, fy3-16-L3-01).
- New task fy3-9-L2-10 and fy3-11-L2-10 read in full at 390 px (source link first, a–d, long solution): typography and Finnish fine.
- Not every changed solution was opened as a capture; the rest by the DOM measurement only.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 4
