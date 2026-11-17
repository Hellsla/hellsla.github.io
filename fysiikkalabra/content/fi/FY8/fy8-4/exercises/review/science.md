VERDICT: PASS
CONTENT-HASH: 2d131b382d63c27b
SCOPE: delta added-exercise from df0225f5b9796ad4 base cabadc3e6179

## Blocking

## Polish
- content/fi/FY8/fy8-4/exercises/solutions.md:368 — "Näkyvän valon fotonin energia on vielä tuhatkertaa pienempi": 17,4 keV against about 2–3 eV is a factor of about 7000, not a thousand — write "tuhansia kertoja pienempi".
- content/fi/FY8/fy8-4/exercises/solutions.md:374 — "kolmannen ruudukon viivan kohdalla": counting the 0 line, −3 eV is the fourth grid line, so the count is ambiguous — write "kolmen ruudukon välin päässä nollasta".
- exercises.json fy8-4-L2-09 — `answer` 2.67 has three figures but the solution's Vastaus is 2,7 (two figures, as the data has). The check accepts both (±2 %), so this is consistent enough. An answer of 2.7 would match the stated precision.
- solutions.md fy8-4-L1-10 Vastaus — "hyväksytään noin ±3 % tarkkuudella" does not match how the page checks: it accepts ±2 % and calls 2–5 % "Lähellä". This could say "pieni ero hyväksytään" instead.

## Checked
- Recomputed independently, one script: L1-09 p = h/λ (546,1 nm) = 1,2133 vs 1,21355; L2-09 p = (E3−E1)/c = 2,6718 vs 2,67178; L1-10 (hc/λ)/(0,511 MeV), using m_e c² = 0,51099895 MeV, = 3,413 % vs 3,41295. All agree.
- L1-09 figure (fy8-2/lamp-spectrum, to scale, 1,53 px/nm): the green line is at 546 nm and can be read to within a few nm. A tolerance of 0,03 allows λ ≈ 534–562 nm, so a careful reading is accepted and a wrong line (436 or 577 nm) is not. The description gives the same values and does not give away the momentum.
- L2-09 figure (fy8-3/levels-task): E3 = −3,0 eV and E1 = −8,0 eV on the 1 eV grid; ΔE = 5,0 eV (UV, 248 nm). The task states that the recoil is neglected, as the solution's energy conservation needs.
- L1-10: within FY8 scope (mass–energy equivalence, photon energy, eV conversion); the unit MeV/c² is explained correctly.
- L1-10 reasonableness check: Δλ/λ = (E/m_ec²)(1−cos θ) ≤ 6,8 %, so "muutaman prosentin" is right. The quoted 0,0711 → 0,0735 nm is 3,4 % and matches L2-01's data.
- Symbolic form before substitution, unit conversions and significant-figure reasoning are present in all three solutions. The notation (p, E, h, λ, c) matches the brief.
- The three answers.py lines compute the physics the task texts describe.
- Hash the same at the start and the end.
