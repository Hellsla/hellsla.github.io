VERDICT: FAIL
CONTENT-HASH: 0f632e8514615b4f

Delta review of the new `hints` in `sovella/tasks.json` (work queue 11c), against each part's rubric, answer and `sovella/solutions.md`. The en hints say the same physics as fi and carry the same two errors.

## Blocking

1. **s3 a, hint 2 (en), A.** "…and look where it meets the vertical axis." With scales starting from zero, the fitted line never meets the vertical axis: its intercept is $\Delta m \approx -9\,\text{g}$. The rubric (criterion 4) and the solution want the line extended to the horizontal axis and not forced through the origin. Replacement: "…Fit a line that runs between the points, and check whether it passes through the origin."
2. **s6 d, hint 2 (en), B.** "Which of them can give out its internal energy to the air?" This implies that the discs cannot, yet part c finds that about $40\,\%$ of the discs' energy goes to the air. Replacement: "Which of them can give out its internal energy to the air at a high power for the whole long descent without overheating?"

## Polish

3. **s3 b, hint 2 (en).** "…the heater supplies the energy $P\,t$. Write down conservation of energy…" This invites $Pt = r\,\Delta m$, the one-point model that part d criticises. Suggest: "The energy needed for vaporisation is $Q = r\,\Delta m$; part $P_\text{loss}\,t$ of the heater's energy $P\,t$ is conducted to the room: $(P - P_\text{loss})\,t = r\,\Delta m$. Work out what the slope of the line tells."

## Checked

All numbers the hints state are right and use the decimal point: $0.0300\,\text{m}$, $334\,000\,\text{J/kg}$, $350\,000\,\text{W}$, $86\,400\,\text{s}$, $15 \cdot 10^{6}\,\text{J/kg}$, $0.80$, $0.85$, $896\,\text{J/(kg}\cdot\text{K)}$ and $0.60\,\text{kg}$.

I recomputed every answer they lead to with my own formulas:
- s1: $21.9\,\text{GJ}$ and $17.4\,\text{h}$; phase shares $16/82/2\,\%$.
- s2: $81.6\,\text{K}$, $1.67\,\text{kW}$ and $35.8\,\%$.
- s3: $2.26\,\text{MJ/kg}$ and $69\,\text{W}$; the d percentage is $12.6\,\%$.
- s5: $370.8$ and $333.0\,\text{kJ/kg}$.
- s6: $31.5\,\text{K}$, $133.7\,\text{K}$ and $40.2\,\%$.
- s7: $0.222\,\text{K/s}$, $900$ and $360\,\text{s}$.
- s8: $2083$, $333$, $270\,\text{kJ}$ and $0.30\,\text{kg}$.

Symbols match the en solutions ($c_\text{w}$, $c_\text{i}$, $m_\text{wood}$, $m_\text{stone}$, $m_\text{discs}$, $m_\text{m}$, $P_\text{loss}$, $Q_\text{brakes}$). No hint gives a final answer. The physics of s4 and s7 d matches the rubrics.
