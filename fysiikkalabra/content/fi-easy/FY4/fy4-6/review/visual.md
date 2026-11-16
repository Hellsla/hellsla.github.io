VERDICT: PASS
CONTENT-HASH: 26546fe8d6e3ece7

## Blocking
None.

## Polish
- [Minor] The unit lines after "missä …" in the Kaava section ("(N)", "(kg)") are plain text and come from older, untouched text. They could become `$\text{N}$` the next time the text is edited.
- [Minor] The `malli-veto` model figure opens only after the "Olen tehnyt ratkaisun" tick, so no capture shows it. I judged only its alt text, which is complete and uses the term liukukitka. It is a teacher-approved figure, so layout is covered by `check_layout.py`.

## Checked (delta 2026-11-15, work queue 8m)
- Delta: liikekitka changed to liukukitka everywhere (lesson.md, inquiry.json, meta.json, figure labels and alt texts), and "lähtökitka / täysin kehittynyt lepokitka" was added to the Ydinajatus and Kaava text. Captures regenerated for fi-easy (101 captures, 9 contact sheets).
- Opened `fy4-6-fig-10-390` (friction graph): the label reads "liukukitka" in blue and fits, and the axes, ticks and the red dashed drop to 35 N are intact.
- Opened `fy4-6-example-390-1`: the worked example's text and figure read "liukukitka", and the figure labels stay legible and unclipped.
- Opened `fy4-6-stage-selita-390-1` and `-4`: the "Lepokitka ja liukukitka" heading and paragraph, the new sentence on lähtökitka, the Kaava definitions and the bold terms all render without KaTeX errors, and the layout and column width are intact.
- The terminology matches the glossary (liukukitka, lepokitka, täysin kehittynyt lepokitka eli lähtökitka), and the case endings after the maths are correct.
- I did not open the exercise captures or the simulation captures. The exercise and inquiry changes are word swaps with no layout effect.

(Report text of the visual-editorial-reviewer run, saved by the orchestrator because the agent's report did not reach the file.)

## Scores
illustrations 5 · typography 5 · Finnish 5 · accessibility 5
