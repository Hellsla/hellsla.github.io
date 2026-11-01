VERDICT: PASS
CONTENT-HASH: 6909041be653193e

## Blocking
(none)

## Polish
- [Minor] Esimerkki task (example-390-1, Sovella) — "+$30\,°C$:n" has the plus outside the maths, and "12 · 10⁻⁶ 1/K" is plain Unicode while step 1 sets the same value in maths — put both in `$...$` ("$+30\,{}^\circ\text{C}$:n", "$12 \cdot 10^{-6}\,\tfrac{1}{\text{K}}$").
- [Minor] Table headers "α (10⁻⁶ 1/K)" / "γ (10⁻³ 1/K)" (theory-1280-2) — plain-Unicode superscripts render tiny and differ from the KaTeX alpha beside them — set the unit in maths.
- [Minor] Fig 3 (volume-expansion) — warm flask is labelled only "T₀ + ΔT", the cold one "kylmä, T₀" — add "lämmin" for parity with fig 4.
- [Minor] Experiment Alkutila line (tutki-390-2, lab-1280-1) — "T = 20 °C" is plain text next to maths "L₀ = 10 m" — render the value as maths.
- [Minor] "Siksi" opens many consecutive sentences in Kaava and Ydinajatus — vary a couple.

## Checked
- Contact sheets not needed; opened top-390, intro-1280, fig-1..5-390, theory-1280-1..3, fig row, sim-390, sim-1280, example-390-1/2, ennusta-390-1, tutki-390-1..3, selita-390-1/3, sovella-390-1, exp-2-390-1, lab-1280-1, open-tarkista-1280-1, open-exercises L1/L2/L3 (lesson-level exercises seen via the exercise set).
- All five figures read at 390 px, labels LaTeX, no clipping; hero and scene flat style consistent; sim canvas and readout in KaTeX, decimal comma accepted.

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
