VERDICT: PASS
CONTENT-HASH: d90d6579e9978366
SCOPE: delta added-exercise from 844ef976147dad75 base 5b3ca4f81c77

## Blocking

## Polish
- exercises/solutions.md (fy8-12-L2-09, Järkevyys) — "30 mm on näiden puolivälissä" only places the result between 200 and 100. Since 30 mm is 2,5 half-value layers, the check could say the result is the geometric mean, $\sqrt{200 \cdot 100} \approx 141$, rather than the arithmetic 150. That makes it a real check of the exponential model. This is optional.
- exercises.json (fy8-12-L2-09) — the value at 30 mm can also be read straight from the figure (about 140 on the 50-pulse grid). The answer agrees either way, so this is not an error. The text already asks for the calculation through $d_{1/2}$.

## Checked
- Hash d90d6579e9978366 at the start and the end. Only fy8-12-L2-09 and fy8-12-L3-07 were judged.
- The figure's data come from lesson-answers.py: `CHK_R0, CHK_D = 800, 12.0`. The curve is $800 \cdot (1/2)^{d/12}$. The graph is drawn to scale (screenshot L2-13), and the value 400 at 12 mm lies on a grid line, so $d_{1/2} = 12\,\text{mm}$ can be read without ambiguity. The description gives $R_0$, the range and the grid but not $d_{1/2}$, so it does not give the answer away.
- L2-09 recomputed independently: $800 \cdot 0{,}5^{2{,}5} = 141{,}42$ pulses/min, the same as answers.py (141,421356). A tolerance of 0,02 accepts 138,6–144,2, which covers both 140 and 141,4. The two figures follow from the $d_{1/2}$ read from the graph.
- L3-07 recomputed: $d = 12 \cdot \ln 20/\ln 2 = 51{,}86\,\text{mm}$, the same as answers.py (51,863137). Rounding up to 52 is correct: a limit of "enintään 1/20" for the rate means a minimum thickness, so it rounds to the safe side (CLAUDE.md P7). A tolerance of 0,02 accepts 50,96–53,04, which covers 51,86 and 52.
- L3-07 conclusion: $R(48\,\text{mm}) = 800/16 = 50 > 40$, so 48 mm is not enough. The values 1/16 and 1/32 bracket 1/20, so the reasonableness check works.
- Both solutions use net count rates, which matches the lesson brief ("nettopulssimäärä … taustasäteily vähennetty"). The law $R = R_0(1/2)^{d/d_{1/2}}$ fits photon radiation. "Gammasäteily" is stated in the task.
- L3-07: the unknown is solved symbolically ($d = d_{1/2}\ln(R_0/R)/\ln 2$) before substitution. This is the same method as the lesson's worked example, applied to a different datum (a graph instead of a given $d_{1/2}$) and with an added decision step, so it fits level 3.
- The notation ($d$, $d_{1/2}$, $R$, $R_0$) and units agree with the brief. Both tasks stay within FY8's central contents.
