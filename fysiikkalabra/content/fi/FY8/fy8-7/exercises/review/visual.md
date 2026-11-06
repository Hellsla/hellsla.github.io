VERDICT: FAIL
CONTENT-HASH: 550d4a2308e6dc21
Round: 1 (delta)

## Blocking
- [Major] solutions.md fy8-7-L1-09 Mallivastaus — two calculation lines are wider than the phone column at 390 px (render: `hc = 6,626 · 10^-34 J s · 2,998 · 10^8 m/s = 1,9865 · 10^-25 J m` is 508 px in a 304 px column, `hf = (1,9865 · 10^-25 J m)/(650 · 10^-9 m) = 3,056 · 10^-19 J` is 360 px); the right end is cut off and only reachable by scrolling — the result cannot be read in one view, and the chain rule is about 300 px — fix: split each line at the equals sign (`hc = 6,626 … · 2,998 … m/s` on one line, `hc = 1,9865 · 10^-25 J m` on the next; `hf = \dfrac{…}{…}` and `hf = 3,056 · 10^-19 J` on separate lines).

## Polish
- [Minor] exercises.json L1-09 — the only hedged statement ("vahvistuu lähinnä") is a true one; a guesser can use the form. Add a hedge to a false one or drop it.
- [Minor] exercises.json L1-09 statement feedbacks — judged from text only (they are hidden in the render until opened); fine, each short and in the chapter's own warned-mistake pattern.

## Checked
- Own 390 px render (scratch script) of 7-9: the five statements answered, solution open; overflow measured per KaTeX element (two kx-wide lines above, nothing else, no page-level horizontal scroll).
- Text only: the diff (L1-09 statements, L3-01/L3-02 paragraph splits), Finnish and the numbers; the L3 splits read well and need no capture.
- Not opened: other exercise captures (unchanged layout).

## Scores
illustrations n/a (5) · typography 3 · Finnish 5 · accessibility 4
