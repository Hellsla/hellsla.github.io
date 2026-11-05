VERDICT: PASS
CONTENT-HASH: 561ea006852fe64e

Visual and editorial review of the Selkeä suomi translation of fy9-kokeellisuus. The preview was built with `python3 scripts/build.py fy9-kokeellisuus` and checked in Playwright (scripts/_browser) at 390 px and 1280 px, with every `<details>` element opened (hints, solutions, model answers, rubrics).

Results:
- No horizontal page scroll at either width (scrollWidth equals clientWidth). There are 0 `.katex-error` elements, no raw `$…$` left in the text, and no console errors.
- All five figures render: hero, kartta, virhe, fy9ko-s4-graph and fy9ko-s6-graph. At 390 px they are 298–358 px wide, and their labels are legible: "suunnittelu/analyysi", "b ≈ 52 g = lasin massa", "systemaattinen virhe", "Δ(T²) = 3,21 s²", "Δl = 0,80 m", "(60 m²/s²; 7,2 m)".
- The figures use the decimal comma. figures.json translates every alt description into simpler sentences. The in-image labels stay as in the source, which is correct for fi-easy.
- The colours follow the source: blue for the slope construction and red for the systematic-error intercept.
- "Luvun tärkeät käsitteet" renders after the opening, before Pohdinta. It has the fixed lead, bold terms and KaTeX in the explanations ($\bar{x} \pm \Delta x$, $k = \frac{\Delta y}{\Delta x}$), and no note fields.
- The editorial conventions hold throughout: LaTeX for every quantity, `\,` before units, `{,}` decimal commas, ":" for division in text, and ”…” quotes.

## Blocking
None.

## Polish
1. inquiry.json activities.7 (Ryhmän jousimittaus): at 390 px the four-column table is 324 px wide inside a horizontal scroller. The last header "$k = F : x\ (\text{N/m})$" is cut until the student scrolls; the scroll shadow does show. The source has the same layout. If wanted, shorten the header to "$k\ (\text{N/m})$" in both languages.
2. sovella/solutions.md: the passages copied word for word from the source (see pedagogy.md, Polish 1) make long line blocks at 390 px. Splitting them would also help the layout.

## Shared issues
None.
