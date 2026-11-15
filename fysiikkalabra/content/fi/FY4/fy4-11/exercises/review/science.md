VERDICT: PASS
CONTENT-HASH: 92b3863b2eaf9805

## Blocking

## Polish
- content/fi/FY4/fy4-11/exercises/solutions.md:309 (fy4-11-L2-10, Kaava) — the final form "Törmäysnopeus on $v = \sqrt{v_0^2 - 2a\,(d - v_0\,t_\text{r})}$" comes after the part d friction sentence; move it right after $v^2 = v_0^2 - 2as$ so the derivation reads in order.
- solutions.md:345 (L2-10, Vastaus) — the reason for two significant figures is right; it could also say that a student who reads other values from the calculator on a later date gets another number (the Annettu line says it, the Vastaus does not).
- exercises.json (L2-10) — the answer box accepts only $69{,}4\,\text{km/h} \pm 3\,\%$; if Liikenneturva changes the calculator's reaction time or deceleration, the box and answers.py need the new values (the solution's dated note covers the student, not the check).

## Checked
- All 23 numeric answers recomputed with my own formulas (fits of L2-05, L2-06 and L3-04 included): agree with exercises.json and answers.py inside each tolerance.
- L2-10 source values (reaction time $1\,\text{s}$; $9\,\text{m/s}^2$ dry, $1{,}5\,\text{m/s}^2$ icy; rounding to a metre; dry 11/7/18, 17/15/32, 22/27/50, 28/43/71; icy 165 and 187 at $80\,\text{km/h}$): the same as the coordinator's record of the calculator; the model reproduces every rounded value.
- L2-10 is solvable with the source and the chapter's model; the task gives no source value, the solution states them with the date (16.11.2026) and tells the student to use the values they read if these have changed.
- L2-10 b: $6{,}86$, $15{,}43$, $27{,}43$, $42{,}87\,\text{m}$; four-fold from 40 to $80\,\text{km/h}$; derived from $t_\text{j} = v_0/a$ and the triangle area, as the brief does.
- L2-10 c: $49{,}66\,\text{m} < 50\,\text{m}$ (margin $0{,}34\,\text{m}$, said to be inside the model's uncertainty: safe-side conclusion); $100\,\text{km/h}$: $v = \sqrt{771{,}6 - 400{,}0}\,\text{m/s} = 19{,}28\,\text{m/s} = 69{,}4\,\text{km/h}$; with the rounded $28\,\text{m}$ $69{,}8\,\text{km/h}$, inside the tolerance.
- L2-10 d: $186{,}8\,\text{m}$ against $49{,}7\,\text{m}$; six-fold braking distance; $\mu mg = ma$, $\mu = 0{,}92$ and $0{,}15$; forces named correctly.
- L2-10 e: ABS cannot raise the friction coefficient; $1{,}25^2 = 1{,}56$, calculator 27 to $43\,\text{m}$.
- L3-05 fix: $80{,}0\,\text{kg} \cdot 4{,}5\,\text{m/s} : 0{,}020\,\text{s} = 18\,\text{kN}$, two figures from $4{,}5\,\text{m/s}$; a) $0{,}79\,\text{m}$, b) $10\,\text{kN}$.
- L2-05 fix ("kahden tai kolmen numeron": data $6{,}5$ to $39{,}6\,\text{m}$) and L3-06 fix ($10{,}5\,\text{kN}$ shown as $11\,\text{kN}$; tolerance 0.05 accepts 11).
- Hash the same at the start and the end.
