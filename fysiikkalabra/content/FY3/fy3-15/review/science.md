VERDICT: PASS
CONTENT-HASH: f29a78207a998f19

## Blocking

## Polish
- lesson.md:117–118 (figure 1): the 248 MW lobe is labelled $\text{lauhdutin}$, while the text and figure 3 call it the steam-cycle loss (turbine and condenser). — Label it $\text{höyrykierto}$ or $\text{turbiini ja lauhdutin}$. This would also match the hook and pred-1.
- lesson.md:293 (Esimerkki, Järkevyys): "Lauhduttimeen siirtyy $P_1 - P_2$" counts all of the steam-cycle loss as condenser heat. That is a fair approximation, but the lesson itself says $P_\text{L}$ is only the largest part of the loss. — Write "Höyrykierrossa, pääosin lauhduttimeen, siirtyy …".
- lesson.md:106: the gradient `fy315-loss` has two identical stops, so it is a plain fill. — Replace it with `fill="#ffc078"` (cosmetic).

## Checked
- Round-2 blocker fixed. L2-01 now reads "lähes kaksi kolmasosaa (noin 63 %)", and $1 - 0{,}880 \cdot 0{,}420 = 0{,}630$ is correct. All round-2 polish items are done too: the L1-04 wording, $90{,}0\,\%$ in L1-05, the L3-02 wording, "tai heijastuu" in L1-03, and the invisible paths are gone from figure 3.
- I recomputed all 12 answers in one script. They match answers.py and exercises.json (90.2, 42.0, 4.20, 480, 90.0, 109, 43.1, 167, 7.16, 206, 13.6, 87.7), and every one is within tolerance.
- Worked example: 546 → 240 → 228 MW, $\eta = 0{,}380$, $P_\text{h} = 372\,\text{MW}$. It is symbolic first and staged.
- Figures are to scale. Figure 1 is 0,4 px/MW: 200/16/99,4/4,6/80 px. Figure 3 is 0,5 px/MW: 250/230/105,8/100 px, with loss boxes of 20/124,2/5,8 px. Figure 2: 160→120 MW electricity, 352 MW at 232 MW, total 400 MW. Every label is a LaTeX `foreignObject`, and the 390 px captures are crisp.
- Inquiry numbers: 520 MJ, 248 MW, 48 MW, 130 MW, 8,64 MW (5,6 % of 155,5 MW), 342/360/540 MW and 216 MW. Each mistake value reproduces the wrong method its feedback names, and every correct option is right.
- Pred-2 physics: a hotter condenser means a smaller pressure drop and less turbine work. The figure of 0,17 MW of electricity per MW of heat is realistic.
- Exit ticket: 0,432; 85 % and 15 MW; the explanation of hydro vs. a heat engine is correct.
- Magnitudes are realistic: 46 kg/s of wood chips, 7 m³/s of cooling water, about 270 wagons of coal, and a heat pump at 87,7 vs. 263 vs. 111 kWh.
- Scope: efficiency, the chain product, energy conservation and $Q = cm\Delta T$ are FY3 content. No FY4 formulas are used.
- All solutions are in LaTeX and symbolic before substitution. No lesson ids appear in student-visible text.
