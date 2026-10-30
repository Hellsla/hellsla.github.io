VERDICT: PASS
CONTENT-HASH: e78078188591d62b

## Blocking
None.

## Polish
None.

## Checked (revision e78078188591d62b)
- **Hero motion, recomputed from figures.py.** The time step is 0.2. The car starts from rest at $s_0$ with constant acceleration and reaches the corner at $t_c = 0.95$ with speed $v = a t_c$. After that it runs on the level part at constant speed $v$.
  - The steps along the track are 26, 79, 132, 185, 236 and 251 px. The incline steps grow linearly, as constant acceleration requires.
  - The $t = 1.0$ step (236 px) is partly incline and partly level, so it is correctly a little shorter than the full level step $v \cdot 0.2$ (251 px).
  - The $t = 1.0$ ghost is wholly on the level part. The gate car is at $t = 1.2$, before the stopper.
  - The embedded SVG matches figures.py. Regenerating it leaves the hash unchanged. The rendered figure was checked; the laptop on the desk is fine.
- **Laajennus.** Tire friction and air resistance are now named as what turns energy into internal energy. Wheel-rotation energy "ei ole hävinnyt, mutta se ei näy auton nopeudessa". This is correct and agrees with the theory.
- **No regressions:**
  - Rotational energy is part of mechanical energy, and the derivation neglects it as a stated condition. $mgh$ equals the translational kinetic energy.
  - $v = \sqrt{2gh}$ and the linearised $v^2 = 2g \cdot h$. Slope $2g$, unit m/s². $E_k/E_p = k/2g$.
  - $v^2 = kh$ for a constant share of the energy. The fixed-incline question is in `O OO`, and teacher.md explains it (friction work $\propto h$).
  - A positive $h$-intercept from the constant loss on the level part. Air drag bends the high points downward.
  - $v = L/t$ as the mean speed on the level part.
  - $\Delta k/k = (\Delta k/k)_\text{sovitus} + 2\,\Delta L/L$, and the half-range $\Delta k$.
  - The smooth-corner advice in teacher.md.
  - The setup figure: $h$ from mark to mark, $L$ along the motion.
  - No invented data, no \vec or \mathbf, faithful to card p. 13–14.
