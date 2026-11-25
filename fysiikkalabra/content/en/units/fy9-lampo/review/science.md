VERDICT: PASS
CONTENT-HASH: cc078aeb3697aa69

This is a round 2 delta review of the `hints` in `sovella/tasks.json`. I judged them against each part's rubric, answer and `sovella/solutions.md`.

## Blocking

None. The three round 1 findings are resolved:
- s3 a, hint 2: it now says to fit a line between the points and to check whether it passes through the origin. It no longer points to the vertical axis. This agrees with rubric criterion 3 (the line is not forced through the origin) and with the horizontal-axis intercept used in c.
- s3 b, hint 2: it now gives the solution's energy balance $(P - P_\text{h})\,t = r\,\Delta m$, so the slope is $t/r$. This is the same model as rubric criterion 2, not the one-point model that d criticises.
- s6 d, hint 2: it now asks which object can give energy to the air at a high power for the whole descent. It no longer implies that the brake discs give no energy to the air, so it agrees with c (about $40\,\%$ goes to the air) and with the rubric.

## Polish

1. s3 b, hint 1 (en). "The heater supplies energy that the water takes as it vaporises" still suggests that all of the heater energy goes into vaporisation. Hint 2 corrects this, so it is not an error. Suggested text: "Most of the heater's energy vaporises water. Which feature of the graph tells how much more water vaporises when the power increases?"

## Checked

- I recomputed s3 with a least-squares fit: the slope is $0.1326\,\text{g/W}$, the intercept is $-9.1\,\text{g}$, the horizontal-axis intercept is $69\,\text{W}$, $r = 2.26\,\text{MJ/kg}$, and the one-point result is $12$–$13\,\%$ too high. These agree with the answers and the rubric's accepted ranges. No hint states a part's final answer.
- s6 a–d: the $0.85$ share, the conversions $h = 250\,\text{m}$ and $s = 4.0\,\text{km}$, and the energy chain are unchanged from round 1 and correct.
- The symbols match the solutions: $P_\text{loss}$ (as in the English solutions), $m_\text{discs}$, $Q_\text{brakes}$. Numbers with units are in LaTeX with a decimal point. The physics is the same as in the fi hints.
- I ran the hash at the start and at the end, and it was the same both times.
