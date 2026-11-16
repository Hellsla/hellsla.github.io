VERDICT: PASS
CONTENT-HASH: 75cc6de28fa950e1
SCOPE: delta added-exercise from 21165e7fa5250d9b base b5600a63ddae

## Blocking

## Polish
- content/fi/FY5/fy5-12/exercises/solutions.md:234 (L2-10, Vastaus) — "1,20 m" has three significant figures, but the same sentence says the results have two, as λ = 0,80 m has. — Write 1,2 m, both here and in the Sijoitus on line 232.
- content/fi/FY5/fy5-12/exercises/exercises.json:305 (L2-10) — "käynnistä molemmat lähteet lähteiden omista painikkeista": the source notes do not confirm that each source has its own button. This is minor. — Write "käynnistä molemmat lähteet".

## Checked
- The hash was the same at the start and at the end. Round 2, a delta review of the added exercise L2-10 only. `git diff 09d57eb5ac..HEAD` changes nothing else in the set or in answers.py.
- Round-1 Polish on the icon and the green buttons is fixed. The speaker icon and the green buttons are no longer in the text.
- Round-1 Polish on 0.4 is handled. The stored answer stays 0.4, and the solution now says that 0,40 and 0,4 are the same number in the box. Tolerance 2 %.
- New part c) recomputed. The next destructive path difference is (n + ½)λ with n = 1, so 3λ/2 = 1,20 m. The smallest destructive one is λ/2 = 0,40 m, and the smallest constructive one is λ = 0,80 m (n = 0 gives zero). The solution solves in symbols first. The note in Järkevyys, that such points exist only when the source separation is larger than Δs, covers the new value too.
- The rest of L2-10 (a, b, d) is as I passed it in round 1.
