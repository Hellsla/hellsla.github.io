VERDICT: PASS
CONTENT-HASH: 23e60ba393ad4a06

## Blocking
None. The previous blocking issue (buoyancy left out of the all-modes text) is fixed. The Teoria now gives $\overline{F}_\text{noste}$, says it is large for a balloon (recomputed: about 10 g against 3 g of rubber), and gives $F_\text{v} = G - F_\text{noste}$ with the inside air counted in $G$. The tuki OO block defines $mg = G - F_\text{noste}$ as the scale reading, and teacher.md agrees.

New force diagram, checked against the drawing rules:
- The body is a rectangle, and every force is a red arrow.
- $\overline{G}$ starts at the centre and is 130 px long (13 g).
- $\overline{F}_\text{noste}$ starts beside the centre and is 100 px (10 g). The centroid is the correct point of action.
- $\overline{F}_\text{v}$ pushes up from the bottom surface and is 30 px (3 g).
- The up arrows sum to the length of $\overline{G}$, which fits $a = 0$.
- The arrows are visibly apart, $\overline{v}$ is blue and beside the body, and the LaTeX labels are inside the figure and legible at 360 and 1280 px.
- The in-figure equation and the aria-label match the text.

## Polish
None. The previous polish items are applied: the slope label sits by the line, the extension notes that the paperclips change the shape and $A$, and teacher.md notes the drag crisis ($Re \approx 4\cdot10^5$).

## Checked
- **Drag model:** $F_\text{v} = \tfrac12 C\rho A v^2$, with $v$ relative to the air, $A = \tfrac14\pi d^2$ and constant $C$ stated. Valid at a balloon's $Re \approx 2\cdot10^4$.
- **Formula:** $C = 2mg/(\rho A v_\text{r}^2)$, where the scale reading $(M - \rho V)g$ equals the drag at terminal speed.
- **Air density:** from a table or $\rho = pM/(RT)$.
- **Uncertainty:** $\Delta C/C \approx \Delta m/m + \Delta\rho/\rho + 2\Delta d/d + 2\Delta v_\text{r}/v_\text{r}$. The extreme-value method and the rounding rule are fine.
- **Extension:** $m = \frac{C\rho A}{2g}\cdot v_\text{r}^2$ is a line through the origin, and $C = 2gk/(\rho A)$.
- **Prediction 3:** $v_\text{r} \propto \sqrt{m}$.
- **teacher.md distances:** a balloon reaches 95 % of $v_\text{r}$ in about 0.25 m, a 1 kg gym ball in about 12 m (recomputed).
- **Other figures:** they follow $s = v_\text{r}\tau\ln\cosh(t/\tau)$ and show no invented data.
- **Hash:** the same at the start and the end.
