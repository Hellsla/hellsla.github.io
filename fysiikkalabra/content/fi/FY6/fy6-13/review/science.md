VERDICT: PASS
CONTENT-HASH: ffc9647383412788

## Blocking

## Polish
- lang/fi.json:1946 (`sims.fy6-13.lukemat_lap`) — "arvot ennen läpilyöntiä" is slightly loose. The values shown are $Q = CU_0$ and $W = \tfrac12 CU_0^2$ at the set source voltage, which the capacitor never reaches. Example: d = 1,0 mm, air, U0 = 3,1 kV shows 549 nC and 851 µJ, but just before breakdown (U = 3,0 kV) the ideal model gives at most 531 nC and 797 µJ. "Ideaalimallin laskennalliset arvot jännitteellä $U_0$ (läpilyöntiä ei mallinneta)" would be exact. C-level, teacher's wording.

## Checked
- Diff: sim.js picks `lukemat_lap` only when `S.lap && !S.burnt` (connected and in breakdown). Q and W move under the ideal-model label, and C, U, E and Emax stay as before. No calculation and no simState key changed.
- Browser (rebuilt preview, fi), d = 1,0 mm, air:
  - U0 = 3,0 kV: no breakdown, normal readout (177 pF, 531 nC, 797 µJ).
  - U0 = 3,1 kV, kytketty: breakdown, new label with Q 549 nC and W 851 µJ, then the breakdown text and the mallirajaus note.
  - irrotettu: Q = 0, purkautui text, normal readout.
- Recomputed: C = ε0·A/d = 177,1 pF, Q and W at 3,0 and 3,1 kV as above. All agree with the sim.
- The previous Polish item (name Q and W as ideal values) is now done on screen. The readout and the mallirajaus note agree.
- The key exists in fi, en and fi-easy.
- The rest of the lesson is unchanged since the last PASS (5d937e42ff5cf67a); predictions, experiments and numbers were checked there.
- Hash identical at start and end.
