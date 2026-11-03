VERDICT: FAIL
CONTENT-HASH: dee2764a7a7b4845

## Blocking
- [Major] inquiry.json exp-1 and exp-2 (Alkutila line and table headers, captures exp-exp-1-390, exp-exp-2-390, stage-tutki-390-2) — the Alkutila line shows "suunta φ = 0 °" and the exp-2 table header "suunta φ" with a plain-text φ, and "0 °" with a space; headers read "$B_m$ (µT)" with an italic subscript m and a plain-text unit, while the lesson writes $B_\text{m}$ and $\mu\text{T}$ — a plain symbol where the student looks is a blocking finding (NOTES §1), and the notation differs from the rest of the chapter — make the build convert φ and µ (add φ to the SYMBOL pattern in scripts/inquiry.py, and turn "B_m (µT)" into $B_\text{m}$ with $(\mu\text{T})$), or write the labels so they come out as maths: "suunta $\varphi$", "$\varphi = 0^\circ$".

## Polish
- [Minor] sim-390 / sim-1280 and experiment panels — the "Näytä magneetin kenttäviivat" and "Näytä kompassiruudukko" checkboxes sit above their label text, not beside it, and read as detached — put the box and label on one line.
- [Minor] fig vector-sum — the upper left of the figure is empty, since the content sits in the lower half and "pohjoinen" is in the corner — move the vectors up or lower the viewBox height.
- [Minor] fig inclination — the label $I$ touches the dashed vertical line — move the label about 6 px right.
- [Minor] lesson.md Ferromagnetismi — "vastakkaisnimisen navan" next to "erinimiset" elsewhere, and the clumsy "raudalla noin 770 °C:seen" — use "erinimisen" and "raudalla noin 770 °C:n lämpötilaan".
- [Minor] hero at 390 px — the compass and magnet, the subject, are small, so the deflected needle is hard to see — enlarge the subject slightly.

## Checked
- Opened at readable size: top-390, intro-1280, theory-1280-1 to 5, and figures 2, 8, 10, 12, 14, 17, 19, 23 (fig-N-390) and 30.
- sim-390, sim-1280, example-390-1 and -2, stage-herata, stage-ennusta-390-1, stage-tutki-390-1 and -2, exp-1 and exp-2 at 390, stage-sovella-390-1, stage-tarkista-390-1.
- open-ennusta-1280-1, open-tarkista-1280-1, open-exit-1280; contact sheets 3 and 4.
- Source lines of the vector-sum and inclination figures, to check that the vectors are to scale. They are: 14:20 and 14:52.
- The exercise-set captures are covered in exercises/review/visual.md.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
