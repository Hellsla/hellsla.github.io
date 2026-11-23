VERDICT: FAIL
CONTENT-HASH: 382b458b6fc38b7a
SCOPE: delta round 1 (work queue 8g, Kaava steps from basic equations)

## Blocking
- content/fi/FY1/fy1-5/exercises/solutions.md:219 — (A, quantitative/internal consistency) fy1-5-L1-09 asks for the distance $s$, but the new Kaava step goes $s = vt$ → $v = \dfrac{s}{t}$. It "solves" for the given speed and ends on a form the Sijoitus does not use. The derivation runs backwards (every other L1 task goes $v = \Delta s/t \Rightarrow \Delta s = vt$) — write $v = \dfrac{s}{t}$ first and end with $s = vt$.

## Polish
- none

## Checked
- I checked every other changed Kaava step: L1-01–L1-08, L2-01, L2-02, L2-04–L2-08, L3-01, L3-03.
  - Each starts from $v = \Delta s/\Delta t$ and $\Delta s = s - s_0$.
  - Each solves symbolically, for $t = (s - s_0)/v$, $t = 2d/c$, the meeting time $t = v_2t_0/(v_2 - v_1)$ (the algebra steps are right), $\varepsilon = \Delta t/t \Rightarrow t \ge \Delta t/0{,}020$, and the piecewise model.
  - Each ends on the substituted form.
- I recomputed the numbers myself:
  - meeting at 60 s and 90 m;
  - 3498,8 vrk;
  - 41,58 h;
  - $v_\text{ka}$ = 1,33 m/s;
  - 2,96 km.
  None changed.
- L1-07: $\Delta s = A_\text{suorakulmio} = vt$ is correct for a $(t, v)$ graph of uniform motion.
- The splits in L3-02 (bullet) and L3-03 (graph C) keep every sentence, including Δt > 0 and the distance-versus-position distinction.
- The hash was 382b458b6fc38b7a at the start and at the end.
