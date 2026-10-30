VERDICT: FAIL
CONTENT-HASH: a0bd29f839e5dfac

## Blocking
- exercises.json:22 (L1-03), :99 (L3-02), :108 (L3-03) — **B**: the model's conditions are not stated in these tasks. L1-03 never says the string is light. L3-02 and L3-03 say nothing about the string or the pulley. Yet every solution uses T₁ = T₂ = T and a common a. The L1-03 solution even lists "lanka ja väkipyörä ovat kevyet" under *Annettu*. This breaks the teacher's rule that every condition is stated, and the guardrail "state the model's assumptions in the task". — Add "Lanka on kevyt ja venymätön ja väkipyörä kevyt ja kitkaton" to each of the three tasks. In L2-02, L2-04 and L3-01, add "venymätön" to the string or rope, because their solutions rely on it ("lanka on venymätön, joten …").

## Polish
- solutions.md:56 (L2-01) and figures.py malli_ketju — Both ends of the lower rope are named T₂. In the lesson, T₁/T₂ name the two ends of *one* string. The names are not wrong, but the convention changes between the theory and this solution. Either say so in one clause or rename the forces (e.g. T_A, T_B).
- L1-04 answer 29 N sits at 1,5 % of 29,43 N, inside the 2 % tolerance but close to its edge. That is fine as is; consider 0,03.
- L1-05 / L2-03 — "kitka jätetään huomiotta" is stated. Air resistance is not mentioned; adding it would be consistent with the other tasks.

## Checked
- Recomputed all 12 answers in one script with my own formulas (scratchpad recompute.py): 2,0; 4,686; 2,803; 29,43; 4,0; 880,8; 6,54; 8,0; 0,9073; 8720; 0,4405; 0,857. answers.py agrees, and every answer rounded to the data's figures stays inside its relative tolerance.
- Each solution names the bodies and their forces, then the positive direction per body, then the equations. The unknown is solved in symbols before any number, and the Järkevyys checks are real checks (net force = m a; T between the weights; free-fall time 0,43 s).
- Force diagrams in the solutions: one diagram per body. In L2-01, the upper crate correctly has T₁ up, G₁ down and the lower rope's T₂ down. No third-law pair sits on one diagram, and no velocity or acceleration is drawn as a force. malli-ketju is to scale: T₁ is longest, and T₂ is equal on both diagrams.
- Rounding reasons name the limiting datum (L3-01: masses to 100 kg).
- Conventions hold: overline vectors, \cdot, LaTeX symbols and units.
- Hash a0bd29f839e5dfac at start and end.
