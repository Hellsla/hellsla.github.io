VERDICT: PASS
CONTENT-HASH: 717355b26a3c9247

## Blocking

## Polish
- lesson.md:180 — "muuttaa sähköenergiaa lämmöksi" sits awkwardly beside the Joule passage that treats heat as a transfer, not a stored form — consider "muuttaa sähköenergiaa kiukaan ja ilman sisäenergiaksi" (carried from round 1).

## Checked
- Round 2: changes since cb4b8f4 are inquiry.json:94 ("mallin arvojen mukaan", P 120 W → 30 W unchanged and right) and lesson.md:149 (comma → full stop); both round-1 polish items fixed, no physics changed.
- W = Fs for a constant force along the motion, area under (s,F) for a varying force, W = mgh at constant speed, P = W/t = Fv; no E_p, E_k, cos α or work–energy theorem, inside the FY3 scope note.
- Worked example symbolic first: W = ½F_max s = 4,0 J, the 8,0 J error explained.
- answers.py unchanged since round 1: all 12 answers matched, rounding within tolerance.
- solutions.md unchanged: unknowns isolated before substitution; sanity values right.
- Figures unchanged: spring-work graph to scale; lift figure F = G arrows equal; work-graphs schematic consistent.
- Simulation unchanged: W = F·s, P = W/t, area fills in proportion to distance; speed control changes only pace; model box states constant speed with friction equal to the pull.
- exp-1 varies s at fixed F, t; exp-2 varies t at fixed F, s; simState carries W and P.
- Predictions 600 → 1200 J; 120 → 30 W; horizontal carrying W = 0; Joule table 196 J, ΔU/W ≈ 0,99, labelled invented values.
- siirto 240 W; check-2 180 J; exit ticket 98 J, 20 J, equal work and double power.
