VERDICT: FAIL
CONTENT-HASH: 4661e52103fa565a

## Blocking
1. [Major] French corner, `inquiry.json` `fx-cl-french`, phrase *un corps noir* (capture `fx-4-390`). The respelling "õ KOR NWAR" gives *un* the vowel of *on*. *Un* is a front nasal vowel, and the course writes it *ẽ*: the photoelectric unit has "*ẽ fo-TÕ*". As written, the tip teaches a wrong vowel in the first unit of the course. Fix: write "*ẽ KOR NWAR*: the *p* and *s* of *corps* are silent."

## Polish
2. [Minor] Respelling style, `fx-cl-french`. The tips are roman, but the pilot units set respellings in italics and explain the convention once ("capitals show the stressed syllable, and *õ*, *ã* and *ẽ* are nasal vowels"). This is the first French corner of the course. Fix: put the respellings in italics and add that one sentence to the French-corner box.
3. [Minor] Figure *Reading the curves* (`figures.py` `curves()`, my 390 capture). The red "4000 K" label (`lx=1180, ly=0.2`) sits between the green and blue curves, above the red one, and its white background cuts the blue curve. Fix: move it under the red curve near its peak, for example `(1000, 0.07)`, or right of it at `(1500, 0.12)`, clear of the 5000 K curve.
4. [Minor] Worked example at 390 (all steps open). Inline equalities break after "=": "$b =$ / $2.898…$" and "$h = 6.626 \cdot$ / $10^{-34}$" in **Given**, "$1\ \text{eV} =$ / $1.602…$" in **Unit conversions**, "$\approx 1.07\ \mu\text{m} =$ / $1070\ \text{nm}$" in **Answer**. Fix: wrap each equality in braces, `${b = 2.898 \cdot 10^{-3}\ \text{m} \cdot \text{K}}$`, as the photoelectric review asked.
5. [Minor] Spectrum figure (`spectrum()`): the labels "X" and "micro" are abbreviations that the text never uses. Fix: `\text{X-rays}` (it fits at 24 units) and `\text{micro-}` with "waves" below it, or explain the abbreviations in the aria-label and caption.

## Checked
- The page was rebuilt and recaptured for 4661e52103fa565a. The hash changed during the review, from 9f4b777715798bfc, but only through the shared `timeline.json` (JET dates, Aston 1920). I looked at the new timeline captures.
- Captures: top and intro at 390 and 1280, every stage at 390 and 1280, contact sheets 1–5, `fx-2-390-1` (timeline), `fx-4-390` (say).
- My own 2× captures at 390 of all four figures (hero with no text, spectrum, curves, catastrophe), and the worked example with all seven steps open at 390.
- In Playwright: the smallest figure label is 14.3 px at 390 and 16.6 px at 1280. No `.katex-error`, no raw `$`, no horizontal overflow, no console errors.

## Scores
illustrations 4 · typography 4 · English/French 3 · accessibility 4

## Shared issues
- `assets/units/fy14/fx/timeline.js` and `data/timeline.json`:
  - Card text writes "E = mc²", "80 keV" and "4.8 MeV" as plain text, not LaTeX. Fix: render `$…$` in card text (KaTeX auto-render on the list) and write `$E = mc^2$`.
  - At 390 the legend wraps one item per line except the last two, and the strip's year labels (font-size 15 in a wide viewBox) render at about 11 px. Fix: use `flex-wrap` with a gap for the legend, and size the year labels to the rendered width.
