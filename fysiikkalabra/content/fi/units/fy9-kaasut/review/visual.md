VERDICT: PASS
CONTENT-HASH: 12867208110cf969

Round 2 (delta review of round 1 fixes; round 1 hash 795ad25aae986918)

## Blocking
(none in round 1, none now)

## Verified
I rebuilt with `python3 scripts/build.py fy9-kaasut` and opened the page in Playwright at 390 (2x) and 1280 with every details element open. There were no console errors, no .katex-error, no raw $, and scrollWidth was 390 at 390, so nothing scrolls sideways. I took a capture of each changed figure.
1. rengas: the bar ends now read "331 kPa" and "286 kPa", and the labels clear the frame at 390.
2. s3-graph: a two-slash break mark sits at the bottom of the V axis, and it does not collide with the (0; 37,7) label.
3. s6-vaaka and s6-pysty: the pad is drawn grey and labelled "laikka". In s6-pysty, N comes from the pad side and F_p from the other side, and the drawing makes clear why. Forces are red and acceleration orange, as the convention requires.
4. kartta: at 1280 it is capped at 440 × 682 px. At 390 it is 358 px wide and unchanged.
5. kone heat colour: left as is, which is acceptable. The figure has no acceleration in it, and HEAT is figlib's shared heat colour.
6. The new Finnish text is fluent, with decimal commas and LaTeX units: the S3 d task and solution, the new theory sentences, and the luukku and pallo wording.

## Polish
(none new)

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
