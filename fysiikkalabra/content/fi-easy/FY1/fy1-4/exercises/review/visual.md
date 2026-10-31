VERDICT: FAIL
CONTENT-HASH: fdb7c84f91dfb89b

## Blocking
- [Critical] exercises.json fy1-4-L2-03 (open-exercises-L2-1280-3) — the litre is written `\text{l}`, which renders as the digit 1: the task reads "(3,01; 3,9 kg) ja (9,01; 9,9 kg)" — the given volumes read as 3,01 and 9,01 and the unit is lost — write `\textsf{l}` (as solutions.md already does; lint error per NOTES §1).

## Polish
- [Minor] L2-02 (open-exercises-L2-1280-2) — the inline value "$t = 8{,}0\,\text{s}$" ends the line and the full stop starts the next one; reword so the sentence does not end in maths, or bind the period.
- [Minor] L2-02 solution — "3,6 . . . 4,2 m" shows spaced dots; use "3,6–4,2 m" or `\ldots` without spaces.
- [Minor] L2-02 Sijoitus — "6,0 s − 0 s" mixes precision with the Annettu line; write 0,0 s.
- [Minor] figure fy1-4/scatter-points (L2-02) — y axis tick labels at 1–4 but gridlines every 0,5 m with no labels; fine for reading, but the 0,5 m step is only in the description.

## Checked
- open-exercises-1280-1 (L1-01), open-exercises-L2-1280-1, -2, -3 (L2-01 to L2-03, scatter-points figure), open-exercises-L3-1280-1 (L3-01).
- Remaining exercises read from exercises.json source; their solution layout matches the opened ones.

## Scores
illustrations 4 · typography 2 · Finnish 4 · accessibility 4
