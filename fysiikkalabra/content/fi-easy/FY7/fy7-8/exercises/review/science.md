VERDICT: PASS
CONTENT-HASH: a57d3a1e79b21477
Mode: full (translation review against the reviewed Finnish set)
Round 1

## Blocking
(none)

## Fixed
- solutions.md L3-04 Järkevyys: "sen neliö 3,3: 4,959 MW : 1,500 MW = 3,3" is now "sen neliö 3,3. Näin on: ...". No number changed.
- solutions.md L3-05 Periaate: "saadaan tästä derivoimalla" is now "saadaan tästä etsimällä funktion huippu derivoimalla" so the step is explained.

## Polish
- "lukuvirhe" and "derivoimalla" stay as in fi; a Finnish teacher can explain them.

## Checked
- All 8 new ids exist with the same level, kind, answer, tolerance, units and correct flags as fi; L1-06 has one correct choice, the same as fi, and the model answer equals its text.
- Every data-table cell and every number in exercises.json and solutions.md is identical to fi (automatic number comparison: no difference); decimal comma in LaTeX, point in table JSON as in fi.
- Recomputed: 486 kierrosta, 87,7 %, 0,20 A, 210 kW, 90 %, 1,515 milj. euroa, 54,35 kW; all match.
- Wrong-choice feedback in L1-06 is correct physics and explains the error.
- check_i18n fi-easy: 0 errors.
