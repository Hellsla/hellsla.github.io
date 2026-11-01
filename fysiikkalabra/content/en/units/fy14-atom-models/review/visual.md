VERDICT: FAIL
CONTENT-HASH: 4f300b7cb4a81aa3

## Blocking
1. [Critical] Opening illustration (`figures.py` `hero()`, `ys = [380, 230, 180, 160]`, captures `intro-390`, `top-390`). The grating sends red (656 nm) below the straight-through image and the other three lines above it, in the wrong order: turquoise (486) lies closest to the centre, then blue (434), then violet (410), which is farthest. A grating deflects longer wavelengths more, so on one side the order from the centre is 410, 434, 486, 656. The picture is physically misleading, and the unit itself teaches gratings and these four wavelengths. Fix: put all four lines on one side of the central image, with the offset proportional to λ (for example `y = 268 - 0.33 * λ` for 410→133 … 656→51, then rescaled to fit the screen). Optionally add the mirror set below.
2. [Major] Energy-level diagram (`levels()`, the label offsets `(3, 12), (4, -9)`; my 2× capture at 390). The labels "$n = 4$" and "$-0.85\ \text{eV}$" sit level with the $n = 5$ line. "$n = 3$" and "$-1.51\ \text{eV}$" float half a line below the $n = 3$ line. A student reads the wrong energy for the levels the 486 nm and 656 nm arrows start from. Fix: use `dy = 0` for $n = 3$ and about `dy = +5` for $n = 4$ (nothing is labelled below it), or add short leader lines from each label to its level.
3. [Major] French corner, `inquiry.json` `fx-am-french`. "õ-na-TOM" and "õ-ne-lek-TRÕ" give *un* the vowel of *on*. The course writes *un* as *ẽ* (photoelectric: "*ẽ fo-TÕ*"). Fix: "*ẽ-na-TOM*" and "*ẽ-ne-lek-TRÕ*".

## Polish
4. [Minor] Hydrogen-lines figure (`lines()`). The ticks at 400, 450 … 700 nm have no numbers, and the line labels are offset from their lines: "410" sits under the 400 tick and "486" sits near the 500 tick. Fix: number the ticks (400, 500, 600, 700) and put the four wavelengths above the lines in their colours.
5. [Minor] Worked example, **Reasonableness** (my capture at 390 and 1280). The long inline calculation "$1.328 \cdot 10^{-12}\ \text{J} : … \approx 8.3\ \text{MeV}$" is shown as a display box in the middle of the sentence, and the comma is lost: "The kinetic energy is [box] a typical energy …". Fix: "The kinetic energy is about $8.3\ \text{MeV}$ ($1.328 \cdot 10^{-12}\ \text{J} : 1.602 \cdot 10^{-19}\ \text{J/eV}$). This is a typical energy …".
6. [Minor] The heading renders as "energy levels of hydrogen" because the template drops "Formula:". Fix: `## Formula: Energy levels of hydrogen`.
7. [Minor] `levels()`: "−13.60 eV" against "13.6 eV" everywhere in the text. Fix: format $n = 1$ as `-13.6`. In `scatter()`, the $b$ bracket has no end ticks and merges with the orange path. Fix: add 8-unit horizontal ticks at both ends.

## Checked
- Stamp current. Captures: top and intro at 390 and 1280, every stage at 390 and 1280, contact sheets 1–2.
- My 2× captures at 390 of all four figures (the levels figure zoomed), and the worked example with all steps open at 390 and 1280.
- In Playwright: the smallest label is 14.3 px at 390. No `.katex-error`, no overflow, no console errors. Hash unchanged at the end.

## Scores
illustrations 3 · typography 4 · English/French 3 · accessibility 4

## Shared issues
- The page script turns a long inline formula into a display box in place, even in the middle of a sentence, and the following punctuation is lost. Seen here and in fy14-quantum-tunnelling. Fix: break long inline maths only at relation signs, or warn in `units.py check` when a long inline formula is followed by lower-case text.
