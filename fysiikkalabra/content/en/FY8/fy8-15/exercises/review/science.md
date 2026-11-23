VERDICT: PASS
CONTENT-HASH: e905c2c9ca243e0d
SCOPE: delta answers,comments,md-paragraphs,numbers,reflow,structure,typography,wording from 510d3aaf9406538a base b5600a6
Mode: delta (new figure tasks L1-10 and L2-08 on fy8-15/taulukko; "(example data)" dropped from two captions; Kaava steps of 8g)

## Blocking
(none)

## Polish
- exercises/solutions.md (L1-10 Principle) — "every row has the same charge" is not true of the mediator column ($g, \gamma, Z^0$ neutral, $W^\pm$ charged). The reading step treats that column correctly. Fix: "every row of fermions has the same charge; the mediators are read one by one".
- figure fy8-15/taulukko on the en page — the labels (kvarkit, leptonit, välittäjähiukkaset, Higgsin bosoni) and the description are Finnish. This is for the visual and editorial reviewer: L1-10 and L2-08 tell the student to read this figure.

## Checked
- Hash e905c2c9ca243e0d (`--exercises --lang en`) at the start and the end.
- The figure has 17 boxes: 6 quarks ($+2e/3$, $-e/3$), 3 charged leptons ($-e$), 3 neutrinos (0), $g$, $\gamma$, $Z^0$ (0), $W^\pm$ ($\pm e$), $H$ (0). The figure code and its description match the physics.
- L1-10 recomputed: neutral boxes 3 + 3 + 1 = 7, of which 3 are leptons (the neutrinos). This matches answers.py (7) and exercises.json (7). The 10 + 7 = 17 check is a real check. One box per particle, with antiparticles not counted, is stated in the task.
- L2-08 recomputed: $q_X = \tfrac23 - 1 = -\tfrac13$, so −0.3333 e, which matches answers.py and the JSON. The task gives $B_X = \tfrac13$, which makes $X$ a quark. The antiquark exclusion ($+\tfrac13$, $-\tfrac23$) is right, and so is the candidate set $d, s, b$. Physically $t \to W^+ b$ dominates, and the solution rightly says the charge alone does not decide.
- Both new tasks are inside FY8's "hiukkasfysiikan standardimalli". Charge and baryon-number conservation are the lesson's tools.
- Captions: "Quark combinations" and "Reactions" hold real quark content and PDG-type masses, not invented measurements, so dropping "(example data)" leaves no false claim.
- L1-04 Kaava: $E_\text{initial} = 2m_ec^2 = 2E_\gamma = E_\text{final}$ gives $E_\gamma = m_ec^2$. Equal photon energies follow from zero total momentum, as the Principle says.
- Pair-production wavelength: $E = hf$ and $c = \lambda f$ give $\lambda = hc/E$. Correct.
- The re-split line $Q = (139.570 + 938.272 - 1115.683 - 497.611)\,\text{MeV} = -535.452\,\text{MeV}$ was recomputed and is correct.
- answers.py run against exercises.json: all 19 numeric answers are within tolerance.
