VERDICT: FAIL
CONTENT-HASH: b84833cced408b83

## Blocking
- exercises.json:309 and solutions.md:184 (fy8-2-L2-08, option A) — **A**. The text says "Tämä on emissiospektri, jonka kuuma kaasu lähettää itse". A hot gas of this atom also emits the 4→2 line at 653 nm (1,90 eV), which is in the visible range. Its emission spectrum would therefore show three bright lines, not the two drawn in figure A. The lesson's own Tiivistelmä also says that the absorption lines are only *osa emissioviivoista*. — Fix: write "Kirkkaat viivat mustalla pohjalla ovat emissiospektri, eli kaasun itse lähettämää valoa, eivät sen läpi kulkenutta valoa." Then either drop "kuuma" or add that a hot gas would also show 653 nm.

## Polish
- solutions.md:174–182 — at 390 px the λ lines (`λ12 = 1240 eV nm : 2,50 eV ≈ 496 nm` and the two like it) are clipped at the right edge, so the unit "nm" is cut off. The `E_y − E_a` chains also reach the edge. — Split each chain after the "=" or the ":".

## Checked
- I recomputed in one script: transitions from the ground state give 496,0, 413,3 and 281,8 nm (UV), and 2→4 gives 652,6 nm. 3→4 (886 nm) and 2→3 (2480 nm) are infrared ✓. Answer C (two dark lines at 413 and 496 nm) is the only correct option ✓.
- Distractor B (adds an absorption from an excited state) and distractor D (the lesson's "riittävä energia absorboituu" error, dark from 380 to 496 nm) are both really wrong, and their feedback is right. figures.py draws the four options to scale at the stated wavelengths, and the descriptions are complete ✓.
- The condition is stated in the task (room temperature, so almost every atom is in the ground state) ✓. The task is within the scope of the chapter.
- Render: preview/fy8-2.html at 390 px, with every option's feedback and the solution opened. There is no page overflow; the clipping is noted above.
- The hash is the same at the start and the end.
