VERDICT: PASS
CONTENT-HASH: 71985e313cf3f576
Review of the recognition chart (queue 9c) and the term change against the version passed at c0e5f30c40e0a14a; full on the chart, delta on the rest.

## Blocking
(none)

## Polish
- The chart writes $Q_\text{released} = Q_\text{absorbed}$; the Formula section and inquiry.json say $Q_\text{received}$. Same quantity; one subscript would be cleaner.

## Checked
- Every row: $Q = cm\Delta T$ without a change of state; $Q = sm$ melting/freezing; $Q = rm$ boiling/condensing; insulated mixing $Q_\text{released} = Q_\text{absorbed}$; $l = l_0(1+\alpha\Delta T)$; $V = V_0(1+\gamma\Delta T)$; $P = UA\Delta T$. All agree with the Formula section.
- The aria-label matches the chart.
- Term change: the diff's other lines are "concept map" -> "recognition chart" in teacher.md and new figures.json keys; no formula, number or task changed. The key "vastaanotettu" (now "absorbed") is used only by the chart.
- The en chart (docs/figures/fy9-tunnistus/fy9-lampo-en-360.png) and the hash, taken at the start and the end (71985e313cf3f576).
