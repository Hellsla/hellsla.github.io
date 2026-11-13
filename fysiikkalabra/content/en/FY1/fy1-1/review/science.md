VERDICT: FAIL
CONTENT-HASH: 22cf64c4b70126f8

## Blocking
- lesson.md:94 with inquiry.json:456-477 (check-1) — **B (unstated condition; consistency/assessment 6, 7).** The simplified paragraph now gives only "the power of ten closest to the number on the axis of powers of ten" and two examples far from the boundary (1.7 → 10⁰, 8.8·10³ → 10⁴). Nothing in the theory now says where the switch to the next power lies, and "closest" holds only on a logarithmic axis: on an ordinary number line 4.0·10¹⁶ is closer to 10¹⁶ (distance 3·10¹⁶) than to 10¹⁷ (6·10¹⁶). Check-1 asks exactly that borderline case (a = 4.0, correct option 10¹⁷), and its feedback (lines 460, 464) uses a rule, "factor part more than about 3", that the lesson text no longer states. The keyed answer is correct physics (the sim's `kohdeExp = Math.round(log10 m)` and the glossary also use the ≈3 boundary), but a student who reads "closest" literally will get it wrong with no support in the theory. — Fix (keeps the teacher's simplification, no √10): add one short clause to line 94, e.g. "On this axis the point halfway between $10^{n}$ and $10^{n+1}$ is at about $3\cdot10^{n}$, so a factor above about 3 rounds up", or add a third example such as $4.0\cdot10^{16}\,\text{m} \to 10^{17}\,\text{m}$. The exercise set's solutions.md:105 also uses "less than about 3" (not judged here; the exercise review should note it).

## Polish
- lesson.md (Oort cloud) — "about 2000–100 000 AU": the outer edge is often given up to ~200 000 AU; "100 000 AU or more" would be safer. Not an error at this level.

## Checked
- Recomputed in one script: worked example k = 6.47·10⁴ → 6.5·10⁴, 5 steps; exp-1 Δn = 5, exp-2 Δn = 8 (sim n: Neptune 4.5·10¹² → 13, Milky Way 9.5·10²⁰ → 21), exp-3 midpoint −4 (hair 7.0·10⁻⁵ → −4); siirto 12 732 km; check-2 57 917; Sun/Earth 109; MW–atom 31.
- Sizes: Sgr A* horizon diameter 2·R_s(4.3·10⁶ M☉) = 2.54·10¹⁰ m; light-year 9.46·10¹⁵ m; 8.8·10²⁶ m = 93·10⁹ ly; neutron star 20–25 km; p–p Coulomb/gravity 1.2·10³⁶; stadium/pea 4·10⁴.
- Order-of-magnitude examples on line 94 correct (log 1.7 = 0.23, log 8 800 = 3.94); summary agrees with the new paragraph.
- Fundamental interactions, β⁻ decay, residual strong force, scale-dominance argument: correct mechanisms.
- Observable universe vs whole universe, expansion explanation: correct, no cosmology equations (in scope).
- Predictions, interpret, tunnista, vuorovaikutukset, virhe: one correct option each, every distractor wrong with correct feedback.
- Sim object table and `kohdeExp` give the measured keys at the experiments' settings; model box states the limits.
- Exit ticket matches the theory.
