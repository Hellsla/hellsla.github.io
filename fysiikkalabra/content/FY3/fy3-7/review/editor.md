VERDICT: PASS
CONTENT-HASH: a60972b7e5883f38

Lint reports 0 errors and 0 warnings. The lesson delivers all three goals. The mikromalli is in the core idea (lesson.md:6-8) and is tested by exit-ticket q1. The ominaishöyrystymislämpö measurement with an immersion heater on a balance is the worked example (lesson.md:51-57), and L3-03 extends it with the two-power method. The phase change itself is covered by the plateau argument, the s and r formulas, the constants table and the (Q,T) curve, which is drawn to scale. Length is 875 words, in line with the other FY3 lessons (660-1190). Theory, example, exercises, exit ticket and sim tell one story: temperature is constant while energy breaks the bonds, and the plateau lasts sm/P or rm/P. Nothing is redundant. The example (one run, a loss argument) and L3-03 (two runs, the loss cancels) do not repeat each other. Round 1's polish is in. No blocking issues.

## Blocking
(none)

## Polish
1. lesson.md:14-19 — the page puts the sim after "Kaava", but the text never mentions it, so the student does not know what to try — add one sentence after the formula, e.g. "Kokeile simulaatiolla: muuta tehoa ja huomaa, että tasanteiden kesto muuttuu mutta niiden lämpötila ei."
2. lesson.md:12 — "faasikaavio" is a glossary term, a goal-adjacent term and a summary bullet, but there is no figure or worked reading of one, so it stays a statement — optional: a small p–T diagram with the triple point, or one L2 reading task. Not required by the LOPS wording, so not blocking (the fixer already declined it on scope).
3. exercises.json L1-05 — a level-1 task that asks for both an explanation and a graph reading (a difference of two readings) is closer to level 2 — optional: split it so the level-1 part is only the subtraction, or keep it as the bridge to the curve.
4. exit-ticket.json q2 — near-duplicate of the lesson's misconception sentence (lesson.md:8), so it tests recall — optional: ask what happens at P = 3000 W compared with 1000 W (the boiling takes a third of the time, T stays 100 °C), which also echoes the sim.

## Checked
- Goals 1-3 against lesson.md, example, L3-03 and exit ticket: all covered.
- Numbers: 2260/334 = 6,8 ("lähes seitsemän"); 2260/419 = 5,4 ("yli viisi"); 334/4,19 = 80 K (misconception).
- Example: 300 kJ / 0,128 kg = 2,34 MJ/kg, 3,7 % above the table value ("muutaman prosentin").
- L3-03: loss about 60 W; single runs give 2,45 and 2,67 MJ/kg; difference method gives 2,26 MJ/kg.
- L1-05: 186 − 19 = 167 kJ, m = 0,50 kg, and 2100 · 0,50 · 18 = 18,9 kJ, consistent with the curve.
- L3-01 and L3-02 solutions: all ice melts (36,7 kJ > 20,0 kJ); stones cool by 27 K.
- SVG plateau widths 52 : 351 follow s : r; the steeper ice and steam segments match the lower c.
- Sim spec, sim.js constants, table values and solutions use the same s, r and c values.
- Levels have 5/4/3 tasks; the exit ticket has 3 questions; the glossary terms are used in the text.
- Scope: no E_k or vectors, FY3 only. The sim is on the page after "Kaava", as NOTES says.
