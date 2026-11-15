VERDICT: FAIL
CONTENT-HASH: 3e03261bd159c50a

## Blocking
- exercises/solutions.md:211 (fy8-2-L2-05) — A: the rounding reason is false: "kolme merkitsevää numeroa, koska aallonpituudessa 546,3 nm on kolme"; 546,3 nm has four significant figures (as do h, c and 1 eV), so nothing in the data limits the answer to three — give the answer as 2,270 eV with "neljä merkitsevää numeroa, kuten aallonpituudessa ja vakioissa", or state the measured lines to three figures in the task.
- exercises/solutions.md:239 (fy8-2-L2-07) — A: same error: "lukemassa 16,4 mm ja aallonpituuksissa on kolme"; the calibration wavelengths (404,7 … 577,0 nm) have four — name the really limiting datum only: the scale reading 16,4 mm (three figures).

## Polish
- exercises/exercises.json:157 (L2-05) — 435,7 nm is called "violetti", while L2-09 and the lamp figure call the same mercury line 436 nm "sininen" (405 nm is the violet one) — use one colour name.
- exercises/solutions.md:285 (L3-05) — Kysytty lists only part b, though the task has parts a–d (all four are solved below) — list them.
- exercises/exercises.json:347 (L3-01) — "Viivat eivät kuitenkaan koskaan ylitä tiettyä rajaa": the wavelengths fall towards a limit — "aallonpituus ei kuitenkaan alita tiettyä rajaa".

## Checked
- All 19 numeric answers recomputed in one script from the task texts (h = 6,626e-34, c = 2,998e8, e = 1,602e-19): each agrees with answers.py and exercises.json within rounding.
- L2-07: own least-squares fit λ = 12,010x + 299,65; residuals 0,57 / −0,76 / 0,26 / −0,07 nm; 496,6 nm.
- L2-08: 2,50 / 3,00 / 4,40 eV give 496 / 413 / 282 nm; 2→4 gives 653 nm; exactly one spectrum fits a cold gas; figure code draws those lines to scale.
- L3-04: line energies 3,90 / 2,80 / 2,40 / 1,50 / 1,30 eV; levels 1,10 / 2,40 / 3,90 eV reproduce all six lines; mirror set excluded only by the task's condition, as the solution says.
- L3-05: shares 18,9 / 22,1 / 15,1 %; part d 477 nm; assumptions (one photon out, rest to internal energy) stated in the task.
- L3-06: 3,0617 − 2,2711 = 0,79 eV; Hg 404,7 and 546,1 nm do share the upper level (6³P₀, 6³P₂: 0,794 eV); two-figure reason sound.
- Solutions symbolic first, conversions shown, checks real; scope inside FY8; L2-06 lines real, E_y = −0,85 eV.
- Choice tasks L1-06, L1-08, L2-08: one correct option, distractors wrong, feedback physics right.
