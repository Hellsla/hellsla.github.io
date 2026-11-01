VERDICT: PASS
CONTENT-HASH: c24379ba79d6f049

## Blocking
(none)

## Polish
1. [Minor] *Energy scales: chemical and nuclear fuels* appears twice in a row: as the activity title (`scales-text`) and as the component's own heading. Fix: drop the activity `title`, or give the component no heading.
2. [Minor] Sun–reactor table at 390: the row label breaks as "temper- / ature". Fix: give the first column a minimum width, or turn off hyphenation in tables (`hyphens: manual`).
3. [Minor] "about $150$ million degrees" in the hook, the *Fusion in the laboratory* text, the `lab-vs-sun` model and `check-3`. Next to "$15$ million kelvin" and $1.5 \cdot 10^{8}\ \text{K}$ in the table, "degrees" has no unit. Fix: "$150$ million kelvin".
4. [Minor] Figure `barrier`: the white-backed "strong force" label sits on the green well wall and the tunnelling arrowhead at $r \approx 3\ \text{fm}$. Fix: move it about 20 units down or left, into the well.
5. [Minor] Reaction component, step 2 (shared `fx/reaction.js`): the two $\overline{v}$ labels sit on the edges of the "Coulomb barrier" box. Its inline chains also break after "$\cdot$" at 390 (for example "$= 0.799 \cdot$ / $17.6\ \text{MeV}$"). Fix: move the labels above the box, and brace the inline equalities. For science: the `reaction-describe` model answer says "about $10^{-15}\ \text{m}$", where the text says $3\ \text{fm}$.

## Checked
- Fresh build and captures for this hash: contact sheets 1–2, top/intro at 390 and 1280.
- I captured each figure myself at 390 and 1280: the hero (no text), `ppchain` and `barrier` (labels 14.3 px or larger).
- Worked example with all steps at 390. The coal solution.
- I stepped the D–T reaction component through all 6 steps at 390: velocity is blue, force red, and the $v_\text{n} : v_\alpha$ arrows are to scale.
- Energy-scales chart at 390: the bars now line up with the log axis.
- The order, match and say components. No KaTeX errors, no raw `$`, no overflow, no console errors.
- French respellings: I checked *tritium* \tʁi.sjɔm\ against Wiktionnaire. The hash was the same at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4

## Shared issues
- `fx/reaction.js`: the step-2 label overlap and the inline line breaks above. The energy-scales axis misalignment that the developer reported no longer shows at 390.
