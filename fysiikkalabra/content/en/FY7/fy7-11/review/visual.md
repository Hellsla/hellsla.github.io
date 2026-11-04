VERDICT: FAIL
CONTENT-HASH: 4e78ccdf13e1a945

## Blocking
- [Major] lesson.md worked example (steps 1, 5), lang/en.json `fy7-11.lukemat` (sim readout), inquiry table — red is marked with subscript `\text{p}` (Finnish "punainen"): `n_\text{p}`, `\alpha_\text{p}`, `\delta_\text{p}`, while violet is `\text{v}`. An English reader sees "red … n_p" with no p-word anywhere; the symbol reads as arbitrary and breaks the red/violet pairing the whole chapter rests on. Fix: `\text{r}` (red) and `\text{v}` (violet) in en everywhere, including exercises/solutions.md (see exercise report). Subscripts are not meant to be shared with the Finnish text.

## Polish
- [Minor] lang/en.json `fy7-11.selite` — 17 words, so sim-embed.js folds this legend into a second disclosure "Assumptions of the model and explanation" (4 disclosures, one of them just the dashed-line legend; fi-easy shows it as plain text). Shorten to "Dashed lines: the surface normals and the extension of the incident ray." (under 15 words).
- [Minor] sim-390 / exp-koe-1 tables — headers hyphenate "differ-ence (°)", "angle of inci-dence"; at 1280 the experiment table's last column (difference) is cut off in the card and needs a sideways scroll. Shared layout, all languages.
- [Minor] Key idea, citation line — "water at $20\,{}^\circ\text{C}$: M. Daimon…" colon reads as a ratio; use a full stop or "at 20 °C (M. Daimon…)".
- [Minor] Check-your-understanding feedback "Suggestion: one answer does not show everything you can do, but review…" is mechanical; "One answer does not show what you know, but review the theory summary and do the core exercises." reads better.

## Checked
- Contact sheets 1–4; hero (fig-2), prism (fig-5), drop (fig-7), observer (fig-9), n-graph (fig-11), prism-angles (fig-13), theta-graph (fig-15), scene (fig-17) at 390; top-390, sim-390, example-390-1/2, lab-1280, theory-1280-1/3, open-tarkista-1280-1. check_layout --width 340 OK. No Finnish text visible (grep of lesson, inquiry, exit ticket, exercises). Figures: geometry, red/violet colours, labels all LaTeX/English, to-scale statements correct, alt texts translated.

## Scores
illustrations 5 · typography 4 · Finnish (English prose) 4 · accessibility 4
