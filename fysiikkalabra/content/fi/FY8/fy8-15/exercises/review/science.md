VERDICT: FAIL
CONTENT-HASH: e79762c7bcbdc277

## Blocking
- exercises.json:331, solutions.md:167, 172, 173 (L3-04) — **A.** Co-60 is 1332,49 keV (ENSDF), so it rounds to 1,332 MeV, not 1,333. The other lines are correct. — Write 1,332 in all four places. No answer changes.
- exercises.json:265, solutions.md:134 (L2-07) — **A, wrong cause.** Being composite is not why a particle decays: the proton is composite and stable. A stable electron also cannot refute "perushiukkanen ⇒ hajoamaton"; only a decaying elementary particle can, such as the muon. — In the feedback and the model answer, write: "Osa perushiukkasista hajoaa (myoni). Hajoamisen ratkaisevat säilymislait ja $Q > 0$; neutronin $d$-kvarkki voi muuttua $u$-kvarkiksi."
- exercises.json:57 (L1-06, feedback of the correct option) — **B.** "ei vaikuta varauksettomaan neutroniin kokonaisuutena" is false, because the neutron's magnetic moment does interact. — Delete it, or write "Neutroniin ei kohdistu sähköistä voimaa, koska sen kokonaisvaraus on nolla."

## Polish
- exercises.json:310, 315 (L3-04) — The energies are real reference data, and only the scenario is invented. — Caption: "Gammaviivojen energioita (ENSDF, pyöristetty)".
- solutions.md:169 — "jätetään huomiotta, joten … jakautuu tasan" is a non sequitur. — Write "ja tehtävän oletuksen mukaan".
- solutions.md:173 — The subtraction keeps thousandths, so the answer is 0,797 MeV, not two figures. In c), add that the total momentum is zero, which is why the two photons have equal energies.
- solutions.md:183 (L3-05) — "neljä merkitsevää numeroa kuten kaonin massa" is wrong. — Keep 218,471 MeV. Optionally note that the collision has Q = −535 MeV, so the pion's kinetic energy pays for it.
- L1-08 is the third task that sums quark charges, and the kind "reasoning" does not fit it.

## Checked
- Hash e79762c7bcbdc277 at the start and the end.
- All 17 numeric answers recomputed independently: all within tolerance.
- L2-05 gives 5 (rows 1, 3, 5, 6, 7). L2-06 gives 3 (reactions 3 L, 5 q, 7 B).
- L3-04: threshold 1,022 MeV, four lines above it, E_k = 0,7965 MeV, 0,511 MeV photons. The other gamma energies are correct.
- L3-05: q, B and the u/d/s counts balance; Q = 218,471 MeV; the track explanation is right.
- MC L1-06, L1-07 and L2-07 each have exactly one correct option.
- The plan in docs/exercise-bank/FY8.md is covered, and the levels fit.
- L3-04 renders at 1280 px.
