VERDICT: PASS
CONTENT-HASH: 40aa8b8489e870d0
## Blocking

## Polish
- lesson.md:379 — "The static friction acting on an object at rest equals $G_x$" holds only when no other force acts along the slope — add "when no other force acts along the slope".
- inquiry.json:102 — the sim lead says the free-body diagram is "to scale", but the sim rescales the arrows per mass ($S = 4S_0/m$; only the canvas note says so) — add "the scale depends on the mass" to the `model` box so exp-2's equal-looking arrows are not read as equal forces.

## Checked
- Recomputed in one script with my own formulas: worked example ($F_\mu = 48.0\,\text{N}$, $a = 1.48\,\text{m/s}^2$, $G_x = 74.6\,\text{N}$, frictionless $4.15\,\text{m/s}^2$), Moon/Earth weights, every inquiry number (pred feedback 3.41/6.71/8.60 N, slip at $26.57^\circ$ so rest at 26°, slide at 27°, 5.24 N, $a_{35} = 3.216\,\text{m/s}^2$, exp-1 answer and mistakes, interpret mean 0.3504 and mistake 3.4375, siirto 20.31/75.81/78.48, check-2 0.3057/0.2924/0.9563, check-3 N 184, $F_\mu$ 46, $T$ 113 N); all agree.
- Figures measured from the SVG: kitka graph to scale (50 N and 35 N at $N = 100\,\text{N}$); kalteva (30°) and kalteva-ydin (40°): $G_x = G\sin\alpha$, $G_y = N = G\cos\alpha$, $F_\mu = G_x$, directions and points of application right; esimerkki lengths in proportion 176.6 : 74.6 : 160 : 48 N; kuorma $F_\mu/G = a/g = 0.20$.
- virhe, valitse-a…d, malli-veto (figures.py): each wrong option has exactly the one error its feedback names; the model diagram has four forces, friction down the slope, $v$ not drawn as a force; no third-law pairs, no component double-counted.
- sim.js implements the stated model ($N = mg\cos\alpha$, rest iff $G_x \le \mu_0 N$, else $\mu N$ and $a = g(\sin\alpha - \mu\cos\alpha)$); the model values in the `model` box match `SURF`; `simState` gives Gx, N, Fmu, a.
- exp-1 locks surface and mass, varies only α; exp-2 locks surface and α = 35° (slides, as $\tan 35^\circ > 0.50$), varies only m (2, 3, 4 kg exist).
- Exactly one correct option in every choice; distractor feedback physically right; exit ticket and conclusion model answer match the theory.
- Terms follow P8 (static friction, sliding friction, maximum (fully developed) static friction); conditions on $N = mg\cos\alpha$ stated at each use; friction in the direction of motion (truck, walking) explained by relative sliding.
- Scope within FY4's central contents and the slot.
