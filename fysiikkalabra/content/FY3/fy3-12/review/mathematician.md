VERDICT: FAIL
CONTENT-HASH: d23d088adff6a242

## Blocking
1. content/FY3/fy3-12/lesson.md:65 — in the wall figure the temperature line (polyline, line 66) runs straight through the label "eriste": rendered at 360 px the label box is x 286–349, y 127–155 and the line crosses it at about (309–324, 133–150). NOTES §4 says no label may overlap a line. — Move the label below the line inside the insulation, e.g. `<text x="318" y="228" …>eriste</text>`. There the line is above y ≈ 179 for x ≤ 349, so the two stay apart.

## Polish
1. lesson.md:61 — the figure is schematic (the board and cladding each drop about 1,8 K, which is not to scale), but the aria-label does not say so. — Add "Periaatekuva:" at the start of the aria-label (NOTES §4).
2. lesson.md:118 — the energy is computed from the rounded value 1,45 kW, but the rule is to round only at the end. — Write `1{,}4544\,\text{kW}` or `1454\,\text{W}` (the result is still ≈ 35 kWh).
3. lesson.md:124 — "niiden läpi menee yhtä paljon lämpöä", but the example computes 720 W against 734 W. — Write "lähes yhtä paljon".
4. solutions.md:53, 61, 77, 85 — the conversion factors have no units ("230 · 24 h", "7 · 24 h", "10 · 3600 s", "365 · 24 · 3600 s"). In L3-02, "9,0" hides 10 · f. — Write "230 vrk · 24 h/vrk" and so on, and "10 · 0,90 · 1,608 · 10²² J".
5. solutions.md:52 — the symbol h stands for the price, while h is also the unit hour in the same line ("0,11 €/kWh", "5520 h"). — Use another letter, e.g. k for the price per kWh.

## Checked
- I ran `lint_lesson.py`: 0 errors. `check_latex.py`: all OK. After `build.py --all`, `check_layout.py fy3-12` reports OK at 360 px. I re-ran answers.py and it matches exercises.json.
- Worked example, stage by stage: ΔT = 36 K; P = (U_sA_s + U_iA_i)ΔT is solved symbolically before any numbers go in; 734,4 W + 720 W = 1454 W ≈ 1,5 kW; E = 34,9 kWh ≈ 35 kWh; 20/120 = 1/6 and 1,0/0,17 ≈ 5,9 (the "lähes kuusinkertainen" in Järkevyys).
- Each of the 12 solutions ends its Kaava line with the unknown solved symbolically. Sijoitus has the values with units, and I recomputed every number.
- L2-02 chain: 245,7 W, then 5520 h, then 1356 kWh, then 149 €, giving 150 € (2 sf). L2-03: 1,26 kW · 168 h = 211,7 kWh; the old and new windows lose 1,76 kW and 0,50 kW.
- L3-02: 3,1536 · 10⁷ s, then 1,608 · 10²² J, then 0,139 K. cm = 1,04 · 10²⁴ J/K. L3-03: 2755 kWh / 2,8 = 984 kWh. ε matches fy3-11.
- L3-01: 50 400 J / 2514 J/K = 20,05 K, and 90 °C → 70 °C is consistent.
- Significant figures: every final answer has 2 sf, as the data does, and lies within tolerance 0,02 of the stored answer.
- The checks in Järkevyys hold: 102 + 238 = 340 W/m², 238 → 241,4 W/m², 49 kWh ≈ 180 MJ, 3,5 kW · 24 h = 84 kWh, −9 °C.
- Exit ticket: 0,20 · 50 · 30 = 300 W.
- Wall SVG geometry: of the 158 px drop for 36 K, the board takes 8 px, the insulation 142 px and the cladding 8 px, so the largest drop is across the insulation. 21 °C and −15 °C sit at the ends of the curve.
