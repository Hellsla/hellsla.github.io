VERDICT: PASS
CONTENT-HASH: e808871f5f949aef

## Blocking
(none)

## Polish
- lang/en.json:2017 — "does not model the discharge current maintained by the connected voltage source" is dense; "does not model the current a connected source would keep driving through the dielectric" is clearer.
- Two sentences in the readout is more text than Lesson page 4 prefers; accepted as the teacher's request.

## Checked
Full review forced by the sim change; lesson text, inquiry, example stages, figures and exit ticket unchanged since the last PASS (hash differs only by sim.js/lang). New: the model-limitation note shows on its own line under the bold breakdown text only with the source connected (sim.js:82). It is correct for a learner: it says the ideal model fails at breakdown and the sim does not model the sustained discharge current, so a student does not read the readout as real physics. It does not disclose any answer or break an experiment. Deterministic checks (inquiry 116/0, layouts 360/768/1280) pass.
