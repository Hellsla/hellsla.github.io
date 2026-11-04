VERDICT: PASS
CONTENT-HASH: 535bf6b0f9d800a7
Round: 2

## Blocking

## Polish
- solutions.md:142 (L2-07, model answer) — The model answer says "d-kvarkki voi muuttua u-kvarkiksi" twice and still opens with "Virhe on lähtöoletus". — Give the two errors as two sentences: (1) the neutron is not an elementary particle (udd); (2) "perushiukkanen ⇒ hajoamaton" is false anyway (muon); decay is decided by the conservation laws and Q > 0. Drop the repeated clause.
- exercises.json:106 (L1-08) — K⁺ = u s̄ is now the same combination as L2-05 row 7, and the L2-05 solution names it "kaoni K⁺". This is the fourth time the same quark-charge sum appears. — Use another hadron (e.g. Σ⁺ = uus or K⁻ = s ū), or accept it as L1 practice.
- exercises.json L3-05 — `answer` 218.5 while the solution's Vastaus is 218,471 MeV. The 0,5 % tolerance covers it; aligning the two is optional.

## Checked
- Round 1 Blocking A (Co-60 1,333): resolved. The value is 1,332 in the table and in solutions (Annettu, Sijoitus, Vastaus).
- Round 1 Blocking A (L2-07 cause): resolved. The correct option is now "kvarkin laji voi muuttua", and the feedback names the muon, the conservation laws and Q > 0. The distractor feedback no longer uses the stable electron as a refutation.
- Round 1 Blocking B (L1-06 neutron): resolved. The text now reads "Neutroniin ei kohdistu sähköistä voimaa, koska sen kokonaisvaraus on nolla", in both the feedback and the model answer.
- Round 1 Polish resolved: the caption is ENSDF; "tehtävän oletuksen mukaan" is used; L3-04 answers 0,797 MeV and c) states zero total momentum; the wrong sf claim in L3-05 is replaced, and Q = −535,452 MeV for the collision (recomputed) is added.
- L2-05 Sijoitus rewritten: rows 2 (q 1/3, B 2/3) and 4 (q 5/3, B 1/3) are rejected, and 5 are hadrons. This is right.
- Recomputed: L1-08 +1; L3-04 (2,615 − 1,022)/2 = 0,7965; L3-05 497,611 − 279,140 = 218,471. All are within tolerance and agree with answers.py.
- The MC tasks L1-06, L1-07 and L2-07 each still have exactly one correct option.
- The hash 535bf6b0f9d800a7 was the same at the start and at the end.
