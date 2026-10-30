VERDICT: PASS
CONTENT-HASH: 41e17ad1edac25ec

## Blocking
None.

## Polish
None.

## Checked (revision to 41e17ad1edac25ec)
- Hero (checked from figures.py; no browser was available here). A staircase of 12 steps rises from the second-floor floor surface (y = 430) through an opening in the slab (x 150–420) to the third-floor floor surface (y = 298). The total rise is 132 px, equal to the slab spacing, so the drawing shows the floor-to-floor height. The student measures the first step's rise with a ruler at the foot of the stairs. The alt text and the docstring match the drawing and the page's method (number of steps × rise). The earlier blocking point is resolved.
- Measuring hints: the axis check now uses the signed reading. This also works on phones that read about $-9{,}8$ face up, where the sign-flip rule then applies. The new unit check says that a rest reading of about $1{,}00$ means units of $g$, to be multiplied by $9{,}81\ \text{m/s}^2$. Both are correct.
- Sensor model, "Mitä anturi mittaa": the rest reading is about $g$ or near zero depending on the app, never exactly zero. The lift's acceleration is the change from the rest reading. This is correct for raw and "linear acceleration" modes alike. Ennusta Q2 comes before the theory.
- The numerical-integration paragraph moved into the OO calculation block, unchanged. The table, the offset $a_0$ from the rest period at the start, $a = a_\text{mitattu} - a_0$ with the sign rule, and the trapezoid recurrences for $v_i$ and $s_i$ from 0 are all correct. Mode I keeps the principle (signed areas under the graphs).
- Drift: $\delta a \cdot t$ and $\tfrac12 \delta a t^2$; $\delta a = v_\text{loppu}/t_\text{loppu}$ gives $\tfrac12 v_\text{loppu} t_\text{loppu}$. The extension's correction makes $v$ end at 0. The warning about the start and end rest readings differing is correct.
- Phases figure: $\overline{v}$ points up in all phases. $\overline{a}$ points up at the start, is $a = 0$ while cruising and points down while slowing. Velocity is blue and acceleration orange, and the labels are LaTeX. The model and drift graphs show shapes only, from the same integration, with no invented data.
- The card on pages 15–16 is fully covered.
