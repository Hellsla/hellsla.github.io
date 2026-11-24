VERDICT: PASS
CONTENT-HASH: 9d097573ebce40fc
SCOPE: delta numbers,reflow from 619f4ca1980ab94e base c48271b

## Blocking

## Polish
- solutions.md:189 (L3-04, Kaava): the row $R = 0{,}040\,\tfrac{\Omega}{\text{km}} \cdot s$ is still missing, though Sijoitus a) uses it. Put it back as the first row of the chain.
- solutions.md (L3-04, Sijoitus): the chain now ends at $R P^2 t\,(1/U_\text{A}^2 - 1/U_\text{B}^2)\cdot\text{hinta}$, but Sijoitus still goes through $I$, $P_\text{h}$ and $E$ step by step. That is fine because parts a) and b) ask for those values. A one-line substitution into the final form would show that it gives the same $1{,}515\cdot 10^{6}\,\text{€}$.

## Checked
- Delta: only the Kaava lines of L3-04 and L2-09 changed. No number, answer, Muunnokset or Sijoitus changed. The hash was the same at the start and the end.
- L3-04: $E = P_\text{h} t = R P^2 t / U^2$ is correct at constant $P$ and $R$ (two-wire model, as Periaate says).
- L3-04: säästö $= (E_\text{A} - E_\text{B})\cdot\text{hinta} = R P^2 t\,(1/U_\text{A}^2 - 1/U_\text{B}^2)\cdot\text{hinta}$ is correct, with the same $R$, $P$ and $t$ for both options.
- L3-04, recomputed from the final form: $6{,}0\,\Omega$, $200\,\text{MW}$, $8760\,\text{h}$, $220/400\,\text{kV}$, $50\,\text{€/MWh}$ give $1{,}5149\cdot 10^{6}\,\text{€}$. The step-by-step route and answers.py give the same ($1{,}514901$).
- L2-09: $R = P_\text{h}/I^2 = 0{,}030\,P/(P/U)^2 = 0{,}030\,U^2/P$ is correct algebra. This closes my earlier polish item.
- L2-09, recomputed: $0{,}030\cdot(200\cdot10^{3}\,\text{V})^2 / (200\cdot10^{6}\,\text{W}) = 6{,}0\,\Omega$. This matches Sijoitus and answers.py.
- Both new final forms are dimensionally right ($\Omega\cdot\text{W}^2\cdot\text{h}/\text{V}^2 = \text{Wh}$; $\text{V}^2/\text{W} = \Omega$).
