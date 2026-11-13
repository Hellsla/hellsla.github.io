VERDICT: PASS
CONTENT-HASH: 1d761ff1cb9a18e2
SCOPE: delta added-exercise from 628ca4af401209e3 base 81db4a6fd727

## Blocking

## Polish
- exercises.json:12 (L1-09) and answers.py header: the set now gives Mars two values, 3,72 m/s² (MAFY, L1-09) and 3,71 m/s² (L2-04 and the docstring "Mars 3,71"). The L1-09 solution explains that table values differ, so this is acceptable. Updating the docstring would avoid confusion.
- `fy5-9/kuvaaja-k` is also the figure of a Tarkista osaamisesi check (figures.py docstring). I cannot open inquiry.json, so please confirm that the check does not ask for k from m = 0,150 kg (L2-09) or for E from k = 120 N/m (L1-10).
- solutions.md (L2-09): reading T over two periods (0,80 s / 2) is a more accurate reading than reading one period. Optional.

## Checked
- The hash was the same at the start and at the end. Only L1-09, L1-10 and L2-09 were judged.
- Recomputed: L1-09 gives 2π√(1,00/3,72) = 3,258 s; L1-10 gives ½·120·0,030² = 0,054 J; L2-09 gives 4π²·0,150/0,40² = 37,01 N/m. All three equal answers.py.
- Figure data: x = 3 cos(2πt/0,40) cm gives A = 3,0 cm on a labelled tick and maxima at 0, 0,40 and 0,80 s on the grid. The description gives the same values. L1-10 reads A and L2-09 reads T, so neither gives the other away.
- MAFY task L1-09: 3,72 m/s² is the VERIFIED row fy5-9, and the hint names only the table. The ±4 % in the solution matches `tolerance` 0.04. The small-swing condition is stated.
- Sig figs: L1-10 has 2 (A = 3,0 cm), L2-09 has 2 (T = 0,40 s; the answer 37 is inside 2 %), and L1-09 has 3.
- L1-10 is like L1-04 (same k) but reads A from a graph, so it is not a repeat.
- Notation ($T = 2\pi\sqrt{m/k}$, $E = \tfrac12 kA^2$, l, g) is the brief's.
