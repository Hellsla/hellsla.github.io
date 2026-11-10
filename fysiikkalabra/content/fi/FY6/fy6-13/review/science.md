VERDICT: PASS
CONTENT-HASH: 5d937e42ff5cf67a

## Blocking

## Polish
- content/fi/FY6/fy6-13/inquiry.json:113 (simulaatio `model`) — the Mallin oletukset box says how a disconnected capacitor behaves at breakdown but not that, connected, the sim keeps showing the ideal $Q = CU_0$ and $W$; the new readout note (lang/fi.json:1949 `sims.fy6-13.mallirajaus`) says it only on screen — optionally add the same sentence to the box so theory and sim boxes say the same.
- lang/fi.json:1949 — the note could name what stays ideal: "the shown $Q$ and $W$ are the ideal model's values" (C-level, not a finding).

## Checked
- Diff: `mallirajaus` appended after the bold breakdown text only when `S.lap && !S.burnt` (connected); its claim is right (breakdown violates the ideal-dielectric assumption; a source-sustained arc current is not modelled) and it removes the risk of reading the displayed $Q$, $W$ as physical during breakdown.
- Browser (preview, fi): d = 1,0 mm air, U0 = 3,0 kV → E = 3,00 MV/m, no breakdown; 3,1 kV → lapilyonti 1, Q 549 nC, note shown; then irrotettu → Q = 0, purkautui text, no note.
- Recomputed in one script with own formulas: sim load 88,5 pF / 88,5 nC / 44,3 µJ; koe 1–4 Q, W, U, E (lasi 0,179 kV, 7,9 µJ; kytketty lasi 496 nC, 248 µJ); koe 5 U_max 3,0 kV; paper 160 V; example 6,75 J, 6,75 kW, 3,4 s; kertaus 150 kV/m; virhe 0,034 J; siirto 190,35 µJ; TV 12 J; exit 1,2 mC — all match lesson-answers.py and the texts.
- Predictions 1–2, kertaus, virhe, tarkistus 1–2: exactly one correct option each; distractor feedback right.
- Experiments: each isolates its varied parameter (locked lists correct); simState gives every measured key.
- Models and conditions: plate formula (small gap, filled gap), U_max = E_max d, half-energy loss stated as a result of this charging model, kytketty/irrotettu table and its mechanism.
- Scope: charging/discharging qualitative only, no capacitor connections.
- Numbers, setups and correct options identical in the en and fi-easy versions.
- Hash identical at start and end.
