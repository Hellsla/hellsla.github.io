VERDICT: PASS
CONTENT-HASH: 914daee64065bfde
SCOPE: delta added-exercise from 689c71af3cad3c07 base 415cbc7c6bc3

## Blocking

## Polish
- content/fi-easy/FY8/fy8-1/exercises/solutions.md:408 and :431 — Annettu says a slider reading "voi poiketa muutaman nanometrin", Vastaus says "noin ±10 nm"; the two disagree — give one figure (the 530–550 nm range fits ±10 nm).
- content/fi-easy/FY8/fy8-1/exercises/solutions.md:412 — "vihreällä ... valolla" releases electrons, yet green runs to about 570 nm, and 540–570 nm gives no current; "Muut metallit" also covers the "?" metal, whose work function was not checked — say "lyhyemmillä kuin noin 540 nm (vihreä–violetti, UV)" and "muut nimetyt metallit".
- content/fi-easy/FY8/fy8-1/exercises/solutions.md:432 — "natriumin raja-aallonpituudella 544 nm teoriassa" gives no source or reason; 544 nm is the value for a tabulated W ≈ 2,28 eV, not a theoretical value — name it so, or drop it. The aligned block inside the sentence is a layout issue too.

## Checked
- Recomputed: f0 = c/539 nm = 5,562e14 Hz, hf0 = 3,686e-19 J = 2,3006 eV; answers.py gives 2,30055 ✓.
- Reading range 530–550 nm gives 2,340–2,255 eV; tolerance 0,05 is relative in lesson.js (±0,115 eV), so it accepts every reading in that range ✓.
- Physics: hf ≥ W is the release condition, hf0 = W, E_k,max = hf − W does not depend on intensity, current grows with intensity; the classical-wave argument (d) is right. Symbol W matches the lesson.
- Source facts against the verified list: wavelength and intensity sliders (no frequency), sodium 2,3 eV, zinc 4,3 eV, platinum 6,3 eV, the graphs, a browser run, all ✓. Nothing else is attributed to PhET.
- The box value (2,3 eV) is the model's own and does not depend on the student's reading; the dated example reading is given.
- Hash 914daee64065bfde at the start and the end.
