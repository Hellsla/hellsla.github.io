VERDICT: PASS
CONTENT-HASH: d1b8cf415123c2e3

## Blocking
(none)

## Polish
- inquiry.json ennuste-1 / koe-1 — the earlier Polish items on the prediction wording (what is predicted versus what the sim returns) and on koe-1 asking for the loss share instead of the efficiency were not part of this diff and still stand; both are minor.
- inquiry.json ennuste-2 / koe-2 feedback — the "simulaatio vain toistaa oletuksen" meta-talk noted before still stands; shorten when next edited.
- lesson.md:126 — the long paragraph noted before still stands (split off the heater example).

## Checked
- ennuste-1 prompt: the hint that nearly gave the answer is gone; the prompt now asks the question only, so the student commits before the evidence. Resolves the earlier Polish item.
- koe-2 prompt: the P_a : P_o = 5 % value is no longer given. The student reads P_a from the readout (the howto names it) and computes both ratios from at least two table rows, so the observation ("the ratios are the same") comes from the student's own calculation. The correct option names 5 %, which the student now derives; no premature disclosure.
- ennuste-2 and koe-2 are now core (not optional): the experiment varies only t with laite and P_o locked and records E_o and E_a with min 3, so it can refute a prediction such as "energy efficiency grows with time". This is a model-value lookup by design, stated in the lesson.
- Workload: 2 predictions, 2 short experiments, 2 checks, the third check and the reflection still optional. Still about one lesson hour.
- ennuste-1 no longer optional wording elsewhere: the earlier "optional: true" removal from the misconception option (the lamp that warms up over time) concerns the options list, not the activity; the feedback there still repairs the misconception.
- The rest of the lesson is unchanged from the version I passed; the deterministic checks are green (inquiry 114 passed, layout at four widths).
- Not opened: captures (no layout-relevant change in the diff).
