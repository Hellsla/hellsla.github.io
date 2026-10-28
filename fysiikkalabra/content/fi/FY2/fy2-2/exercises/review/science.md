VERDICT: PASS
CONTENT-HASH: 4ab013bb23ca27b4

## Blocking

## Polish
- exercises/solutions.md (L2-01, Periaate) — "Energiat lasketaan yhteen, ja energia on additiivinen" says the same thing twice. Use "Kokonaisenergia on osien summa".
- exercises/solutions.md (L1-01, Järkevyys) — the comparison with a match's 1 kJ is weak. A clearer check is "$54\,\text{kJ}$ is about 54 match flames, a sensible amount for a battery that runs a phone all day".

## Checked
- Hash 4ab013bb23ca27b4 at start and end. All round-2 blocking items are fixed: $(200\,\text{g})$ and $100\,\text{g}$ are in LaTeX in exercises.json and solutions.md. Both round-2 polish items are fixed too: L1-04 now rounds to the whole megajoule, and L1-03 says about 90 tankfuls.
- All 12 answers recomputed independently in one script. They match answers.py and exercises.json, and each rounded student answer is inside its tolerance: 54 000 J, 2,3, 140 GJ, 3,0 MJ, 33, 3,0 MJ, 1,3 GJ, 6,0 kJ, 950, 6, 3200, $1{,}2 \cdot 10^{7}\,\textsf{l}$ (3,8 % < 5 %).
- Data: 790 TJ a day (stat.fi gives 79,8 TWh for 2023, which is 787 TJ). OL3 gives 138 TJ net and 372 TJ thermal a day. 4,5 kg of U-235 matches 370 TJ. A TNT tonne is 4,184 GJ. 72 GJ a house is 20 MWh and is marked as an example.
- L2-03 physics is right: the absorbed light becomes heat, so the answer is 6,0 kJ. In L3-01, rounding up with 5 against 6 units is justified.
- Every solution has all seven parts and solves symbolically first, with conversions by substitution and colon division. Subtraction and addition round by the least precise datum (L1-04, L2-01).
- Scope: no work, $E_k$, $E_p$, $Q = cm\Delta T$ or efficiency products. No ×, and no plain numbers with units in the texts (scripted scan).
