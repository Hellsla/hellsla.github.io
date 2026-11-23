VERDICT: FAIL
CONTENT-HASH: 8a3a2c048540e528

## Blocking
- content/fi/FY5/fy5-2/exercises/solutions.md:152 — L2-07 (A, internal consistency). The new Kaava block opens with `\Sigma M = 0`, the sum of moments, and in the same block `M = \dfrac{m r_1}{r_2}` is the ruler's mass $M$, the symbol the task and Kysytty use. Read literally, the block says the moment sum is zero and then gives it a nonzero value in grams. The diff introduced this clash; the old block had no $\Sigma M$ row. — Fix: start the block from the moment condition without the clashing symbol, e.g. a first row `m g\, r_1 &= M g\, r_2` introduced in words as the momenttiehto about the support. Or name the moment sum differently in this solution only (e.g. $\Sigma M_\text{tuki}$ is still a clash, so use words). Do not rename the asked mass.

## Polish
- solutions.md:95, 128, 199, 225 — the Kaava rows in L2-02, L2-05, L3-02 and L3-04 are split by hand with `\\ &\quad +` / `&\quad -` (house rule: never split a chain by hand for the layout). Write each equation on one row.
- solutions.md:45, 75 — L1-05 and L1-08 drop $g$ between `m_1 g\, r_1 = m_2 g\, r_2` and `m_1 (x_\text{pp} - x_1) = …` without saying so. This is correct; a word ("g supistuu") would help.

## Checked
- Hash was the same at the start and the end. I judged only the diff: 19 Kaava steps rewritten. Sijoitus, answers, units and tolerances are unchanged, and the exercises.json and answers.py diffs are empty.
- Every new block starts from $\Sigma M = 0$, $\Sigma F = 0$ or the moment equality, and ends in the form Sijoitus substitutes into.
- The signs and lever arms are right for each chosen moment point:
  - L2-01: support 2, $r_G = 1{,}00\,\text{m}$, $r_1 = 2{,}50\,\text{m}$.
  - L2-02 and L2-05: the far end; L2-05 has $k = -mg/L$.
  - L2-06: leg 1.
  - L3-01: trestle 2.
  - L3-02: the hinge, with the perpendicular component $T\sin\alpha$.
  - L3-03: the rear carrier.
  - L3-04: the ladder foot, with $N_\text{s} L\sin\alpha$ against the $\cos\alpha$ arms.
- The algebra of L3-03 is right step by step: $(mg - F)a = \tfrac12 mgL - FL$.
- L1-04: the symmetric step $N_1 = N_2 = N$ leads to $2N - mg = 0$. This is right for supports at the ends of a uniform plank.
- I recomputed every number in one script and all of them match the Sijoitus values: 960; 0,75; 206,7; 58,86; 0,60; 0,98; 1,6; 98,1; 555,9; 12,53°; 448,65; −202,5 → 61,9; 209,9; 108,5/111,3/109,6/111,4; 3,333; 196,2; 1,213; 4,575; 42,2 cm → 52,97°.
