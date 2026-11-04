VERDICT: PASS
CONTENT-HASH: 2bb592b2d865407e
Round 2: full review of the exercise set after the round-1 fixes (commit e6301a0ac).

## Blocking

## Polish
- docs/exercise-bank/FY6.md fy6-12 Taso 2 — the planned V(x) graph task for two situations was replaced by the ion-mass data task L2-07. Update the plan line.

## Checked
- Hash 2bb592b2d865407e at start and end. Diff since 048b5f229 read in full.
- Round-1 Blocking 1 (L2-06, B) fixed: distractor feedback now says "levosta lähtevä positiivinen varaus kiihtyy / liikkuu kohti pienempää potentiaalia"; the model answer says a positive charge reaches higher potential only "jos sillä on liike-energiaa tai ulkoinen voima tekee työtä". No force-equals-velocity picture remains; consistent with L3-03.
- Round-1 Blocking 2 (L2-05) fixed: the solution fits the origin line by least squares, Σx² = 55,0 cm², ΣxV = 275,7 V·cm, k = 5,013 V/cm, E = 501 V/m, U = 30,1 V (recomputed: 30,08 V); the task allows least squares or one point read from the line; origin justified by the zero at the negative plate; answer 30.1 in exercises.json and answers.py.
- Round-1 Polish fixed: L2-07 6,66·10⁻²⁷ kg with three figures; He⁺ named; "Taulukon tulkinta" in L2-05 and L3-05; L3-04 c 1,4·10¹⁴.
- L1-06, L1-07, L2-06 after reordering: exactly one correct option, `answer` equals it, distractor feedback right.
- answers.py re-run: all 17 numeric answers agree with exercises.json.
- Scope (uniform field, E_p = qV, W = qU, eV), levels and notation unchanged; no duplicates.
