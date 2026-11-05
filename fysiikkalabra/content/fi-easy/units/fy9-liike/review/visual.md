VERDICT: PASS
CONTENT-HASH: 63ff7bc3c9a8481e

Visual and editorial review of the Selkeä suomi (fi-easy) translation of fy9-liike. Preview: `python3 scripts/build.py fy9-liike` → preview/fi-easy/fy9-liike.html. Checked in Playwright (scripts/_browser) at 390 and 1280 px, with every `details` opened (hints, solutions, model answers, rubrics, Opettajalle).

## Blocking
None.

## Polish
1. Layout: no horizontal page scroll at 390 (scrollWidth 390) or at 1280. The only elements wider than the viewport are the stage TOC strip, which scrolls sideways as designed, and figure paths at 1280 that the SVG clips. No console or page errors, and no `.katex-error`.
2. LaTeX: every number with a unit, every formula and every table cell is in $…$ with `\,\text{}` units, including the new S2 sentences and the key_concepts ($a = \frac{\Delta v}{\Delta t}$, $(t,x)$-kuvaaja, $x_\text{A}(t) = x_\text{B}(t)$). Decimal comma everywhere, also in the figures (48,5 s; −2,3 km/h per s) and the s3 and s6 tables.
3. Figures: the hero, the concept map, the tram $(t,v)$ graph, the tangent and area diagram, and the s3 model graph render the source figures, with the fi-easy descriptions from figures.json as aria-labels. They are readable at 390 (about 300–358 px wide), the colours follow the course rules (velocity blue, acceleration orange, area green), and all labels are in Finnish.
4. Luvun tärkeät käsitteet: it renders after the opening and before the first stage, with the fixed lead, the Vapaaehtoinen tag, the terms in bold and the formulas typeset. There are no note fields (§12.8–9).
5. Tables (s3 train, s6 video) fit at 390 without scrolling.
6. Language: natural Selkeä suomi, short connected sentences, no fragments apart from pedagogy.md finding 6, and quotation marks ”…” as in the source. teacher.md renders in Opettajalle.

## Shared issues
7. The source-note box ("Keksitty esimerkkiaineisto · …") uses a pill radius. At 390 the three-sentence S2 note for s4 (Keskinopeusvalvonta) becomes an oval with text close to its curved edges (not clipped). Fix in the shared CSS: a smaller border-radius when the note wraps to more than one line.
