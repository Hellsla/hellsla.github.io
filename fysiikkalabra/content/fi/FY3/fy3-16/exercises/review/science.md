VERDICT: PASS
CONTENT-HASH: 5f49adfd0e5ee772

## Blocking

## Polish
- exercises.json fy3-16-L2-01, fy3-16-L3-03 — with tolerance 0.07 the check accepts 1.58–1.82 kg (key 1.7) and 1.49–1.71 kg (key 1.6), so the value one step above the key (1.8 kg; 1.7 kg) also passes — follows from the teacher's both-directions decision; no change needed.

## Checked
- Round 4, full: all 21 numeric answers recomputed in one script from the task texts with my own formulas; all agree with exercises.json and answers.py.
- Limit-value tasks L2-01 and L3-03: key and model answer round up (1.617→1.7; 1.511→1.6), answers.py uses ceil; tolerance 0.07 accepts the rounded-down 1.6 (5.9 %) and 1.5 (6.3 %) as the teacher decided; the unrounded values pass too.
- Every other tolerance lets a student who rounds to the data's figures pass (680 vs 678, 2.4 vs 2.444, 140 vs 139, 480 vs 480.6, 590 vs 592).
- Laws and conditions: Q = cmΔT only without a change of state (said in each Periaate), sm and rm at constant temperature, P = UAΔT with the inside at 0 °C stated in the task, mixing task checks 251 400 J > 167 000 J first and states the "not enough" case correctly.
- Multiple choice L1-06, L1-07, L2-08: exactly one correct option; each distractor is wrong and its feedback gives the right physics (net transfer wording, no "cold flows", t ∝ m/(UΔT) ratio = 2).
- Intermediate numbers of the solutions recomputed (period efficiencies, break-even price 0.44 €/kg, stage energies, fitted line, axis crossing ≈ +20 °C): all right.
- Figures fy3-6/heating-line and fy3-7/melting-curve give the needed readings (180 s, 40 K; 220 kJ), agree with c_ice·m·ΔT + sm = 20.2 + 200 kJ, and do not show the answer.
- Scope: FY3 central contents only (heat, changes of state, U-value from the lesson); symbols as in the brief (s, r, c, m/t, UA).
- Guardrails: melting explained by interaction energy, heater efficiency "käytännössä 100 %", example data called esimerkkiaineisto, slope read from the fitted line.
