VERDICT: FAIL
CONTENT-HASH: 191d9a7966bb3115

## Blocking
- content/en/FY2/fy2-1/exercises/solutions.md:67–90 (fy2-1-L1-10), exercises.json:166 (`answer`), lessons/FY2/fy2-1/answers.py:179. **A (quantitative, data)**: the task sends the student to the MAFY table, but the solution and answers.py quote $H = 43\,\text{MJ/kg}$ for petrol "from the MAFY table". The current table (mafytaulukot.fi, *Polttoaineiden LHV-lämpöarvoja*, row *bensiini*) gives $43{,}4\,\text{MJ/kg}$. A student who reads the table correctly gets $E = 43{,}4 \cdot 2{,}0 = 86{,}8 \approx 87\,\text{MJ}$, and the model solution then shows a different table value and a different answer ($86\,\text{MJ}$). The check still accepts 87 (1 % off, inside 0.04), but the solution misquotes its named source. Fix: $H = 43.4\,\text{MJ/kg}$ in Given and Substitution, `a["fy2-1-L1-10"] = 43.4 * 2.0`, `answer` 86.8, Answer "$E \approx 87\,\text{MJ}$ (two significant figures, from $m = 2.0\,\text{kg}$)", and about $24\,\text{kWh}$ in the check (still right). Keep tolerance 0.04, because other tables give 42–44 MJ/kg.

## Polish
- solutions.md (L1-10), Reasonableness: the table's wood value is $16{,}2\,\text{MJ/kg}$ (dry wood). "About $16\,\text{MJ/kg}$ for dry wood" names the row the student would look up.
- exercises.json (L1-10): "changes into kinetic and thermal energy". In an engine most of the chemical energy ends up as thermal energy and only part becomes kinetic energy. "mostly thermal energy, part of it kinetic energy" would be more exact. This is level C, not a finding.

## Checked
- Hash 191d9a7966bb3115 (`--exercises --lang en`) at the start and the end.
- The L1-10 scope finding from round 1 is fixed. $E = Hm$ is in FY2's scope notes, and the task gives the formula and defines $H$. A level-1 task with one formula is FY2-level content.
- I fetched the MAFY table *Polttoaineiden lämpöarvoja* from mafytaulukot.fi: bensiini 43,4, petroli 43, kuiva puu 16,2 MJ/kg (LHV).
- Recomputed L1-10: $2.0 \cdot 43 = 86$ (answers.py 86.0) and $2.0 \cdot 43.4 = 86.8$. The heating values 42–44 MJ/kg all fall inside ±2.3 % of 86, so the unit (MJ) and tolerance are sound.
- L1-10 physics: the heating value is the energy released per kilogram burned, as the guardrail says. Energy conservation is stated without saying energy is created.
- Recomputed L2-08 from the figure data (A 700/0 J, B 300/300 J): 100 J thermal, $p = 14.29\,\%$, matching answers.py. The rounded 14 % is 2 % off, inside 0.03.
- The L2-08 Polish item from round 1 is fixed. Reasonableness now checks $0 < p < 100\,\%$ and $600 + 100 = 700\,\text{J}$, with no claim that B is halfway.
- L2-08 isolated system (skater, half-pipe, surroundings): friction turns mechanical energy into thermal energy, as the guardrail requires. Consistent with L1-03 (200 J by C).
- Both solutions have all seven stages and solve symbolically before substituting.
