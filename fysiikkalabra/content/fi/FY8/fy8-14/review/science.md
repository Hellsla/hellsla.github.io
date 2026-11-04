VERDICT: PASS
CONTENT-HASH: 93b09f7b2b9b0175

## Blocking

## Polish
- inquiry.json (ennuste-2 feedback), sim-spec "tyypillinen arvontajärjestys" — seed 73 is slower than the median at small N (18,4 against 4,2 cm at N = 10). "Kymmeniä" holds; "melko hidas arvontajärjestys" would be more exact. Carried over.
- lesson.md:178 "kalsiumatomeissa on paljon elektroneja" — the main cause is the larger atomic number (photoabsorption rises steeply with Z). Carried over.
- lesson.md:69 figure and ennuste-3 "terve kudos … noin 0,40 Gy" — less than the entrance dose (L3-01 gives 1,3 ×). Carried over.
- lesson.md:58 "volframilla ne ovat noin 59 keV:n kohdalla" — tungsten's K lines are at about 59 (Kα) and 67 keV (Kβ). Write "noin 59 ja 67 keV:n kohdalla". Carried over.
- PET about 6 mSv is FDG only, without the CT part of a PET-TT scan. Carried over.

## Checked
- Only change since the passed version: figures.py sadehoito() moves the labels "kasvain"/"2,0 Gy" and "terve kudos"/"0,40 Gy" from x 452 to 440 and the leader-line ends from 446 to 434 (lesson.md:298–303). Text, colours and numbers unchanged.
- The leaders still start at the same points, (T+16, T−6) on the tumour circle and (B+16, B) on the downward beam, so "kasvain" still points at the tumour and "terve kudos" at tissue on one beam only; the 6 px gap to the label is kept. "keila" label untouched.
- The figure still shows 5 × 0,40 Gy = 2,0 Gy at the tumour and 0,40 Gy on a single beam, matching the aria-label, theory, ennuste-3 and summary.
- Rest of the lesson unchanged and as approved in the previous rounds (sim model, worked example 3,59 → 3,6, 511 keV, siirto 770 MBq, TOF 4,5 cm).
- Hash unchanged between start and end.
