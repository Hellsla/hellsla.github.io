VERDICT: PASS
CONTENT-HASH: e01ece4a5152a50f
SCOPE: delta added-exercise from aea1d440c4ddfe37 base 5b3ca4f81c77

## Blocking

## Polish
- exercises.json fy8-5-L2-08 (text, part c) — a hydrogen atom has one electron, so "how many electrons can the subshells 1s, 2s and 2p hold" is a count of capacity, not of hydrogen's electrons; the solution's neon check makes this clear, so it is a fair simplification (C) — optionally add "in an atom with more electrons" to part c.

## Checked
- Recomputed in one script: L2-08 2·(1+1+3) = 10 (answers.py 10); L2-09 E_4 − E_2 = −0.850 − (−3.40) = 2.55 eV = 4.0851e-19 J, hc = 1.98647e-25 J m, λ = 486.27 nm (answers.py 486.273, answer 486 nm). Matches Hβ (486 nm). Unit, tolerance and 3 s.f. fit the data.
- L2-08 physics: 1s no node, 2s one radial node (sphere), 2p one angular node (plane through the nucleus); zero wave amplitude at a node means zero probability there; "the wave is a state with no path" answers the "how does it cross" misconception correctly. Pauli: 2 per orbital, 3 p orbitals.
- L2-08 figure `fy8-5/nodes`: stated "not to scale"; 2s node sphere (r 34) lies between the inner region and the outer shell (gradient transparent to ~36); 2p lobes vertical with the nodal plane horizontal through the nucleus. Figure labels name the node kinds, which is what part a) asks the student to read: acceptable.
- L2-09 figure `fy8-5/levels-n4`: linear energy axis (Y ∝ −E), so "to scale" holds; tick values −0.850, −1.51, −3.40, −13.6 eV equal −13.6/n²; 1/3/5/7 boxes per subshell, n² = 16 for n = 4; no wavelength shown, so the answer is not given away.
- Transitions 4s→2p and 4d→2p are both allowed (Δl = ±1); part c)'s reason (hydrogen energy depends only on n) agrees with the lesson's Kaava and worked example (3d→2p = 3s→2p).
- Solutions complete: given/asked, principle (energy conservation, E_f = hc/λ), symbolic λ = hc/(E_4 − E_2) before numbers, conversions, rounding justified by the 3-s.f. readings, real reasonableness checks (visible, Balmer second line, shorter than 656 nm since 2.55 > 1.89 eV; 2 + 8 = 10, neon 1s² 2s² 2p⁶).
- Scope: inside FY8 "atomin elektronien kvanttitilat ja aaltomekaanisen atomimallin periaate"; no Schrödinger equation.
- Hash the same at the start and the end.
