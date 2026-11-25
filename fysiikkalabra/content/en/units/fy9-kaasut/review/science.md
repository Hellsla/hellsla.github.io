VERDICT: PASS
CONTENT-HASH: a08354d9b60cd1ad

Delta review (work queue 11c): only the new `hints` in `sovella/tasks.json` (en), diff against origin/main. 9 tasks, 33 parts, 99 hints.

## Blocking
None.

## Polish
1. s2 b, hint 2 (en): the task and the solution call $H$ the "heat of combustion"; the hint says "heating value". Replace "where $H$ is the heating value" with "where $H$ is the heat of combustion"; in hint 3 replace "the heating value to $\text{J/kg}$" with "the heat of combustion to $\text{J/kg}$".
2. s2 c, hints 2–3 (en): the symbols $P_\text{out}$ and $P_\text{rec}$ are not the ones the solution uses ($P_2$ for the heat power given away, $P_\text{h}$ for the recovered heat power). Not wrong, but a student who compares with the model answer meets two names. Replace them with: hint 2 "$P_0 = P_\text{s} + P_2$, so the heat power given out is $P_2 = P_0 - P_\text{s}$"; hint 3 "$\eta_\text{tot} = \dfrac{P_\text{s} + P_\text{h}}{P_0}$".

## Checked
- Every hint against its part's model, rubric, solution and answer: same laws (force balance $\Delta p\,A = mg$, $pV = nRT$ and its constant-$n$ forms, $Q = cm\Delta T$, $Q = \Delta U + W$, $W = Q_1 - Q_2$, $P_1 = P_W + P_2$, $F_{\mu 0} \le \mu_0 N$), same sign conventions, same conversions; no hint states a part's final answer.
- Recomputed: s1 a $\Delta p = 562\,\text{kPa}$; s5 a $\Delta n = 0.129\,\text{mol}$, $M = 25.5\,\text{g/mol}$; s6 a/b/c $11.2$, $18.7$, $37.4\,\text{kPa}$; s7 c $\Delta T = 11.3\,\text{K}$; s3 c hint 3's check from one point ($5\,{}^\circ\text{C}$, $38.2\,\text{ml}$) gives $1.67\,\text{mmol}$, consistent with $1.65\,\text{mmol}$ from the slope; s4 b hint 3's $23\,\text{K}$ vs $276\,\text{K}$; s9 c the volume ratio check.
- Values stated in hints ($T = 298.15\,\text{K}$, $104\,000\,\text{Pa}$, $0.0160\,\text{kg/mol}$, $1\,\text{h} = 3600\,\text{s}$, $\pm 0.3\,\text{ml}$, $-20 + 273.15$) match the task data; numbers with units are LaTeX with decimal points.
- Evaluation parts (s3 d, s4 a, s5 b, s7 d–e) and the design part (s5 c): hints point at the mechanism (systematic offset leaves the slope unchanged; need for a cold reservoir; $M = \Delta m/\Delta n$ directions; $\Delta m = \dfrac{MV}{RT}\Delta p$) without dictating the conclusion; s7 c hint 3 matches the solution's "upper estimate".
- s6 a hint 1 (zero rim force at the limit) and s6 b hint 2 ($N = F_\text{p}$ horizontal, friction carries the weight) agree with the force-diagram rubric.
- Content hash the same at the start and the end.
