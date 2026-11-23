VERDICT: PASS
CONTENT-HASH: 45fdfdfb9c1b9d20
none

## Blocking
(none)

## Polish
- solutions.md:107 (L3-02, the change of orbital speed) — the chain ends with v_1, v_2 and Δv = v_2 − v_1 as separate rows; add Δv = sqrt(γM/(R + h_2)) − sqrt(γM/(R + h_1)) as the last line, which the Substitution then uses.
- solutions.md:190 (L2-07, speed from the force) — the chain starts with F = γMm/r² and F = m v²/r; naming it ΣF = m a_n, as in the other tasks, would keep the same starting point throughout.
- Substitution rows now carry a manual "\quad" before "· 5.97 …" in the γM line; this is a layout break only, same numbers and order. The visual reviewer checks it.

## Checked
- The diff in the packet shows the new Kaava steps flattened to one line; the file has them as aligned rows, one equation per row.
- Every orbit task now starts from ΣF = m a_n with the gravitational force as the net force, then γMm/r² = m v²/r, v² = γM/r, v = sqrt(γM/r); the formula of the lesson is derived and not quoted (L1-01, 03, 05, L2-01, 02, 06, 07, L3-01, 02).
- L3-01, L3-03, L3-04, L3-05 and L2-05 add v = 2πr/T and give Kepler's form r³ = γMT²/4π² before the cube root or the mass; every algebra step is shown.
- L2-03 (the near-surface orbit): mg = m v²/R gives v = sqrt(gR); the basic equation is named first.
- The geostationary L3-01 ends with r = cube root(...), h = r − R, and the Substitution uses that; the symbolic result is reached before numbers.
- L2-09 (the data task) derives T² = (4π²/γM) r³ first, then fits the data; the part on Mars uses the constant ratio.
- Paragraph splits (Principle, Model answer, Reasonableness) keep each idea in its own paragraph; nothing removed.
- Substitution, answers and tolerances unchanged; figure radat unchanged and approved by the teacher.
- The content hash at the start and end is the same as the packet's.
