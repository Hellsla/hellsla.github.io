VERDICT: PASS
CONTENT-HASH: cad095f844334ca5

## Blocking

## Polish
- content/fi/FY5/fy5-2/exercises/solutions.md:95, 128, 199, 225 — the Kaava rows of L2-02, L2-05, L3-02 and L3-04 are still split by hand with `&\quad +` / `&\quad -`. The house rule says never to split a chain by hand. — Write each equation on one row and let the page wrap it.
- solutions.md:187 — the L3-01 block ends at `x - x_2 = …`, but Sijoitus substitutes into `x = x_2 + …`. — End the block with the row `x = x_2 + \dfrac{m_\text{L}(x_2 - x_\text{L})}{m_\text{m}}`.
- solutions.md:45, 75 — L1-05 and L1-08 drop $g$ between two rows without saying so. This is correct, but a short "g supistuu" would help the reader.
- solutions.md:225 — L3-04 stops at $s$ in terms of $N_\text{s}$ rather than going on to $N_\text{s} = \mu(G_\text{t}+G_\text{h})$ in one final symbolic form. Sijoitus follows the same steps, so this is acceptable.

## Checked
- The hash was the same at the start and the end. I judged only the diff, which rewrote the Kaava steps and split some paragraphs. The Sijoitus values, answers and tolerances are unchanged.
- The previous Blocking item is fixed. The L2-07 block (line 152) no longer has a $\Sigma M$ row: it starts from the lever arms and `m g\, r_1 = M g\, r_2`, so $M$ now means only the ruler's mass.
- In L1-05 and L1-08, `M_1 = M_2` stands for the moments of the two weights. These blocks do not use $M$ as a mass, so there is no clash.
- Every block starts from $\Sigma M = 0$, $\Sigma F = 0$, the moment equality or the centre-of-mass definition. Each is simplified symbolically to the form that Sijoitus substitutes into.
- I checked the algebra of L3-03 row by row, as well as the sign conventions and lever arms of L2-01, L2-05, L2-06, L3-02 and L3-04.
- The new paragraph breaks in L1-06, L1-09, L2-06, L2-07, L3-02, L3-04 and L3-05 change no physics.
- I recomputed every number in one script, and all of them match:
  - L1: 960; 0,75; 206,7; 58,86; 0,60; 0,98; 1,6
  - L2: 98,1; 555,9; 12,53°; 448,65; 61,9 kg; 209,9
  - L2-07: 108,5 / 111,3 / 109,6 / 111,4 → 110,2 g
  - L3: 3,333; 196,2; 1,213; 4,575; 42,2 cm → 52,97°
