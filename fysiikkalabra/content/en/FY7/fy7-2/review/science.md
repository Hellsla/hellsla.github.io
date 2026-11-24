VERDICT: PASS
CONTENT-HASH: 3c64f8e7836feef7

## Blocking
None.

## Polish
- lesson.md:234: the cyclotron photo caption says "bends the particles onto a circular path". It comes right after the ring-accelerator paragraph, which says the field is strengthened so that r stays the same. A cyclotron does the opposite: B is constant and the radius grows with the speed, so the path is a spiral. Fix: "onto a spiral path that widens on every turn, while an electric field accelerates them". This is not an error in what the lesson teaches, only a pairing that could mislead (C/B borderline).

## Checked
- I recomputed every number in one script with my own formulas. Key idea: F = 3.2e-14 N, r = 5.2 cm, weight 1.6e-26 N (ratio 2e12). r-graph: proton 10.4 cm and deuteron 20.9 cm at 2.0e6 m/s; the plotted pixel positions match the axes, so "drawn to scale" holds. Worked example: v = 3.00e5 m/s, m = 3.324e-26 kg = 20.01 u, Ne-22 lands at 27.4 cm. LHC: 6.8 TeV = 1.09e-6 J. Electron and proton mass ratio is 1837.
- Inquiry: the revision item gives 4.4e5 and 8.8e5 m/s, and its distractors 1.8e6 and 7.0e6 m/s are the stated wrong models. Error-spotting item: 4.38e5 m/s and 4.57 cm against the correct 6.19e5 m/s and 6.46 cm. Transfer task: B = 0.2252 T, with mistake values 0.159 and 0.00712 T. Third check: 6.22 cm, proton 3.13 cm, mistake value 12.4 cm. Exit ticket: 3.0e5 m/s. All agree with lesson-answers.py.
- Simulation: I ported its Boris integrator to Python. Experiment 1 gives d = 5.22, 10.44, 15.66 and 20.89 cm at 0.5–2.0 Mm/s, with an end speed equal to the start speed. These are emergent values matching the feedback's 10.4 and 20.9 cm. Experiment 2 gives y = 0 for all four particles, exactly (the Boris half-kicks cancel), with F_m = F_s = 24.03 fN (proton) and 48.06 fN (alpha), matching the feedback's 24 and 48 fN and 4.8e-14 N.
- Experiment setups: experiment 1 locks particle, B, direction and E and varies v; experiment 2 locks v, B, direction and E and varies the particle. simState gives d, vLoppu, poikkeama, Fm15 and Fs15.
- Directions: in the sim F = q v × B with Bz = ±B and E upward from + to −. In the force-dir figure, a positive charge (B into the page) feels a force up and a negative one down. In the circle-path figure, a positive charge in B out of the page goes clockwise with the force towards the centre. The spectrometer figure's E up, B1 out, F_s up, F_m down and its downward bend in B2 out of the page are all correct. In the track-sign check, a downward curve in B into the page means a negative charge, and exactly one option is correct.
- Every prediction has exactly one correct option, and each distractor's feedback names the real mechanism (the force is perpendicular to v and does no work; mv²/r ∝ v²; the charge cancels from qE = qvB).
- Conditions are stated: the non-relativistic limit (r formula, LHC, 0.1 % and 0.2 % of c), gravity neglected, a uniform field and a vacuum. These are the same in the sim's model box and in the sim code (speeds below 1 % of c, SLOW = 1e-7 s).
- Scope: everything is inside the FY7 contents (the velocity selector and mass spectrometer come from the teacher's sheet). Revising W = qU from FY6 fits the slot.
- Theory, summary, glossary terms, the explain model answers and their criteria all agree.
