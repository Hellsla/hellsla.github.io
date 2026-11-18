VERDICT: FAIL
CONTENT-HASH: 86d9a24892665c87

## Blocking
- [Major] Tiivistelmä list (390 px, own capture) — after the display formula the remaining list items ("Suomalaisen keskimääräinen…", "Radonin hajoamistuotteet…", "Ulkoiselta säteilyltä…") render as one run-on paragraph with literal " - " separators instead of bullets — structure and readability broken by the formula move — keep the formula inside the bullet as a properly indented block (blank line + 2/4-space indent per the markdown list rules) or put it in a `\(...\)` inline-block span so the list continues.

## Polish
- [Minor] Formula line ends with "…" touching the box's right edge at 390 px; fits, no clipping.

## Checked
- Own 390 px capture of the opened Teoria/Tiivistelmä (scratchpad t.png; no 390 theory capture exists in the packet). Formula fits, no overflow (scrollWidth 390); "kudosten herkkyyden. Molempien…" continuation reads fine.

## Scores
illustrations 4 · typography 4 · Finnish 4 · accessibility 4
