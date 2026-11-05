VERDICT: PASS
CONTENT-HASH: 9bb9fde6012ead07
Round: 1

## Blocking

## Polish
- [Minor] fy2-6-L1-09 (6-9) Mallivastaus at 390 px — the calculation lines "$P_\text{ka} = 0{,}33 \cdot 3{,}0\,\text{MW} = 0{,}99\,\text{MW} = 990\,\text{kW}$" and "$E = 990\,\text{kW} \cdot 8760\,\text{h} = 8{,}67 \cdot 10^{6}\,\text{kWh}$" are wider than the column (383 and 340 px against 304) and become their own sideways-scrolling lines (kx-wide), so the end of the chain (990 kW, kWh) is cut off with no cue — write each chain on a "**Sijoitus:**" line so the build sets it as rows, or split it at the second "=".

## Checked
- Rendered live (Playwright, preview/fy2-6.html; no review/shots for this hash): L1-09 at 390 and 1280 px, with a wrong choice committed (feedback box) and Mallivastaus open; the stem reads as three short paragraphs and the question, options are whole rows, the feedback opens inside the card. At 1280 px every chain fits.
- Rendered L3-03 (6-19) at 390 px closed: the new paragraph break is good.
- Overflow measurement at 360 and 390 px: no page-level horizontal overflow; only the kx-wide lines above scroll.
- From the diff only: the Finnish of the four distractor feedbacks (clear, one idea each) and solutions.md wording.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
