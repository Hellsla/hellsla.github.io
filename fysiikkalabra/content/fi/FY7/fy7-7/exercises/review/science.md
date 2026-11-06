VERDICT: PASS
CONTENT-HASH: 08148d6414cd1c3b
ROUND: 2

## Blocking

## Polish
- solutions.md:215 (L1-09) — round-1 item still open: "kahden peräkkäisen samaan suuntaan tapahtuvan nollakohdan välistä" → "kahden peräkkäisen nollakohdan välistä, joissa käyrä on nousemassa".

## Checked
- 202302c75 changes only the option figures' layout: height 380 → 406, the plot moved down 26 px, and a −10 tick and label added by hand at ax.Y(−10). The curve function, peaks (5,0 / 7,1 V), periods (25 / 40 ms) and axis ranges are unchanged, so the physics of every option is unchanged.
- Catalog descriptions are unchanged apart from the size; they still match the curves. The "lukuarvot kahden voltin välein" wording is now true at −10 too.
- Recomputed again: e₀ = 5,0 V · √2 = 7,07 V, T = 25 ms; only B is right, and the 2 × 2 options hide the answer's form.
- Checked from figures.py and the diff, not from renders.
- answers.py runs with -I; nothing changed in exercises.json or solutions.md.
- Hash 08148d6414cd1c3b at start and end.
