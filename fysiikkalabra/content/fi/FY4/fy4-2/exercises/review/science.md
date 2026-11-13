VERDICT: PASS
CONTENT-HASH: 335dab662a9be35b
SCOPE: delta added-exercise from 8ae950d4924a8353 base 81db4a6fd727

## Blocking

## Polish

## Checked
- Round-1 polish fixed: L1-09's Vastaus now gives 1,27 s, three significant figures like the MAFY value 24,79 m/s², with h = 20 m read as exact. The line no longer contradicts itself.
- Physics unchanged: free fall from rest with air resistance left out. h = ½gt² comes from x = x₀ + v₀t + ½at², and t = √(2h/g) is solved in symbols first.
- Recomputed in one script (my formula beside python -I answers.py): t = √(40/24,79) = 1,2703 s. answers.py, exercises.json (1.2703, tolerance 0,04) and my value agree. Both 1,27 s and 1,3 s are inside the tolerance.
- The reasonableness check is a real one: 2,02 s on Earth divided by √(24,79/9,81) ≈ 1,59.
- Hash 335dab662a9be35b at the start and at the end.
