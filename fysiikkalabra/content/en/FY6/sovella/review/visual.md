VERDICT: FAIL
CONTENT-HASH: 8d806aafb6c72eb4

## Blocking
- [Major] fy6-s2 circuit figure (lessons/FY6/sovella/figures.py:131) — the cable is labelled $R_\text{k}$ (Finnish "kaapeli"), but the English task, solutions and rubric all use $R_\text{c}$ — the student meets two symbols for one quantity, and "$R_\text{k}$" is never explained — label the English figure $R_\text{c}$ (language-specific label; do not change the Finnish one).

## Polish
- [Minor] fy6-s1 and fy6-s2 circuit figures — current arrows are in the momentum purple `#7048e8`; current is neither momentum nor one of the FY4 colours — name the implication to the teacher; no change asked.
- [Minor] fy6-s2 figure — lamp ratings "12 V / 24 W" are small muted grey type, harder to read at 390 px than the other labels — raise to ink colour.
- [Minor] fy6-s2 figure — the Finnish-only "sulake" check: "fuse" is already English, so only the symbol is wrong (see Blocking).
- Process: `screenshot.py` cannot capture the English Sovella page (it only captures `fi`), so `content/en/FY6/sovella/review/shots/` does not exist. I captured the English page myself with the same Playwright setup, in the scratchpad, at 390 px.

## Checked
- Own English captures at 390 px of `preview/en/FY6-sovella.html`: all four figures (s1 circuit, s1 graph, s2 circuit, s3 field) and the page's first screens, including the task text, results list and parts a–c of s1.
- The page does not overflow sideways (scrollWidth 390).
- Not opened: the 1280 px captures, the 43-part full-page captures, the contact sheets (the existing captures are Finnish, for another hash), and the teacher's notes. Prose and solutions were read from the packet source.
- Source read: the graph has axes with units, markers distinct from the fitted line, a dashed extension to the vertical axis, and the marked axis start at 3.6 V. The notation is consistent.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
