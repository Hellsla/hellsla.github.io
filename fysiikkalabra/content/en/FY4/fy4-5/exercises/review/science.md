VERDICT: PASS
CONTENT-HASH: 35974d17254a902e
SCOPE: delta added-exercise from 0856c4022f143716 base 7db0992d648a
## Blocking

## Polish
- content/en/FY4/fy4-5/figures.json:28 — the alt text of ruutu-vinot still says "Puck", while the task and solution now say "block" (the Finnish figure description still says "Jääkiekko"). Make the word match in both languages when the figure is next touched.

## Checked
- Round 2 diff: "puck" → "block" in the L2-08 text and solution. A square body on frictionless ice is now named consistently; no number changed.
- Direction now "$53^\circ$ from the $x$ axis towards $+y$": $\arctan(8.0/6.0) = 53.1^\circ$ is right, and in a top view the old "above the horizontal" was misleading.
- L2-08 recomputed: $\Sigma F_x = 6.0\,\text{N}$, $\Sigma F_y = 8.0\,\text{N}$, $\Sigma F = 10\,\text{N}$, $a = 4.0\,\text{m/s}^2$. Vertical forces cancel, as stated.
- answers.py run: L2-08 equals exercises.json. Other entries differ only by rounding inside their tolerance (unchanged).
- Script comparison with content/fi: every number in the texts and solutions.md identical, as are answers, units and tolerances.
