VERDICT: FAIL
CONTENT-HASH: bd334d98527c8667

## Blocking
- [Major] solutions.md L1-05, L2-02, L2-03, L3-01 force diagrams (`open-exercises-1280-6`, `-L2-1280-3/4`, `-L3-1280-1/2`) — a `voimakuvio` block with only vertical forces (no or narrow horizontal extent) is scaled to the full card width, so a two-arrow diagram is about 1300 px tall at 1280 px, with strokes about 10 px and labels about 70 px; the horizontal diagrams (L1-04, L2-04, L3-03) render at a normal size — this breaks the reading flow of the solution (a whole screen of scrolling per diagram), is inconsistent with the other diagrams and is not print quality — give the generated figure a maximum rendered width/height matching the horizontal diagrams (for example, cap the width by the viewBox, not the card), then re-capture.

## Polish
- [Minor] L3-01 diagram — the orange $\overline{a}$ arrow stands on the floor hatching and its label sits under the floor line, so it reads as part of the ground; place it beside the box above the floor as in L3-03.
- [Minor] L1-02 Järkevyys — "kun tien voima renkaaseen vähennetään vastusvoimilla" is ungrammatical → "kun tien voimasta renkaaseen vähennetään vastusvoimat".
- [Minor] L3-02 Järkevyys — "kiihtyvyys pienenee $2{,}5$-kertaisesti" → "kiihtyvyys on $2{,}5$ kertaa pienempi".
- [Minor] Sijoitus rows (L1-01, L1-03, L3-01, L3-03) — the left side $a$/$m$/$\Delta t$ sits above the axis of the first "=" when the right side is a fraction; align it on the math axis (mathlayout rendering).
- [Minor] L1-05 Järkevyys — "kahdeksan kilon ämpärin" is colloquial in a solution → "$8{,}0\,\text{kg}$:n ämpärin".

## Checked
- contact-5, contact-6 (all exercise captures #51–#69)
- `open-exercises-1280-6` (L1-05 diagram at full size), contact views of `-1280-1…5,7` (L1-01…L1-04 incl. L1-04 diagram)
- `open-exercises-L2-1280-4` (L2-03 diagram, a/v arrows, $T$ longer than $G$), contact views of L2 1…7 (L2-02 and L2-04 diagrams)
- `open-exercises-L3-1280-1/2/4` (L3-01 diagram, Sijoitus layout, L3-02 task, L3-03 diagram), contact views of L3 3, 5
- source scan of exercises.json and solutions.md prose for plain number+unit: none found
- "Kirjoita ratkaisu" buttons present on every task (project decision, not judged)

## Scores
illustrations 3 · typography 4 · Finnish 4 · accessibility 3
