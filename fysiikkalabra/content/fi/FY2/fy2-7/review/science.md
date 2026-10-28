VERDICT: FAIL
CONTENT-HASH: b6e1d96d15ea188c

## Blocking
- lesson.md:231 — The rounding justification is false: "$9{,}0\,\%$ tunnetaan kolmen numeron tarkkuudella". $9{,}0\,\%$ has two significant figures. $\eta = 0{,}910$ (from $100\,\% - 9{,}0\,\%$) has three, so 223 MWh is fine. The loss $22{,}05\,\text{MWh}$, however, carries the two figures of $9{,}0\,\%$, as the exercise solution L3-01 itself says. — Answer $E_\text{häviö} \approx 22\,\text{MWh}$ with two figures and justify each result by its own data ($\eta$ three figures; the loss share two).
- inquiry.json:315 (tarkistus-2) — The listed mistake value 496 (adding 9 % of the delivered energy, $455 \cdot 1{,}09 = 495{,}95$) is 0,8 % from 500, inside the relative tolerance 0,02. The wrong method is graded correct and its feedback never fires. — Either set the tolerance to 0,005 (500 has two significant figures, and a student's $5{,}0 \cdot 10^2$ is exact) or use a larger loss share, e.g. $\eta = 75\,\%$: $607$ vs $569$.
- lesson.md:11, :113, :248; inquiry.json:19 — These numbers with units are plain text: "110–400 kV", "20 kV", "0,4 kV", "230 V", "4 %", "83 TWh", "36 TWh", "32,7 TWh", "9 %". The teacher's standing rule is that everything is in LaTeX. — Write them as `$110\text{–}400\,\text{kV}$`, `$4\,\%$`, `$83\,\text{TWh}$` and so on.

## Polish
- lesson.md:141, :138 — The labels "potentiaali" and "pumppuvoima" should read $\text{potentiaalienergia}$ and $\text{pumppuvoimala}$, matching the text.
- inquiry.json "jannite" — 100 MW at 20 kV needs 5000 A, which is unrealistic even for a labelled model. A 10 MW example would be more believable.
- lesson.md:113 — "Kuuma vesi on ympäristöä selvästi lämpimämpää, ja siksi … suhteessa suurempi" reads as the only cause. Add that heat leaks through the insulation along the whole length of the pipe network, as the johtopäätös model answer already says.

## Checked
- Data verified against energia.fi: Sähkövuosi 2024 (83 TWh total use, losses 4 % of it); Kaukolämpötilasto 2024 Taulukko 1 (36 000 / 32 700 GWh). The 9,2 % is correctly called an estimate.
- The high-voltage explanation is qualitative and correct, with no $P = UI$; the model table follows $1:U^2$. The ennuste-2 feedbacks are correct.
- No FY3 content: no U-value, no conduction formula, no chain-efficiency product.
- The grid voltages are correct, and the Sankey widths are to scale.
- Every lesson-answers.py and inquiry number recomputed; all match. The other mistake values lie outside tolerance.
- No ×; division is written with a colon; the worked example is solved symbolically first.
