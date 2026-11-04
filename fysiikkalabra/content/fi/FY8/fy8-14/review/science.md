VERDICT: PASS
CONTENT-HASH: 112a16e09d45b232

## Blocking

## Polish
- inquiry.json (ennuste-2 feedback), sim-spec "tyypillinen arvontajärjestys" — seed 73 is slower than the median at small N (18,4 against 4,2 cm at N = 10). "Kymmeniä" holds; "melko hidas arvontajärjestys" would be more exact. Carried over.
- lesson.md:178 "kalsiumatomeissa on paljon elektroneja" — the main cause is the larger atomic number (photoabsorption rises steeply with Z). Carried over.
- lesson.md:69 figure and ennuste-3 "terve kudos … noin 0,40 Gy" — less than the entrance dose (L3-01 gives 1,3 ×). Carried over.
- lesson.md:58 "volframilla ne ovat noin 59 keV:n kohdalla" — tungsten's K lines are at about 59 (Kα) and 67 keV (Kβ). Write "noin 59 ja 67 keV:n kohdalla". Carried over.
- PET about 6 mSv is FDG only, without the CT part of a PET-TT scan. Carried over.

## Checked
- figures.py: only the positions of the "luu" label (X-ray figure) and the "säätö" label (thickness gauge) moved; no number, arrow or physical element changed. The luu label still points at a bone, and the controller still closes the loop to the rolls.
- sim.js: the canvas text "ei kuvaa" now comes from the lang key ei_kuvaa_kanvas (fi: "ei kuvaa"); the model, seed and simState are unchanged, and the label shows only in single-photon mode, where no line and no image arise.
- Hash unchanged between start and end.
- All round-2 checks (sim model over seeds 1–100, worked example 3,59 → 3,6, 511 keV, f = 1,2355·10²⁰ Hz, siirto 770 MBq, TOF 4,5 cm) are untouched by this diff.
