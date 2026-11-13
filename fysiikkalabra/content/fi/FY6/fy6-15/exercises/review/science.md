VERDICT: FAIL
CONTENT-HASH: 382ccde4ebe17d63

## Blocking
- content/fi/FY6/fy6-15/exercises/exercises.json:268 and lessons/FY6/fy6-15/figures.py:445 (fy6-15-L2-08) — (A, invented provenance) The task and the figure's description call the data "mitattu aineisto". The graph is a constructed, ideal step function: five exact round values (1000, 3000, 4000, 2000 and 3500 W) on whole-minute steps, with no source. A real measured household load shows switching transients and the thermostat cycling of a kettle or oven. The guardrails require saying whether each number is measured, simulated or calculated, and the house rules forbid presenting invented data as measured. Fix: write "esimerkkiaineisto" (or leave out the provenance, as the 2026-11-13 read-through asks for example data) in both the task text and the figure's description. The figure then needs the teacher's approval again; nothing else changes.

## Polish
- solutions.md (fy6-15-L2-08, Vastaus) — "kaksi merkitsevää numeroa kuten sulakkeen nimellisvirrassa" names a value that does not enter the calculation. The limiting datum is the graph reading of 4000 W, read on a 1000 W grid line, together with U = 230 V. Name those instead.

## Checked
- Hash 382ccde4ebe17d63 at start and end; I judged only fy6-15-L2-08 (delta added-exercise).
- Figure in figures.py: the steps match the alt text and the solution's reading. The maximum is 4000 W at 10–16 min, on a grid line, and no current or fuse limit is drawn.
- Physics: the group's devices are in parallel at 230 V, so I = ΣP : U, the brief's formula. The brief's power-factor condition (devices with a power factor of about 1) applies, as in the worked example (C).
- Recomputed: I = 4000 W : 230 V = 17,39 A, which equals answers.py. The tolerance of 3 % fits an answer of 17 A.
- The fuse statement is correct: P_max = 230 V · 16 A = 3680 W. Only the 4000 W step exceeds it, and "ei välttämättä laukea heti" agrees with the worked example's slow-overload remark.
- The solution is otherwise complete: the principle and why it holds, the graph reading, the formula before the numbers, units, and a real check against 3680 W.
- Scope: the group current and the fuse are FY6 sähköturvallisuus (sulake).
