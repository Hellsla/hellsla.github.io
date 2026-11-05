VERDICT: PASS
CONTENT-HASH: c994e0f8e59709cd

## Blocking

## Polish
- exercises.json (L3-05 text). "aallonpituus on kaikilla osuuksilla noin 200 km valtamerellä ja yli 10 km myös rannikolla" reads awkwardly, because "kaikilla osuuksilla" clashes with "valtamerellä". Better: "aallonpituus on valtamerellä noin 200 km ja rannikollakin yli 10 km". The physics is consistent: with a constant period, λ₃ = 200 km · √(50/4000) ≈ 22 km.
- L2-06 vs fy5-14-L1-01 (carried over from round 1). Both find the speed of sound from an echo, v = 2L/t. Medium, apparatus and averaging differ, so this is not a duplicate.
- docs/exercise-bank/FY5.md (carried over). The gel and S-wave questions are level-1 multiple choice here, and level 3 has a tsunami task. Update the plan to match.

## Checked
- Round-1 Blocking 1 is resolved. The bat-wavelength task L1-08 has been replaced by a multiple-choice item on why the highest frequency is not always used (absorption). It does not duplicate any FY5 task. No other FY5 set asks about ultrasound absorption against frequency (the fy5-16 noise-barrier and ANC tasks are a different topic). It complements this chapter's L2-02 (frequency from resolution) without repeating it.
- New L1-08 has exactly one correct option. Each distractor is really wrong and its feedback is right: speed does not depend on frequency, v = fλ gives a short λ at high f, and reflection depends on the materials, not on f. The model solution and the correct option say what the lesson's misconception section says.
- answers.py: the L1-08 line has been removed. The script runs, and all 17 numeric answers agree with exercises.json.
- Round-1 Blocking 2 is resolved. L2-05 now has d₂ = 4,54 cm, and the check gives 8,41 − 4,54 = 3,87 cm, equal to the answer. The rounding excuse is gone.
- The round-1 polish items are fixed: "Taulukon lukeminen" in L2-05, "vaikuta" in the L1-06 feedback, and the L3-05 wavelength assumption.
- L1-07 feedback now says "lähes koko pulssi" and "vain pieni osa" instead of percentages. It is still correct.
- The other new tasks (L1-06, L1-07, L2-06, L2-07, L3-04, L3-05) are unchanged in substance. Their round-1 recomputation still holds.
- The hash was the same at the start and at the end.
