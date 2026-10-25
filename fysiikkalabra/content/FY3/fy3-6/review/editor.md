VERDICT: PASS
CONTENT-HASH: a5d04c8a34f74850

Round 3 re-read after the fixer's changes. The lesson still tells one story: why sand and water heat differently, then Q = cmΔT, then C = cm, then the balance equation and its solution for T as a heat-capacity-weighted mean, then the calorimetric worked example (which the sim defaults reproduce), then the misconception (the 35 °C case rather than 50 °C), then the summary. The exercises (five level-1 tasks on Q, level 2 on mixing, power and rearrangement, level 3 on masses and scale reasoning) and the exit ticket (q3 uses the same weighted-mean idea, 50 °C and 65 °C) follow the same line. The fixer's edits are layout and polish only: the wide displays are split into rows, the paragraph is split, c_metalli replaces c_m, and the weighted-mean sentence is added after the 35 °C working. None of them change the story or the maths. Length is 1057 words without the SVG (986 in round 2), the longest FY3 lesson (others 601–865). The growth is about 70 words from the added intermediate row and the weighted-mean sentence; both serve the multi-term-equation goal, so the length is acceptable. Gold (content/_gold) is a stub of about 113 words and gives no usable length guide.

## Blocking
(none)

## Polish
- lesson.md:87 — The worked example is now two paragraphs of about 100 and 45 words after the displays; the lesson is at its upper length limit. — Do not add more text in later rounds. If trimming is wanted, cut the repeated "luultavasti kuparia" explanation, not the derivation.
- exercises.json:78 — Still no task that determines c from measured calorimeter data (the experimental goal is practised through the example and sim only). — Optional, as in round 2; not needed for PASS.

## Checked
- Lint 0 errors, 0 warnings; check_layout.py fy3-6 OK at 360 px; hash a5d04c8a34f74850 at start and end.
- Goals in meta.json match curriculum.json; each goal has theory, tasks and a sim or exit-ticket check.
- Split displays at lesson.md:33-39, 81-83, 85-89, 94-100 are algebraically unchanged and read in order.
- 35 °C working: 1,0(80 - T) = 3,0(T - 20) gives 140 = 4T, T = 35 °C; matches the weighted mean 140/4.
- Text "Kolmannella rivillä" matches the row where the division by kg and the expansion happen.
- "mitattu 0,1 K pienempi lukema" matches the sim default (24,6 °C for copper) and the 24,5 °C measurement.
- Exit-ticket answers: 4190 / 450 about 9; (3 · 80 + 20) / 4 = 65 °C. Both consistent with the lesson.
- solutions.md additions (ΔT row in L2-02, upper-limit remark in L3-02) agree with answers.py; the numbers are unchanged.
- Scope: no phase changes (fy3-7), no vectors, no E_k; g not used.
