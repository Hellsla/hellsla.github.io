VERDICT: PASS
CONTENT-HASH: d049914a3ec3f36c

Science review (round 2) of the en translation of fy9-kaasut. Source: content/fi/units/fy9-kaasut/.

## Blocking
None.

## Polish
1. The concept map `kartta` still draws its three branch headings in Finnish (neste, kaasu, lämpövoimakone). This does not change any physics, but it is Blocking for pedagogy and visual. See visual.md 1.
2. $P_\text{l}$ (recovered heat power, s2 c) uses a Finnish-derived subscript. It is defined in the text, so this is optional: $P_\text{h}$ would read better.

## Round-1 findings
- Polish 1 ($W_\text{k}$ and $\eta_\text{kok}$): fixed. $W_\text{g}$ is now used in unit.md, inquiry.json and solutions.md, and `"k": "g"` in figures.json redraws the concept-map formula. $\eta_\text{tot}$ is used in solutions.md and tasks.json. Both now match fy3-11 and fy3-15. No `W_\text{k}` or `eta_\text{kok}` is left.
- Polish 2 (exit-ticket 1.a): fixed. The new wording "The heat delivered indoors is the electrical energy plus the heat moved from outside" is correct.

## Checked
- `check_i18n.py`: en 0 errors, fi-easy 0 errors. No answer, unit, tolerance, correct option, formula or figure differs from the source.
- I read the round-2 diff in full: symbol renames, the s1 text ("lifted $1.20\,\text{m}$ slowly at a constant speed"), s2 c ("it does not increase the electricity obtained"), the exit-ticket sentence, and the "work done by gas" label. Every edit keeps the physics and the numbers of the source.
- The `"k": "g"` mapping in figures.json affects only a stand-alone `\text{k}`. It does not touch kPa, kJ or kW.
- All numbers from round 1 (tyre, mol amounts, hatch, pump, balloon, ΔU = 750 J, s1–s6) are unchanged.
