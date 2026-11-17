VERDICT: PASS
CONTENT-HASH: f6b4c858316a58cf
Mode: delta

## Blocking
(none)

## Polish
- content/en/FY8/fy8-4/exercises/solutions.md (fy8-4-L1-10, Reasonableness) — the two estimate expressions run together with no separator ("$\approx 17\,400\,\text{eV} \dfrac{E}{m_\text{e}c^2} \approx \ldots$"), so it reads as one product — put a comma or "and" between them.
- content/en/FY8/fy8-4/exercises/solutions.md (fy8-4-L1-10, Reasonableness) — "a thousand times smaller still": a visible photon (about 2–3 eV) is about 6000–9000 times weaker than 17.4 keV — "thousands of times smaller" would be more exact (C, not an error).

## Checked
- I recomputed all three new answers myself (h = 6.626e-34, c = 2.998e8, e = 1.602e-19). L1-09: h/546 nm = 1.2136e-27, and the reading range 543–549 nm gives 1.207–1.220, inside tolerance 0.03. L1-10: E = 17 440 eV, which is 3.413 % of 0.511 MeV (3.413 % with CODATA 0.51099895 MeV too). L2-09: 5.0 eV / c = 2.672e-27. The answers.py values and exercises.json agree.
- en answer, unit, tolerance and figure id are the same as in the Finnish set for all three tasks.
- fy8-2/lamp-spectrum: drawn to scale, ticks every 10 nm and numbers every 50 nm on 380–720. The green line at 546 nm matches mercury (546.1 nm). The description gives the same values, and the momentum is still left to compute.
- fy8-3/levels-task: the 1 eV grid gives E3 = −3.0 and E1 = −8.0 eV, so ΔE = 5.0 eV. Recoil is ignored, and the task says so. λ = 248 nm (UV) is correct.
- Physics: p = h/λ = E/c for a photon, E = hc/λ, photon energy equal to the level difference, and rest energy m_e c² with the MAFY value 0.511 MeV/c². All are within FY8's central contents (photon, quantum states, mass–energy equivalence). No de Broglie wavelength is used.
- Solutions: symbolic first, conversions shown, rounding reasons right. L2-09 gives 2.7 with two figures and accepts 2.67, and 2.7 is within the page's ±2 % check. The reasonableness checks are real: ordering by wavelength, the 1240 eV·nm estimate, and the comparison with the L2-01 Compton shift of 3.4 %.
- The MAFY lookup has a hint naming the table, and the solution notes that table editions can differ.
- Hash f6b4c858316a58cf at start and end (`--exercises --lang en`).
