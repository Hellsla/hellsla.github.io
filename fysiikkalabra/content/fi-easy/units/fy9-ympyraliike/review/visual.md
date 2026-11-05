VERDICT: PASS
CONTENT-HASH: c6971c6b158dd450

## Delta review

Only change since the PASS at ca70b3b450bf3201: figure "tilanteet", "Maa" label x 300 -> 328 (git diff confirms nothing else in content/fi-easy or lessons/units/fy9-ympyraliike). Rebuilt (build.py) and checked in Playwright at 360 and 1280 px with all details open: the label sits right of the a-label and above the end of the Earth arc, fully inside the viewBox (rendered 262-294 of 328 px at 360; 489-549 of 608 px at 1280), no overlap; no horizontal scroll (360/360, 1280/1280), 0 katex-error, no page errors. check_layout.py --width 360 and --width 1280: OK for preview/fi-easy/fy9-ympyraliike. No new findings.

## Earlier review

Visual & editorial review, round 2, of the fi-easy translation of fy9-ympyraliike. Preview rebuilt with
`python3 scripts/build.py fy9-ympyraliike` (preview/fi-easy/fy9-ympyraliike.html) and checked in Playwright
(scripts/_browser.launch) at 390 px and 1280 px with every details element (hints, solutions, model answers,
rubrics, exit answers) opened.

- No horizontal page scroll at 390 (scrollWidth = clientWidth = 390) or 1280; no KaTeX element overflows the viewport
  outside a scroll container; 0 katex-error; no raw `$…$` left in text; no decimal point in rendered math; no console
  or page errors.
- Figures (hero, kartta, geo, tilanteet, s3-ft, s3-lin and the reused fy5-6/vr, fy5-4/kuvaaja) render at 358/324/298 px
  at 390 and stay sharp and readable; Finnish labels with decimal comma (6,6 R, 42 200 km, 0,4 … 1,6); colours follow
  the convention (force red, velocity blue, acceleration orange).
- "Luvun tärkeät käsitteet" (Vapaaehtoinen) renders after the opening, before Ennusta, with the fixed lead and five
  terms; formulas render; no note fields.
- The round-1 text fixes (Lähtötaso 5 feedback, pallosymmetrinen, voiman varsi, activities[13], teacher.md) render
  correctly; LaTeX and `{,}` decimal commas unchanged.

## Blocking

None.

## Polish

1. The reused chapter figures fy5-6/vr and fy5-4/kuvaaja keep their chapters' standard-Finnish aria-labels (shared;
   carried over from round 1).

## Shared issues

- Unit page layout at 1280 (single narrow column with empty right area) comes from the shared template.
