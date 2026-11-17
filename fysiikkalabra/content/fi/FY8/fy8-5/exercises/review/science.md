VERDICT: PASS
CONTENT-HASH: 599e18e38085bad0
SCOPE: delta added-exercise from 56f61bb434bbcc6b base 5b3ca4f81c77

## Blocking

## Polish
- fy8-5/levels-n4 (figures.py levels_n4) — at 1280 px the n = 4 and n = 3 rows sit only about 0,66 eV apart on the scale, so the 4s and 3s boxes nearly touch and the arrow's start can be misread as 3s. The figure is still correct and to scale, and the task text names 4s. — This is for the visual reviewer: a slightly larger label offset or a short leader line would help.

## Checked
- Delta only: the added exercises fy8-5-L2-08 and fy8-5-L2-09 and their answers.py lines. I recomputed both in one script with my own formulas.
- L2-08 c: the 1s, 2s and 2p subshells hold 1 + 1 + 3 orbitals. The task text says there are three 2p orbitals, so the student does not depend on the one drawn. At 2 electrons per orbital that is 10, the same as answers.py (10). The unit kpl is right, and an exact count fits the tolerance. The Järkevyys check (2 + 8 for n = 1 and n = 2, neon 1s² 2s² 2p⁶) is a real cross-check.
- L2-08 a, b: the nodes match the figure code (1s none, 2s a dashed node sphere at r = 34, 2p a horizontal nodal plane through the nucleus). "The wave is zero at a node, so the probability is zero, and there is no path through the node" is correct and qualitative, within the scope (no Schrödinger). The figure's "opposite phases" inside and outside the 2s node is correct.
- L2-09: E_4 = −13,6/16 = −0,850 eV and E_2 = −3,40 eV both match the figure's axis labels, and Y(E) is linear, so the description "mittakaavassa" holds. ΔE = 2,55 eV = 4,0851·10⁻¹⁹ J and hc = 1,98647·10⁻²⁵ J m give λ = 486,27 nm, the same as answers.py (486,273). The answer is 486 nm. Three significant figures are justified (2,55 eV, as in the worked example's 13,6 eV), and the 2 % tolerance fits.
- L2-09 c: n = 4 has 1 + 3 + 5 + 7 = 16 = 4² orbitals, matching the brief's n². In hydrogen the energy depends on n alone, so 4d → 2p gives the same line. This is consistent with the brief, which says the same about 3d/3s → 2p.
- The chosen transitions 4s → 2p and 4d → 2p are both allowed (Δl = ±1), so the task suggests no forbidden line.
- Reasonableness: 486 nm is Hβ, the second Balmer line (measured 486,1 nm), and it is blue-green. It is shorter than 656 nm because 2,55 eV is more than 1,89 eV.
- Solutions: both are complete. Each states the given values and the asked quantity, its principle (energy conservation, Pauli), a symbolic λ = hc/(E_4 − E_2) before substitution, the conversions, each chain's quantity named, and the reasoning for the rounding.
- The figures give every value the tasks need, and neither gives away the answer (levels-n4 has no wavelength). The descriptions carry the same values.
- The hash was 599e18e38085bad0 at the start and at the end.
