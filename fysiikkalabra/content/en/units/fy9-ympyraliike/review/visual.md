VERDICT: PASS
CONTENT-HASH: 83e12053f0efcc73

Visual and editorial review of the English translation of fy9-ympyraliike, round 3 (source PASS at 678dc353273487b6). Reviewer 2026-11-04.

Preview rebuilt with `python3 scripts/build.py fy9-ympyraliike` (preview/en/fy9-ympyraliike.html) and checked in Playwright (scripts/_browser.launch) at 390 and 1280 px with every details element opened: scrollWidth equals the viewport at both widths, 0 KaTeX errors, no raw `$…$`, no console errors, and no Finnish text on the page apart from the language switcher ("Selkeä suomi"). All eight figures captured at both widths (hero, fy5-6 orbital speed graph, kartta, geo, tilanteet, fy5-4 a_n graph, s3 F–T graph, s3 linearised graph): English labels, decimal points (8.0 N, 1.95 N·s², 1.6 s), consistent colours (force red, velocity blue, acceleration orange), all readable at 390 px.

## Blocking
1. Round-2 Blocking 1 **fixed**: with \textbf{} now handled by scripts/figlib.py translate() and the figure redrawn, the concept map (unit.md, figure `kartta`) shows the headings **equilibrium**, **circular motion**, **gravitation**. "circular motion" fits its box at 390 px. check_i18n.py reports no "figures differ" error.

## Polish
1. Applied by this reviewer: concept-map label "does not move" → "does not start to move" (figures.json + units.py figures --lang en); it fits right-aligned at 390 px without overlapping the formula.

## Shared issues
None new (the round-2 \textbf{} shared issue is resolved).
