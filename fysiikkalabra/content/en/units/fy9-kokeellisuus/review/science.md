VERDICT: FAIL
CONTENT-HASH: 57b16d7452a47e0a
SCOPE: delta: new tasks s7 (Measuring sliding friction) and s8 (The magnetic field of a coil and sources of error) and the changed intro; older tasks s1-s6 untouched

## Blocking
- **s8 b, criterion 3 and Reasonableness (A, causality; 7, assessment).** The point is given for "It cannot be known whether the dependence stays linear, for example when the coil warms up", and the solution gives the reason "a large current heats the wire of the coil and increases its resistance". The graph is $B$ against the current itself. For a long air-core coil $B = \mu_0 n I$ (given in the task) has no saturation, and a higher resistance changes the voltage needed for a given current, not $B$ at that current. A student who says "with no iron the law stays linear, so $4.9\,\text{A}$ is a sound estimate if coil and supply can carry it" is right and loses the point. Fix: the point goes for noting that the current is outside the measured range, so the coil and supply must be able to give it, and the estimate is checked by measuring.
- **s8 common mistakes, second item (A, assessment).** "the current is calculated as $12 : 6.2 \cdot 2.5\,\text{A}$" is listed as a mistake, but $(12/6.2) \cdot 2.5\,\text{A} = 4.84\,\text{A}$ is a correct proportion for a line through the origin and falls inside the accepted $4.8\text{–}5.0\,\text{A}$. Remove it or replace it with a real mistake.

## Polish
- s8 d: "the current heats the coil and changes its resistance" names no effect on $B$. The effect is real only if the current drifts between readings under a voltage-set supply, or if the sensor drifts with temperature.
- s8 a Answer: "values read are of two or three figures". All four have two.
- s7 a: a scale (calibration) error would also pass through the origin. "the zero point at least is in order" is right; one clause would make that explicit.

## Checked
- The translation matches the Finnish text part by part: the same numbers ($0.1\,\text{N}$, $0.3\,\text{N}$, $2.4\,\text{N}$, $12\,\text{mT}$, $0.04\,\text{mT}$), answers, tolerances, criteria and points. The decimal point is used throughout. "Sliding friction", "coefficient of sliding friction" and "normal force" follow the house terms; "turn density" is defined in the task. The level of the English is right for the age group.
- Numbers recomputed in the same script as the Finnish review, from the figure sources: s7 mean 0.2152, ±0.005, fit intercept 0.010 N, c 0.24 / 0.21 / 14.3 %, d 4.5 % and 0.93 %; s8 k = 2.467 mT/A, n = 1963 1/m, b 4.86 A, c 3.08 % and 0.645 %. All agree with answers.py.
- The physics is otherwise right: zero error vs slope, current reversal, the stated model conditions. Points: s7 14, s8 14, criteria summing to the part points. The intro says "Eight", which matches the 8 tasks.
- `practice.py check` OK; hash the same at start and end.
