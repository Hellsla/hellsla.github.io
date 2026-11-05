VERDICT: PASS
CONTENT-HASH: 4b1233005b94d34d

Follow-up review of the fix commit 2c31ff041 (delta from 4d3ca50f138fdce2, whose full review is kept below). Changes: ennuste-1's correct-option feedback and tarkistus-3 criterion 2 now give $-18\,{}^\circ\text{C}$ as the effective radiating temperature of a simple radiative-balance model beside the surface mean $+15\,{}^\circ\text{C}$.

## Blocking

None.

## Polish

1. inquiry.json:71 (ennuste-1 last distractor, "yhdessä ne nostavat lämpötilaa … noin $33\,\text{K}$") and :410 (tarkistus-1, "se nostaa lämpötilaa noin $33\,\text{K}$"): "ero, noin $33\,\text{K}$, havainnollistaa …" would give one wording everywhere (C).
2. lesson.md Ydinajatus — "ilman sitä merien vesi olisi jäässä" after the caveat; "olisi todennäköisesti jäässä" keeps it consistent (C).

## Checked

- Earlier blocking item resolved: inquiry.json:63 now reads as proposed; physically right ($T_\text{eff} \approx 255\,\text{K}$, $288 - 255 = 33\,\text{K}$, not a prediction of the no-greenhouse surface).
- tarkistus-3 criterion 2 now asks only what the model answer (:501) states ("säteilytasapainomallin antamassa noin $-18\,{}^\circ\text{C}$:ssa").
- Consistency: grep of "-18" in lesson.md and inquiry.json — Ydinajatus (:136), misconception (:328), Tiivistelmä (:331), sim model box (:112), koe-1 (:154), ennuste-1, tarkistus-3 — all use the model wording; no counterfactual surface-temperature claim remains in the lesson.
- Mechanism: shortwave largely transmitted, thermal IR absorbed and re-emitted, N₂/O₂ nearly transparent; CO₂ $280 \to 424\,\text{ppm}$ (WMO 2025), "alle puoli promillea" — right.
- Combustion C + O₂ → CO₂, hydrogen → water; biomass carbon timing and IPCC's zero-combustion convention — right.
- AR5 WG III Annex III medians (820, 490, 230, 41–48, 24, 12, 11–12 g/kWh) correct; $820:12 \approx 68$.
- Recomputed: example $2{,}352\,\text{t}$ (wind $58\,\text{kg}$, ×41); virhe $43\,\text{kg}$; siirto $49\,000\,\text{t}$ (mistakes $0{,}049$, $4{,}9\cdot10^{10}$); tarkistus-2 $15{,}9\,\text{kg}$ (mistakes $13{,}2$, $15\,900$); perustele $1200$ vs $49\,000\,\text{t}$; exit $120\,\text{g}$, ×70. All agree with lesson-answers.py.
- Each choice has exactly one correct option; photo captions right.
- Hash same at start and end.

## Shared issues

- Outside this hash: exercises/solutions.md:125 ("nostaa … arvosta noin $-18\,{}^\circ\text{C}$ arvoon noin $+15\,{}^\circ\text{C}$") and exercises.json:69 keep the older wording; align them when the exercise set is next edited.
