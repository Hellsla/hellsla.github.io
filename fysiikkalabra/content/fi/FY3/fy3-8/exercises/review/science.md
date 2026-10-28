VERDICT: PASS
CONTENT-HASH: e84f30aeda6e6c9c

Delta review over the audit's PASS (95f447a9c89c7a99): L2-04 replaced by figure task length-graph (α of a beam), LaTeX units elsewhere.

## Blocking
- none
## Polish
- solutions.md:90 Järkevyys — "Millimetrin murto-osa metrien pituudella" does not fit the 3,0 mm read here. Say "noin 0,6 mm metriä kohti 50 K:n muutoksella" or drop the sentence.
- solutions.md:89 says 11,6…12,4 is accepted, but tolerance 0,03 on 12 accepts 11,64…12,36. The readings are exact, so this is cosmetic; narrow the stated range or set tolerance 0.034.
- exercises.json:14 and :56 — the minus of −27 °C and −22 °C sits outside the maths ("−$27\,...$"); put it inside $...$.
## Checked
- Recomputed: α = 0,0030 m / (5,00 m · 50 K) = 12 · 10⁻⁶ 1/K → steel; aluminium would give 5,75 mm and copper 4,25 mm (checked); answers.py 12,0.
- Figure length-graph: (20 °C; 0) and (70 °C; 3,0 mm) on 10 °C × 0,5 mm grid crossings; the description names no α or material.
- ΔT = 50 K is within the about 100 K range where the linear formula holds (guardrail); two significant figures from the 3,0 mm reading.
