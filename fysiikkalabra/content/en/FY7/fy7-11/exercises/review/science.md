VERDICT: PASS
CONTENT-HASH: 849d12ae290a8132

## Blocking

## Polish
- solutions.md fy7-11-L3-02 Principle and Reasonableness — "the red edge … at an angle that no red ray exceeds" is given as $42.3^\circ$. That value belongs to $n = 1.3315$. With the task's own $n = 1.332$, the greatest θ is $42.22^\circ$ (at α ≈ 59.5°). The conclusion "inside the arc" stands — say "about $42^\circ$", or give $42.2^\circ$ for this n.
- solutions.md fy7-11-L3-05 Answer — "$7.4^\circ$ (with accurate intermediate values $7.42^\circ$)" reads as if two different calculations gave the two numbers. In fact $7.42^\circ$ is the unrounded result and $7.4^\circ$ is the same result rounded to two significant figures — say so.
- fy7-11-L3-05 — the task says $n\sin\alpha_3 < 1$ and the solution says $\le 1$. Harmless (the limiting case α₄ = 90° is used in both), but use one form.

## Checked
- One script recomputed all 18 numeric answers with my own Snell, prism and droplet formulas. All agree with exercises.json and answers.py. For L2-03 and L2-07, my Cauchy values (1.63866 and 1.51627) are within 0.02 % of the keys (1.6387 and 1.516), inside the tolerances.
- L3-04 after the edit: the β and n of each row are right (1.3997–1.4002), the mean is 1.4000, and the answer is $n = 1.40$. The water column matches θ = 4β − 2α with 1.3315 exactly. The solution column matches n = 1.40 with the scatter the task declares (±0.03°). Its maximum, 33.25° near α = 55.6°, fits the table's 33.26°. "Inside the water arc" is right.
- L3-01 after the edit: a chain rounded to hundredths gives $\alpha_4$ 34.83° and 35.81°, so $0.98^\circ$. The accurate value is 0.966°. Both are inside the 2 % tolerance of 0.9659. δ_r = 29.83° and δ_v = 30.81° are right, and so is the single-surface value of about 0.3° (0.32°).
- L3-05 after the edit: the single-surface difference at 50° is 0.649°, so "about $0.65^\circ$" is right. A_max is 64.98° for violet and 66.57° for red. At 64° the deviations are 56.40°, 63.82° and Δδ = 7.42°. At 60°, Δδ = 3.91°. The check at 65° gives $n_\text{v}\sin\alpha_3 = 1.0005$. Violet limits the apex angle.
- L2-05: 0.765°, 0.414° and 0.461° are right, and the check Δα ≈ (Δn/n) tan α₂ (0.763°) is right.
- L2-06: θ 42.29° and 40.63°, turnings 137.7° and 139.4°. The model answer correctly separates "turns least" from "largest θ".
- L2-01: Δt = 265 ns. The group-velocity caveat is correct physics.
- L1-06 and L1-09: exactly one correct option, and the true/false key is right. The feedback is right: frequency is unchanged at a boundary, v = c/n, violet is on the inner edge, and with the sun at 45° the top of the arc is at −3°.
- L1-08 and L2-04: the top of the arc is at θ − h (12.3° and 15.65°). The antisolar geometry is stated in the tasks.
- Figures: flint-points and n-graph are drawn from Cauchy fits that match the keys. The 450 nm point lies between the 1.638 and 1.640 grid lines, and 600 nm has no point. Neither figure shows the answer. The content is inside FY7 (refraction, dispersion, the prism, the rainbow).
