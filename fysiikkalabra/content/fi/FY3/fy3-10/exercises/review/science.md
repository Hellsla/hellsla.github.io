VERDICT: PASS
CONTENT-HASH: 68489463e63623ab
SCOPE: delta added-exercise from 8c50fb38cfdcf2c1 base 81db4a6fd727

## Blocking

## Polish
- exercises/solutions.md (fy3-10-L2-09, Vastaus) — "kolme merkitsevää numeroa luetuista arvoista": 60 kPa read on a 10 kPa grid is more like two figures; the 3 % tolerance accepts 1,7 anyway, so only the reason could be worded "luettu ruudukon viivoilta".

## Checked
- Previous blocking point fixed: L2-09 now uses the vessels as L2-04 does (both $2{,}00\,\textsf{l}$) and asks $n_\text{A}/n_\text{B}$, which L2-04 does not; no contradiction with figures.py (A 0,0602 mol, B 0,0361 mol).
- Recomputed: at 400 K $n_\text{A}/n_\text{B} = (p_\text{A}/T)/(p_\text{B}/T) = 100/60 = 1{,}667$; the 200 K points (50 and 30 kPa) give the same; answers.py 1,667, stored 1,67, tolerance 0,03.
- Principle right: rigid closed vessel, ideal gas, so $p/T = nR/V$ and with equal $V$ the slope ratio is the amount ratio; conditions stated in the task.
- Check real: $n = pV/(RT)$ gives 0,0602 and 0,0361 mol, ratio 1,67, consistent with L2-04's difference 0,024 mol.
- Figure gives both lines on grid crossings; the description lists the points, not the amounts or the ratio.
- L1-09 unchanged: $p = (500/39{,}95)\cdot 8{,}31 \cdot 293/0{,}0100 = 3{,}047\,\text{MPa}$.
- The duplicated answers.py comment is gone.
- Every answers.py value lies inside its exercise's tolerance (one script).
- Hash same at start and end.
