VERDICT: PASS
CONTENT-HASH: 5c5e2726a63ff9d8
SCOPE: delta md-paragraphs,numbers,reflow,typography from ffd2c67e70d46b4c base cabadc3

## Blocking
None.

## Polish
- solutions.md:188 (fy4-9-L3-04 Kaava) — "$I = \Delta t \cdot \Sigma F$": here $\Sigma F$ is the sum of the table's force values, while the course's $\Sigma F$ is the net force (the same collision as in fy4-3-L3-05); fix: "$I = \Delta t \cdot (F_1 + F_2 + \dots + F_9)$" or "$\Delta t \cdot \Sigma F_\text{taulukko}$".
- solutions.md:190 (Muunnokset) — the new $\Delta t_\text{e} = 25\,\text{ms}$ and the airbag's $100\,\text{ms}$ are not converted in the Muunnokset row, only inside Sijoitus; fix: add "$25\,\text{ms} = 0{,}025\,\text{s}$ ja $100\,\text{ms} = 0{,}100\,\text{s}$".
- Previous polish (L2-08 opening, double "joten") not part of this diff and stands as before.

## Checked
- Round 1 blocking fix verified: the stopping time of the rigid obstacle is now $\Delta t_\text{e} = 25\,\text{ms}$, distinct from the sampling step $\Delta t = 10\,\text{ms}$; the Kaava, Sijoitus and Järkevyys rows use it consistently, and the task text (c) gives $25\,\text{ms}$.
- Arithmetic unchanged and correct: $981 / 0{,}025 = 39\,240\,\text{N}$; answer $39\,\text{kN}$ with two significant figures follows the data.
- Kaava still reads principle to symbols: $I = \Delta t \cdot \Sigma F$, $-I = \Delta p = 0 - mv_0$, $I = F_\text{ka}\,\Delta t_\text{e}$, then $F_\text{ka} = I/\Delta t_\text{e}$ before substitution.
- Järkevyys comparison (39 kN against 17,4 kN, and airbag 100 ms) still holds; Finnish ("pysähtymisaika", case after unit "$25\,\text{ms}$:sta") correct.
- No answer, tolerance, task, id or figure changed; layout checks ran ok at 360-1280 px; text-only change.
- Captures opened: none.
