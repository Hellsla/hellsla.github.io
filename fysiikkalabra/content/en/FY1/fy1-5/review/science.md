VERDICT: FAIL
CONTENT-HASH: 40c234e16b882e67

## Blocking
- content/en/FY1/fy1-5/exit-ticket.json:8 — (A, internal consistency) the new answer writes the model as $x = x_0 + vt$, but the lesson defines position as $s$ with initial position $s_0$ (lesson.md:308–312, "Formula: Uniform motion"; inquiry.json and the Voyager example likewise). The exit ticket introduces an undefined symbol for the same law, so it does not say what the theory says. — fix: write $s = s_0 + vt = 4\,\text{m} + 3\,\text{m/s} \cdot 2\,\text{s} = 10\,\text{m}$ (the Finnish exit-ticket.json:8 has the same $x$/$x_0$ and needs the same change).

## Polish
- content/en/FY1/fy1-5/exit-ticket.json:8 — "distance travelled" could carry the lesson's symbol, $\Delta s$: $3\,\text{m} \to 6\,\text{m}$, linking it to "only the distance $\Delta s$ is directly proportional to time" (lesson.md:319).

## Checked
- Delta: new exit-ticket item 2 (trolley $s_0 = 4\,\text{m}$, $v = 3\,\text{m/s}$): recomputed 7 m at 1 s, 10 m at 2 s, distance 3 m → 6 m; answer "No" correct.
- The reasoning (position not proportional to time when $s_0 \neq 0$, distance is) matches lesson.md:319 and the inquiry's misconception about direct proportionality.
- Question gives the start position at $t = 0$ implicitly ("starts at"); with uniform motion along a line in the positive direction stated in the theory, the model applies.
- Item 1 unchanged (90 km/h, 20 min → 30 km).
