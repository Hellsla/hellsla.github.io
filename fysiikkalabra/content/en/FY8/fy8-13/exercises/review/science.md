VERDICT: PASS
CONTENT-HASH: a632bdf9634c4105

## Blocking

## Polish
- lessons/FY8/fy8-13/answers.py:43 — the comment says "15,14 µSv/h", but the value is 15.157 (the solution says 15.16) — change the comment to 15,16.
- exercises/exercises.json (fy8-13-L2-10) — the graph's $d_{1/2} = 5.0\,\text{cm}$ differs from the lesson's Cs-137 value for concrete (about 4 cm). This is physically fine for an unnamed source. A short note that the source's gamma rays are more energetic than Cs-137's would stop students seeing a contradiction.
- exercises/solutions.md:315 (L3-06 c) — reading $2.5\,\mu\text{Sv/h}$ at the right edge is near the stated reading accuracy of 1 µSv/h. The five-half-value-layer route ($80 : 2^5$) is sturdier and is already in Reasonableness. It could also be named under "Reading the graph".

## Checked
- The hash a632bdf9634c4105 was the same at the start and the end. The packet's lesson brief is empty, but the diff can be judged from the fi brief and the figure code. I judged the diff: new L2-10 and L3-06, their solutions and two answers.py lines.
- The figure is drawn from H0 = 80.0 µSv/h and d½ = 5.0 cm, so the readings (40 at 5 cm, 20 at 10 cm, 5 at 20 cm, 2.5 at 25 cm) match the curve.
- I recomputed L2-10: $80 \cdot 0.5^{2.4} = 15.157\,\mu\text{Sv/h}$, which rounds to 15. A tolerance of 0.04 accepts 14.55–15.76. Two significant figures are justified.
- I recomputed L3-06: $\dot{H} = 5.0\,\mu\text{Sv/h}$ and $t = 4.0\,\text{h}$, which matches answers.py. In c), $\dot{H}_\text{max} = 2.5\,\mu\text{Sv/h}$ gives exactly 25 cm. "At least 25 cm" is the correct boundary, because the dose there equals the limit.
- The task states the conditions of the model (the half-value law, a constant rate, scattering ignored), and the solutions use the same ones. The scattering margin in d) is physically right.
- The numbers, symbols and units are the same as in the fi version. The solutions solve symbolically before substituting.
