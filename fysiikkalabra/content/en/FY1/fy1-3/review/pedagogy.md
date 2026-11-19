VERDICT: PASS
CONTENT-HASH: 97e76b1902e96d98

## Blocking

## Polish
- inquiry.json `johtopaatos` — `after` lists exp-1 and exp-2 only, but its prompt and criterion 3 need the thermometer data (`data`) — add `data` to `after`, or drop the thermometer from the prompt.
- inquiry.json `simulaatio` `text` — the visible lead is about 48 words; the page rule is at most 30 — cut it to the picture and the sliders ("The ball rolls down the ramp and the hand stopwatch gives a reading each time. Choose the number of repeats and the two errors."); the rest is already in the closed boxes.
- inquiry.json `check-c2` — four checks (concept, resolution, calculation, explain) against the form's three, and the core path keeps 1-2 — mark `check-c2` `optional`, or merge its point (resolution is not uncertainty) into `check-1`. Its correct option is also the longest, a length cue; `karkea` has the same.
- inquiry.json `karkea` — the six readings are the worked example's with 3.31 changed to 4.31, so the student recognises the data rather than reasoning from fresh data — use a different series (a gross error such as 3.52 for 3.25, as in the lesson text, works).
- inquiry.json `siirto` — answer 5.44 g, tolerance 0.02 g: a student who rounds to two figures (5.4 g) falls outside it, against the rule that rounding to the stated figures stays inside — widen to 0.05 or state the figures in the prompt. Also "accuracy" and "resolution" are used as terms but are not in glossary.json; add them with the three terms already pending.

## Checked
- Quoted numbers recomputed from sim.js's fixed series: exp-1 (n=1: 2.18 s, -0.22 s; n=40: mean 2.40 s, half-range 0.26 s; n=5 and 10: 0.25 s), exp-2 (n=40: 2.70 s, +0.30 s), exp-3 (0.0850 s and 0.525 s, ratio 6.2), and the hook's five readings, all match.
- Worked example, gross-error item, coin task, check-2 and exit-ticket arithmetic and rounding are correct (19.09 s; 3.18 ± 0.12 s; 3.8 %; 5.44 g; 2 %).
- Order is hook, retrieval in the same stopwatch situation, two committed predictions with reveal after the experiments (min 3), sim, experiments, data, conclusion, theory, reflect, example, error-spotting, transfer, exercises, checks, exit; no answer is disclosed before commitment.
- Both predictions have wrong options that map to real misconceptions, with feedback that repairs them and cites the experiment; the experiments lock the controlled parameters and vary one.
- The simulation emerges from random readings (not a formula check); model values are labelled as such, and the true time is called known only to the model.
- Scope: relative uncertainty, rounding of the estimate and the reading uncertainty fit "assess reliability" for FY1; workload is one lesson with exp-3 optional.
- Theory: no paragraph over about 120 words, figures follow the paragraphs they explain, and the stages in the worked example are one step each.
- Opening question is answered (mean for random error, reference comparison for systematic error) and the reflect returns to it.
- Exercises were not judged (reviewed apart).
