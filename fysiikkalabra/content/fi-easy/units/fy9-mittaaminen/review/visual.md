VERDICT: PASS
CONTENT-HASH: 167a7e1ffcb6d0db

Visual & editorial review of the fi-easy translation of fy9-mittaaminen (preview/fi-easy/fy9-mittaaminen.html, built with scripts/build.py fy9-mittaaminen).

## Blocking
None.

## Polish
1. [Minor] sovella/solutions.md s5 "Yleisiä virheitä" ("tarkempaa mittaamista") and s6 ("lähes vakio") use straight quotes. Finnish typography uses ”…” as elsewhere in the unit (tasks.json s2, s4). Fix: ”tarkempaa mittaamista”, ”lähes vakio”.
2. [Minor] solutions.md s2 a) Muunnokset ends with a repeated "ja \,\text{mm} = 1000\,\mu\text{m}$". Drop the repetition (it is also in the source).
3. [Minor] for science: see science.md item 1 (key concept "mittausepävarmuus" wording).

## Checked
- Playwright captures at 390 and 1280 with every details element open. No page errors or console errors. No horizontal scroll (scrollWidth equals innerWidth at both widths). No element overflows. No raw LaTeX is left in the page text. No decimal point: the only "d.d" matches are the chapter numbers 1.2.
- Figures at 390: hero, kartta, anatomia, linearisointi, fy3-3 extrapolation-points, s3-pisteet, s3-sovitus, s5-kuvaaja and s6-kuvaaja (298–358 px wide). The labels are readable, they use a decimal comma (0,919; 118,6 g; 2,6 MPa·ml; −1,8 ml) and they have no clipping.
- figures.json: all 24 figure texts are present. The 8 long descriptions (alt texts) are rewritten in short Selkeä suomi sentences, and the short labels are kept.
- The key concepts block at 390: terms in bold, LaTeX k = Δy/Δx renders inline, no input fields.
- Solution cards (Annettu/Kysytty/Periaate/Kaava/Muunnokset/Sijoitus) and the multi-line Sijoitus blocks fit at 390 and 1280. The rubric and self-assessment cards are in Finnish.
- The LaTeX rules hold: quantities and units are in $…$ with \text{} units and {,} decimals, and the formulas are unchanged from the source.

## Scores
illustrations 4 · typography 4 · Finnish 5 · accessibility 4
