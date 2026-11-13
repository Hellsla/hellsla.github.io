VERDICT: PASS
CONTENT-HASH: fd054a287d5cf164
SCOPE: delta added-exercise from 2040e0e2c0e5a3c7 base 81db4a6fd727
## Blocking

## Polish

## Checked
- Round 2 change, lessons/FY4/fy4-10/figures.py ex-vt-kaarryt: `ticks_below=True` only moves the time tick labels under the plot, away from the $v = 0$ axis. I rendered the figure: A goes 0.8 → 0.2 m/s and B goes −0.4 → 0.6 m/s at 2.0 s, all still read at grid crossings, and no data point moved.
- L2-09 recomputed: $m_\text{B} = 0.50 \cdot 0.6 / 1.0 = 0.30\,\text{kg}$. Momentum is 0.28 kg·m/s before and after, and kinetic energy drops (0.184 J → 0.064 J), so the collision is physically possible. The forgotten-sign value of 1.5 kg is right.
- L3-06 recomputed: $v = 0.60$, $v' = 0.20\,\text{m/s}$, $m_\text{B} = 0.60\,\text{kg}$, $\Delta E_\text{k} = 0.054 - 0.018 = 0.036\,\text{J}$. The fraction $m_\text{B}/(m_\text{A}+m_\text{B}) = 2/3$ is right.
- answers.py run: every numeric answer equals exercises.json.
- Script comparison with content/fi: answers, units, tolerances, figure ids and every number identical.
