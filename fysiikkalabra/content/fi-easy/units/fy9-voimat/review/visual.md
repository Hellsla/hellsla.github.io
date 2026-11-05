VERDICT: PASS
CONTENT-HASH: 37ee21db139040ce

Visual and editorial review of the Selkeä suomi translation of fy9-voimat. Preview built with
`python3 scripts/build.py fy9-voimat` → `preview/fi-easy/fy9-voimat.html`, checked in Playwright
(`scripts/_browser.launch`) at 390 and 1280 px with every `details` (hints, solutions, model answers, rubrics,
exit-ticket answers) opened.

- No console or page errors; 0 `.katex-error`; no raw `$…$` left in the rendered text; LaTeX is used for every
  quantity, unit and symbol (`$100{,}0\,\text{kg}$:n`, `$25^\circ$:n`), decimal comma throughout (no decimal
  point found outside SVG coordinates and file names).
- 390 px: `scrollWidth` = 390, no page-level horizontal scroll; only the sticky stage bar (its own scroller)
  extends beyond the edge. No KaTeX display overflows outside a scroll container. All 23 figures and tables were
  captured as element screenshots: the hero, the jumpers' graph, the concept map (358 × 593), the slope and belt
  figures, the vaunu graph and every force diagram are legible at 390 px; the three tables (rekit, F–a data,
  phone report) fit.
- 1280 px: one reading column, stage navigation, *Luvun tärkeät käsitteet* card with *Vapaaehtoinen* tag and the
  fixed lead, lesson sections and long tasks in order; the teacher notes appear at the end of the preview only.
- Every text is translated: unit.json, inquiry (incl. the inline belt figure's aria-label), exit ticket, tasks,
  solutions, rubrics, teacher.md and figures.json (the descriptions of hero, kartta, kalteva and the vaunu graph are
  rewritten in short sentences; the in-figure words — kappale, voimakuvio, tilannekuva, paino … — are already plain
  and stay the same, which is correct). Colours follow the convention (forces red, velocity blue, acceleration
  orange) because the figures are the shared figures.py drawings.
- Language: correct, natural Finnish; case endings after maths correct; no fragments or English leftovers.

## Blocking
None.

## Polish
1. `inquiry.json` activities.11 choice 1 feedback wording — see pedagogy Polish 1.

## Shared issues
1. `lessons/units/fy9-voimat/sovella/figures.py`, vaunu graph (task s3): the orange label "$F_0 \approx 0{,}24\,\text{N}$"
   sits on top of the dashed extension and touches the circled point at (0,40 N; 0,19 m/s²) at 390 px. Move the
   label below the axis or to the right of the intercept marker. Same in every language; not caused by the
   translation.
2. Same file / `lessons/units/fy9-voimat/figures.py`: in the belt and slope force diagrams the $\overline{F}_\mu$
   label slightly touches its arrowhead at 390 px; a 4–6 px offset would clear it. Shared, polish only.
