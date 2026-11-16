VERDICT: FAIL
CONTENT-HASH: b6940bfa43676459

## Blocking
- [Major] fy5-5-L1-02, L1-03, L1-04, L2-03, L3-03 solutions, Sijoitus chain at 360 px (L1-02, L1-04, L2-03 also at 390) — the chain's long fraction row does not wrap and sits in a sideways-scrolling `.eq-chain`: "…\cdot (3,30 \cdot 10^{23}\,kg)/(2,44 \cdot 10^{6}\,m)" is cut at "kg"/"m)", L1-02 at "(200", L2-03's numerator at "5,97 \cdot 10"; scrollWidth 285–371 px against 272 — the work item 5d was exactly this, and the teacher's 2026-11-15 rule calls a row that must be scrolled to clipped; L1-03 and L2-03 are tasks this diff touches — write the substitution so it breaks before a `\cdot` (a first row with the constants, then `\cdot \dfrac{…}{…}` on its own row), or give the numerator and the denominator as their own steps, and re-run `check_layout.py fy5-5 --width 360`.

## Polish
- [Minor] L2-06 Vastaus — the justification now runs as one long paragraph with the b-part appended; split "Kohta b:" to its own sentence block.

## Checked
- Own captures of the built page with `?ratkaisut=1` at 360 and 1280 px (the packet's exercise captures were missing): L1-02, L1-03 (chip "Syventävä tehtävä" beside the number, task text follows; Merkurius), L2-03 (changed Järkevyys 21 700 km), L2-06 (changed Vastaus, table caption without marker), all `...-360.png` opened; the other tagged tasks (L1-09, L2-02, 04, 05, 07, 09, L3-02, 04, 05) carry the same chip by source and scan; scan of every `.eq-chain` on the page at 360 and 1280.
- 1280 px: no overflow anywhere.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 3
