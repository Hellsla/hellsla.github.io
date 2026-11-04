VERDICT: FAIL
CONTENT-HASH: d049914a3ec3f36c

Pedagogy review (round 2) of the en translation of fy9-kaasut.

## Blocking
1. [Untranslated figure text, not fixed since round 1] Theory summary, concept map `kartta`: the three branch headings still read **neste**, **kaasu** and **lämpövoimakone** in the preview at 390 and 1280 px. The teacher plan asks the class to go through the concept map branch by branch, and an English student cannot read the branch names.
   - Cause: lessons/units/fy9-kaasut/figures.py line 120 draws the heading as `r"\textbf{" + head + "}"`. figlib.translate() translates only `\text{}`, `\mathrm{}` and `\textsf{}`, so figures.json cannot reach these words.
   - I tried to fix it in the translation files only, by editing the SVG in unit.md. check_i18n then fails ("figures differ from figures.py"), so I reverted the edit. The fix has to be in the shared code half.
   - Fix (shared, lessons/units/fy9-kaasut/figures.py): `r"\textbf{\text{" + head + "}}"`. Then add `"neste": "liquid"`, `"kaasu": "gas"` and `"lämpövoimakone": "heat engine"` to the en figures.json, and redraw with `units.py figures fy9-kaasut --lang en` or translate_kit apply.
   - fi-easy has the same three headings, which is fine there because they are Finnish words. They will need their fi-easy figures.json entries (the words themselves) once figures.py changes, or check_i18n will report them as missing.

## Polish
2. $P_\text{l}$ (s2 c) keeps a Finnish-derived subscript. It is defined, so this is optional.

## Round-1 findings
- 2 ($W_\text{k}$ and $\eta_\text{kok}$ differ from the linked chapters): fixed everywhere, including the concept map.
- 3 (s1 wording), 4 (s2 c wording), 5 (exit ticket 1.a), 6 ("work done by gas"): all fixed, and the new wording is natural.

## Checked
- I read the round-2 diff against the source and the round-1 report.
- Preview `python3 scripts/build.py fy9-kaasut` → preview/en/fy9-kaasut.html, checked in Playwright at 390 and 1280 px with every `details` open. The only Finnish words left in the page text are the three concept-map headings.
- The 75-minute plan, task counts, feedback and hints are as in round 1.
