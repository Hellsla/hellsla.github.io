VERDICT: PASS
CONTENT-HASH: cc71cb661f7317ac

## Delta review (2026-11-04)

The only change since the previous PASS: in figure "tilanteet" the "Earth" label moved right (foreignObject x 270 -> 298, box 298-358 × 634-658). The ā label sits at 243.5-272.5 × 612-636, so the two no longer overlap, and the label stays inside the 380-wide viewBox, right of the end of the Earth arc. `git diff HEAD` shows nothing else changed. Rebuilt with scripts/build.py and checked in Playwright at 360 and 1280 px with all details open: the label is clear, readable and not clipped. check_layout.py at --width 360 and --width 1280: OK for preview/en/fy9-ympyraliike, no FAIL. Verdict stays PASS.

## Earlier report

Visual and editorial review of the English translation of fy9-ympyraliike, round 3 (source PASS at 678dc353273487b6). Reviewer 2026-11-04.

Preview rebuilt with `python3 scripts/build.py fy9-ympyraliike` (preview/en/fy9-ympyraliike.html) and checked in Playwright (scripts/_browser.launch) at 390 and 1280 px with every details element opened: scrollWidth equals the viewport at both widths, 0 KaTeX errors, no raw `$…$`, no console errors, and no Finnish text on the page apart from the language switcher ("Selkeä suomi"). All eight figures captured at both widths (hero, fy5-6 orbital speed graph, kartta, geo, tilanteet, fy5-4 a_n graph, s3 F–T graph, s3 linearised graph): English labels, decimal points (8.0 N, 1.95 N·s², 1.6 s), consistent colours (force red, velocity blue, acceleration orange), all readable at 390 px.

## Blocking
1. Round-2 Blocking 1 **fixed**: with \textbf{} now handled by scripts/figlib.py translate() and the figure redrawn, the concept map (unit.md, figure `kartta`) shows the headings **equilibrium**, **circular motion**, **gravitation**. "circular motion" fits its box at 390 px. check_i18n.py reports no "figures differ" error.

## Polish
1. Applied by this reviewer: concept-map label "does not move" → "does not start to move" (figures.json + units.py figures --lang en); it fits right-aligned at 390 px without overlapping the formula.

## Shared issues
None new (the round-2 \textbf{} shared issue is resolved).
