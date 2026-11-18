VERDICT: FAIL
CONTENT-HASH: 3812096306ca1735

## Blocking
- [Major] lesson.md "## Summary" (opened Summary box, 390 px) — the display formula now sits on its own line and is no longer clipped, but the list broke: the next three bullets ("The binding energy…", "The binding energy per nucleon…", "The reaction energy…") are merged into one paragraph with literal "- " markers, and the lone "." after the formula is drawn inside the formula box at its right edge ("m_atom·"), nearly clipped — the summary is hard to read, and the markers look like a rendering error — fix: keep the formula inside the bullet as its own block with a blank line after it, so the following "- " lines start new list items. Put the full stop inside the formula (`\,.` at the end of the display) or drop it; do not leave `$$…$$.` as a trailing paragraph. Check Finnish and fi-easy for the same pattern.

## Polish
- none

## Checked
- Own capture of the opened Summary box at 390 px (/tmp/claude-0/-home-user-hellsla-github-io/bf43dda7-b9d6-5d8a-b9af-2263f4c15c3d/scratchpad/sum.png, from preview/en/fy8-10.html; scrollWidth 390, no overflow); the formula fits at 390 px.
- stage-selita-390-5/-6 (Summary closed, layout around it intact), stage-tarkista-390-1/-2.
- The packet's captures show Summary closed only.

## Scores
illustrations 4 · typography 3 · Finnish 4 · accessibility 4
