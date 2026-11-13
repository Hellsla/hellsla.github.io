VERDICT: FAIL
CONTENT-HASH: 394ed5393a14f07f

## Blocking
- exercises/exercises.json (fy3-3-L2-08) + solutions.md "Kuvaajan lukeminen" — A (assessment): the answer cannot be read from `fy3-3/extrapolation-points` to the stated tolerance. The figure has only 25 kPa gridlines (about 1,9 px per kPa at 1280 px, shot L2-10) and no value labels, yet the solution "reads" $102{,}5\,\text{kPa}$, and the asked $90\,\text{kPa}$ lies only $1\,\text{kPa}$ above the 50 °C point. The slope is $0{,}275\,\text{kPa/°C}$, so a $1\,\text{kPa}$ reading error moves θ by about $4\,{}^\circ\text{C}$: reading the 50 °C point as 90 kPa gives $50\,{}^\circ\text{C}$, as 88 kPa gives $58\,{}^\circ\text{C}$, both outside the tolerance 0,04 ($52{,}3$–$56{,}7\,{}^\circ\text{C}$), and a least-squares line gives $54{,}0\,{}^\circ\text{C}$. The solution's "53–56 °C hyväksytään" is not what the task can expect from the figure. — Fix: either give the task a figure whose points sit on readable grid values (e.g. a 5 kPa minor grid, points on whole grid values) and ask for a pressure far from a measured point, or give the measured values in the task text (`data`) and keep the figure as illustration; then align the solution's reading and the tolerance with what can be read.

## Polish
- exercises/exercises.json (fy3-3-L1-10) — "nestetypen lämpötila" equals the boiling point only for liquid nitrogen boiling at normal pressure (e.g. in an open dewar); the task names normal pressure only for the lookup. Optional B-type clause: "avoimessa astiassa normaalipaineessa". The solution's "Nestemäinen typpi on kiehuvaa" could say the same.
- exercises/exercises.json (fy3-3-L1-10) — repeats L1-03 inversely (77,4 K → −196 °C); physics fine.

## Checked
- MAFY value verified on mafytaulukot.fi (*Aineiden olomuodon muutokset*, 1 atm): typpi kiehumispiste $-196\,{}^\circ\text{C}$, as the solution uses.
- L1-10 recomputed: $T = -196 + 273{,}15 = 77{,}15\,\text{K} \approx 77\,\text{K}$; with −195,8 °C 77,35 K, inside tolerance 0,04; answers.py agrees. Rounding reason (whole degrees) right; check by back-conversion real.
- L1-10 solution complete; kelvin conversion as in the brief (numeric values, no "kelvinaste").
- L2-08 recomputed: endpoint slope $0{,}275\,\text{kPa/°C}$, $\theta = 15/0{,}275 = 54{,}5\,{}^\circ\text{C}$; least squares $k = 0{,}276$, $b = 75{,}1$, $\theta = 54{,}0\,{}^\circ\text{C}$. Physics (linear $p(\theta)$ at constant volume, closed rigid vessel stated) right; symbolic solve before substitution present.
- Figure code: points as the description lists; description does not give the answer.
- Rest of the set unchanged since PASS; hash same at start and end.
