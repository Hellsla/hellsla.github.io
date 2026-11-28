VERDICT: PASS
CONTENT-HASH: efc68d20d4e31a89

## Blocking
None.

## Polish
- fy3-s3-c Principle: the stray bracket is still there, "(part d) estimates the effect of warming)". Reword to "part d estimates the effect of warming".
- fy3-s3-d: the third bullet still carries the closing conclusion ("rough estimate, not a guarantee, leave a reserve"), and the ideal-gas note sits in the same bullet. The rubric awards a point for the conclusion, so give it its own paragraph.
- fy3-s3-c Principle: say in a word that "the air used from the tank" is what Δp V = Δn RT describes. The Principle does this already, but the Formula could carry a short label on that row.
- fy3-s1-c Formula: the P_o, P_a, eta rows are a chain of definitions. A short word label on "P_a = P" would help.
- fy3-s2: the table's source line (source_note) is not in the packet. Check that the page shows it.

## Checked
- Round 2, s3 c Formula: it now starts from the tank's two states, p_1 V = n_1 RT and p_2 V = n_2 RT. It subtracts them to get Δp V = Δn RT, sets pV = Δn RT at the depth pressure, and solves symbolically for V and then t. The earlier problem, where Δp V = nRT could be read as the whole tank's air, is fixed. A student can follow every step.
- Numbers: 15 000 kPa · 12.0 l / 248 kPa = 725 l, and 725 / 20 = 36 min. This matches the answer and the tolerance.
- The litre is written \textsf{l} in the task text, the solution and the criteria. The unit "l/min" is plain text, which is acceptable.
- The task still demands independent application. No heading or prompt names a formula, and the assumption that the tank and the lungs are equally warm is stated and then evaluated in d.
- The criteria are specific and fair, with no points for irrelevant things. The common mistakes are real, for example using only ρgh, using Celsius, and comparing the tank with the surface pressure, which gives 89 min.
- The workload fits a 2-credit module, and the three tasks differ (graph, phase change, gas laws).
- Hash confirmed with practice.py hash FY3 --lang en.
