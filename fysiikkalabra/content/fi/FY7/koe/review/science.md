VERDICT: PASS
CONTENT-HASH: d63f5c2e6544c73f

## Blocking
None.

## Polish
- fy7-k4 b Kaava: the step now runs through a derivative, $e = -N\,\text{d}\Phi/\text{d}t$, $\Phi = BA\cos(2\pi f t)$. Physics and sign are right, but the course sheet gives $e_0 = NBA \cdot 2\pi f$ directly, and a student without the long maths syllabus cannot follow a derivative. Consider the sheet's form with the derivative as an aside. Not an error (C).
- fy7-k3 d Mallivastaus: the hypothetical case says "vastus [saisi] lämpöä". Following P1, "vastuksen sisäenergia kasvaisi" would match the next paragraph. It is inside a counterfactual, so it is not blocking.

## Checked
- Full review of tasks.json, solutions.md and answers.py. Focus: the rewritten Kaava steps (8g). Each starts from the basic law. Each is solved symbolically before substitution, and each derivation is algebraically correct: $r^2 = m_\text{e}^2v^2/(e^2B^2) = 2m_\text{e}U/(eB^2)$, and $\Delta\Phi = Blv\Delta t$.
- Kaava steps ending in several unknowns (k3 c, k4 c, k6 a–c): every unknown is expressed only in givens or in unknowns solved earlier. In k6 c, the note defining p, K and S is consistent with Sijoitus and with the rubric.
- I recomputed everything in my own script. Every number agrees with answers.py and with the solutions:
  - k1 d: 0,08 / 0,12 / 0,40 mV; k1 i: 73,7°.
  - k2: r² and error bars; least-squares fit 1,739·10¹¹; slope read from the graph 1,72·10¹¹; extreme lines verified inside all five bars; 1,68 and 1,85·10¹¹, so ±0,084·10¹¹.
  - k3: 0,30 V, 0,50 A, 0,060 N, 0,15 W, I²R = 0,15 W.
  - k4: 40 Hz, 12,37 V, B = 0,0516 T, N₂ = 2788/2789, I₁ = 3,72 A.
  - k5: d = 3,327, 3,347, 3,321 µm; Δd = 27, 12, 6 nm; k_max = 6 (6,26); 73,4°.
  - k6: 600 A, 1,728 MW (14,4 %); 109,1 A, 57,1 kW (0,48 %); N₁ = 500; 6912 and 228,5 MWh; 334 175 €; 8,98 a; with transformer losses 9,67 a.
  - k7: b = 2,758·10⁻³ (origin fit), 2,75·10⁻³ read; 4,8 %; random 2,6 %; all λT below literature; 9,47 µm; 5269 K.
- k3 b direction: v to the right × B into the page gives the force up, which agrees with Lenz's law (current counterclockwise).
- Osa 1: exactly one correct option per item, and the distractor explanations are right.
- Scope: everything is within the FY7 central contents. No self-induction, and polarisation is qualitative only.
- Hash d63f5c2e6544c73f at start and end.
