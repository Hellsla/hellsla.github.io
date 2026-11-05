VERDICT: PASS
CONTENT-HASH: 410641b2006a3acc
Round: 2

## Blocking

## Polish
- [Minor] fy2-6-L1-09 (6-9) Mallivastaus, "Muut vaihtoehdot" at 390 px — the new chain "$3{,}0\,\text{MW} \cdot 8760\,\text{h} : 5000\,\text{kWh} \approx 5300$" is 319 px in a 304 px column, so it scrolls sideways and the result shows as "≈ 530" (last digit cut, no cue) — put it on its own line after "nimellistehoa:" with the result after "eli", or write "noin $5300$" in the sentence.

## Checked
- Round 2. The round-1 clipping is fixed: the model-answer chains are now split ("$P_\text{ka} = 0{,}33 \cdot 3{,}0\,\text{MW}$, eli ..."), and all three fit the column at 390 px (rendered, measured).
- Rendered live (Playwright, rebuilt preview/fy2-6.html; no review/shots directory exists for this hash) at 390 and 1280 px, closed and with a wrong choice committed (new "noin 5000 taloa" feedback) and Mallivastaus open. No page overflow at either width; at 1280 px nothing scrolls.
- The new stem ("Valitse lähin arvo.") and the 5000-taloa feedback read fluently and fit the card.
- From the diff only: the Finnish of solutions.md wording not visible in the captures.

## Scores
illustrations 5 · typography 4 · Finnish 5 · accessibility 4
