VERDICT: FAIL
CONTENT-HASH: bce5197e309debb6

## Blocking
- lesson.md:111 (Formula, after $P = UA\Delta T$) — **B / consistency**: "As long as there is ice in the bag, the inside temperature is $0\,{}^\circ\text{C}$ and $\Delta T$ is the outside temperature" states as fact what the Key idea now corrects: only the ice–water mixture in thermal equilibrium stays at about $0\,{}^\circ\text{C}$, "elsewhere in the cool bag the temperature can be higher". The worked example and the Investigate texts already present it as the model's assumption. Fix: "In the model, the inside of the bag is taken to be at $0\,{}^\circ\text{C}$ as long as there is ice, so $\Delta T$ is the outside temperature in degrees Celsius."

## Polish
- inquiry.json `kayra` solution (Principle) and `taulukko` text: "the inside stays/is at $0\,{}^\circ\text{C}$" — prefix "in the model" as the activity text already does ("the model assumes that everything inside is at the same temperature").
- Common misconception, mixing example: "the temperature of the mixture is $0\,{}^\circ\text{C}$" — "about $0\,{}^\circ\text{C}$" would match the Key idea (C).

## Checked
- Full review: Key idea's new wording (ice–water mixture in equilibrium at about $0\,{}^\circ\text{C}$, the rest of the bag may be warmer) is correct; boundary cases in step 4 and the Summary ("not enough → melting point", "just enough → exactly the melting point", ice initially at $0\,{}^\circ\text{C}$) match the guardrails.
- Recomputed in one script: worked example $41\,900\,\text{J}$, $33.6\,\text{W}$, $t = 8.69 \cdot 10^3\,\text{s} = 2.4\,\text{h}$, 2.8 h without drinks, $19\,\text{K/h}$ after melting; sauna $67$/$452\,\text{kJ}$; graph plateau $3.68\,\text{h}$, $E \approx 333\,\text{kJ}$; table $t$ 8.59 … 2.86 h, $Pt = 334\,\text{kJ}$; prediction 2 $2.9\,\text{h}$; löyly share 85.7 % (mistakes 14.3, 6.0); transfer $64.9\,\text{s}$ (mistakes 8.4, 56.5); check 2 $213\,\text{kJ}$ (mistakes 200, 12.6); check 3 criterion 13 %; exit $175.5\,\text{kJ}$. All agree with lesson-answers.py.
- Physics: $s = 334\,\text{kJ/kg}$ ≈ 80 K of water heating, glycol mixture $c \approx 3500$, ice conducts better than water, steam condensation releasing $rm$, coolant $P = c(m/t)\Delta T$ in steady state: correct.
- Every choice has exactly one correct option with right feedback; no simulation; the model's values are labelled as model values.
- Hash at start and end: bce5197e309debb6.
