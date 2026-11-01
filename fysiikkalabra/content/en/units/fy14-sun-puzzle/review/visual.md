VERDICT: FAIL
CONTENT-HASH: 8e99d0c59ea3fbba

## Blocking
1. [Major] Key idea, Aston's masses (`unit.md`, the display after "With today's AME2020 masses", 390 px). The aligned display is 374 px wide in a 356 px box, so the first line ends "$= 4.03130$" with the "0 u" cut off. This is the number the whole unit argues from. Fix: break the chain:
   `4 \cdot m(^{1}\text{H}) &= 4 \cdot 1.007825\ \text{u} \\ &= 4.031300\ \text{u} \\ m(^{4}\text{He}) &= 4.002603\ \text{u}`

## Polish
1. [Minor] Kelvin's 1862 claim is ambiguous in two places. The text says "had most probably not lit the Earth for 100 million years", and the order component says "has most probably not shone for 100 million years". Both can be read as "has not shone during the last 100 million years". Fix: "had most probably shone on the Earth for less than 100 million years" (text), and "Kelvin calculates that the Sun has most probably shone for less than 100 million years (1862)" (`fx-sp-timeline`).
2. [Minor] Figure `estimates`, aria-label: "about 5351 years" is a false precision. Fix: "about 5000 years".
3. [Minor] `find-error` prompt: the inline `$t = \frac{Mc^2}{L}$` sets a small stacked fraction in the line. Fix: `$t = Mc^2/L$`.
4. [Minor] `check-explain` model answer uses "$E = mc^2$", where the unit elsewhere writes $E = \Delta m \cdot c^2$. Fix: use the unit's form.
5. [Minor] Hero: the rock layers stick out past the cliff's edge line as pale wedges, which reads like a drawing error at 1280. Fix: clip the layers at the cliff face, or drop the edge line.

## Checked
- Fresh build and captures for this hash: contact sheets 1–2, top/intro at 390 and 1280.
- I captured each figure myself at 390 and 1280: the hero (no text) and `estimates` (log axis, bars and the 4.6-billion-year line to scale; labels 15.5 px).
- Worked example with all seven steps at 390, plus the solutions of the coal, mass-loss and Kelvin tasks.
- The Eddington source, the order component, match and say.
- Measured each display's width with Playwright: only the Key idea display overflows. No KaTeX errors, no raw `$`, no console errors. The hash was the same at the end.

## Scores
illustrations 4 · typography 3 · English/French 4 · accessibility 4
