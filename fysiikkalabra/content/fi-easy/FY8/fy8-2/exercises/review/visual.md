VERDICT: FAIL
CONTENT-HASH: e5f214473aa0341c

## Blocking
- [Major] L2-09 solution, SIJOITUS, 360 px — the first row of the chain is one fraction that does not fit (chain scrolls 281 > 272 px): the numerator ends "…10^8 m/" and the "s" of m/s is cut off — a unit appears wrong and only a hidden horizontal scroll shows it — set hc as its own step as L3-06 does: `hc = 6{,}626 \cdot 10^{-34}\,\text{J s} \cdot 2{,}998 \cdot 10^{8}\,\text{m/s} = 1{,}9865 \cdot 10^{-25}\,\text{J m}`, then `E = \dfrac{hc}{\lambda} = \dfrac{1{,}9865 \cdot 10^{-25}\,\text{J m}}{436 \cdot 10^{-9}\,\text{m}}` (the later rows break correctly at 360 px)
- [Major] L3-06 solution, JÄRKEVYYS, 360 px — inline chains `5{,}461 eV − 4{,}667 eV = 0,794 eV` and `1240 eV nm : 0,79 eV ≈ 1570 nm` do not wrap and are clipped by the card ("1570 nm" jää leikatuksi ("1570")) — the result is cut — split each into two shorter inline formulas or display rows (`5{,}461\,\text{eV} - 4{,}667\,\text{eV}` / `= 0,794\,\text{eV}`)

## Polish
- [Minor] kuva 360 px:ssä — asteikon numerot are about 9 px high in the task figure; luettavia mutta pieniä.

## Checked
- 1280 px: opened the en captures open-exercises-L2-1280-12 and L3-1280-9, -10 (figure, ticks, axis label, solution chains aligned); the fi and fi-easy 1280 captures were not opened (same templates, judged from the 360 px captures).
- Made own 360 px captures of 2-9 / 2-23 cards (L2-09, L3-06) with solutions open, all three languages (scratchpad s/*-360.png); measured chain overflow in the DOM.
- Figure SVG source not opened (no defect traced to it).
- Delta covers only the two added figure tasks (fy8-2-L2-09, fy8-2-L3-06) and the figure lamp-spectrum; other exercises not re-read.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 3
