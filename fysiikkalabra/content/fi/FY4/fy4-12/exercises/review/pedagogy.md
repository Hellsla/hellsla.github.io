VERDICT: PASS
CONTENT-HASH: 0e7961781cc75498
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,typography,wording from bc0ea52e2d8d623c base b5600a6
## Blocking
(none)
## Polish
- solutions.md, bus-and-runner (x0R = -8,0 m), cyclist-and-scooter, car-overtakes-cyclist and truck-overtaking tasks, Kaava — each is now 90–110 words in one paragraph; split after the equation of meeting ("…, eli … = 0.") so the quadratic solution is its own short paragraph.
- solutions.md, the (t,x) graph task, Kaava — the formula $t = \dfrac{x_{0\text{B}} - x_{0\text{A}}}{v_\text{A} - v_\text{B}}$ is derived although the answer is read from the graph; fine as a check, but the Kaava could end "…; tässä $t$ luetaan kuvaajasta leikkauspisteen vaakakoordinaattina" so the order graph first, formula as check is clear.
- solutions.md, the minimum-distance task, Kaava — "Sijoitetaan tämä välimatkaan ja sievennetään: $s_\text{min} = -x_{0\text{R}} - \dfrac{v^2}{2\,a}$" skips the line where $\tfrac12 a t^2 - v t$ becomes $-\dfrac{v^2}{2a}$; add "$\tfrac12\,a\,\dfrac{v^2}{a^2} - v\,\dfrac{v}{a} = -\dfrac{v^2}{2a}$".
## Checked
- Round 1, delta: the Kaava rewrites, paragraph splits and the caption-label change judged; numbers, answers, tasks and ids unchanged (Sijoitus lines only gain explicit signs, "- (-3,0 m/s)", same values).
- Every changed Kaava now starts from $x = x_0 + v\,t$ (or $x = x_0 + v_0 t + \tfrac12 a t^2$), the meeting condition $x_\text{A} = x_\text{B}$, then solved for the asked quantity in symbols before the Sijoitus.
- Spot-checked the algebra of all rewritten chains (meeting time, overtaking, quadratic roots, $s_\text{min} = -x_{0\text{R}} - v^2/(2a)$, $s_\text{max}$): all correct and consistent with the substitutions.
- Sign handling is explicit: $v_\text{B} = -3{,}0\,\text{m/s}$ shows as "$2{,}0 - (-3{,}0)$" in the substitution; the graph task derives $v_\text{B}$ before using it.
- Truck-overtaking and maximum-distance tasks: the relative-motion idea is introduced in symbols before numbers, and $t = v_\text{A}/a_\text{B}$ is now computed in Sijoitus.
- Marker "esimerkkiaineisto" removed from captions per the teacher's approval: no student-facing information lost.
- Captures opened: content/fi/FY4/fy4-12/review/shots/fy4-12-open-exercises-L3-1280-2.png (Kaava of the bus task as running text with inline formulas, readable, nothing clipped); phone widths judged from the text.
