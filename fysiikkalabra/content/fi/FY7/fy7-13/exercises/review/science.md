VERDICT: PASS
CONTENT-HASH: 2599a88ef30c6ad1
Round 2.

## Blocking

## Polish
- solutions.md:190 (L3-05 Vastaus c) — the mean is now given to two significant figures (0,74 µm), the same as the reference value, so "0,36 % pienempi" claims more precision than the data have — fix: "noin −0,4 %. Ero on pienempi kuin mittausten epävarmuus, joten tulos vastaa DVD:n raitaväliä."
- exercises.json:85 (L1-08, answer 4) and the existing L2-01 (7) — the answer box accepts ±1 in the last digit (data-step 1), so 3 and 5 count as correct for an integer order. This comes from the build's step rule, not from the task. Raise it with the tooling (a count answer should get step 0).
- L2-07 (solutions.md:167) — the lesson's measurement paragraph answers it word for word, so it is closer to level 1 (carried over).
- L3-05 — close to the existing L3-02 (CD) as planned; the plan's level-2 picture questions (`pattern`, `setup`, `white`) are still missing (pedagogy; carried over).

## Checked
- Round-1 Blocking L3-05 b) resolved: the solution now says two spots (k = ±1) and three maxima, with k = 0 returning back through the hole. The task asks where the zero order goes.
- Round-1 Blocking L3-04 b) resolved: 17 rows, each new row equals cos²(πx/5,0 mm) to ±0,01 (0 → 1,00, 1,0 → 0,65, 2,5 and 7,5 → 0,00, 9,0/9,5/10,0/10,5 → 0,65/0,91/1,00/0,89). b) reads the 10,0 mm peak; the computed x₂ is 10,0001 mm. The c) grating is called fictional (4 lines/mm).
- L3-04 a) now asks for the I(x) graph (round-1 Polish).
- One script recomputed every new answer: 32,14°; 4; 633,7 nm (LSQ through the origin); 5,53 %; 625,0 nm; 0,7374 µm (sin θ₂ = 1,443). All agree with exercises.json and answers.py.
- The answer box accepts what the solutions call good (read from the built preview: data-tol, data-step and the 2 % floor). L3-05 0,74 falls within 0,715–0,760.
- L2-06 now has a separate "what is wrong" part, and the Vastaus names the sin ≈ x/L error.
- L1-06 and L2-07 (options reordered): exactly one correct option, it matches `answer`, and all feedback is right.
- Hash the same at start and end.
