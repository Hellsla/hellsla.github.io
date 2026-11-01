VERDICT: FAIL
CONTENT-HASH: d34eff70d761834f

Pedagogy review of fy14-fr-nombres (2026-11-01), against the pilot fy14-fr-bonjour. Built with `python3 scripts/build.py fy14-fr-nombres` and tested in Playwright at 390 px over HTTP.

## Blocking
1. **The pair listening is reading, not listening.** This is `pairs-listen` in inquiry.json. Each partner uses their own device, and B's price list (`fx-match-heardB`) sits directly under table A (`fx-say-pricesA`). Table A shows every French line and its respelling, for example *Un café, c'est un euro quatre-vingts* with *ka-trö-VẼ*. So B reads the answer on their own screen, and A does the same in round 2. teacher.md calls this task "the core of the lesson", and the page defeats it.
   **Fix:** put each table where the listener cannot see it. Wrap each `say` table in a closed box headed "Partner A only (B keeps this closed)", or make it a separately folded activity (`fold`). Change the instruction to say that the listener keeps the other table closed.
2. **The feedback shows wrong arithmetic.** Eight feedback strings have broken `$…$`, so the page shows text such as "Quatre-vingt ( 4⋅4⋅20 = 80$$)" and "80 + 80+1 = 81$$". This is the feedback that should repair the 70–99 misconception.
   - Where: `match-numbers` (84, 81), `pairs-listen` (A3, A4, B2, B3) and `gapfill` (95, 90).
   - **Fix:** write each one as a single formula, for example `$4 \cdot 20 = 80$`, `$80 + 1 = 81$`, `$95 = 4 \cdot 20 + 15$`.

## Polish
3. Line B5 in table B (*quatre-vingt-quatre euros*) has no row in `fx-match-heardA`. Either add the row (84 €) or remove the line.
4. In `notice`, the correct option is the longest: 42 characters against 29–36. Shorten it, for example "Four twenties plus 10 to 19", or lengthen a distractor.

## Checked
- **Progression:**
  - The unit builds on the pilot: polite *vous*, the same respelling style, the same ITER scenario.
  - It feeds the café unit.
  - The market role-play has a real information gap, because the seller's prices are on paper.
- **Predictions:**
  - Neither the hook, the Why line nor the hero gives away either prediction.
  - Both lock on commit with no feedback.
  - Both stay closed through Investigate and open with their own theory section: `theory-count` and `theory-prices`.
- **Model answers:** all three `explain` tasks stay closed when the box is empty and with 3 characters, and open after a real answer.
- **Option lengths:** balanced elsewhere.
- **Distractors:** they target real misconceptions (*septante*, *sept-dix*, *virgule*, 87 for 97).
- **Timing and support:**
  - The 75-minute timing adds up.
  - teacher.md has a fast-pair plan, a plan for running out of time, and asks the teacher to check the videos first.
  - Word bank and sentence starters are given where they are needed.
  - The theory is about 520 words, close to the pilot.
- No console errors, no `.katex-error`.

## Shared issues
- None new. The `say` component cannot hide the French text, for example for a listening task. A `hide_fr` option would help listening tasks, but it is not needed for this unit's fix.
