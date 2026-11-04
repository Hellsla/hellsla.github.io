VERDICT: FAIL
CONTENT-HASH: beb42d2e273c0e91

## Blocking
- exercises/solutions.md:191 — fy5-15-L2-06, Kaava: a stray fence line "```" after the closing fence of the latex block; it renders as a literal ``` in the solution (L2 capture at 1280 px, part 8). A broken render. — delete line 191.
- exercises/exercises.json:74 — fy5-15-L1-07 (new) copies the setting and the answer of the existing neighbouring task fy5-16-L1-02: two identical ventilation units/fans of 70 dB → 73 dB. A new task must not duplicate a task or answer of a neighbouring chapter (A). — change the source and the level, e.g. two identical 64 dB dishwashers, the student gets 128 dB, the correct answer 67 dB; change the options, feedback and the solution to match (105 dB → e.g. 96 dB, mean 64 dB, 10-fold 74 dB).

## Polish
- exercises/solutions.md:244 — fy5-15-L3-04: "315 m, kolme merkitsevää numeroa kuten mittarin lukemissa" — the limit 55 dB is given in whole decibels; ±0,5 dB moves r between 297 m and 334 m. Give 3,2 · 10² m with two significant figures and widen the tolerance to about 0,05.
- exercises/solutions.md:245 — fy5-15-L3-04 c: "todellinen taso on yleensä pienempi kuin malli ennustaa" while the same sentence lists reflections from buildings and temperature layers, which can raise the level. Write "voi olla pienempi tai suurempi; ilman ja maan vaimennus pienentää sitä yleensä".
- exercises/exercises.json:105 — fy5-15-L1-08 (1,0 W/m² → 120 dB) is answered word for word in the feedback of L1-06 (exercises.json:60) and in the lesson summary. Use another intensity, e.g. 0,25 W/m² → 114 dB.

## Checked
- Recomputed all 8 new answers in one script: L1-08 120; L2-05 6,025 (steps 6,1/5,8/6,1/6,1); L2-06 3,96; L2-07 mean 4,0 dB → 2,51; L3-04 P = 0,394 W, r = 315 m; L3-05 84,9 dB, 44,6 m. All match answers.py and the solutions.
- L2-06: the reflections explain the direction of the error (measured level above the 1/r² model, gap growing with distance). L2-07: microphone saturation explains the low reading at 90 dB.
- L1-06, L1-07 MC: exactly one correct option, and the distractor feedback is right.
- Assumptions are stated in the task (point source, no reflection or absorption) and do not contradict the later explanations in L3-04 c and L2-06 c.
- Scope: intensity, level, summing intensities, 1/r²; the log-scale reasoning in L3-05 c follows the plan. There are no figures, so no values read from figures and no "graph" kinds.
- fy5-14 and fy5-17: no overlap.; plan 8/7/5 met.
