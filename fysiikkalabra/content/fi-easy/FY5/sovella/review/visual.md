VERDICT: PASS
CONTENT-HASH: 10312941cf0bba5e

## Blocking
(none)

## Polish
- [Minor] fy5-s2 task text at 390 px — the inline $\gamma = 6{,}674 \cdot 10^{-11}$ … unit breaks across lines, as in fi. Fix: put the constant on its own line.
- [Minor] fy5-s4-signal — the zero line is unlabelled and the y axis has no ticks, as in fi.
- [Minor] fy5-s1-fbd at 390 px — small (about 300 px wide). θ, x and y are tiny.

## Checked
Captures are in content/fi-easy/FY5/sovella/review/shots/. The script refuses --lang for a Sovella set, so I took them with a copy of screenshot.py patched to capture preview/fi-easy/FY5-sovella.html, built from the current content.
- contact-1 (390 px: "Selkeä suomi" top, task 1 text and crane, model answers a–e, Hyväksytään myös / Yleisiä virheitä, rubric cards)
- contact-5 (figures #49–#57: Jupiter graph (5,0; 6,35), spring graph (0,100; 0,226)/(0,350; 0,722), signal "signaali"; task card #58–#60 with the crane "tornin akseli")
- fig-1/2 inside contact-1 #3 and #8 ("tilannekuva", "voimakuvio", "akseli")
- check_layout.py FY5-sovella --width 345: OK for fi-easy (one wide table scrolls, as in fi)
- Decimal commas in text, LaTeX and figures. The shorter sentences do not leave gaps in the cards.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
