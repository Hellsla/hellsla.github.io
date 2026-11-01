VERDICT: FAIL
CONTENT-HASH: 9b8e68e634f060d3

## Blocking
1. [Major] Worked example, step 5 *Substitution* (`unit.md`, 390 px). The first line, $\Delta m = 2 \cdot 1.007825\ \text{u} + 2 \cdot 1.008665\ \text{u}$, is 348 px wide in a 337 px box, so the student reads "$1.00866$". A wrong-looking number in the model solution is an error at the place where students copy. Fix: break before the second term:
   `\Delta m &= 2 \cdot 1.007825\ \text{u} \\ &\quad + 2 \cdot 1.008665\ \text{u} \\ &\quad - 4.002603\ \text{u} \\ &= 4.032980\ \text{u} - 4.002603\ \text{u} \\ …`
   Step 3 *Formula* (`… - m(^{4}\text{He})`) also touches the right edge. Move `- m(^{4}\text{He})` to its own `&\quad` line.
2. [Major] Binding Energy Explorer, *Whole curve* (`fx-be-explorer`, 390 and 1280; shared `fx/binding.js`). This is the unit's central graph, and its labels mislead:
   - $^{4}\text{He}$, the nuclide selected at the start, is hidden under its own selection ring: only the "4" shows.
   - $^{56}\text{Fe}$ is printed at about $A = 40$–$45$, left of the iron point and outside the shaded peak. At 390 it collides with the axis title $B/A\ (\text{MeV})$.
   - The configured highlights $^{12}\text{C}$ and $^{235}\text{U}$ get no label.
   - With *U-235 fission* chosen, the $^{235}\text{U}$ label runs 3 px past the right edge. The Q steps become scroll boxes: the $m_\text{before}$ line is 483 px wide in 300 px, which hides "$+ 1.008665\ \text{u}$" and the "/u" of $931.494\ \text{MeV/u}$.

   Fix in the component:
   - place each highlight label beside its own point, outside the marker radius;
   - push labels that would collide with the axis title down or to the right;
   - keep labels inside the plot;
   - break the reaction's $m_\text{before}$/$m_\text{after}$ sums one term per line on narrow screens.

   Until then, the unit can start without a selected nuclide (`"select"` removed) and highlight only `H-2`, `He-4`, `Fe-56`. The light-nuclei view and the D–T reaction are fine.

## Polish
1. [Minor] Worked example, step 1. "$1\ \text{u} \cdot$ / $c^2 = 931.5\ \text{MeV}$" breaks after the dot at 390. Fix: brace it, `${1\ \text{u} \cdot c^2 = 931.5\ \text{MeV}}$`.
2. [Minor] Worked example, *Answer*. "$\Delta m = 0.03038\ \text{u}$" has four significant figures. The sentence "Three significant figures are enough, although the masses have more digits, because the difference is what matters" is hard to follow. Fix: "$\Delta m = 0.0304\ \text{u}$ … three significant figures, because $931.5\ \text{MeV/u}$ is given to four and the result is used only to three."
3. [Minor] Figure `ladder`. "$B =$" and "$28.3\ \text{MeV}$" sit on two lines beside the arrow. Fix: write one label, `$B = 28.3\ \text{MeV}$`, under "add".
4. [Minor] Explorer reaction tables use "3 ×" (shared `binding.js`, line 178). Fix: `3 \cdot` or "3 neutrons".

## Checked
- Fresh build and captures for this hash: contact sheets, top/intro at 390 and 1280.
- I captured each figure myself at 390 and 1280: the hero (no text), `ladder` and `qbars`. The smallest label is 14.3 px.
- Worked example with all steps at 390. I measured each display's width with Playwright.
- Explorer at both widths: whole curve, light nuclei, and each reaction (D–T, D–D, U-235). Labels are 14.7 px.
- Match and say components. No KaTeX errors, no raw `$`, no console errors. The hash was the same at the end.

## Scores
illustrations 3 · typography 3 · English/French 4 · accessibility 3

## Shared issues
- `fx/binding.js`: label placement and long display chains, as in Blocking 2, plus "×" in the reaction table. The 8–10 px label size the developer reported is fixed: labels now measure 14.7 px at 390.
