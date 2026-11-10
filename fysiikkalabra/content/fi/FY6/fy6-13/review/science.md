VERDICT: PASS
CONTENT-HASH: ffc9647383412788

## Blocking

## Polish
- assets/sims/fy6/fy6-13/sim.js:81 — the code comment still says "the ideal model's values before it". It is not shown to students and is optional to update. This is C-level.

## Checked
- batch delta review: the packet's wording diff is empty. The only change is lang/fi.json:1946 `sims.fy6-13.lukemat_lap` (it is outside the content hash, which is unchanged) and now reads "Ideaalimallin laskennalliset arvot tällä jännitteellä, jos läpilyöntiä ei tapahtuisi". sim.js:62–64 confirms that, connected and in breakdown, U = U0 (the voltage shown on the line above), Q = C·U0 and W = ½·Q·U0. "Tällä jännitteellä" is therefore exact, and last round's Polish item is resolved. Example: d = 1,0 mm in air, C = 177 pF, U0 = 3,1 kV gives 549 nC and 851 µJ. The label and the mallirajaus note agree; the label is used only when S.lap && !S.burnt; no simState key or calculation changed; fi-easy says the same. Hash identical at start and end.
