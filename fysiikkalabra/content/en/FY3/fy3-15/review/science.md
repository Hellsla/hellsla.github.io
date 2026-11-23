VERDICT: PASS
CONTENT-HASH: d89bf7dd1d8a286a

## Blocking

## Polish
- inquiry.json:tyypit (correct option) and check-c2 (correct option) — "the turbine takes/converts the kinetic energy of the water directly": a Francis or Kaplan turbine mainly uses the pressure from the height drop, not only kinetic energy (C at FY3 level, where E_p is FY4) — consider "the energy of the flowing water" to match the lesson's own wording "power of flowing water".
- inquiry.json:pred-2 Bea feedback — "District heating is taken from the waste heat of the condenser, not from electricity" reads as absolute, but the same feedback (and Cem's) shows electricity does drop by 40 MW — consider "mostly from the waste heat".
- lesson.md:246–250 — $P_\text{L} = c\,q_m\,\Delta T$ assumes steady flow and cooling water that stays liquid; both are obvious here, so this is only a possible half-sentence ("steady flow").

## Checked
- Recomputed in one script: Sankey 500 → 460 → 211.6 → 199.96 MW, losses 40 / 248.4 / 11.6 MW, product 0.39992; the bar chart heights (0.5 px/MW) and the stacked-area graph (0.6 px/MW, x 1.84 px/MW: 160 → 120 MW, 232 MW of district heating, 352 MW, waste heat 48 MW) are to scale as the captions say. In the Sankey picture the band and arrow widths match 40 px/100 MW within what the eye can judge.
- Worked example: 0.38038, 228.228 MW, 371.772 MW, boiler loss 54 MW, condenser 305.76 MW (> half), generator 12.0 MW; derived symbolically first; 3 s.f. justified.
- Numeric tasks: ketju 248 (mistakes 270, 211.6, 288.4, 300 each correctly diagnosed), kaukolampo 48, kaukolampo-tarve 130 (η_tot 0.76), siirto 8.64 (155.52/164.16 MW; 2 s.f. reasoning sound, within tolerance), check-2 216 (η_tot 0.900), kertaus 520 MJ and η 0.35, virhe 0.342/342 MW and 540 MW, pysahdy 0.342, exit ticket 0.432, Cem 40/232 ≈ 0.17.
- Exactly one correct option in kertaus, pred-1, pred-2, tyypit, virhe, check-1, check-c2; every distractor wrong and its feedback right.
- Heat-engine loss stated as unavoidable only "completely", tied to release to a colder reservoir; electrical, total and recovered heat kept apart (guardrail CHP).
- Energy wording: "transferred to the surroundings as heat", never "into heat"; waste heat is not lost energy (misconception section).
- Efficiency denominators for hydro, wind and solar correctly said to be non-comparable with fuel; typical values (38–42 %, ~35 % nuclear, 0.25–0.35 CHP electric, 85–90 % total, ~90 % hydro, 40–45 % wind, ~20 % PV) plausible and consistent with the example plants (CHP 120/400 = 0.30 matches check-3).
- Condenser heat vs. total waste heat distinguished correctly; Q = cmΔT used for liquid water only.
- Scope: efficiency, energy conservation, heat quantity: within FY3 central contents; no FY4 quantities used.
- Hash identical at start and end.
