VERDICT: FAIL
CONTENT-HASH: 020a2d39a5af90ba

## Blocking
- [Major] solutions.md, Substitution lines of 5-19 (wood and oil) and of the moist-wood task (m_40 and m_20) — the new chain reads "$\Delta m = E\left(\tfrac{1}{H_\text{wood}} - \tfrac{1}{H_\text{oil}}\right) = 8.0\,\text{kg} - 2.96\,\text{kg} = 5.04\,\text{kg}$" and only afterwards, under "where", defines $8.0\,\text{kg}$ and $2.96\,\text{kg}$ (capture open-exercises-L3-1280-1) — the symbolic form is never substituted into, the second row has numbers that appear from nowhere, so the equals chain is not followable and breaks the house order (symbolic → substitution → result) — fix: substitute into the last symbolic form first, $\Delta m = 120\,\text{MJ} \cdot \left(\dfrac{1}{15\,\text{MJ/kg}} - \dfrac{1}{40.6\,\text{MJ/kg}}\right) = 8.0\,\text{kg} - 2.96\,\text{kg} = 5.04\,\text{kg}$, and give the two masses after it as a check; the same for $m_{40}$, $m_{20}$.

## Polish
- [Minor] solutions.md: "(intermediate value $E_\text{in} = …$)" stands as a detached paragraph under the Substitution box (L3-1280-4, L2-1280-2); a "where" sentence would attach it to its chain.
- [Minor] task 5-11 and 5-19 (untouched): the expand button covers the end of the first task line at 1280 px (shared component).

## Checked
- Delta: solutions.md Formula/Substitution lines read in source (all hunks); exercises.json caption marker removal.
- Captures opened: open-exercises-L2-1280-2 (5-10 chain, 5-11), L3-1280-1 (5-19 Formula and Substitution: defect above), L3-1280-4 (5-20 peat power chain, 5-22 task), L3-1280-6 (5-22 pellets/oil rows with fractions: aligned, readable, nothing clipped).
- Rows with nested $\tfrac{\text{MJ}}{\text{kg}}$ in fractions legible; answer boxes and reasonableness blocks intact.

## Scores
illustrations 5 · typography 3 · Finnish 4 · accessibility 5
