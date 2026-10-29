VERDICT: PASS
CONTENT-HASH: 7e3a56e6bf3861b1

## Blocking
(none)

## Polish
- lesson.md Ydinajatus / inquiry check-c2 — the correct option's feedback cites 230 g/kWh right after "polton hiilidioksidi on ilmassa vuosikymmeniä"; the 230 excludes that CO2 (the table note says so). Add "ilman polton hiilidioksidia" to the feedback.
- lesson.md table note — gas 490 is the combined-cycle median; say so (a condition, minor).
- inquiry.json koe-1 values — "420: nykyinen määrä" and the CO2 424 ppm in the text differ; the sim's model box explains the rounding, so add "pyöristetty" to the value label too.
- lesson.md "CO2-ekv." — GWP time horizon (100 a) unstated; fine at this level.
- Figure: nuclear/wind bars drawn at 5.5 px (12.5 g/kWh) vs 5.28; "noin 70-kertainen" holds.

## Checked
- CO2 424 ppm: WMO Greenhouse Gas Bulletin No. 21 (2025), 2024 global mean 423.9 ppm; 280 ppm preindustrial fine; "alle puoli promillea" true (0,42 ‰).
- Table equals IPCC AR5 WG3 Annex III medians (820, 490, 230, 41/48, 24, 12, 11/12); ranges explained correctly.
- Sim: 420 ppm rounded level stated; settled values -18/14/16/17 °C consistent with 14+3·log2(1,5)=15,75 and AR6 ECS 3 (2,5-4); start +15; labelled illustration, not a calculation.
- Experiment koe-1 isolates co2; Teq keys exist in simState; 0 ppm caveat (no water vapour) stated.
- All predictions, feedbacks, numerics (820 kg, 49 000 t, 15,9 kg, 43 kg, 2,352 t, 58 kg, ratios 41 and 68) recomputed OK.
- Biomass, transport (8x distance), checks and exit ticket consistent with theory.
