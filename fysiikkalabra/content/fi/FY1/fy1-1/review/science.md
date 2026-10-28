VERDICT: PASS
CONTENT-HASH: aeb2e62b44a9f8b7

## Blocking

## Polish
- assets/sims/fy1/fy1-1/sim.js:790-795 — the orbit objects (1 AU, Saturnus, Neptunus, heliopaussi, Oort) are drawn at their diameter but labelled with their radius. Mallin oletukset says so, but comparing the Sun with 1 AU by eye gives a factor of 2 wrong.
- lessons/FY1/fy1-1/sim-spec.md:1 and the sim.js header — say objects show from about 1/2000 of the view. Laskennan selitys says 1/1000, and the code gives about 1/1200. Use "noin 1/1000" in all three.
- lesson.md:46 — "nykyiset teoriat eivät enää toimi" is an expectation, not a tested fact. "teorioiden odotetaan lakkaavan toimimasta" is safer.
- tests/sims/fy1-1.json:365 — the note on the neighbouring assertion still calls $4{,}0\cdot10^{16}\,\text{m}$ "its size label". It is a value label for the distance. This is not student-facing.

## Checked
- Round 2: re-check of round-1 Blocking items against the fix diff (round 4: the test update).
- lang/fi.json:739 "o_proxima": "etäisyys Proxima Centauriin". The readout no longer gives the distance as the star's size. It matches its siblings, check-1 and menetelmat, and it reads correctly in the jump menu and on the canvas.
- tests/sims/fy1-1.json:368 still tests the same thing: that the object's name label is drawn on the canvas, which sim.js builds as `$\text{${__('o_'+id)}}$`. Only the expected string follows the rename. The tolerance and expected value are unchanged, and the value label $4{,}0\cdot10^{16}\,\text{m}$ is still asserted separately. No physics changes.
- Everything else is as reviewed in full in round 1: all numbers recomputed, exactly one correct option per item, physics and scope fine.
- Hash identical at start and end.
