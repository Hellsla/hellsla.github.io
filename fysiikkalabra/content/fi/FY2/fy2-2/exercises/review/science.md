VERDICT: PASS
CONTENT-HASH: 6527b074c113a0ce

Round 2: all three round-1 blocking items are fixed. L1-06 now has the correct option 0,0033 GJ = 3,3 MJ, which has the smallest numeric value, so picking the largest number (3 000 000 J = 3,0 MJ) is wrong. L1-07 now says "noin kahdeksasosa (12 %)". L2-06 is now about breakfast, lunch and a snack, and its check calls 2,5 MJ "noin neljäsosa päivän tarpeesta". The round-1 Polish was also taken up: L3-04 now says "kymmenien tuhansien", L1-08 has a `kind`, and L2-07 says "likimain verrannollinen".

## Blocking
(none)

## Polish
- solutions.md L1-06 Mallivastaus — the last sentence ("ja jouleina ilmoitetulla energialla on suurin lukuarvo mutta pienin yksikkö") is right but hard to read. A shorter version: "Suurin lukuarvo (3 000 000 J) on energialtaan vasta kolmanneksi suurin."
- solutions.md L2-07 Kuvaajan lukeminen — the fitted line's intercept (8 kJ) is not zero, which the model "likimain verrannollinen" leaves open. One sentence would close it, e.g. "pieni vakio johtuu lukematarkkuudesta".

## Checked
- Recomputed in one script (scratchpad recompute_r2.py): L1-06 2,9 / 3,1 / 3,0 / 3,3 MJ, so exactly one option is correct; L1-07 1200 kJ (12 % of 10 MJ); L1-08 350 MJ; L2-05 7,32 km; L2-06 2,5 MJ; L2-07 5,99 km; L3-04 49 383, so 49 000, and 3,2·10⁶ / 70 ≈ 45 700 houses; L3-05 0,892 kg. All match the answer key and solutions.md.
- Every L1-06 distractor's feedback has the right conversion, and the correct option's feedback lists the other three in MJ correctly.
- L3-05: the 5 % tolerance covers the rounding of the 1,10 MJ deficit, and the note is right.
- No new physics was added. The scope holds (no mgh, c·m·ΔT, work or force), and the invented data are marked as examples.
- The hash was the same at the start and the end.
