VERDICT: PASS
CONTENT-HASH: eb2ae3787808b0eb
Round: 2

## Blocking

## Polish
- exercises.json:212 (L2-06) — `answer` is 170.9, while solutions.md:160 now answers 1,7 · 10² Mpc. The 2 % tolerance accepts 170, so this is optional alignment.
- L2-05 — The plan's `hubble-t` figure is still missing. This is for pedagogy and visual to judge.

## Checked
- Round 1 Blocking A (L3-05 b, "ei liiku valoa nopeammin avaruudessa"): resolved. The task asks "Miksi tulosta ei voi pitää galaksin nopeutena?", and the answer says that v = cz is a small-z approximation (z < 0,1). The speed-of-light sentence is gone. Järkevyys adds the z vs 1 + z slip (8,2 K), which is right.
- Round 1 Polish resolved: Planck Collaboration 2018 is cited; L1-06 has a Doppler distractor with correct feedback (distant redshift comes from expansion, and peculiar motion is a small part); L2-06 is 1,7 · 10² Mpc with 2 sf; L3-04 says "muutaman kilometrin sekunnissa".
- L1-06, L1-08 and L2-07: the options were reordered and reworded. There is still exactly one correct option each, and the feedback is right.
- L2-05: the tolerance is now 5 %, which matches the stated eye-fit range of 65–72. The least-squares value 68,45 is unchanged.
- L3-04: dropping "1 kpc = 0,001 Mpc" is fine, because no conversion is needed.
- Recomputed: L2-06 d = 2,998·10⁵ · 0,03991 / 70 = 170,9 Mpc, about 4900 times smaller than the student's result; L3-05 z = 3,000 and T = 4 · 2,725 = 10,9 K, with T·λ = 2,89 K mm before and after. All the other answers are unchanged and agree with answers.py.
- The hash eb2ae3787808b0eb was the same at the start and at the end.
