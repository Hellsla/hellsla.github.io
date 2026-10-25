VERDICT: PASS
CONTENT-HASH: ada6a0da8647272c

## Blocking
(none)

## Polish
- tests/sims/fy3-1.json:2-9 — the two default-state assertions ("g = 9,81", "G = 98,1") have no `setup`, so they pass only when run first on an untouched page (shuffled order: G got 8,1; reversed: g got 1,62). Give each the setup `{"setup": "const s=document.querySelector('#sim-root select'), r=document.querySelector('#sim-root input[type=range]'); s.value='Maa'; r.value=10;"}` (keep the note that the defaults are Maa and 10 kg, or add a separate check that `select.value` and `range.value` are 'Maa' and '10' on load).
- tests/sims/fy3-1.json (no-setup assertions: G = m g, options, canvas size, slider label, slider min/max) — state-independent or self-consistent, so order does not matter; no change needed.
- Canvas-only drawing (spring rest length, 2 px bar and 3 px arrow floors, 10 px value-label floor, y axis ending at full scale with a tick, highlighted bar) is not readable from simState and not asserted; acceptable.

## Checked
- test_sims.py: PASS preview/fy3-1  [] []  (no console or page error; 28 assertions in tests/sims/fy3-1.json, all pass)
- Independence: ran all 28 on a fresh page each: all pass; shuffled and reversed on one shared page: only the two default-state assertions above fail, the other 26 pass
- lint_lesson.py fy3-1: 0 error(s), 0 warning(s); build.py --all built fy3-1 without errors
- Formula in sim.js:44 (G = m * g, g = 1,62 / 3,71 / 9,81 / 24,8 m/s²) equals lesson.md:27 and its table; no N/kg in sim.js or the test file
- Round-2 additions present and passing: arrow = 110 px at 100 kg on Jupiter (exact), readout scale "asteikko 0–49,6 N" at 2 kg (one-decimal branch), "g = 9,81 m/s²" and "g = 3,71 m/s² (Mars)" in the readout text
- Every spec quantity is asserted: m, body, g, G, stretch, arrow, bars, chartFull; slider 1-100 kg with unit in label; select with exactly Kuu, Mars, Maa, Jupiter
- Proportionality: stretch/G constant across bodies and masses, arrow/G constant, bar ratios equal g ratios, ten times the mass gives ten times G and stretch with unchanged bar proportions
- Fit: stretch <= 190 px, arrow <= 120 px (and = 110 at full scale), bar <= 220 px, canvas 600x400
- Tester hash unchanged at start and end (ada6a0da8647272c)
