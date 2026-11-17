VERDICT: PASS
CONTENT-HASH: eacff728d2981da8

## Blocking

## Polish
- lessons/FY8/fy8-13/answers.py:43 — the comment says "15,14 µSv/h", but the value is 15,157 (the solution says 15,16) — change the comment to 15,16.
- exercises/solutions.md:315 (L3-06 c) — reading $2{,}5\,\mu\text{Sv/h}$ at the graph's edge is near the reading accuracy of $1\,\mu\text{Sv/h}$. The five-half-value-layer route ($80 : 2^5$) is sturdier and is already in Järkevyys. It could also be named in "Kuvaajan lukeminen".

## Checked
- The hash eacff728d2981da8 was the same at the start and the end. I judged the diff: new L2-10 and L3-06, their solutions and two answers.py lines.
- The figure is drawn from H0 = 80,0 µSv/h and d½ = 5,0 cm, so the readings in the solutions match the curve.
- I recomputed L2-10: $80 \cdot 0{,}5^{2{,}4} = 15{,}157\,\mu\text{Sv/h}$, which rounds to 15. A tolerance of 0,04 accepts 14,55–15,76.
- I recomputed L3-06: $5{,}0\,\mu\text{Sv/h}$ and $4{,}0\,\text{h}$. In c), $2{,}5\,\mu\text{Sv/h}$ gives exactly $25\,\text{cm}$. "Vähintään" is the correct boundary, because at 25 cm the dose equals the limit.
- The added explanations are physically right: annosnopeus as the dose per hour, $d_{1/2}$ as the thickness that halves the rate, and "siroaa eli kimpoaa", a fair simplification at this level (C).
- The numbers, the assumptions (half-value law, constant rate, scattering ignored), the significant figures and the d) model answer are the same as in the fi version.
