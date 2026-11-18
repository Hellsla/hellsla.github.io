VERDICT: PASS
CONTENT-HASH: 5c5e2726a63ff9d8
## Blocking

## Polish
- solutions.md:176, 187 (L2-07, L3-04 Kaava, pre-existing) — $\Sigma F$ there means the sum of the tabulated force readings, while the chapter and L3-05 use $\Sigma F$ for the total force. Fix: write the sum in words or as $\Sigma F_i$ ("sisäpisteiden voimien summa") (carried over).
- solutions.md Kaava rows of L1 (bat, puck, belt), L2 kick — "…, joten …, joten …" twice in one sentence. Fix: second "joten" → "ja siitä" or a full stop (carried over).

## Checked
- Round-1 Blocking fixed: L3-04 Kaava now gives the rigid-obstacle stopping time its own symbol, "pysähtymisaika on $\Delta t_\text{e} = 25\,\text{ms}$ ja $I = F_\text{ka}\,\Delta t_\text{e}$, joten $F_\text{ka} = \dfrac{I}{\Delta t_\text{e}}$"; $\Delta t = 10\,\text{ms}$ stays the strip width in $I = \Delta t \cdot \Sigma F$ and Muunnokset, so the two times no longer collide.
- Sijoitus c) names $\Delta t_\text{e} = 0{,}025\,\text{s}$ and substitutes it: $981\,\text{N·s} : 0{,}025\,\text{s} = 39\,240\,\text{N}$ → $39\,\text{kN}$; $25\,\text{ms}$ is in task part c); a) $981\,\text{N·s}$, b) $14{,}01\,\text{m/s} = 50{,}45\,\text{km/h}$ unchanged.
- Järkevyys still compares $9{,}81\,\text{kN}$ (airbag mean over $100\,\text{ms}$) with $17{,}4\,\text{kN}$ peak and $39\,\text{kN}$; consistent with the new symbol.
- No other change since round 1 (git diff d97ccea596..HEAD on the set: L3-04 Kaava and Sijoitus only); no answer, tolerance, task or id changed.
- Captures: none opened (the fix is a symbol in text; judged from the source).
- Hash 5c5e2726a63ff9d8 at start and end.
