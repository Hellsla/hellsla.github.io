VERDICT: PASS
CONTENT-HASH: e7a0733ff5667593

Follow-up review of the fix commit 2c31ff041 (delta from bce5197e309debb6, whose full review is kept below). Change: lesson.md:111, the paragraph after $P = UA\Delta T$.

## Blocking

None.

## Polish
- inquiry.json `kayra` solution (:126 Principle), `taulukko` (:135), model answer (:167): "the inside stays/is at $0\,{}^\circ\text{C}$" — prefix "in the model" as the activity text already does (C).
- Common misconception, mixing example: "about $0\,{}^\circ\text{C}$" would match the Key idea (C).

## Checked
- Earlier blocking item resolved: "In the model, the inside of the bag is taken to be at $0\,{}^\circ\text{C}$ as long as there is ice, so $\Delta T$ is the outside temperature in degrees Celsius. Then all the energy coming through the wall melts ice" — the formula $t = sm/(UA\Delta T)$ now carries its condition and agrees with the Key idea.
- Consistency: grep of "$0\,{}^\circ\text{C}$" in lesson.md and inquiry.json — no remaining unqualified claim outside the model contexts listed under Polish.
- Key idea (ice–water mixture in equilibrium at about $0\,{}^\circ\text{C}$, elsewhere warmer), step 4 boundary cases and Summary match the guardrails.
- Recomputed: worked example $41\,900\,\text{J}$, $33.6\,\text{W}$, $2.4\,\text{h}$, 2.8 h without drinks, $19\,\text{K/h}$ after melting; sauna $67$/$452\,\text{kJ}$; plateau $3.68\,\text{h}$, $E \approx 333\,\text{kJ}$; table 8.59 … 2.86 h, $Pt = 334\,\text{kJ}$; prediction 2 $2.9\,\text{h}$; löyly 85.7 % (mistakes 14.3, 6.0); transfer $64.9\,\text{s}$ (mistakes 8.4, 56.5); check 2 $213\,\text{kJ}$ (mistakes 200, 12.6); check 3 13 %; exit $175.5\,\text{kJ}$. All agree with lesson-answers.py.
- Physics: $s = 334\,\text{kJ/kg}$, glycol $c \approx 3500$, steam condensation $rm$, coolant $P = c(m/t)\Delta T$: correct.
- Every choice has exactly one correct option with right feedback; model values labelled.
- Hash at start and end: e7a0733ff5667593.
