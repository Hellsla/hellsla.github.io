VERDICT: PASS
CONTENT-HASH: c608f2d0b5a85f56

## Blocking
- none

## Polish
- content/en/FY1/fy1-3/exercises/solutions.md (fy1-3-L2-09, Model answer c) — "and next four experiments at Gran Sasso" reads oddly — "and later four experiments at Gran Sasso".

## Checked
- Hash (--exercises --lang en) c608f2d0b5a85f56 at start and end.
- Independent recompute: t = s/c = 7.30e5 m / 2.998e8 m/s = 2.435 ms; Δt/t = 2.464e-5 = 0.002464 % = answers.py = exercises.json; unit %, tolerance 0.03 covers 0.0025 %.
- c·Δt = 17.99 m ≈ 18 m, about 90 times the 20 cm distance uncertainty ("almost a hundred"); t/Δt ≈ 40 600 matches "about 40 000".
- Source facts (730 km, 20 cm, better than 10 ns, over 15 000 events, ~60 ns early, GPS oscillator and fibre connector, ICARUS and the four Gran Sasso experiments) match the Finnish version.
- Error classified as systematic with the right reason; random error reduced by repetition, systematic not: consistent with the guardrails.
- Part d) treats an outlying result as checked, not dismissed; consistent with the outlier guardrail.
- Two significant figures justified by the 60 ns datum; reasonableness check real.
- fy1-3-L1-09 change is whitespace in a formula only; numbers unchanged.
