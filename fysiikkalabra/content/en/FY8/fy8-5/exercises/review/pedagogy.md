VERDICT: FAIL
CONTENT-HASH: 3fa2c76f56f19e19

## Blocking
- exercises/exercises.json:8, 24, 58, 66, 84, 92, 100 (L1-01, L1-03, L2-03, L2-02, L3-01, L3-02, L3-03; unit "kpl") — Finnish word as the answer unit on the English page (scripts/check_i18n.py WORD_UNIT flags it). — use "pcs" for counts and "hits" for measurement counts (L1-03, L2-03, L3-03), or leave the unit empty.

## Polish
- exercises.json L1-03, L3-03 — "the 90 % boundary ... is drawn in the picture" but the task has no picture. — drop "is drawn in the picture" or supply the figure.
- Coverage: all twelve tasks are numeric; none asks about standing waves, nodes or the meaning of the boundary in words, though the lesson teaches them. — make one level 3 task a short reasoning one (for example, the number of nodes and which of two states has the higher energy in hydrogen).
- exercises.json L2-03 — the radii 0.071 nm and 0.14 nm are given but unused (the solution says so). A useful trap, but the lesson does not prepare it. — add "(the radii are not needed)" to the solution's first line, or mention a check against the 0.14 nm figure from the lesson.
- exercises.json L3-02 is a counting task that only needs the filling order; level 2 in demand, level 3 in label. — add one step (for example, ask for the number of unpaired electrons or the shell of the outermost electron).
- The exercise brief in the packet is empty (the lesson excerpt is missing), so the "no repeat of the example" check was made against the lesson's worked example as read in the lesson packet.

## Checked
- Counts 5/4/3 match the course; levels rise from one formula (L1) to two steps (L2) to new situations (L3).
- None repeats the worked example (3d to 2p, 656 nm); L2-01 (3p to 1s) uses the same method on a different transition.
- Each task gives the situation first and the question last; contexts are physical but recognisable.
- Solutions follow Given/Asked/Principle/Formula/Conversions/Substitution/Answer/Reasonableness; principles are explained, not just named.
- Photon energy, wavelength and orbital-count answers recomputed: 103 nm, 365 nm, 16 orbitals, 4235 hits (answer 4240), all correct.
- Long calculations in L2-01, L2-04 and L3-01 stay readable at 664 px width.
- English wording and terms (orbital, shell, subshell, nodal sphere) match the lesson.
