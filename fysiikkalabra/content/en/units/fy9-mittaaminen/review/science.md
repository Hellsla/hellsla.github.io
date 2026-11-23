VERDICT: PASS
CONTENT-HASH: 3e94f6a46e4cf227
SCOPE: full: the three new "Pysähdy ja mieti" boxes (```pysahdy) in unit.md judged first against the Finnish version, then unit.md, inquiry.json, teacher.md and the Sovella set s1–s8 (tasks, solutions, answers.py, figures.py).

## Blocking
None.

## Polish
- Box 3 ($(t^2, s)$ line, $a = 2k$): the question does not repeat "from rest, time counted from the start". The paragraph just above states that condition and the box follows it, so this is class C. The Finnish box is the same.
- Carried over: the `### Hyväksytään myös` / `### Yleisiä virheitä` headings in the en solutions.md are in Finnish. If the renderer uses them as keys this is fine; otherwise translate them.
- s2 c: "about $\pm 20\,\text{kg/m}^3$" is $15\,\text{kg/m}^3$ rounded to one figure. That is correct, but writing "$\pm 15$, about $\pm 20$" would make the step visible.

## Checked
- Box 1 (does repeating remove a too-fast clock's systematic error): No. A systematic error has the same sign in every reading, so it stays in the mean. This is correct physics, the same as fi line 227, and consistent with the theory, the common-mistakes list and lahto-2/virhelaji.
- Box 2 (slope read from far-apart points of the line): the fitted line represents all the data, and large $\Delta x$ and $\Delta y$ shrink the relative reading error. Correct, the same as fi line 244, and consistent with lahto-3.
- Box 3: $s = \tfrac{a}{2}t^2$ gives $k = a/2$, so $a = 2k$. Correct, the same as fi line 351, and consistent with kuula-kouru and s8.
- One script (scratchpad `rc.py`, own least squares and extreme-line search) recomputed every number next to answers.py, and every value agrees:
  - Inquiry: lahto-1 2.705→2.7; kolikot 2.70 %; jousi 79.0 N/m and $L_0$ 0.135 m, with mistakes 48.6 and 8; kuula 1.24; kattila 10.0, with mistakes 13.0 and 16.1; gas −271.7 °C; tarkista-2 28 kg/m³; tarkista-1 means 1.8033 m, ±0.0005 and ±0.015.
  - s1: 13.71 s, 7.294 m/s, 26.26 km/h, Δv 0.123, Mira 13.96 ± 0.16.
  - s2: 102 µm, 79.85 g/m², 782.8 kg/m³.
  - s3: fit 0.9183 / 118.65 g; extreme lines 0.908–0.932, Δρ 0.012; the 60 ml row is 9.7 g off against a largest residual of 0.7 g; 1.378 kg.
  - s4: ratio 1.0205, 750 g.
  - s5: 0.477 m/s, intercept 0.358 m, extremes 0.464–0.492 m/s, forced line 0.634, deviation 0.247 m.
  - s6: pV grows by 8.1 % with every step positive; C 2.603 J, $V_0$ 1.77 ml, n 1.06·10⁻³ mol; with $V_0$ added, pV varies by 0.5 %.
  - s7: 30.0 N/m, limits 28.83–31.27, Δk 1.22, x-intercepts −0.20/+0.27 cm, $F_0$ −0.002 N, 15.0 ± 0.6 cm.
  - s8: slope 5.175, $s_0$ 0.010 m, limits 5.094–5.242, g 10.35 ± 0.15, 3.7 times Δg, frame interval factor 1.027.
- Physics, causality and assessment: air resistance correctly excluded as the cause in s8 c; isothermal and leak assumptions in s6 d have the right directions; s4 relative error versus zero error is correct. Every choice item has exactly one correct option, and the distractor feedback is right. Rubric parts match the prompts. Scope stays within FY1 measuring, plus FY3/FY4/FY5 links that a review unit is allowed. Figure descriptions match the data (anatomia, linearisointi 0.50 → 0.25 m/s²). `practice.py check` reports OK.
- Hash 3e94f6a46e4cf227 at the start and at the end.
