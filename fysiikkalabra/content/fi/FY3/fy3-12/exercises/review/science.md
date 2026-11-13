VERDICT: PASS
CONTENT-HASH: 94c37286703dbe0d

## Blocking
- none

## Polish
1. content/fi/FY3/fy3-12/exercises/solutions.md (L1-09) — Annettu still writes $T_\text{sisä} = 20\,{}^\circ\text{C}$ for a Celsius value. This was carried over from the previous report and is not part of this diff.

## Checked
- Diff: only the "Kuvaajan lukeminen" lines of the two solutions that use fy3-12/earth-flows changed (L1-05 and L2-09). No number, symbol or step changed.
- figures.py earth-flows: the reflected arrow is `block_arrow(262,102 → 176,50)`. It starts beside the Earth (x 304) and points up and to the left, towards the Sun's side (x −4). "Auringon ja Maan välissä ylös vasemmalle osoittava nuoli" describes it correctly. The old wording, "ylempi oikea nuoli", was wrong, because the only right-hand arrow is the dashed thermal-radiation arrow (x 376–560).
- "Alempi oikea nuoli, jonka arvo on kysymysmerkki" is the dashed arrow at y 150 on the right. Since it is the only arrow on the right, "alempi" is redundant but not wrong.
- Physics is unchanged: reflection at the top of the atmosphere goes back to space; P_im = 341 − 102 = 239 W/m², which equals the thermal radiation out in balance; 102/341 = 29,9 %. The previous recomputations still hold.
- The figure description (341 and 102 W/m², the unknown not to scale) still matches both solutions and gives away no answer.
- Hash is identical at the start and the end.
