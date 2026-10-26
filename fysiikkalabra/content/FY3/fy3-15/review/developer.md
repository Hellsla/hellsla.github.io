VERDICT: DONE

Round 1 fix: all Blocking items and the eight listed Polish items. `check_lesson.py` all ok; layout ok at 1280/1920 px; tables fit at 360 px (296/279/315 px in 326). Only lint warning: the accepted LaTeX-in-solutions one.

- lesson.md: the condenser heat is now $P_\text{L}$ (`\text{l}` reads as 1) (formula, symbols, figure 4, summary). One sentence says it is the largest part of $P_\text{h}$, not all. The waterfall is shifted 50 px down, and every loss bar is labelled (häviö 40/248/12 MW). $\eta_k$ is replaced by $\eta_1,\eta_2,\eta_3$. "edellisessä luvussa" is removed. Sijoitus now computes $P_1 = 546$ and $P_2 \approx 240$ MW, which Järkevyys uses.
- inquiry.json: the ketju question now asks for the steam-cycle loss (248 MW), with new hints, mistakes and solution; the text says the table tests prediction 1. kaukolampo now checks the hukkalämpö it asks for (48 MW). The 174 MW question moved to a new interpret item, kaukolampo-tarve. In pred-1 the option reads "Turbiinissa ja lauhduttimessa". The typo is fixed. Tables are narrower: Tapahtuma/Lähde columns dropped, CHP header shortened.
- solutions.md: all 12 solutions are in LaTeX. L2-03 substitutes directly into $m = P_\text{s}t/(\eta H)$, and L2-04 uses $P_\text{L}$.
- answers.py: comments only ($P_\text{L}$).

Not fixable here: none.
