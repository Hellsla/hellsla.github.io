VERDICT: PASS
CONTENT-HASH: 8b7fc3f905554b7f

## Blocking
(none)

## Polish
- inquiry.json ennuste-1 / koe-1 — the prediction asks about a real engine, but the sim only returns the 25 % it was given, so the experiment can refute the guess only as a data lookup. The lesson says so openly ("simulaation mallin arvo"), so it is not blocking. Fix: call koe-1 an "arvojen luku" task, or add one line to the prediction ("mallin tyypillinen arvo") so that the student predicts the same thing the table shows.
- inquiry.json ennuste-1 prompt — the hint ("muista Pohdinnan kuuma hehkulamppu. Kuumenevatko moottori ja pakoputki?") nearly gives the answer before the student commits. Fix: drop the second question and leave "muista Pohdinnan lamppu".
- inquiry.json koe-1 question — it asks for the loss share (75 %), while the prediction and the lesson goal are the efficiency; the student needs an extra step (100 % - 75 %). Fix: ask for E_a : E_o, or ask for both.
- lesson.md:126 — the paragraph "Hyötysuhde on hyötyenergian osuus..." runs to about 150 words and holds four ideas (the 100 % limit, the real-device loss, motor and lamp, heater). Split it so that the heater, with its example, gets its own paragraph, as CLAUDE.md allows about 120 words at most. The sentence "Kun laitteen hyöty on muuta kuin lämpöä, hyötysuhde vaihtelee paljon: sähkömoottori ..." is followed by a table that includes the kettle, whose benefit is heat. Reword to "Hyötysuhde vaihtelee laitteen mukaan".
- inquiry.json ennuste-2 / koe-2 are optional and their model repeats the arithmetic by design; fine as secondary, but the feedback sentences about "simulaatio vain toistaa oletuksen" are meta-talk for a 16-year-old. Shorten them.

## Checked
- Learning path: the prerequisite (E = Pt) is retrieved with misconception-based distractors; the slot's goal (η = E_a/E_o = P_a/P_o) is met and nothing from FY3 appears (no chain of efficiencies, no heat engine).
- The opening question (where does the lamp's energy go, how to measure goodness) is answered by the Sankey figure, the table and the reflection, and the answer is not given before the student commits.
- The predictions have feedback that repairs the misconception, not just the answer; the 120 % pysahdy item and the heater-versus-lamp item address the real misconceptions (loss = lost energy, power = efficiency).
- Worked example: seven stages, one step each, the principle explained, conversions and a check shown; it does not repeat the exercise or the transfer task.
- Etsi virhe and the transfer task (solar panel) have three hints and mistake feedback that names the slip; the solutions follow the seven-part form.
- The explain criteria are observable and match the prompt. The exit ticket tests the core idea, including the power-versus-efficiency misconception.
- Workload: one hour (2 predictions, 1 required experiment, 3 checks, the core path marked optional).
- Figures: the three figures are placed right after the paragraphs they explain (their descriptions give the data without the answer), and the captions and descriptions are legible; the pair figure shows the same data as the text.
- Finnish: terms agree with the glossary; the case after number+unit is correct.
- Not opened: captures (phone and wide), because the deterministic layout checks pass at all four widths.
