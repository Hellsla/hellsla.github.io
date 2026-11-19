VERDICT: FAIL
CONTENT-HASH: b1a35fc043573446

## Blocking
- inquiry.json experiment 1 `question` (answer 9.81 kPa) + simulation readout (390 px capture) — the readout prints "slope $\rho g$ = 9.81 kPa/m" and "The total pressure is 1.97 times atmospheric pressure" as soon as the sim opens, so the numeric question "read it from your measurements" is answered without any measurement and prediction 1 is shown ready-made; the slope-from-data skill (the slot's line with a constant term) is not practised — fix: remove the slope and ratio lines from the readout (keep them in "How the calculation works") or reveal them only after the experiment's rows are recorded.

## Polish
- inquiry.json (predictions 1, 3, experiment 1, conclusion, reflect) — "your measurements" for simulation values; use "the model's values".
- inquiry.json (prediction 3, three feedbacks) — "the theory summary"; the stage is called Theory.
- lesson.md (Worked example, Reasonableness stage) — closing paragraph about the diver's body not being crushed is off the check; cut or move.
- lesson.md ("Where does pressure come from?") — the derivation paragraph is long; split before "Pressure is not a force".

## Checked
- Faithful to the Finnish structure; path from weight (FY3-1) and particle model (FY3-3) to p = F/A and p = p₀ + ρgh.
- Dam question answered via gauge pressure after the student has committed.
- Predictions built on real misconceptions (proportional total, density, vessel width); experiments lock the right variable.
- Worked example has seven stages, cm² conversion explicit.
- Checks test gauge orientation, vessel shape, slope from graph and an explanation with criteria.
- Phone: sim legible at 390 px.
