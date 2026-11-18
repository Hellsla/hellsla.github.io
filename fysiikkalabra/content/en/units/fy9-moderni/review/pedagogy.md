VERDICT: PASS
CONTENT-HASH: f4531b7790ea5ae7
SCOPE: delta: new tasks s8 (concrete wall) and s9 (recession of galaxies) and the intro; older tasks untouched

## Blocking
- (none)

## Polish
- s9 a: the task text gives the line's grid point ($250\,\text{Mpc}$, $18\,000\,\text{km/s}$) and the figure description repeats it. The graph need not be read, so the `graph_read` criterion measures nothing and the nine data points are decoration. Better: drop the point from the text and the description so $H_0$ is read off the grid; s8 already works that way (the description gives only the value at $d=0$).
- s9 a: the second "far apart point" is the origin, which is given. Reading a graph is only practised if the point has to be found.
- s8 gives the model $\dot{H}=\dot{H}_0 e^{-\mu d}$ in the text. That suits the graph-reading goal, but recognising exponential attenuation is not practised; a conscious choice.
- s9 c: the text gives the constant-velocity assumption, not the chain $t=1/H_0$; the structure is not revealed. Good.
- Rounding: inputs have two significant figures and the answers too (6.6; 24; 120; 1.4·10^10); the exact $\mu$ used in later parts is explained in the solution.

## Checked
- Opened the en packet: checks (practice.py check OK), s8 and s9 in tasks.json (own English text), solutions.md, answers.py and the figure descriptions.
- Translation fidelity: same numbers, points, criteria and tolerances as the Finnish; decimals are points (1.5 h, 0.14), "recession velocity", "attenuation coefficient", "dose rate", "Hubble constant" are the right terms; the "Milky Way" explanation criteria match the Finnish. Units fields (1/cm, µSv/h, a) are language-neutral. Language level suits upper-secondary students.
- Recomputed: $\mu=0.1386$ per cm; $6.6\,\mu\text{Sv/h}$; $330\,\text{h}$, $2.18\,\text{mSv}$; $3.03\,\mu\text{Sv/h}$, $23.6\,\text{cm}$; $H_0=72$; $116.7\,\text{Mpc}$; $1.36\cdot10^{10}\,\text{a}$. Tolerances accept the two-figure roundings.
- Level and variety: s8 reading, model, judgement, design and assumption; s9 reading, inverse calculation, unit conversion, conceptual explanation. Points 3+3+3+4 and 3+3+4+3 equal the criterion sums; common mistakes are real.
- Figure alt names ($\dot{H}$, $d$, $v$) match the text; s8's alt does not give the $5.0$ read-off.
- Intro says "Nine" for 9 tasks (136 p); problems 7, 8, 9 correctly referred to. 360 px: relied on check_layout and shots.md (same hash), did not open captures.
- Hash same at start and end.
