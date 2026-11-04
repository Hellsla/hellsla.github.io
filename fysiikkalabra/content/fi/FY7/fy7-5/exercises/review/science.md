VERDICT: FAIL
CONTENT-HASH: 7cc9464b740f2877

## Blocking
- exercises/solutions.md:134 and exercises/exercises.json:77 (fy7-5-L1-07), **A**. The reason "kolme merkitsevää numeroa, koska tulos on tarkka tulo" is wrong: e₁ = 0,90 V has two significant figures, so the answer is 2,3 V. A student who gives 2,3 V is 2,2 % off 2,25 with tolerance 0,02, so the check shows "Lähellä" instead of correct. Fix: set `answer` 2.3, `tolerance` 0.03, Vastaus "2,3 V, kaksi merkitsevää numeroa kuten jännitteessä 0,90 V". Or change the data, for example N₂ = 240, which gives 1,8 V.

## Polish
- solutions.md:188/190 (L3-05): Periaate has e Δt = −NΔΦ, then A_a = NΦ with a positive area. Fix: write |A_a| = NΦ, or say the sign depends on how the scope is connected.
- solutions.md:178 (L3-04): k = 0,164 is "for example" read from a raw point as 0,165. Fix: read it from the fitted line through the origin (guardrail: Fits).
- exercises.json:125 (L2-05): kind `graph` but only a table is given, and it repeats L2-02 (largest |e| from Φ(t)). The plan's "piirrä e(t) Φ(t):stä toisella N:llä" is missing. Fix: ask for the e(t) drawing, or update the plan.
- exercises.json:323 (L3-05): its core repeats L3-03 (Φ at the centre = area ÷ N), and part b) is what is new. The plan's flip-coil task (B and inclination) was not written. Pedagogy and the plan should decide.
- solutions.md:151 (L2-05): the steepest single interval is 0,40–0,50 s (1,452 V). Both readings give 1,45 V, so add one clause saying so.

## Checked
- I recomputed all 20 answers in one script, and they agree with exercises.json and answers.py: L1-08 0,060 T; L2-05 1,45 V; L2-06 0,150 T (fit through the origin); L3-04 1,64 m/s² and 1,18 m; L3-05 0,0778 and 0,0787 mWb.
- L1-06 and L2-07 MC: exactly one correct option, and every feedback is right (v ∥ B gives e = 0).
- Each line through the origin has its physical reason.
- L3-05: the pulse areas are equal to within 1 %. The second pulse is narrower and taller because the magnet speeds up, and the sign is explained without Lenz, as the plan asks.
- Units, conversions and notation match the lesson. Hash unchanged at start and end.
