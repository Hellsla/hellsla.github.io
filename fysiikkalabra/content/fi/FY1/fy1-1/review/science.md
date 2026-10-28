VERDICT: PASS
CONTENT-HASH: ca26f894b74a6477

## Blocking

## Polish
- assets/sims/fy1/fy1-1/sim.js:790-795 — the orbit objects (1 AU, Saturnus, Neptunus, heliopaussi, Oort) are drawn at their diameter but labelled with their radius. Mallin oletukset says so, but comparing the Sun with 1 AU by eye gives a factor of 2 wrong.
- lessons/FY1/fy1-1/sim-spec.md:1 and the sim.js header — say objects show from about 1/2000 of the view. Laskennan selitys says 1/1000, and the code gives about 1/1200. Use "noin 1/1000" in all three.
- lesson.md:46 — "nykyiset teoriat eivät enää toimi" is an expectation, not a tested fact. "teorioiden odotetaan lakkaavan toimimasta" is safer.

## Checked
- Round 2: re-check of round-1 Blocking items against the fix diff.
- lang/fi.json:739 now reads "o_proxima": "etäisyys Proxima Centauriin". The readout "Kooltaan lähin kohde: etäisyys Proxima Centauriin, koko 4,0·10¹⁶ m" no longer gives the distance as the star's size. It matches its siblings ("heliopaussin etäisyys", "Oort-pilven säde"), check-1 ("Proxima Centaurin etäisyys") and menetelmat ("Lähin tähti").
- The same key also feeds the "Siirry kohteeseen" menu and the canvas label. The new text is correct Finnish in both, and no inquiry experiment records this object, so no table text changes.
- The lesson hash is unchanged (lang/fi.json is not in it). Everything else is as reviewed in full in round 1: all numbers recomputed, exactly one correct option per item, physics and scope fine.
