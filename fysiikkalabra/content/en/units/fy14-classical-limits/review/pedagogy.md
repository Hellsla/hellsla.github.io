VERDICT: PASS
CONTENT-HASH: 9f4b777715798bfc

Pedagogy review of fy14-classical-limits (2026-11-01). Read unit.md, inquiry.json, teacher.md, developer.md and the hero and Predict captures. Page rebuilt with `python3 scripts/build.py fy14-classical-limits` and tested in Playwright at 390 px.

Browser check: both predictions lock on commit and show no feedback. `pred-peak` opens only when *Key idea* comes into view, after the curves, the peak table and `curves-talk`. `pred-share` opens when *The ultraviolet catastrophe* comes into view. The three model answers stay closed until the student has written something. There are no console errors and no `.katex-error`.

The learning path is sound. The page goes from the glow of everyday things to the black-body curves, a pattern the student finds in a table (λT is constant), the classical prediction and how it fails, and Planck's packets. CLIL support is strong: a word bank and sentence starters for every speaking and writing task, a pair talk, a biography speaking task, and a French corner with `say`. The selita sections run to about 440 words.

## Blocking
None.

## Polish
1. `inquiry.json` `pred-share`, third option ("The power falls to zero, as for a real hot object."): before the student has seen the curves, it says what real hot objects do at short wavelengths. Fix: use "The power falls to zero at short wavelengths." and move "as for a real hot object" into its feedback.
2. `inquiry.json` `pred-share` prompt: it gives the whole chain of reasoning (more patterns, the same share each), so the prediction comes close to recall. This is acceptable as a "follow the model" prediction. Fix: cut "and the shorter the wavelength, the more wave patterns fit into the oven" and ask the student to justify the choice.
3. `inquiry.json` `pred-peak`: it uses **black body** and "radiates most strongly" before *Reading the curves* defines them. Fix: add a short gloss to the prompt, such as "(an ideal glowing object)".
4. `inquiry.json` `hook-talk` says "Write down your ideas: you will come back to them", but nothing comes back to them. Fix: add one line to `back-to-predictions`: "Look at the glowing things you named at the start: which was the hottest?"
5. Workload: teacher.md packs the worked example, the camera task, timeline exploration, the ordering task, the one-minute biography talk and the writing into 40–60 min. That is tight. Fix: say in teacher.md that the written half of `people-task` is the first thing to set as homework, as the short-of-time plan already suggests.
6. Option lengths: in `check-1`, `check-3` and `pred-share` the correct option is the longest, though only by 1–2 characters. Fix: shorten the correct option of `check-3`, for example "Short waves need big packets, which heat rarely gives."

## Shared issues
- `templates/inquiry.js` §1: a theory-linked prediction is revealed as soon as any pixel of its section enters the viewport, whether or not it has been read. This unit works around it by pointing each reveal at the explanation after the evidence, so it does not block. Proposed fix: a threshold of about 40 % of the section, or start counting only after the commit (developer.md Shared issues 4).
