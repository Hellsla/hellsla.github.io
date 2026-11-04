VERDICT: PASS
CONTENT-HASH: cbbd2024efecc6d6

## Blocking

## Polish
- solutions.md:99 (L2-04): still open from the last round. "pyörrevirtajarrun voimakin pienenee" applies F ∝ v to a train at 250 km/h, outside the model's range. Fix: drop the clause.
- exercises.json:106 and :206 (L1-08, L2-07), and also L2-02: "käämin läpi kulkeva magneettivuo" can be read as the flux through the whole coil. Fix: "yhden kierroksen läpi", as in fy7-5.
- exercises.json:206 (L2-07), **B**: e · Δt = NΔΦ holds for the mean voltage of the push. Fix: "keskimääräisen induktiojännitteen e".
- solutions.md:168 / exercises.json:322 (L3-05): P ∝ d² needs sheets thin compared with the skin depth, which is about 0,7 mm in iron at 50 Hz, so example data at 4,0 mm and the extrapolation to 5,0 mm are unrealistic. Fix: use about 0,25–1,0 mm. Also, d) does not say what it compares with: add "kuin 0,35 mm:n levyillä".
- exercises.json:267 (L3-04): c) uses "kuvaajan muutosnopeus", but no graph is given or asked for. Fix: add "Piirrä (t, v)-kuvaaja". L1-08 is a plain fy7-5 calculation (like fy7-5-L1-02) and does not appear in the plan; that coherence note is for pedagogy.

## Checked
- I recomputed all 20 answers in one script, and they agree with exercises.json and answers.py: L1-08 6,0 V; L2-05 26,8 mW; L2-07 0,349 mWb; L3-04 2,65 m/s²; L3-05 0,931 W, and 190 W at 5,0 mm.
- L3-04: the data fit v_r(1 − e^(−gt/v_r)) to within 0,01 m/s. The model gives a(0,10 s) = 2,61 and the central difference 2,8 m/s², both inside 2,7 ± 4 %. k = 0,66 N·s/m and P = 0,36 W are right.
- L2-05 c): F:v is 1,44 against 0,78 N·s/m, and the 3,3 s difference is much larger than the spread.
- L1-06 and L1-07 MC: exactly one correct option, and every feedback is right.
- L2-06: N face, repulsion and the energy argument are all right.
- L3-05: P:d² is constant within 1,3 %, and the Lenz reasoning suits the level.
- Units, 2 s.f. reasons and notation are correct. Hash unchanged at start and end.
