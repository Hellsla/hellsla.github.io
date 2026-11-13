VERDICT: PASS
CONTENT-HASH: 952835976a9af62b
SCOPE: delta added-exercise from 5e665cb7dcc6d97e base 89bcb63b7431

## Blocking
(none)

## Polish
- solutions.md (L1-09) Annettu — $T_\text{sisä} = 20\,{}^\circ\text{C}$ uses $T$ for a celsius value, while the brief keeps $T$ for kelvins and $\theta$ for celsius; $\theta_\text{sisä}$, $\theta_\text{ulko}$ would match.
- L1-09 — $U = \lambda/d$ leaves out the surface resistances of a real wall (a real one-log wall is nearer $0{,}6\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$). Since the task gives the formula this is a fair simplification (C); a half-sentence "kun pintojen vaikutus jätetään huomiotta" would state it.

## Checked
- Only L1-09 and L2-09 judged (delta added-exercise); the rest unchanged per packet.
- L1-09 recomputed: $U = 0{,}14/0{,}20 = 0{,}70\,\tfrac{\text{W}}{\text{m}^2\cdot\text{K}}$, $P = UA\Delta T = 0{,}70 \cdot 10 \cdot 30 = 210$ W; answers.py agrees. λ(mänty) = 0,14 matches docs/mafy-arvot.tsv (VERIFIED).
- L1-09: $U = \lambda/d$ is given in the task (not a chapter formula), so nothing untaught is needed; steady temperatures implied by the given constant inside/outside values, matching the brief's condition for $P = UA\Delta T$; $\Delta T$ in celsius = kelvins stated; two figures from λ; check against 0,17 (factor ≈ 4) is right.
- L2-09 recomputed: $102/341 = 0{,}2991$ → 29,9 %; answers.py agrees; value matches the accepted global mean albedo ≈ 0,30.
- figures.py earth-flows: the two given arrows' shafts 34 and 10 units at 1 per 10 W/m² (to scale as the description says); the outgoing arrow dashed and labelled "?", not to scale, as stated; the description gives 341 and 102; the answer is not shown.
- L2-09 physics: reflection at the top of the atmosphere includes clouds and air, so "heijastuu takaisin avaruuteen" is right; balance statement in the description is consistent (239 W/m² out).
- Both solutions complete (given/asked, principle with reason, symbolic first, conversions, substitution with units, rounding reason, real check); within FY3 (lämmön siirtyminen, energiatasapaino ja ilmastonmuutos).
- Units W and %, relative tolerances 0,04 and 0,02 fit the data.
- Hash identical at start and end.
