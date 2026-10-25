# Notes: things to take into consideration

Living checklist for the human and every agent. Read it before drafting or reviewing a lesson.
When a mistake costs a review round, add a line under the right heading (what, why, how to check).

## 1. Math in LaTeX

### How it is rendered
- `lesson.md` goes through `scripts/build.py`, then KaTeX 0.16.11 (vendored in `templates/vendor/katex`, no CDN) renders it in the browser.
- Delimiters: `$$...$$` for display, `$...$` for inline. A ```` ```latex ```` fence becomes display math.
- The build hides all math from the markdown converter first, so `_`, `*` and `\` inside formulas are safe.
- Math also renders in `exercises.json` (`text`) and `exit-ticket.json` (`q`, `a`), because auto-render runs over the whole page. In JSON every backslash is doubled: `"$\\frac{1}{2}$"`.
- `solutions.md` is **not** published and not rendered. Write it in plain text with Unicode (`W₁`, `m/s²`, `·`).
- The simulation canvas and the inline SVG figures cannot use LaTeX either. Use plain text and Unicode there (`W = F · s`, `m/s²`).

### Writing rules
1. Every formula appears once in display form with its symbols named (house rule). Use inline math only for short references and numbers.
2. Inline math stays on one line. A `$...$` that spans a line break is not recognised.
3. Units go in `\text{N}` or `\mathrm{N}` after a thin space: `40\,\text{N}`, `9{,}81\,\text{m/s}^2`. A normal space `\ ` also works, but use `\,` in new text.
4. Decimal comma inside math is `{,}`: `0{,}20`, `9{,}81`. A bare `9,81` renders with a gap after the comma. In JSON values (`answer`) use a decimal point.
5. Multiplication is `\cdot`, never `*` or `x`. Degrees are `^\circ`. Square roots are `\sqrt{2gh}`.
6. Use `\frac` in display formulas and `\tfrac` inline, so inline formulas stay compact.
7. Finnish words inside math go in `\text{}`: `F_\text{kitka}`, `\text{työ}`. Ä and ö work.
8. Vectors are `\mathbf{F}`, magnitudes plain `F`. Vectors belong to FY4; FY3 treats force as a scalar.
9. Verified to work: `aligned`, `cases`, `\cancel`, `\boxed`, `\color`, `\Delta`, `\rho`, `\approx`, `\Rightarrow`.
10. Verified **not** to work: siunitx (`\si`, `\SI`, `\unit`) and redefining a built-in with `\newcommand` (for example `\N`).

### Pitfalls
- A bad fragment does **not** fail the page build. The page shows the raw source in red. Always run the checker.
- `\( ... \)` and `\[ ... \]` are not recognised. Use `$` and `$$`.
- A literal dollar sign starts math. Write "euroa" or "€" instead.
- Math in an SVG `<text>` or in canvas text is plain text. Keep the labels short.
- An inline `\dfrac` makes a tall fraction that breaks the line. Put calculations with fractions on their own line in display math.
- A wide markdown table overflows a phone. The site CSS makes tables scroll sideways inside themselves; keep header cells short.

### Check before every commit that touches math
```bash
python scripts/check_latex.py content/FY3/fy3-2     # .md files and every string in the .json files
```
It exits 1 on a bad fragment. CI and the mathematician agent run it too. After changing any formula, also recompute the numbers in `exercises.json` and `solutions.md` in Python.

## 2. Other things learned in this project

### Scope and curriculum
- The MAOL guide in `docs/lops2019/` decides what belongs to a module. FY2 introduces energy forms **without** expressions; `E_k`, `E_p`, the work-energy theorem, vectors and `cos α` are FY4. FY3 has force as a measure of interaction, `W = Fs`, graphical integration in (s,F) and Joule's experiment. Grep the guide before adding a formula.
- Slot ids follow the module: `fy3-2` is the second FY3 lesson. The gold reference is `fy4-4`.

### Numbers
- Round only at the end; show unrounded intermediates in solutions (`v = 80/3,6 m/s`, not `22,2`).
- Final answers have as many significant figures as the data (2 sf data gives 2 sf). Check that a student who rounds correctly stays inside the relative `tolerance` (0,02).
- Compute every answer in Python before writing it.

### Finnish
- Avoid "25 m matka" and "80 N voimalla". Either inflect the unit (`80 N:n voimalla`, `40 N:ssä`) or write nominative sentences ("Voima on 80 N ja matka 25 m").
- "Paino" is a force (`G = mg`). Do not "pitää painoa paikallaan"; say "kappaletta".
- Terms come from `glossary.json`; add a missing term there instead of inventing one.

### Pages and publishing
- Only `status: reviewed` lessons are built into `site/`, which is committed and served by Pages from `main`. Previews and `--all` go to the git-ignored `preview/`.
- The numeric readout in a simulation is DOM text, not canvas text, so it stays readable on a phone. Tap targets are at least 40 px, and there is no horizontal overflow at 390 px.
- Fonts are self-hosted (`vendor/fonts`). Add no third-party requests, tracking, logins or forms.
- Reviewer screenshots stay out of git (`**/review/*.png`).

### Process
- Publishing goes through the gate (`scripts/gate.py`): all reviewers PASS on the current content hash, then the publisher agent commits. Do not hand-edit `status`, `reviewed_by`, `reviewed_on` or `reviewed_hash`.
- Any edit to a lesson changes its hash. After a fix, every reviewer has to run again.
- Reviewers never edit lesson files. After a FAIL, fix, rebuild, test and rerun the failed reviewers.
- Keep commits small and push after each; the branch name is given by the session.

## 3. Matriculation exam material (inspiration only)

- Source named by the human: https://yle.fi/abitreenit/fysiikka (physics exams collected there). Status: **not collected yet**, because the cloud environment's network policy blocked yle.fi (and the exam-file host it links to).
- Store downloaded exam files only in `docs/exams/`, which is git-ignored. They are third-party material, so they never go into commits, `site/` or lesson folders.
- Use them to study, never to copy: which skills each task type tests, typical contexts, how multi-part tasks are built, how many points go to reasoning versus calculation, which formulas the tasks expect students to know.
- Record findings as short pattern notes in this file (for example "typical level-3 task: graph reading plus one calculation"), never as quoted or lightly reworded tasks.
- Every exercise stays original: new context, new numbers, own wording. CLAUDE.md still forbids copying exam questions.
- When a pattern changes how a lesson should be written, add the change to the relevant section above and mention it in the commit.

### Exam-style patterns used so far (from general knowledge, not yet checked against the files)
- A task starts with a context and runs through several parts, from a direct calculation to reasoning.
- Graph reading and graph-based calculation are common. Applied in fy3-2 (area under the (s,F) graph) and fy3-1 (spring stretch against force).
- Tasks ask the student to reason with a changed situation ("what does the scale show on Mars?"), not only to plug numbers in. Applied in the level 3 tasks.
- Units, conversions (g to kg, minutes to seconds) and sensible rounding are part of the grading, so every exercise keeps them.
- Check these against the real files when `docs/exams/` is filled, and replace this list with verified findings.
