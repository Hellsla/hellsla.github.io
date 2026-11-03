VERDICT: FAIL
CONTENT-HASH: f46da1762804f9c9

## Blocking
- exercises/exercises.json:48 (fy7-11-L2-01), solutions.md fy7-11-L2-01 — **B**: a short white *pulse* travels at the group velocity c : n_g, not at c : n. For N-BK7 (SCHOTT 2017) n_g ≈ 1,535 at 656 nm and 1,582 at 405 nm, so the real delay over 5,00 km is about 790 ns, three times the 265 ns the task presents as how much later violet "saapuu". — Fix with the model's condition in a few words, e.g. task: "Oletetaan, että kumpikin väri etenee kuidussa nopeudella $v = c : n$ ja kulkee kuidun suuntaisesti." and the solution's Periaate names the same simplification (or reword the question to ask for the travel-time difference of the two waves at v = c : n rather than the arrival of a flash).

## Polish
- L1-01, L3-02, L3-03 use red n = 1,331 for water; Daimon & Masumura 2007 (20 °C) gives 1,3315 at 656 nm (≈ 1,332). Acceptable as task data, but if the lesson table is corrected (see review/science.md) consider 1,332 for consistency; violet 1,343 is right (1,3431).
- answers.py:L3-03 comments say θ_v 40,64° and width 1,73°; the code gives 40,646° and 1,724° (solution's 1,72° is right).
- L3-01 Vastaus: with the hundredths the task asks for, the student gets 0,96°; "noin 0,97°" reads as a different answer — say "0,96° (tarkoilla välituloksilla 0,966°)".

## Checked
- All 12 answers recomputed independently (L1: 35,14°, 196 078 km/s, 1,516, 37,0°, 42,0°; L2: 265 ns, 34,98°, 183 076 km/s, 15,65°; L3: 0,966°, 30,89°, 1,724°): agree with answers.py within tolerance.
- L1-03 and L1-05 data are physically consistent (n = 1,516 green; sin 55° : sin 38° = 1,33).
- L2-02 ray exits the second face (n sin α₃ = 0,87, α₄ ≈ 60,6°).
- L2-03 figure: flint curve is the sim's F2 fit; n(450 nm) = 1,6387 vs SCHOTT F2 1,6388, readable between grid lines 1,638 and 1,640; figure gives no answer.
- L2-04: violet top 15,6°, red top 17,4° as said; boundary 40,6° right.
- Crown values 1,5143 / 1,5302 match SCHOTT N-BK7 2017 catalogue.
- Solutions: symbolic first, conversions right, rounding reasons right (differences of near-equal numbers to 2 s.f.).
- Notation (α₁…α₄, A, δ, θ = 4β − 2α) same as the lesson brief.
