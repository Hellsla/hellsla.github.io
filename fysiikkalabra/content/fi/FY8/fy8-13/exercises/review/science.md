VERDICT: PASS
CONTENT-HASH: dc17de4ab0685d38

## Blocking

## Polish
- lessons/FY8/fy8-13/answers.py:43 — the comment says "80 · 0,5^2,4 = 15,14 µSv/h", but the value is 15,157 (the solution correctly says 15,16) — change the comment to 15,16.
- exercises/exercises.json (fy8-13-L2-10) — the graph's $d_{1/2} = 5{,}0\,\text{cm}$ differs from the lesson's "betonissa noin $4\,\text{cm}$" for Cs-137. This is physically fine, because the source is not named and a half-value layer depends on the energy. A short note such as "lähteen gammasäteily on energisempää kuin cesium-137:n" would stop students reading it as a contradiction.
- exercises/solutions.md:315 (L3-06 c) — reading $2{,}5\,\mu\text{Sv/h}$ at the graph's right edge is near the stated reading accuracy of about $1\,\mu\text{Sv/h}$. The sturdier route is five half-value layers ($80 : 2^5$), which is already in Järkevyys. It could also be named in "Kuvaajan lukeminen".

## Checked
- The hash dc17de4ab0685d38 was the same at the start and the end. I judged the diff: new L2-10 and L3-06, their solutions and two answers.py lines.
- The figure generator uses CHK_H0 = 80,0 and CHK_D = 5,0 (lesson-answers.py:78), so the values read in the solutions (80; 40 at 5 cm; 20 at 10 cm; 5 at 20 cm; 2,5 at 25 cm) come from the drawn curve.
- I recomputed L2-10: $80 \cdot 0{,}5^{2{,}4} = 15{,}157\,\mu\text{Sv/h}$, which rounds to 15. answers.py gives 15,157166. A tolerance of 0,04 accepts 14,55–15,76. Two significant figures are justified.
- I recomputed L3-06: $\dot{H}(20\,\text{cm}) = 80/16 = 5{,}0\,\mu\text{Sv/h}$ and $t = 20/5{,}0 = 4{,}0\,\text{h}$, which matches answers.py (4,0). The tolerance is 0,02. In c), $\dot{H}_\text{max} = 2{,}5\,\mu\text{Sv/h}$ gives $d = d_{1/2}\log_2(80/2{,}5) = 25{,}0\,\text{cm}$. "Vähintään 25 cm" is the correct boundary, because the dose there equals the limit and does not exceed it.
- The model is the lesson's half-value law with its condition stated in the task ("noudattaa puoliintumispaksuuden lakia"). L3-06 states the constant-rate and no-scatter assumptions, and the solution uses the same ones.
- L3-06 d): the mechanism is right. Scattered and build-up radiation add to the dose rate behind a real shield, which matches the lesson's "mitoitetaan varmuusmarginaalin kanssa".
- Both solutions solve symbolically before substituting and use the lesson's notation ($\dot{H}$, $\dot{H}_0$, $d_{1/2}$, $H = \dot{H}t$).
- The tasks are within the FY8 central contents and scope (doses, protection by time and shielding). The alt text gives $\dot{H}_0$ but not $d_{1/2}$ or the answers.
