VERDICT: FAIL
CONTENT-HASH: f86c35be7cb1d95d

## Blocking
1. [Major] `inquiry.json` `tritium-task`, `mistakes[].feedback` (opened myself at 390 and 1280 with the anticipated wrong answer 93.5). The student sees raw Markdown: "You used the mass of a deuterium \*and\* a tritium nucleus …". The other mistake shows "\*second\*" in the same way. This happens because `templates/inquiry.js` writes this feedback with `textContent`, so Markdown is never rendered (see Shared issues). Visible markup in the feedback for the most likely mistake looks broken and draws attention away from the correction. Fix: remove the asterisks from both feedback strings ("the mass of a deuterium nucleus and a tritium nucleus together", "in one second").

## Polish
1. [Minor] Sorting task `fx-fs-sort` (`tutki-390-4/5`). The item texts write numbers with units as plain text ("3.15 MJ", "2.05 MJ", "69 MJ", "50 MW", "71 %"). The theory text just above typesets the same numbers in KaTeX. Fix: use `$3.15\ \text{MJ}$` etc. Match items are typeset, as fy14-sun-puzzle shows. Also make the shared aria-label strip `$` (Shared issues).
2. [Minor] Fuel-cycle figure (`cycle`, `selita-390-2`, `selita-1280-1`; labels 28 units, 16.7 px at 390). The "D" label touches the deuterium arrow. The "n" label and the neutron arrowhead sit on the blanket's outer edge. The "T" label straddles the blanket outline. The D and n arrows share the same blue. Fix: move D, n and T 10–15 units clear of the lines, end the n arrow inside the blanket, and give n its own colour. Write ${}^{4}_{2}\text{He}$ and ${}^{6}_{3}\text{Li}$ as the text does.
3. [Minor] Worked example (opened with *Show all*, 390 and 1280). In the Formula step, the two stacked fractions in `aligned` touch each other. Fix: add `\\[6pt]` after the first row. For science: the substitution shows $3.375 \cdot 10^{14}$ and the answer rounds it to $3.37$. The unrounded value 3.3748 explains the rounding, but a reader expects 3.38. Show the result as $\approx 3.37 \cdot 10^{14}\ \text{J/kg}$ in the Substitution step.
4. [Minor] Tables at 390 (`tutki-390-2`, `selita-390-2`). The row "other (bioen-ergy, oil and others)" breaks over five lines. The cells "heavy nu-clei split" and "main ra-dioactive waste" are hyphenated. Fix: write "other¹" and add a note under the table, and use "main waste". Hydro "14 %" sits beside one-decimal values, so write it as $14\ \%$ with a note, or as $14.0$ if Ember gives it.
5. [Minor] Editorial. (a) Prior knowledge: "releases $17.6\ \text{MeV}$: $3.5\ \text{MeV}$ to …". The colon reads as division under the house rule. Write "$17.6\ \text{MeV}$, of which $3.5\ \text{MeV}$ goes to …". (b) In the Fuel section at 390, the full stop after the Li reaction wraps alone to the next line. Put it inside `$…$`. (c) "Evaluate" repeats its instruction in two paragraphs ("Sort the nine statements …", "Sort each statement …"). Merge them into one.

## Checked
- Fresh captures for this hash: contact-1…6, top/intro at 390 and 1280, every stage at 390 (herata 1–2, ennusta 1, tutki 1–6, selita 1–4, sovella 1, tarkista) and the 1280 stages through the contact sheets and selita-1280-1. Also fx-3-390 (say).
- Opened myself in Playwright at 390 and 1280: the whole worked example (seven steps), the tritium task with the wrong-answer feedback, three hints and the closed solution, all 4 model answers after writing, and all 7 choices with feedback.
- Figures: hero (no text, nothing clipped) and cycle (zoomed, label sizes measured). No `.katex-error`, no raw `$`, no horizontal overflow at either width, and no console errors.
- French corner and `say` tips: the respelling is consistent, Finnish comparisons are used, and the French text has `lang="fr"`.
- The hash was unchanged at the end.

## Scores
illustrations 4 · typography 4 · English/French 4 · accessibility 4

## Shared issues
- `templates/inquiry.js` §4 (numeric mistakes): it sets `out.textContent = m.feedback`, so Markdown never renders. Use `md()`/`innerHTML` as the other feedback does.
- `assets/units/fy14/fx/match.js`: the select aria-label strips only `{fr}` and `*`. Strip `$`/`\text{}` as well, so that items can use LaTeX.
- `scripts/inquiry.py`: the numeric input has `aria-label="Answer in $\text{kg}$"`, which is raw LaTeX for screen readers.
- Tables at 390: automatic hyphenation splits short words in narrow cells. Consider `hyphens: manual` for `td`.
