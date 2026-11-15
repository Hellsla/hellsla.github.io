VERDICT: PASS
CONTENT-HASH: a05765c3ca384b0a
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A: `unit.md`, Ydinajatus: "liikkuvaan varaukseen ja virtajohtimeen se kohdistaa voiman" holds only when the motion or the wire is not parallel to the field (the formula section already uses the perpendicular component). Add "kun liike ei ole kentän suuntaista".
- A: s7 e: 1,9 K is given as the temperature where the conductor is superconducting; the niobium-titanium winding is superconducting already below about 10 K, and the lower temperature allows the large current and field. "Lämpötilassa 1,9 K käämien johdin on suprajohtavassa tilassa" stays true, so this is optional.
- B: `site/` is not rebuilt on this branch: the built `siirto` figure still shows "lämmöksi 38 %". The new labels are shorter and end-anchored at the same x, so no clipping is expected; look at it after the rebuild.

## Checked
- Item 18 hunks: hook question, s1 c (337,5 W, 0,225 %, 844 kW, 2250 V), unit.md hook answer (174 A, 15 kW, 38 %, 2,0 A, 2,0 W, 0,005 %), figure aria and labels, transmission-loss text: all consistent.
- s7 recomputed in one script: v = 299 780 455 m/s, v/c = 0,99996, difference 12,0 km/s = 0,004 %, rounding interval 2,9976–2,9980e8 m/s (contains c); E1 = 1,0894e-6 J; classical v = 3,61e10 m/s = 120 c; N = 4,0e14; E = 435,7 MJ; both beams 871 MJ; mass 0,67 ng; Ek = 0,5787 MJ; 753 cars (760 with rounded values); wrong 7,5 MJ and 58. All agree with tasks.json, solutions.md and answers.py; `practice.py check` OK (7 tasks, 110 points; s7 3+2+3+3+4).
- Physics: the conclusion in a (the data cannot resolve c - v; a massive proton stays below c) is right; the magnetic force does no work; energy from the cavity electric field; RI^2 argument; the warning against r = mv/(qB) with the rest mass is correct.
