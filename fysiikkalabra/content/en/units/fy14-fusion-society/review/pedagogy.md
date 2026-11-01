VERDICT: PASS
CONTENT-HASH: f86c35be7cb1d95d

Pedagogy review of fy14-fusion-society (2026-11-01). The page was built with `python3 scripts/build.py fy14-fusion-society`, served on port 8775 and tested in Playwright at 390 px.

## Blocking
None.

## Polish
1. `inquiry.json`, option lengths: the correct option is the longest in 5 of 9 choices: `pred-fuel` (35 against 34), `pred-waste` (55 against 54), `check-1` (69 against 64), `check-3` (70 against 62) and `find-error` (76 against 57–61, about 30 % above the others). Shorten `find-error` to "The 2.05 MJ was laser light, made with about 300 MJ." and `check-3` to "Wrong: neutrons activate the machine (short-lived waste)." Or lengthen one distractor in each.
2. `pred-waste`: *Inside ITER* (chapter 7, listed in `prior`) already says that neutrons make the vessel radioactive and that there is no long-lived high-level waste from the fuel. So for students who did that unit, this is retrieval rather than prediction. It is acceptable because the misconception "no radioactive waste" persists. To be honest about it, add "Remember *Inside ITER*, or reason from the neutron:" to the prompt.
3. `back-to-predictions` asks for one or two sentences but gives no sentence starters, unlike the unit's other writing tasks. Add two starters: "Fusion fuel is attractive because …"; "Tritium is a problem because …".
4. `teacher.md`, timing: there are two written pair tasks plus the sort in 28 minutes, and four tasks in the last 11 minutes. This works only with the plan for running out of time. State in the timing line itself that check 4 is usually homework.

## Checked
- The predictions are not answered before they are asked. The hook, the Why line and the hero (no text; its aria-label gives no amounts) do not answer them. Nothing in Energy, Claims, Uncertain or the sort gives 0.21 mg or activation.
- In the browser, both predictions lock on *Answer* with no feedback, and the pending text says "read the theory section". Feedback stays hidden through Energy, the table and the sort. It opens with the committed option's own feedback when *theory-main* comes on screen. The reflection lists both predictions.
- The model answers stay closed with an empty answer and with 5 characters. In all four explain tasks they open only after an answer of the student's own.
- CLIL: there is a word bank and sentence starters for every pair and writing task (hook, grid, sort, headline). There are pair discussions, a source table, a vocabulary match and a French corner with Finnish comparisons. The English is B1–B2.
- The balanced evaluation (result, plan or claim; dated; 9 statements) meets the brief and prepares the debate. The feedback repairs the misconceptions: Q versus electricity, "clean", and a survey as a result.
- Workload: one lesson, with optional NIF and plans for fast pairs and for running out of time. There are no console errors, no raw `$` and no horizontal scroll at 390 px.

## Shared issues
- `templates/inquiry.js`, theory reveal: a prediction opens when the first pixel of its theory section is on screen. The *theory-main* section is 2704 px tall, so at 390 px the feedback opens while the student is still at `sort-explain`, before Fuel and Compare have been read. Proposed fix: require, for example, 30 % of the section, or its first heading, to be visible.
- The reflection says "the data does not support your prediction" for theory-revealed predictions. This is already noted for the pilots.
