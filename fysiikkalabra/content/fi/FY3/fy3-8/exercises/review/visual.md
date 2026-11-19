VERDICT: PASS
CONTENT-HASH: 9574c3020bc20cb0
SCOPE: delta wording from df1aa72edd405367 base 6153818

## Blocking
(none)

## Polish
- [Minor] fy3-8 task 10-14, table caption "1,000 kg veden tilavuus" — wraps to two lines in a narrow box at 1280 px and is cramped; optional: widen the caption or write "Veden tilavuus (1,000 kg)".

## Checked
- Delta, wording only: the first task of the water-volume exercise now reads "Taulukossa on $1{,}000\,\text{kg}$:n vesimäärän tilavuus eri lämpötiloissa." The Finnish is grammatical (genitive "kg:n" + "vesimäärän"), and the earlier Polish item is resolved. Numbers, units and LaTeX are unchanged.
- Built the page (preview/fy3-8.html) and opened captures of the task at 390 px and 1280 px: "1,000 kg:n" renders as a KaTeX number with an upright unit, and ":n" sits directly after it with no gap or break. No horizontal overflow (scrollWidth equals the viewport width). The rest of the card is intact.
- The other tasks and figures were not reopened: the diff does not touch them.
- Hash unchanged at the end.

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 4
