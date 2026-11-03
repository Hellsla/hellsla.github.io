VERDICT: FAIL
CONTENT-HASH: 40bfc5cc82bd45c1

## Blocking
- [Major] inquiry.json koe-1 and koe-2 (captures exp-koe-1-390-1/-2, lab-1280-1) — the experiment cards show Finnish words in the English lesson: "Initial state: virta = 2 A, kierroksia: 200 turns", "Kept constant: virta, kierroksia, ..." and again in the status line after the button — a student reads untranslated words; the `names` entries for I and N are still "virta" and "kierroksia" — change them to "current" and "number of turns" (both experiments).
- [Major] exp-koe-1-390-1 and koe-2-390-1 (390 px) — the "Initial state" box is clipped at the right edge ("direction of the current: downwards at the fron…"), so the value of a fixed quantity is not fully readable — let the long values wrap (or shorten the label "downwards at the front" in `values.dir`).

## Polish
- [Minor] experiment tables (exp-koe-1-390-2) — the header "n (1/m)" is plain sans text while "B (mT)" and "length of the coil (cm)" are KaTeX; write it as $n\ (\tfrac{1}{\text{m}})$ for one typeface.
- [Minor] mittaus unit suffix "· 10⁻⁶ Vs/(Am)" (stage-tutki-390-3) — plain Unicode text beside the input, not LaTeX like the rest.
- [Minor] fig electromagnet (fig-13-390) — the lifted nail on the left is tiny and the B field is not drawn; "iron" label sits close to the coil at 390 px. Slightly larger lifted object would show the point better.
- [Minor] fig coil-dims (fig-17-390) — the green label $\overline{B}$ overlaps the first turns of the coil winding; move it above the arrow.
- [Minor] wire-graph (fig-15-390) — the "0" of the origin stands detached from the axes' corner; place it at the corner as in the coil-fit graph.

## Checked
- contact sheets 1–3; fig-7, 9, 11, 13, 15, 17 at 390 (all six figures, geometry and right-hand-rule directions consistent: anticlockwise from above, N pole at the right for dots above/crosses below); hero via top-390 and intro-1280.
- sim-390, exp-koe-1-390-1/-2, lab-1280-1/-2 (simulation, experiments, tables); stage-ennusta via open-ennusta-1280-1.
- theory-1280-1/-2, example 390 via contact sheets 2–3, exit ticket (open-exit-1280); contact 1–3 triage of the remaining stage captures.

## Scores
illustrations 4 · typography 4 · Finnish (English prose) 4 · accessibility 3
