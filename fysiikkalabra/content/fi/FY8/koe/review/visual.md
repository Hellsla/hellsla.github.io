VERDICT: FAIL
CONTENT-HASH: f88ddf35762aaa28

## Blocking
- [Major] solutions.md, fy8-k2 b) Sijoitus (page-390-13, also fig. in #100) — the fraction `\dfrac{2{,}87\,\text{V} - 1{,}5…}{7{,}0\cdot10^{14}\,\text{Hz} - 4{,}0…}` runs past the card edge and is cut off at 390 px; the numerator's last term is unreadable — the substitution is the step the student checks — fix: break the chain so the fraction wraps or is shown as `\dfrac{\Delta U_\text{k}}{\Delta f}` on its own row (the mathlayout break), never overflow.
- [Major] solutions.md, fy8-k4 b) Järkevyys (page-390-29, #30) — `28{,}30\,\text{MeV} - 2{,}22\,\text{MeV} - 8{,}48\,\text{Me…}` clipped at the right edge at 390 px — same fix: wrap the left side onto two rows before the `=`.
- [Major] fy8-k1 b) Perustelu at 1280 px (page-1280-5) — inline chain `W = hf_0 = 6{,}626\cdot10^{-34}\,\text{J s}\cdot5{,}6\cdot10^{14}\,\text{Hz} \approx 3{,}7\cdot10^{-19}\,\text{J} \approx 2{,}3\,\text{eV}` is cut mid-unit at the box edge, so the eV conversion is lost — fix: move this chain out of the prose sentence into its own Sijoitus-style line (it is then broken by mathlayout) or split it into two sentences.
- [Minor to Major, check] fy8-k4 c) Muunnokset (page-390-29): `m_D+m_T` row's `\text{kg}` touches the card edge; verify it does not clip once the above is fixed.

## Polish
- [Minor] fig-6 (fy8-k3 graph) — the guide label reads `N = 401` while the text says `N_0/2 = 400`; use 400 (the value read off the curve) so label and solution agree.
- [Minor] fig-1 (Monivalinnat b graph) — the fitted line extends past the data without a dashed continuation; acceptable for a question figure, but it should be dashed beyond the points, as fig-3 does.
- [Minor] fy8-k3 c) Sijoitus (#23) — the exponent `-0{,}217\,\text{min}^{-1}\cdot15\,\text{min}` is tiny on a phone; split into a separate row (`\lambda t = …`) first.
- [Minor] Small formula-only fragments (fig-2, 4, 7, 19 are empty 28 px boxes): the collapsed-figure inventory shows empty KaTeX wrappers, not real figures; make sure no empty `<div class="fig-tex">` is left on the page.

## Checked
- All 17 contact sheets (390 px page strips, stage strips and the 1280 px page strips #145–#196).
- Fig 1, 6 and 18 at readable size (graphs: axes with quantity and unit, ticks, markers distinct from line, extrapolation dashed in fig 3); fig 3 and fig 6 contact sheet; the other 21 figures are inline `\sqrt{N}`-type formula fragments, viewed on contact sheets 6–9, all render correctly.
- page-390-13, page-390-29, page-1280-5 at full size; top-390/top-1280 and the exam-structure box on contact sheets 1 and 14.
- Hash re-run at the end: f88ddf35762aaa28 (unchanged; the captures' stamp matches).

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 3
