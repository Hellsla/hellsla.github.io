VERDICT: PASS
CONTENT-HASH: 85363c4f6c7afed7

## Blocking
(none)

## Polish
- tests/sims/fy3-1.json:9-15 — the on-load assertion (Maa, 10 kg) has no `setup` by design and fails in any order but first (shuffled runs: only this one fails). It runs first in `test_sims.py`, and its note says so; no change needed. Optional: none.
- Canvas-only drawing (spring rest length, 2 px bar and 3 px arrow floors, 10 px value-label floor, y axis ending at full scale with a tick, highlighted bar) is not readable from simState and not asserted; acceptable.

## Checked
- test_sims.py: `PASS preview/fy3-1  [] []` (no console or page error; 29 assertions in tests/sims/fy3-1.json, all pass)
- Round-3 polish fixed: default g (9,81) and G (98,1) assertions now carry the setup Maa/10 kg; a separate first assertion checks select 'Maa' and slider '10' on load
- Independence: each of the 29 assertions on its own fresh page: all pass; reversed order on one page: all pass; two random shuffles: only the on-load assertion fails (expected, it must run first)
- lint_lesson.py fy3-1: 0 error(s), 0 warning(s); build.py --all built fy3-1 without errors
- sim.js unchanged since round 3 (99 lines); formula sim.js:44 (G = m * g; g = 1,62 / 3,71 / 9,81 / 24,8 m/s²) equals lesson.md:27 and its table; no N/kg in sim.js or the test file
- Every spec quantity is asserted: m, body, g, G, stretch, arrow, bars, chartFull; slider 1-100 kg with unit in label; select with exactly Kuu, Mars, Maa, Jupiter; readout text (m, g, G, scale)
- Proportionality: stretch/G and arrow/G constant across bodies and masses, bar ratios equal g ratios, 10x mass gives 10x G and stretch
- Fit: stretch <= 190 px, arrow = 110 px at full scale (<= 120), bar <= 220 px, canvas 600x400
- Tester hash 85363c4f6c7afed7 identical at start and end
