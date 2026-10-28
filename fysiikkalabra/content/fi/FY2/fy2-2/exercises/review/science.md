VERDICT: FAIL
CONTENT-HASH: d05f871e4dfe3077

## Blocking
- exercises/exercises.json:14, :72 (L1-02, L2-04) — "(200 g)" is a number with a unit in plain text (teacher's rule: everything in LaTeX) — $(200\,\text{g})$.
- exercises/exercises.json:48 (L2-01) — "100 gramman" — $100\,\text{g}$:n.
- exercises/solutions.md:12, :52, :82 — "suklaalevy (200 g)" / "(100 g)" in plain text — write them in LaTeX in the same way.

## Polish
- exercises/solutions.md:38 (L1-04) — the rounding cites 9,0 MJ, but in a subtraction the least precise datum decides, and 12 MJ is known only to the whole megajoule. Either give the gas as $12{,}0\,\text{MJ}$ or justify $3{,}0\,\text{MJ}$ differently.
- exercises/solutions.md:29 (L1-03) — $140\,\text{GJ} : 1{,}6\,\text{GJ} \approx 90$ tankfuls, not "noin sataa".

## Checked
- Hash d05f871e4dfe3077 at start and end. The round-1 blocking items are fixed: "kahdestatoista" in L1-04, and the L3-03 solution now computes the full $1{,}2 \cdot 10^{7}\,\text{l}$.
- All 12 answers recomputed independently in one script, matching answers.py and exercises.json, and every one is inside its tolerance after rounding: 54 000 J, 2,3, 140 GJ, 3,0 MJ, 33, 3,0 MJ, 1,3 GJ, 6,0 kJ, 950, 6, 3200, $1{,}2 \cdot 10^{7}\,\text{l}$ (3,8 % < 5 %).
- Data: the stat.fi figure of 79,8 TWh in 2023 gives 787 TJ a day (790 TJ). OL3 is 1600 MW (138 TJ a day) and 4300 MW thermal (372 TJ). 4,5 kg of U-235 a day matches 370 TJ. The TNT tonne is 4,184 GJ. 72 GJ (20 MWh) a house is marked as an example.
- L2-03 physics right: the absorbed light becomes heat, so the answer is 6,0 kJ.
- L3-03 check: about 300 tanker trucks; 4,5 kg of uranium (about 240 cm³) fits in a palm.
- Every solution has the seven parts, solved symbolically first, with conversions by substitution and colon division in prose.
- Scope: no work, $E_k$, $E_p$, $Q = cm\Delta T$ or chain-efficiency products; no ×.
