VERDICT: PASS
CONTENT-HASH: 2c7cc76823c0c1d0

## Blocking
(none)

## Polish
- [Minor] fy5-s1-crane — the labels $m_\text{v}$, $m_\text{p}$, $r_\text{v}$, $r_\text{p}$ keep Finnish initials in the English figure. They are defined in the text, so this is not misleading. Fix: per-language subscripts in figures.py (shared, not done here).
- [Minor] fy5-s2 task text at 390 px — the inline $\gamma = 6.674 \cdot 10^{-11}$ … unit breaks across lines, as in fi. Fix: put the constant on its own line.
- [Minor] fy5-s4-signal — the zero line is unlabelled and the y axis has no ticks, as in fi.
- [Minor] fy5-s1-fbd at 390 px — small (about 300 px wide). θ, x and y are tiny.

## Checked
Captures are in content/en/FY5/sovella/review/shots/. The script refuses --lang for a Sovella set, so I took them with a copy of screenshot.py patched to capture preview/en/FY5-sovella.html (stamp 2c7cc76823c0c1d0).
- contact-1 (390 px: top, task 1 text, model answers a–e, rubric)
- contact-5 (figures #49–#58, task card #59–#60)
- fig-1-390 (crane: "axis of tower", English labels)
- fig-2/3/6/11 in contact-5: "situation", "free-body diagram", "axis", "signal" translated. The graphs use the decimal point (5.0; 6.35), (0.100; 0.226), and Amalthea/Io/Europa are labelled.
- top-1280 (title, task tabs "Tower crane / Moons of Jupiter / A spring and masses / Organ pipe", intro)
- check_layout.py FY5-sovella --width 345: OK for en (one wide table scrolls, as in fi)
- No Finnish words remain in the text or figure labels apart from the subscripts above. The alt texts are English and complete.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4
