VERDICT: FAIL
CONTENT-HASH: e6cae411717aad88

## Blocking
- [Major] inquiry.json (koe-1, koe-2 `names`; captures stage-tutki-390, lab-1280, exp-koe-*) — the experiment panels show Finnish words in the English page: "Initial state: alkupaikka = 0 m, nopeus = 2 m/s, hetki = 0 s. Kept constant: alkupaikka, nopeus. Varied: hetki", the table column is headed "hetki", and the locked sliders carry the suffix "(vakio)" — the student cannot read the set-up line or the table header — give `names` English words (initial position, speed, moment) and make the locked-slider suffix language-aware (templates/site.css `label.locked::after`, ask the teacher/template owner).
- [Major] lesson.md, "Linear model" — "The model is still good when the speed changes little compared with the time being considered" compares a speed with a time, which is meaningless — it is the one sentence that states when the model may be used — "…when the speed changes little during the time being considered (here, a few years)."
- [Major] lesson.md, "Direct proportionality" — "the distance travelled $s$ and the time $t$ are directly proportional" uses $s$ for distance, whereas the Formula section defines $s$ as position and the chapter's whole point is position vs distance $\Delta s$ — notation clash in the paragraph on proportionality — write "the distance travelled $\Delta s = s$ when $s_0 = 0$" or use $\Delta s$ and "the ratio $\Delta s : t$".

## Polish
- [Minor] Worked example step 3 — headed "Rearranged formula" but shows $s = s_0 + vt$ unchanged — "Formula".
- [Minor] Worked example "Reasonableness" — the 0.2 AU gravity/initial-distance explanation is stated twice and the final "So the model is accurate to a fraction of a percent" repeats the previous sentence — merge.
- [Minor] Heading "Uniform motion" (Formula section) repeats the chapter title — "Formula: position in uniform motion".
- [Minor] exit-ticket — the "?" falls alone on a new line at 1280 px after "$20\,\text{min}$" — keep the question mark in the same text run.
- [Minor] Prediction 1 option order differs from the source order (shuffled by design); no action.

## Checked
- Opened fig-1/2/3-390 (hero, motion, graph), top-390, intro-1280, sim-390, sim-1280, lab-1280-1, example-390-1/2, stage-sovella-390-1, stage-tutki-390-2, exp-koe-1-390-1, theory-1280-1/2, open-ennusta-1280, open-tarkista-1280-1, open-exit-1280.
- Figures are clear, labelled in LaTeX, legible at 390 px; graph slope/intercept consistent (3 m/s, 6 m over 2 s).

## Scores
illustrations 5 · typography 4 · Finnish (English) 3 · accessibility 4
