VERDICT: FAIL
CONTENT-HASH: 66175cc0749d903c

## Blocking
- lang/fi-easy.json:2014 (`sims.fy6-13.lukemat_lap`, used by assets/sims/fy6/fy6-13/sim.js:81) — **A**: during connected breakdown the readout labels Q and W "Ideaalimallilla lasketut arvot ennen läpilyöntiä", but sim.js computes them as Q = C·U0 and W = ½·Q·U0 at the set source voltage, which is above the breakdown voltage; the capacitor never held them before breakdown. Browser check (fi-easy preview, air, d = 1,0 mm, A = 200 cm²): at U0 = 4,0 kV the label shows W = 1417 µJ "ennen läpilyöntiä", while the most the gap could hold before breakdown is ½C(E_max d)² = 797 µJ (at 3,0 kV). — Either rename them to what they are ("Ideaalimallin arvot, jos läpilyöntiä ei tapahtuisi: …") or show the values at the breakdown limit, Q = C·E_max·d and W = ½C(E_max·d)², under the present label. (fi and en `lukemat_lap` carry the same wording.)

## Polish
- The Mallin oletukset box (inquiry.json, simulation `model`) still does not say that, connected, the readout keeps ideal-model Q and W at breakdown; one sentence there would make the box and the readout say the same.

## Checked
- Diff: sim.js:81 picks `lukemat_lap` only when `S.lap && !S.burnt`; the disconnected case (Q = 0, purkautui text) unchanged; simState keys and values unchanged, so experiments and their measured keys are as in the previous PASS.
- Browser: 3,0 kV → no breakdown, normal readout (C 177 pF, Q 531 nC, W 797 µJ); 3,1 kV and 4,0 kV → breakdown readout, mallirajaus note shown.
- Recomputed: C = ε0·A/d = 177 pF; ½CU² at 3,0 and 4,0 kV = 797 and 1417 µJ; matches the sim.
- No calculation, inquiry item or lesson text changed; the rest relies on the previous PASS.
- Hash identical at start and end.
