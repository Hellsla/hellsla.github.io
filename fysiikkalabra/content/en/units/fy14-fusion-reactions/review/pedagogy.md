VERDICT: PASS
CONTENT-HASH: c24379ba79d6f049

Pedagogy review of fy14-fusion-reactions (2026-11-01). Page built with `python3 scripts/build.py fy14-fusion-reactions` and tested in Playwright at 390 px. `check_layout.py --width 360` is all OK, and there are no console errors and no raw `$`.

## Blocking
None.

## Polish
1. Workload. The theory is about 815 words: Chain, Key idea and Formula in *Theory summary*, plus the 343-word *Fusion in the laboratory* (`theory-lab`). There are three extended writing tasks: `reaction-describe`, `lab-vs-sun` (five or six sentences) and `check-explain`. The 18 minutes of *Apply* in `teacher.md` also have to hold:
   - the worked example;
   - reading `theory-lab`;
   - the pair paragraph;
   - the scales chart;
   - the coal task.
   This is closer to 90 minutes than 75. Fixes:
   - cut the first paragraph of `unit.md` § *Fusion in the laboratory* (it repeats the Oliphant source the students have just analysed);
   - mark `scales-text` + `coal-equivalent` `"optional": true`, or shorten `lab-vs-sun` to three or four sentences.
2. `inquiry.json` `reaction-text`: "Test predictions 1 and 2". The reaction diagram tests prediction 2 (the energy share), but it mentions tunnelling only in a bracket in step 2, and the bracket speaks of a 100-million-kelvin plasma, not the Sun. Write "Test prediction 2" (`pred-barrier` is then answered by `theory-key`, as the design allows), or add a question that asks how the nuclei can get close at all.
3. The energy share is calculated four times: in the reaction diagram's open box, in § Formula, in the worked example and in `check-1`. The worked example adds nothing new. Use it instead for the neutron's speed (now an extension idea in `teacher.md`), or for D–D, or say in its first line that it repeats the diagram's calculation step by step.
4. `teacher.md`, Extension ideas: "look at the reaction *Tritium breeding* in the Binding Energy Explorer of the previous chapter". That unit limits the explorer to `dt`, `dd-he3` and `u235`, so the reaction is not there. Reword the extension, or ask the binding-energy unit to add `li6`.
5. `inquiry.json` `scales-text`: the activity title "Energy scales: chemical and nuclear fuels" is repeated straight away by the component's own heading. The component also prints "about 4.10 times as much as the fission of uranium-235", which answers half of its own Think question. Drop the activity title, and ask only for coal in the question (the numeric task follows).

## Shared issues
- `assets/units/fy14/fx/reaction.js`, step 2: "only very fast nuclei in a plasma of over 100 million kelvin get close enough (helped by quantum tunnelling)". This understates the main idea of chapter 3: in the Sun and in reactors almost all fusions happen *by* tunnelling, below the top of the barrier (this unit's own misconception section). Suggested wording: "… only the fastest nuclei get close enough, and they fuse by tunnelling through the top of the barrier."
- `reaction.js` (scales part): the heading duplicates any activity title (see Polish 5).

## Checked
- Predictions:
  - `pred-barrier`, `pred-share` and `pred-pp` lock on commit with no feedback.
  - They open with `theory-key`, `theory-formula` and `theory-chain`.
  - Nothing before them gives the answers: the hook, the Why line, the hero, the review feedback and the prior list. The prior list names tunnelling, which is fair prior knowledge.
- The model answers of the three explain tasks stay closed until the student writes.
- The worked example is staged.
- The Oliphant source task is genuine evidence-reading, with good distractors (net gain, proton beams).
- Word bank and sentence starters at every writing task.
- The French corner is fine.
- `teacher.md` has plans for fast pairs and for running out of time.
