VERDICT: FAIL
CONTENT-HASH: 78c0faf56737d1db

## Blocking
1. **(A, internal consistency / fbd_magnitudes) fy4-s1 c, drawn voimakuvio: the visible sum along the slope points the wrong way.** The spec values are right, but the drawing has a scaling problem. Friction $F_\mu = 21{,}19\,\text{N}$ is 3 % of $G$, so it is raised to the MIN_SHOWN floor (about 15 px, mostly arrowhead). The dashed component $G_x = mg\sin\alpha = 49{,}3\,\text{N}$ (7 % of $G$) is not raised and is drawn to scale at about 7 px. It shows only as a chevron inside the body, and its label is far to the right. In the picture the uphill friction is twice as long as the downhill $G_x$, so the visible sum along $x$ points up the slope while $\overline{a}$ points down. That contradicts the solution's own sentence "painon rinteen suuntainen komponentti on suurempi kuin kitka" and the "components drawn to show the sum" purpose of `komponentit G`. The text alternative says small forces are enlarged but does not say that the components are not.
   The fix belongs in `scripts/fbdspec.py`, not in solutions.md:
   - Apply the floor to components as well, or raise $G_x$ and $F_\mu$ by the same factor, so that the order of forces along each axis survives.
   - Or make the build fail when a floored force reverses a visible sum, as the docstring promises ("a sum of forces stays a sum").

   Then re-render and re-check.

## Polish
- The spec uses wax A's friction ($21{,}19\,\text{N}$), while the step covers both waxes. A one-word note in the step ("voide A") would tie the numbers to the text. Wax B would give $31{,}6\,\text{N}$.
- Carried over: s2 c $8{,}74$/$8{,}75$; s3 c "pääosin selkänoja"; e intercept $0{,}43$ at the edge of a fair reading.

## Checked
- Delta: the only change since the last PASS (479fb8e6c72f07ad) is the ```voimakuvio``` block in fy4-s1 c. All other judgements carry over.
- Spec numbers, recomputed with $m = 72\,\text{kg}$, $g = 9{,}81\,\text{m/s}^2$, $\alpha = 4{,}0^\circ$:
  - $G = 706{,}32\,\text{N}$.
  - $N = mg\cos\alpha = 704{,}60\,\text{N}$.
  - $F_\mu = m(g\sin\alpha - a_\text{A}) = 49{,}27 - 28{,}08 = 21{,}19\,\text{N}$, which equals $\mu_\text{A}N = 0{,}0301 \cdot 704{,}6 = 21{,}2\,\text{N}$.
  - The net force down the slope is $28{,}1\,\text{N} = m a_\text{A}$. All consistent.
- Geometry, from the rendered SVG:
  - `pinta -4` draws the surface falling to the right at $4{,}0^\circ$.
  - $G$ is drawn from the centre straight down (100 px). $N$ is drawn from the contact surface, perpendicular to it (99,8 px, correctly about $G$).
  - `F_mu … ylös` points up the slope from the upper bottom corner, and `a alas` points down the slope (356°).
  - `akselit -4` puts $x$ down the slope and $y$ out of it, matching the step's text.
  - $G_y$ is as long as $N$.
  - Colours: forces red, components dashed red, acceleration orange beside the body, axes grey. This follows the convention.
- Physics of the diagram: object, three interactions, no driving force, no air resistance (the task excludes it). Third-law pairs are not drawn, which is correct for a free-body diagram. These match b's model answer and c's equations.
- Rendered with `python3 scripts/fbdspec.py show content/fi/FY4/sovella/solutions.md` and screenshotted in Playwright.
- The hash was 78c0faf56737d1db at the start and the end.
