VERDICT: PASS
CONTENT-HASH: 5bf67fc9ccdd56f9

Visual & editorial review (round 3) of the English translation of fy9-harjoituskoe.

## Blocking
None. Round-2 Blocking 1 (Finnish "OSA I" fold tag) is fixed: scripts/check_i18n.py now lists `fold` in TEXT_KEYS, and inquiry.json activities 2–11 read `"fold": "Part I"`. The preview shows the tag "PART I" (uppercased by CSS, like the source's "OSA I") on all ten Part I items at 390 and 1280; the text "Osa"/"OSA" no longer appears on the page.

## Polish
1. [Minor] The Finnish-derived subscripts ($m_\text{j}$, $F_\text{v}$, $R_\text{l}$, $c_\text{k}$) stay because the formulas must match the source. They are acceptable because each is defined in words.

## Checked
- Consistency: "Part I" is the same wording as the Part I activity title, the unit.md table, headings and time plan, the plan figure and the "Part II: …"/"Part III: …" problem titles. No wording change needed.
- Only inquiry.json changed since round 2 (10 fold lines).
- Built with `python3 scripts/build.py fy9-harjoituskoe`; opened preview/en/fy9-harjoituskoe.html in Playwright (scripts/_browser.launch) at 390 and 1280 with every details element open: scrollWidth 390 / 1280 (no horizontal scroll), 0 KaTeX errors, no raw `$`, no comma decimals, no console or page errors. The fold pill sits on one line beside the item title at both widths.
- check_i18n.py: en 0 errors; units.py check: 77 units ok; practice.py check: en 10 tasks, 165 points.

## Scores
illustrations 4 · typography 4 · English 4 · accessibility 4
