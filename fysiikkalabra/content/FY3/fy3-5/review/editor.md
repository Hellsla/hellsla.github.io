VERDICT: FAIL
CONTENT-HASH: 4fa8c934b1046f3e

The lesson tells one story: the pump question opens it, the theory separates temperature, internal energy and heat, ΔU = Q + W appears once with a clear sign diagram, and the example and misconception section both return to the pump. It builds on fy3-2 and fy3-3, leaves cmΔT and calorimetry to fy3-6, and keeps to the first law. Length and structure match fy3-2 and fy3-3. Two problems remain: L3-03 repeats a level-2 task, and one exit-ticket answer breaks the system boundary it sets up.

## Blocking
- exercises.json:98 — L3-03 is L2-03 (exercises.json:64) again: a gas expands and does work, ΔU < 0 is given, find Q > 0. It does not even have the kJ conversion, so it is not a level-3 task. — Replace it with a real level-3 first-law task without cmΔT. Example: a cycle back to the initial state, so ΔU = 0 and net Q = −net W, with W from Fs or Pt.
- exit-ticket.json:11–12 — The question makes the flask's contents the system. The answer then sends energy from the coffee to "pullon kylmempiin seiniin", which are outside that system, so the contents' U would fall. — Make the system "pullo ja sen sisältö", or keep the transfer inside the contents (coffee to cold milk).

## Polish
- lesson.md:43 / exercises.json:82 — The example's closing remark (slow compression, Q = −W, ΔU = 0) gives away the reasoning of L3-01. Shorten it to a hint.
- lesson.md:17 — "edellisellä oppitunnilla": the previous lesson is fy3-4. Work was in fy3-2. Write "aiemmin".
- lesson.md:10 — "eristetty systeemi" is not in glossary.json or meta.glossary. Add it.

## Checked
- lint_lesson.py: 0 errors, 0 warnings
- All goals and the MAOL first-law clarification are covered
- ΔU = Q + W signs are consistent in the lesson, SVG, example, exercises and exit ticket
- All 12 answers recomputed and matching
- P = W/t and W = mgh come from fy3-2, so they are in scope
- No overlap with fy3-6 (cmΔT, calorimetry)
- Levels 5/4/3; the worked example is not repeated
- lesson.md has 675 words (fy3-2: 703, fy3-3: 829), with the same sections
- The meta glossary terms exist in glossary.json
- sim: false, so there is no sim-spec to check
