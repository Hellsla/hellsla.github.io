VERDICT: DONE

Fix, round 1. `check_lesson.py fy8-5`: every line ok.

- `lesson.md`: Blocking: "more nodes, higher energy" is now stated for hydrogen (and for states of the same shape in other atoms), in Ydinajatus and Tiivistelmä; for the string, a node raises the frequency. Added why there are 1, 3, 5 and 7 orbitals (three p directions; the figures show one 2p) and what spin is. Split the two long paragraphs. Esimerkki: $1{,}98647$, $656{,}47\,\text{nm}$ in the chain, and a note on the intermediate digits.
- `figures.py` (regenerated): string aria says "taajuus"; nodes aria says it shows one of three 2p orbitals; cloud aria explains the see-through view, plus a "läpivalaisu" label; levels note beside the 1s box; larger hero cloud and lobes.
- `inquiry.json`: hook without 90 %; ennuste-1 asks how the share varies at 10 and 1000 measurements; ennuste-2 prompt without 0,053 nm; tarkistus-2 feedback (hydrogen, the string's frequency); tarkistus-3 "noin 3–6-kertainen"; sim model box mentions the 2s gap.
- `sim.js`: draws the 2s gap and adds `simState.gap`; `tests/sims/fy8-5.json`: two assertions; `lang/fi.json`: readout formulas grouped so they do not wrap.
- `lesson-answers.py`: keys renamed to tarkistus-3; new numbers added. `solutions.md` L1-01: no g subshell.
