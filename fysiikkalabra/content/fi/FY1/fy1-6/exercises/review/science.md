VERDICT: FAIL
CONTENT-HASH: 0b16b34359b806e5
SCOPE: delta round 1 (work queue 8g, Kaava steps from basic equations)

## Blocking
- content/fi/FY1/fy1-6/exercises/solutions.md:87 — (A, internal consistency) The Kaava step of fy1-6-L2-04, which asks for g from two graph points, is now $v_1 = gt$, $v_2 = gt$, $v_2/v_1 = gt/gt = 1$. That is the formula of L3-01, and the Sijoitus (29,3 and 9,7 m/s) does not follow from it — give it $g = \dfrac{\Delta v}{\Delta t} = \dfrac{v_2 - v_1}{t_2 - t_1}$ (the old step).
- content/fi/FY1/fy1-6/exercises/solutions.md:97 — (A) The Kaava step of fy1-6-L3-01, which asks for $v_2/v_1$, is now L3-02's $g = v_1/t_1$, $t_2 = v_2t_1/v_1$ — give it $v_1 = gt$, $v_2 = gt$, $\dfrac{v_2}{v_1} = \dfrac{gt}{gt} = 1$.
- content/fi/FY1/fy1-6/exercises/solutions.md:107 — (A) The Kaava step of fy1-6-L3-02, which asks for $t_2$, is now only $g = (v_2 - v_1)/(t_2 - t_1)$. It never solves for $t_2$, although the Sijoitus computes $t_2 = 30{,}0/3{,}70$ — give it $g = \dfrac{\Delta v}{\Delta t} = \dfrac{v_1}{t_1}$, $t_2 = \dfrac{v_2}{g} = \dfrac{v_2 t_1}{v_1}$.
(The three steps are rotated by one task. Check the en and fi-easy versions for the same shift.)

## Polish
- none

## Checked
- I checked all the other changed Kaava steps: L1-01–L1-06, L2-01–L2-03, L2-05, L3-03–L3-05.
  - The step $g = \Delta v/\Delta t = v/t$ is valid because each Periaate states that the body starts from rest and that air resistance is neglected.
  - The other steps are correct: $\Delta v = g\Delta t \Rightarrow v_2 = v_1 + g\Delta t$; $t_0 = b/k$; $v = L/\Delta t_\text{valo}$; $t_0 = t - v/g$; and the shortfall of the paper model, "vaje".
- I recomputed the numbers myself: 29,43; 7,848; 6,48; 22,26 m/s; 1,223 s; $g_\text{B}$ = 8,0 m/s² and $t_\text{B}$ = 2,5 s; 26,715 m/s; 9,8 m/s²; 8,108 s; 4,43 m/s; 35,3 km/h. None changed.
- The hash was 0b16b34359b806e5 at the start and at the end.
