VERDICT: PASS
CONTENT-HASH: be5a20d4c273629f
Mode: full
Round: 1

## Blocking

## Fixed
- exercises.json L2-07 vaihtoehdon palaute: "Kaksinkertainen matka kuljetaan kaksinkertaisella vauhdilla yhtä nopeasti." -> "... samassa ajassa." (ensimmäinen muoto oli epäselvä ja tulkittavissa väärin).

## Polish

## Checked
- Scripted comparison of all 20 exercises against the reviewed Finnish: ids, levels, kinds, answers, units, tolerances, correct flags and every number in texts, choices, feedback and data tables are equal.
- solutions.md (193 lines): all numbers and formulas equal to the Finnish (number lists identical in order).
- New tasks L1-06..08, L2-05..07, L3-04..05: science is the same as in the Finnish (0,43 mT; 1,8 ns; 1,0e-8 kg/C; 25,1 u, 25,9 u, 78,9 %; 22,8 u natrium-23; 1,92e7 m/s, 3,07e-13 J, 32 ylitystä, 16 kierrosta, 1,05 us, v : c = 0,064).
- Easy-language additions are correct: "Liike-energia on liikkeessä olevan kappaleen energia" and "Klassinen käsittely tarkoittaa tavallisia Newtonin lakeja ilman suhteellisuusteoriaa".
- "homogeeninen" -> "tasainen" is used consistently; no meaning change.
- Correct flags and feedback of L1-06 and L2-07 match the Finnish.
- check_i18n.py fi-easy: 0 errors.

## Follow-up (be5a20d4c273629f: four solutions.md edits on top of the hash above)
- L1-02 Annettu: ${|q| = e = 1,602 \cdot 10^{-19}\,\text{C}}$ is the right elementary charge, given as a magnitude, so the electron's negative sign is no longer hidden. The outer braces only group.
- L1-02 Kaava: $|q|vB = mv^2/r$, $r = mv/(|q|B)$ is the correct magnitude form, matching the lesson's $|q|$ notation. Recomputed $r = 7,581$ mm → 7,6 mm, unchanged; answers.py and exercises.json untouched.
- L2-03 and L3-02 chapter references (*Homogeeninen sähkökenttä*, *Ympyrärata: jaksonaika ja ratanopeus*) match the current titles of fy6-11 and fy5-3; the physics is unchanged.
- Polish (not from this diff): exercises.json L1-02 still gives the electron's charge without a sign; match the solution: "varaus $1{,}602…$" → "varauksen suuruus $1{,}602…$".
- Hash at start and end: be5a20d4c273629f.
