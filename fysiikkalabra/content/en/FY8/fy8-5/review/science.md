VERDICT: PASS
CONTENT-HASH: ade0d0acde13088d

## Blocking

## Polish
- assets/sims/fy8/fy8-5/sim.js:195,200,265 — on the English page the canvas still draws Finnish labels and a Finnish decimal comma: "1s-orbitaali", the scale bar "0,1 nm" and the axis label "osumia" (seen in review/shots/fy8-5-sim-1280.png). The numbers are right, but the comma breaks the page's decimal convention. — Route these labels through `__()` (lang/en.json sims/fy8-5) and the scale bar through `tx()`.

## Checked
- A script compared lesson.md and inquiry.json with content/fi/FY8/fy8-5 line by line and key by key. Every number, every $…$ formula, every `correct` flag, the numeric `answer`, `tolerance` and `mistakes` values, `initial`, `reveal.min` and the `optional` flags are identical; the only change is the decimal sign. The one figure-label change is solmu → node.
- Read the prose against the source sentence by sentence. Every condition is kept: "in the hydrogen atom" on more nodes, higher energy (Key idea, Summary, check 2), "states of the same shape" for many-electron atoms, "approximately" in P ≈ k/N, "on average every tenth", "expected value", and "in a real experiment … not measured as directly".
- Figure captions (figures.json, aria-labels) keep "not to scale" and "to scale" as in the source, along with "see-through projection", 0.14 nm, −13.6, −3.40 and −1.51 eV, and 656 nm.
- lang/en.json sims/fy8-5 readout and legend are a faithful translation of lang/fi.json.
- Recomputed in one script: 656.47 nm (3d→2p), 10.2 eV (2p→1s), 2700 hits, 1s R50 0.0707 nm and R90 0.1408 nm, matching the text.
- Every choice item (review, predictions 1–2, Find the error, checks 1–2) has exactly one correct option, and the distractor feedback is correct physics in English. The exit ticket for N is 1s² 2s² 2p³.
- Terminology is correct: antinode/node, nodal sphere and nodal plane, principal quantum number, subshell, Pauli exclusion principle, ground state, valence electrons.
