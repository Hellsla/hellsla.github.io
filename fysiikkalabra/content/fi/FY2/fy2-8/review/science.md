VERDICT: FAIL
CONTENT-HASH: 4d3ca50f138fdce2

Full review (scope: the version passed is not in history). Changes of this round: $-18\,{}^\circ\text{C}$ is now the effective radiating temperature of a simple radiative-balance model, not a precise prediction of the surface temperature without greenhouse gases (Ydinajatus, misconception, Tiivistelmä, sim model box, koe-1 feedback, tarkistus-3 model).

## Blocking

1. inquiry.json:63 (ennuste-1, correct option's feedback) — **B.** "Ilman luonnollista kasvihuoneilmiötä keskilämpötila olisi noin $-18\,{}^\circ\text{C}$ todellisen $+15\,{}^\circ\text{C}$:n sijaan" is exactly the reading the theory now rules out ("Lukua $-18\,{}^\circ\text{C}$ ei kuitenkaan pidä lukea täsmälliseksi ennusteeksi pintalämpötilasta, jos kasvihuonekaasut poistettaisiin"). Fix: "Maan yksinkertainen säteilytasapainomalli antaa efektiiviseksi säteilylämpötilaksi noin $-18\,{}^\circ\text{C}$, kun maanpinnan keskilämpötila on noin $+15\,{}^\circ\text{C}$; ero, noin $33\,\text{K}$, havainnollistaa kasvihuoneilmiön merkitystä."

## Polish

1. inquiry.json ennuste-1 last distractor ("yhdessä ne nostavat lämpötilaa … noin $33\,\text{K}$") and tarkistus-1 third distractor ("se nostaa lämpötilaa noin $33\,\text{K}$"): word as "ero, noin $33\,\text{K}$, havainnollistaa …" for one wording everywhere.
2. lesson.md Ydinajatus — "ilman sitä merien vesi olisi jäässä" now follows the caveat that the no-greenhouse case is not precisely predictable; "olisi todennäköisesti jäässä" keeps it consistent. (C otherwise.)

## Checked

- New wording ($T_\text{eff} \approx 255\,\text{K}$ from a simple radiative balance; clouds/ice would change) is physically right and consistent in lesson.md, the sim model box, koe-1 feedback and tarkistus-3 model.
- Mechanism: shortwave largely transmitted, thermal IR absorbed and re-emitted, N₂/O₂ nearly transparent; CO₂ $280 \to 424\,\text{ppm}$ (WMO 2025), "alle puoli promillea" — right.
- Combustion C + O₂ → CO₂, hydrogen → water; biomass carbon timing and IPCC's zero-combustion convention explained — right.
- AR5 WG III Annex III medians (820, 490, 230, 41–48, 24, 12, 11–12 g/kWh) correct; $820:12 \approx 68$.
- Recomputed: example $2{,}352\,\text{t}$ (wind $58\,\text{kg}$, ×41); virhe $43\,\text{kg}$; siirto $49\,000\,\text{t}$ (mistakes $0{,}049$, $4{,}9\cdot10^{10}$); tarkistus-2 $15{,}9\,\text{kg}$ (mistakes $13{,}2$, $15\,900$); perustele $1200$ vs $49\,000\,\text{t}$; exit $120\,\text{g}$, ×70. All agree with lesson-answers.py.
- Each choice has exactly one correct option; check-c3 (per-kWh comparison) and check-c2 (biomass) feedback right.
- Photo captions (GISTEMP 2025 vs 1951–1980 anomaly; ISS night image) — right.

## Shared issues

- exercises/solutions.md:125 (outside this review) still says the effect "nostaa maapallon keskilämpötilan arvosta noin $-18\,{}^\circ\text{C}$ arvoon noin $+15\,{}^\circ\text{C}$"; the exercise set should get the same wording.
