VERDICT: PASS
CONTENT-HASH: b85ecd549e58ccf6

## Blocking

## Polish
- exercises/solutions.md (L1-04) — the intermediate is written 2,55 · 10⁻⁴; writing 2,546 · 10⁻⁴ would make the rounding to 0,00025 obvious.

## Checked
- Recomputed all 11 numeric answers in one script with my own formulas. New data: L2-03 (85 dB at 3,0 m → 12 m) = 72,96 → 73 dB; L3-01 crowd 82,79 dB + PA 80 dB → 1,90 · 10⁻⁴ + 1,0 · 10⁻⁴ = 2,90 · 10⁻⁴ W/m² → 84,63 → 85 dB. Both are within tolerance, and answers.py computes the same physics.
- L3-01: independence is now stated for all sources, and intensities, not decibels, are added. The reasonableness check (+1,8 dB < 3 dB) is a real check.
- L3-03: the task now says I₀ is defined at about 1000 Hz, so the model answer's frequency argument has a basis in the task. The self-assessment criteria ask only what the task gives. I = 3,2 · 10⁻¹³ W/m² is correct.
- Unchanged answers re-verified: L1-01 to L1-05, L2-01, L2-02, L2-04, L3-02.
- Point-source conditions are stated in every task that uses 4πr². Solutions solve symbolically first and justify their rounding, and the notation matches the brief.
- Round 3: only a blank line was added before the L3-03 Itsearviointi list (solutions.md:132); answers, tolerances and answers.py output are unchanged.
