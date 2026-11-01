VERDICT: PASS
CONTENT-HASH: af00c5738a515fa3

Pedagogy re-review of fy14-fusion-reactions (2026-11-01), after the "Fixes after review" in review/developer.md (commit 7843fefa). Page rebuilt and tested in Playwright at 390 px. `check_layout.py --width 360` is all OK, and there are no console errors, no raw `$` and no `.katex-error`.

## Earlier findings: all resolved
- Polish 1, workload. The lesson now fits 75 minutes:
  - The *Fusion in the laboratory* section is cut to about 220 words.
  - `scales-text` and `coal-equivalent` are optional.
  - `lab-vs-sun` asks for three or four sentences.
  - The *Apply* plan in `teacher.md` holds a short worked example, the reading and one pair paragraph.
  - The plans for fast pairs and for running out of time are updated.
- Polish 2: the reaction diagram now has a tunnelling step. It has the barrier top at $r \approx 3\ \text{fm}$, D–T likely near $0.1\ \text{MeV}$, and the fastest nuclei fusing. So "Test predictions 1 and 2" is now true, and `pred-barrier` has evidence before its theory reveal.
- Polish 3: the worked example says in its first line that it repeats the diagram's calculation step by step.
- Polish 4: the tritium-breeding extension works, because the binding-energy explorer now lists `li6`.
- Polish 5: the scales activity has no duplicate title, and its question asks only for coal.
- Shared issue (`reaction.js` step 2): resolved by the new tunnelling step.

## Polish (not blocking)
1. `inquiry.json` `lab-vs-sun` prompt: "write three or four sentences of your own that answers" should be "that answer".
2. The theory is still about 735 words, counting *Theory summary* and `theory-lab`. This is acceptable now that the optional tasks carry the extras. If time is still short in class, the 230-word *Key idea* is the place to trim: the tunnelling sentence there and the diagram's tunnelling step say the same thing.

## Checked again
- Predictions:
  - `pred-barrier`, `pred-share` and `pred-pp` lock on commit with no feedback.
  - They open with `theory-key`, `theory-formula` and `theory-chain`.
  - Nothing before them gives an answer.
- The model answers of the three explain tasks stay closed until the student writes something.
- Word bank and sentence starters at every writing task.
- The French corner is unchanged.
