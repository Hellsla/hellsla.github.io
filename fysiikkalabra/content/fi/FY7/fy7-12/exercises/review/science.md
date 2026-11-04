VERDICT: FAIL
CONTENT-HASH: 5c5e2966c4dba824

Round 3. Round 2 had three blocking items. Two of them are fixed:
- L1-06: option 2 is the small-angle option again. Its feedback answers it ("lähes kohtisuoraan ... menee pääosin läpi"). The four options are now distinct, exactly one is correct, and the Mallivastaus matches them.
- L3-04: the Vastaus is now 17,4°, which is 0,19 % off 17,367 and inside the tolerance.

The third is only half fixed. In L1-08, 103 km now lies inside the tolerance (0,43 % off), but the new rounding reason is wrong.

## Blocking
- solutions.md:143 (fy7-12-L1-08) — A, rounding. The Vastaus says "103 km, kolme merkitsevää numeroa kuten taitekerroin 1,45 ja valon nopeus". The time is given as 0,50 ms (exercises.json:84, solutions.md:137 and 141), which has two significant figures, so the time limits the precision. This breaks the house rule "three significant figures unless the data has fewer". — Fix: give the time as 0,500 ms in the task text (exercises.json:84) and in the Annettu, Muunnokset, Sijoitus and Järkevyys lines (solutions.md:137, 141, 142, 144), and keep "103 km, kolme merkitsevää numeroa". The answer 103,45 and its tolerance stay as they are.

## Polish
- solutions.md:184 (fy7-12-L3-04): the Vastaus first says "kolme merkitsevää numeroa kuten taitekertoimet" and then that n₁ − n₂ = 0,03 has one significant figure, so the result is sensitive to rounding. Those two statements pull against each other. — Write instead: "17,4° laskettuna annetuista arvoista; koska n₁ − n₂ = 0,03, tulos on herkkä taitekertoimien pyöristykselle."
- exercises.json fy7-12-L1-07 vs L1-03 and the plan (carried over): L1-07 (acrylic → water) has the same structure as L1-03 (glass → water), and the plan's "timantin hionta" was replaced by L3-05. — Update the plan or note the swap.
- solutions.md:192 (fy7-12-L3-05, carried over): the triangle geometry is described only in words. — Add a small figure (O, R − a, R + a).

## Checked
- One script recomputed every new answer from the task text: 63,204°; 103,448 km; mean 42,04° gives n = 1,4933 (range 1,477–1,509; polystyrene would give 38,97°); t₀ 49,33 µs and a width of 800 ns; 38,790°; θ_max 17,367/14,033/9,822°; delay numbers 0,0204/0,0137/0,0069; R_min 16,056 mm. All of them agree with answers.py.
- L1-06: every distractor is really wrong, and each one's feedback is right.
- Every Vastaus value of the new tasks lies inside its tolerance.
- The hash was the same at the start and at the end.
