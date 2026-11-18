VERDICT: PASS
CONTENT-HASH: 35eb2ff6a77795e8
Mode: delta, round 2 (new tasks L2-09 and L3-06 on figure fy8-16/hubble-t; "(esimerkkiaineisto)" removed from two table captions)

## Blocking
- none

## Polish
- none

## Checked
- Round-1 finding 1 (L3-06 c, "mahdoton galaksin nopeudeksi") is fixed in fi, en and fi-easy. The text now says $v = cz$ is only the small-$z$ approximation and that $z = 3{,}00 \to 3{,}00\,c$ is "merkki siitä, että likiarvo ei enää päde". It no longer claims recession faster than $c$ is impossible.
- Round-1 finding 2 (rounding reason) is fixed in all three languages. "Kaksi merkitsevää numeroa b)-kohdassa", because $0{,}10\,c$ has two figures, and $H_0 = 72{,}0$ is read from the grid point with three.
- I recomputed both answers in one script. L2-09: $z = 0{,}035253$, $v = 10\,569\,\text{km/s}$, $d = 146{,}79\,\text{Mpc}$. L3-06: $d = 0{,}10c/72 = 416{,}39\,\text{Mpc}$. Both match answers.py and exercises.json (146,8 and 416,4).
- Tolerance 2 %: a student who rounds to 147 Mpc is off by 0,14 % and one who rounds to $4{,}2 \cdot 10^2$ Mpc by 0,87 %, so both stay inside it.
- Figure: the line uses $H_0 = 18000/250 = 72$. A least-squares fit through the origin of the nine T2 points gives $72{,}4$, so the drawn line is a fair fit. Neither the figure nor its description gives either answer away.
- L2-09: $z < 0{,}1$, so $v = cz$ is valid. The solution is symbolic first ($d = cz/H_0$), and the 147 Mpc sits between the points at 120 and 160 Mpc, whose speeds bracket $v$.
- L3-06: the extrapolation beyond the 285 Mpc data (×1,46) and the assumption it rests on are stated, as the guardrail on extrapolation asks. The top of the axis, $21\,000\,\text{km/s}$, corresponds to $z = 0{,}070$.
- The task texts give $c$, the $z < 0{,}10$ condition, the axis end and the farthest point. Both tasks stay inside the FY8 scope and use the brief's notation.
- Removing the caption labels changes no physics.
- Hash at start and end: 35eb2ff6a77795e8.
