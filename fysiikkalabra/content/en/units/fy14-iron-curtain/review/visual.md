VERDICT: PASS
CONTENT-HASH: 1f6cfeb92c19a88f

## Blocking
(none)

## Polish
1. [Minor] `inquiry.json` `kev-kelvin` solution, **Given**: at 390, "$k_\text{B} = 1.381\,\cdot$ / $10^{-23}\ \text{J/K}$" breaks inside the number. Fix: wrap each value in braces (`{k_\text{B} = 1.381 \cdot 10^{-23}\ \text{J/K}}`), as in the pilots.
2. [Minor] `kev-kelvin` **Answer** box at 390 breaks after "=": "$T \approx 1.16 \cdot 10^{7}\ \text{K} =$" / "$11.6 \cdot 10^{6}\ \text{K}$". Fix: put the second form in the sentence below ("that is, $11.6$ million kelvin") and keep one equation in the box.
3. [Minor] `kev-kelvin` **Reasonableness**: "A difference of 273 between kelvins and degrees Celsius" reads oddly. Fix: "The 273-degree difference between the kelvin and Celsius scales does not matter at this size."
4. [Minor] `unit.md` Source C: the quotation spells "Artsimovitch" and the rest of the unit spells "Artsimovich". Students will think these are two people. Fix: add "[Artsimovich]" after the quoted name, or a short note that the original spells it so.
5. [Minor] Figure `thomson`: the laser, the scattered-light arrow and the "hotter" curve are all the same red. Fix: draw the hotter curve in a different colour from the laser (for example the figure orange), so that red keeps one meaning.

## Checked
- Captures regenerated for this hash: contact-1 to -5; intro-390, intro-1280, stage-sovella-390-1 and -2 (the `kev-kelvin` task with all hints and the solution open), the Sources A–E and Thomson sections (contact-1 #8–#14), the French corner (#24).
- Own Playwright captures of `hero` and `thomson` at 390 and 1280. Smallest label is 15.5 px at 390. The curves are of plausible equal area, and the electron velocity arrows are in velocity blue. No `.katex-error`, no raw `$`, no console errors, no horizontal scroll.
- Components `fx-ic-sort` (match) and `fx-ic-french` (say) at 390 and 1280. Hash unchanged at the end.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4
