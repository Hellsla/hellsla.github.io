VERDICT: FAIL
CONTENT-HASH: adfa5c7727829d1c

## Blocking
- [Major] lesson.md, Yleinen virhekäsitys, last sentence (captures selita-390-4/5, theory-1280-3) — the weighted-average check is an inline `\tfrac` with a long numerator (`3,0 kg · 20 °C + 1,0 kg · 80 °C` over `4,0 kg`); it renders at about 8 px, and at 390 px the line breaks after "T =" and leaves the fraction on its own line — the correction of the misconception is the least readable maths on the page — fix: set it as a short display chain (or as `T = (3,0 kg · 20 °C + 1,0 kg · 80 °C) : 4,0 kg = 35 °C`).

## Polish
- [Minor] H1 "Q = cmΔT" is plain text, not LaTeX (top-390); if titles are exempt project-wide, ignore.
- [Minor] Ydinajatus/Kaava prose gives units in plain text "J/(kg·K)", "(J/K)", "(J)", while Tiivistelmä and the example use maths; also unit style varies (tfrac vs `J/(kg·K)`) between Tulos and Järkevyys.
- [Minor] Example step 7 and the "1257 J/K" chain set in a small inline box, smaller than the Sijoitus display (example-390-2/3).
- [Minor] Task heading "Taso 2 · soveltava harjoitus 4 tehtävää" wraps the count onto two lines at 390 px (contact #27).
- [Minor] Sim at 390 px: the Upota button sits beside the first slider's label, offset (sim-390).

## Checked
- fig-1..5 at 390 (hero, water-sand, calorimeter, c-bars, scene): legible, palette consistent, ΔT drawn to scale, no clipping; descriptions match.
- top-390, sim-390, sim-1280, example-390-1..3, theory-1280-1..3, selita-390-4, open-ennusta-1280, contact-1..3 (stages, experiments, exit ticket, tarkista).

## Scores
illustrations 5 · typography 4 · Finnish 4 · accessibility 4
