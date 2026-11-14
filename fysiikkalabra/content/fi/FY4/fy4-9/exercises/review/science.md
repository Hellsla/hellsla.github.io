VERDICT: PASS
CONTENT-HASH: 0b29da9aa00d488c
## Blocking

## Polish
- content/fi/FY4/fy4-9/exercises/solutions.md (L3-02 Kaava) — Earlier note still stands: "$F\,\Delta t = mv_0 - 0$" writes the momentum change the wrong way round (initial minus final). Fix: write $-F\,\Delta t = 0 - mv_0$, which matches L2-01.
- solutions.md (L2-07 Vastaus) — Earlier note still stands: $1{,}50\,\text{m/s}$ has three significant figures, so it does not limit the result. Fix: name only the mass $0{,}50\,\text{kg}$ as the limiting datum.

## Checked
- The changed premise of L1-03 (fi, en, fi-easy) holds. A ball thrown vertically upwards has zero velocity at the top of its path, so "hetkellisesti levossa ylimmässä kohdassa" / "momentarily at rest at the highest point" follows from the throw, and $v_0 = 0$ is justified. The earlier wording left open why the ball was at rest; the new wording explains it.
- The three versions say the same thing: vertical throw, struck at the top, leaves at $18\,\text{m/s}$, weight neglected during the strike. fi-easy splits it into shorter sentences and drops no condition.
- The direction of the departing ball is not stated. That does not matter, because the task asks only for the size of the impulse. The impulse points in the ball's departure direction, as the solution's Järkevyys says.
- The L1-03 solution still fits in all three languages: Annettu $v_0 = 0$, the impulse principle with the hand's force as the net force (weight neglected), the symbolic $I = mv - mv_0 = mv$ before substitution, no conversions, and the reasonableness estimate.
- Recomputed: $I = 0{,}27\,\text{kg} \cdot 18\,\text{m/s} = 4{,}86\,\text{N}\cdot\text{s}$, rounded to $4{,}9\,\text{N}\cdot\text{s}$ (two significant figures, both data). `python -I answers.py` gives 4.86. The rounded answer is 0.8 % off, inside the 2 % tolerance.
- Nothing else in the exercise set changed (diff is this one task text). The data, answer, unit and tolerance are unchanged.
- Hash 0b29da9aa00d488c at start and end.
