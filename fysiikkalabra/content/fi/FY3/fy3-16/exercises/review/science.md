VERDICT: PASS
CONTENT-HASH: 746496959811ec08

## Blocking

## Polish
- solutions.md:167 (fy3-16-L3-03), carried over: the energy conducted through the wall still sits under $Q_\text{luovutettu}$ together with the drinks' heat. As an energy balance this is right, and the Periaate already says it exactly ("seinän läpi tuleva energia sekä juomien luovuttama energia"). Writing the first row as $Q_\text{vastaanotettu} = E + Q_\text{luovutettu}$ would match the Periaate.

## Checked
- I read the changed Kaava block on disk (solutions.md:163–172). There is no array numerator any more, and the total energy is named $E_\text{yht}$.
- The chain is correct:
  - $Q_\text{vastaanotettu} = m(c_\text{jää}\Delta T_\text{jää} + s)$.
  - $P = UA\Delta T$ and $E = Pt$, so $Q_\text{luovutettu} = E + cm_\text{j}\Delta T_\text{j}$.
  - $E_\text{yht} = UA\Delta T\,t + cm_\text{j}\Delta T_\text{j}$ is the same quantity with $E$ substituted.
  - The balance then gives $m = E_\text{yht}/(c_\text{jää}\Delta T_\text{jää} + s)$, the last symbolic form, which the Sijoitus evaluates.
- I recomputed with my own formulas: $(486\,000 + 50\,280)/355\,000 = 1{,}511\,\text{kg}$. The Vastaus $1{,}6\,\text{kg}$ is rounded up as an "at least" value, as the guardrail and the house rule require.
- The model's conditions are stated: the inside stays at $0\,{}^\circ\text{C}$, so the wall's power is constant, and the ice warms from $-10\,{}^\circ\text{C}$ before it melts.
- No Sijoitus, answer or answers.py value changed.
- The hash was the same at the start and the end.
