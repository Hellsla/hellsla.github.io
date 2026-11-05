VERDICT: PASS
CONTENT-HASH: 3eae36b389eddded
Round: 2

## Blocking

## Polish
- [Minor] fy2-7-L2-08 (7-16) Mallivastaus at 390 px — NOT fixed (solutions.md is unchanged): "$E_\text{häviö} = 0{,}040 \cdot 1000\,\text{MWh} = 40\,\text{MWh}$" (338 px) and the kaukolämpö line (328 px) are wider than the 304 px column, so each scrolls sideways and shows "= 40 M" and "= 27 MV"; one calculation per line is not enough, the long subscript is what widens them. The results are repeated in the next sentence and in the first feedback, so no information is lost, hence Minor. Fix: split after the second term ("$E_\text{häviö} = 0{,}040 \cdot 1000\,\text{MWh}$, eli $E_\text{häviö} = 40\,\text{MWh}$") as fy2-6 now does, or use $E_\text{h}$.

## Checked
- Round 2. Rendered live (Playwright, rebuilt preview/fy2-7.html; no review/shots directory exists for this hash) at 390 and 1280 px, closed and with a wrong choice committed (new feedback with the two calculations, which fit), the reason block and Mallivastaus open. Reasons are now plausible-sounding and parallel; options are whole rows; no page overflow; at 1280 px nothing scrolls.
- Measured the clipping at 390 px: the two chains above are the only scrolling lines.
- From the diff only: the Finnish of the reasons and feedbacks (fluent, one voice).

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
