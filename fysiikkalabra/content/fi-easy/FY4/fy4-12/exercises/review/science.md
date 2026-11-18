VERDICT: PASS
CONTENT-HASH: 4e1a211f752c40d9

## Blocking

## Polish
- content/fi-easy/FY4/fy4-12/exercises/solutions.md (graph-reading task at @@ -34, Kaava) — "nopeus on $v = \dfrac{\Delta x}{\Delta t}$" is stated but the step does not say that $v_\text{A}$ and $v_\text{B}$ are read from the graph this way; "nopeudet luetaan kuvaajasta, $v = \Delta x/\Delta t$" ties it to Sijoitus.
- solutions.md (bus, no meeting; Kaava) — "Sijoitetaan tämä välimatkaan ja sievennetään" jumps to $s_\text{min} = -x_{0\text{R}} - \dfrac{v^2}{2a}$; one intermediate row ($\tfrac12 a (v/a)^2 - x_{0\text{R}} - v \cdot v/a$) would let a student follow the simplification.
- solutions.md (bus, first meeting) — saying that $x_{0\text{R}} < 0$ (the runner behind the bus) is why both roots are positive would make "pienempi juuri" self-explaining.

## Checked
- Hash 4e1a211f752c40d9 at the start and the end; since 062f457c28^ only solutions.md changed: `**Kaava:**` lines and five Sijoitus lines that now substitute into the general symbolic form (signed $v_\text{B}$: $2{,}0 - (-3{,}0)$, $6{,}0 - (-2{,}0)$; $s_\text{min}$ from the simplified formula; $t = v_\text{A}/a_\text{B}$ shown); numbers, answers, tolerances, tasks, ids, exercises.json and answers.py unchanged.
- Recomputed: $t = 20/5{,}0 = 4{,}0\,\text{s}$; $40/8{,}0 = 5{,}0\,\text{s}$; $30/8{,}0 = 3{,}75\,\text{s}$; $s_\text{min} = 20 - 16 = 4{,}0\,\text{m}$ (same as the old $16 + 20 - 32$); $t = 6{,}0\,\text{s}$, $s_\text{max} = 36\,\text{m}$.
- $s_\text{min} = -x_{0\text{R}} - v^2/(2a)$ and $s_\text{max} = \tfrac12 v_\text{A} t$ at equal speeds derived correctly; equal speeds give the extreme distance, not the meeting, as the brief's lesson says.
- Every meeting task now starts from $x = x_0 + vt$ or $x = x_0 + v_0 t + \tfrac12 a t^2$, writes both position functions in one coordinate system and sets $x_\text{A} = x_\text{B}$ (the lesson's Kohtaamisehto); signs of velocities toward each other right (trains $D - v_2 t$, scooter $D - vt$).
- Quadratic roots: bus/runner, scooter, car/cyclist and delayed-start ($\tau$) roots right; root choice justified.
- Overtaking task: relative advance $\tfrac12 a t^2$ from $x_\text{h} - x_\text{k}$; consistent with Periaate.
- Captures: none opened (fi-easy judged from text and the packet).
