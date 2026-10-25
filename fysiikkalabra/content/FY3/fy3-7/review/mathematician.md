VERDICT: FAIL
CONTENT-HASH: 4c24e6d9a7103f36
## Blocking
1. lesson.md:26 — The SVG heating curve has its slopes reversed. The slope is 1/(cm), but ice (30 px over 30 px, slope 1,0) is drawn flatter than water (90 px over 60 px, slope 1,5). That implies c(jää) > c(vesi), while the lesson's data (answers.py:7) give 2100 < 4190 J/(kg·K). The plateaus are to scale (40 : 280 against 334 : 2260). — Fix: make the ice and steam segments steeper than the water segment. To scale for 1 kg: `points="70,230 77,200 130,200 197,110 557,110 570,74"`, with dashed x2 at 130 and 197, "sulaa" at x=103, "kiehuu" at x=377, and "höyry" at x=575 with text-anchor end.
## Polish
1. lesson.md:43 — "siirtyy kokonaan veteen" is stated as fact, but :47 attributes the error to losses. — Write "Oletetaan, että … siirtyy kokonaan veteen".
2. lesson.md:57 — The summary uses Δm, but the example (:43–45) uses m for the evaporated mass. — Use one symbol in both places.
3. lesson.md:10, :21 — s, r, Q = cmΔT and Q = sm are plain text, but they are math on :17 and :54–55. — Wrap them in `$...$`.
4. solutions.md:85 — The factors have no units ("4190 · 0,25 · 80 J"). — Write 4190 J/(kg·K) · 0,25 kg · 80 K, as in L2-04.
5. solutions.md:79 — Add a check that all the ice melts: cooling the juice to 0 °C releases about 36,7 kJ, which is more than 20 kJ.
## Checked
- Hash stable; lint 0/0; LaTeX ok.
- Example: 1000 W · 300 s = 300 kJ, and 300/0,128 = 2343,75 kJ/kg ≈ 2,34 MJ/kg. (+3,7 %; losses raise r).
- lesson.md:10: 2260/334 = 6,77 and 2260/419 = 5,39. lesson.md:50: 334/4,19 = 79,7 K ≈ 80 K.
- L1-01…05: products, the plateau subtraction and the sanity figures (2,7 kg, 54 K, 19 kJ) are correct.
- L2-01…04: t = rm/P and m = Q/s are correct, conversions are correct, and the shares are 90 % and 24 %.
- L3-01: the rearrangement is correct, T = 9,676 °C, and the comparison with 0 °C water gives 21,3 °C.
- L3-02: 648 800/24 000 = 27,0 K, with shares 87 % and 13 %.
- L3-03: the total is 3 055 000 J and the share is 73,98 %, which rounds to 74 %. Melting is 10,9 %, and the mass cancels.
- Exit ticket: 334 · 0,50 = 167 kJ ≈ 170 kJ. The formulas match :17 and :21.
