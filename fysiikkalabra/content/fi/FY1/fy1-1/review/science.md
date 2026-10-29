VERDICT: PASS
CONTENT-HASH: 3453b6f46da44c91

Delta review over the audit's PASS (ca26f894b74a6477): new choice check-c2 (orders of magnitude, from the exit ticket), titles renumbered, exit ticket down to two questions and "Lopuksi kaksi". Round 5: the merge adds only the tests/sims/fy1-1.json:368 assertion change over the PASS at 05834f00772d9c82.

## Blocking

## Polish
- assets/sims/fy1/fy1-1/sim.js:790-795 — the orbit objects (1 AU, Saturnus, Neptunus, heliopaussi, Oort) are drawn at their diameter but labelled with their radius. Mallin oletukset says so, but comparing the Sun with 1 AU by eye gives a factor of 2 wrong.
- lessons/FY1/fy1-1/sim-spec.md:1 and the sim.js header — say objects show from about 1/2000 of the view. Laskennan selitys says 1/1000, and the code gives about 1/1200. Use "noin 1/1000" in all three.
- lesson.md:46 — "nykyiset teoriat eivät enää toimi" is an expectation, not a tested fact. "teorioiden odotetaan lakkaavan toimimasta" is safer.
- tests/sims/fy1-1.json:365 — the note on the neighbouring assertion calls $4{,}0\cdot10^{16}\,\text{m}$ "its size label". It is a value label for the distance. This is not student-facing.

## Checked
- check-c2: $10^8/10^3 = 10^5$ is the one correct option. The distractors 5 (difference read as ratio), $10^{11}$ (sum of exponents) and 8/3 ≈ 2,7 (exponents divided) are all wrong, and each feedback names the real mistake correctly.
- Exit ticket: the converted question is gone, two remain, and the exit stage text says "kaksi".
- Titles 2.→3. and 3.→4. are consistent; no other physics changed.
- tests/sims/fy1-1.json:368 is the only content difference from a19ce6e (`git diff a19ce6e`; carry.tsv aside). The assertion still checks that the object's name label is drawn on the canvas, as sim.js builds it from __('o_proxima'). Only the expected text follows the rename to "etäisyys Proxima Centauriin" (lang/fi.json:739). The expected value and tolerance are unchanged, and the value label is still asserted separately.
- Hash identical at start and end.
