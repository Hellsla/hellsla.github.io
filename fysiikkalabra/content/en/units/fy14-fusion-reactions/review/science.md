VERDICT: PASS
CONTENT-HASH: f9123ac373589430

Science re-review of fy14-fusion-reactions, 2026-11-01, after commit 7843fefa (unit) and 371c50b6 (reaction.js, nuclides.json).

## Previous findings
The blocking finding is fixed. The text now says "The arrows compare speeds within one step only; the line under the figure gives the real speeds". In the browser, reaction.js shows these speeds:
- a 10 keV deuteron at .79 \cdot 10^5$ m/s and the triton at .54 \cdot 10^5$ m/s (equal momenta);
- the neutron at .13 \cdot 10^7$ m/s and the alpha particle at .31 \cdot 10^7$ m/s, "52 and 13 times faster".

All of these match my relativistic calculation. The teacher note's "13 and 52" agrees.

On the Coulomb barrier, the sentence I proposed is now in *Key idea* and in the component's new tunnelling step: the top of the barrier is about 0.48 MeV at 3 fm, and D–T fuses readily near 0.1 MeV. Both are correct.

All three polish items are fixed:
1. The distance is now  \cdot 10^{-15}$ m, with tunnelling, in the model answer and in reaction.js.
2. The summary now gives "a few keV in the Sun, about 10–20 keV in a reactor".
3. The *tritium* respelling stays "tree-SYOM". The visual reviewer cites Wiktionnaire for it; it is a matter of French, not physics, and I defer to them.

## Changes checked
- **Cut lab paragraph.** Nothing now refers to the removed text. The 1934 source and the summary still carry the history.
- **Table.** The headers changed ("ITER (plan)"), but the values did not: 1.6·10⁷ K and 1.5·10⁸ K, 150 g/cm³ and 10⁻⁶ of air, 280 W/m³ and 0.6 MW/m³.
- **Temperatures.** "150 million kelvin" is now used everywhere.
- **Methane in nuclides.json.** Both values now use the higher heating value: 9.23 eV and 55.5 MJ/kg, consistent with 890.7 kJ/mol over 16.04 g/mol. The unit quotes no methane number.
- **Optional energy-scales and coal tasks.** The numbers are unchanged: .04 \cdot 10^7$ kg of coal.
- **Browser.** No console or KaTeX errors.

## Blocking
None.

## Polish
1. `unit.json` source title "Heat of combustion (Wikipedia): … methane 50.0 MJ/kg" is out of date now that the data uses the higher heating value. Change it to "methane 55.5 MJ/kg (higher heating value)".

## Checked
Physics, mathematics, the worked example, every option and its feedback, the reaction and energy-scale components and their data, history and sources.

## Re-check 2026-11-01: photographs
Oliphant (1901–2000), D–D fusion at the Cavendish in 1934, and his discovery of tritium and helium-3 are correct and match the text. The image matches the alt. PD-USGov-DOE; credit matches.
