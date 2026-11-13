VERDICT: PASS
CONTENT-HASH: 66c09e02e858349f
SCOPE: delta added-exercise from b59e199ba798ddff base 81db4a6fd727

## Blocking

## Polish
- `fy5-10/valokuva` is also the figure of check 2 in Tarkista osaamisesi (figures.py docstring "tarkistus 2"). I cannot open inquiry.json, so please confirm that the check does not already ask for v from λ = 1,5 m. If it asks for λ alone, L2-08 is still a different task, and the exercises come after the check on the page.
- exercises.json (L1-10): `kind: data` is a loose tag for a table lookup. Optional.

## Checked
- The hash was the same at the start and at the end. Only L1-10 and L2-08 were judged.
- Recomputed: L1-10 gives λ = 5120 m/s / 1000 Hz = 5,12 m; L2-08 gives v = 2,4 Hz · (2,0 − 0,5) m = 3,6 m/s. Both equal answers.py.
- Figure data: y = 4 cos(2π(x − 0,5)/1,5) cm has crests at 0,5, 2,0 and 3,5 m, all on the 0,5 m gridlines, and λ is not marked. The description gives the same values. The x-axis is position, so the reading is λ, as the brief's warning about (x, y) and (t, y) graphs requires.
- MAFY task L1-10: iron 5120 m/s is the VERIFIED row fy5-10 (20 °C), and the hint names only the table. 5120 m/s is the thin-rod (extensional) speed, which is the right one for a struck bar. The ±4 % tolerance fits the 3 sf.
- Sig figs: L2-08 has 2 (2,4 Hz and 1,5 m), and L1-10 has 3 (1,00 kHz and 5120 m/s).
- Physics: the frequency is kept when the medium changes, and the speed comes from the medium. Both match the brief. The air comparison 343/1000 = 0,34 m gives a ratio of about 15.
