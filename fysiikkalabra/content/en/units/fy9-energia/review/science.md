VERDICT: FAIL
CONTENT-HASH: ea3f9b67dd2e79b6
Review of the recognition chart (queue 9c) and the term change against the version passed at 0f8592564d0f83bc; full on the chart, delta on the rest.

## Blocking
- **A, energia chart row 1 and aria-label: "closed system → energy is conserved, $E_\text{initial} = E_\text{final}$".** Energy can enter or leave a closed system as heat or work (glossary *eristetty systeemi*: "Suljettuun systeemiin energiaa voi vielä siirtyä"); the total energy is constant only in an isolated system. The unit's own Formula section says "In an isolated system, which no energy enters or leaves", so the chart contradicts it. Fix: "isolated system" (fi: eristetty systeemi/järjestelmä) in the chart and the aria-label.

## Polish
- (C) "a force moves a distance → $W = Fs$": the force along the displacement is assumed; fine at this level.

## Checked
- Rows 2–8: $P = \Delta E/\Delta t$; at steady power $E = Pt$; $1\,\text{kWh} = 1000\,\text{W}\cdot 3600\,\text{s} = 3.6\,\text{MJ}$ (recomputed); $\eta = W_\text{a}/W_\text{o}$ (MAFY symbols); stages in a row $\eta = \eta_1\eta_2\eta_3$; $Q = Hm$; $W = Fs$. All agree with the Formula section.
- The aria-label matches the chart row by row.
- Term change: the diff's other lines are "concept map" -> "recognition chart" in teacher.md and new figures.json keys; no formula, number or task changed.
- The en chart (docs/figures/fy9-tunnistus/fy9-energia-en-360.png) and the hash, taken at the start and the end (ea3f9b67dd2e79b6).
