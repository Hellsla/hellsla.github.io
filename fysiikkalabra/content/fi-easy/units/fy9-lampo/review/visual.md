VERDICT: PASS
CONTENT-HASH: f527223788565a17

Visual and editorial review of the Selkeä suomi translation of fy9-lampo (2026-11-04). Preview: `python3 scripts/build.py fy9-lampo` → preview/fi-easy/fy9-lampo.html (draft). Checked in Playwright (scripts/_browser) at 390 and 1280 with every details element and the model answer opened.

Results at both widths:
- No console errors and no .katex-error. The page has no horizontal scroll (scrollWidth 390 and 1280), and no element overflows outside a scroll container.
- No decimal point in rendered math or text. Every decimal is written with a comma, as in "8{,}4", "0{,}886" and "2{,}26".
- The language menu offers Suomi and English. The title and html lang are Finnish.
- "Luvun tärkeät käsitteet" renders with the fixed lead, "Vapaaehtoinen", and five bold terms with their LaTeX formulas.
- The figures are drawn from figures.json. In hero, kartta, kayra and the s3 graph, every label is translated or is a formula, and at 390 they are as readable as the source (kartta 17 px and s3 16 px labels).
- Both tables (the s2 data table and the vertical s3 table) fit at 390.
- Every formula, unit and symbol is in LaTeX, including the new explanations, the key concepts and teacher.md.
- The Finnish is consistent and correct, and figure descriptions were also rewritten in short sentences.

## Blocking
None.

## Polish
1. figures.json, the kayra description: "Kuvaaja näyttää kilogramman lunta lämpötilan T celsiusasteina" is ungrammatical. Fix: "Kuvaaja näyttää, miten kilogramman lumierän lämpötila T celsiusasteina muuttuu."
2. figures.json, the kartta description: "Ylhäällä on solmu energia säilyy:" needs the node name marked off. Fix: "Ylhäällä on solmu ”energia säilyy”:"
3. sovella/solutions.md s1 a) Kysytty: "lämpömäärä $Q$, joka on poistettava, gigajouleina" is clumsy. Fix: "poistettava lämpömäärä $Q$ gigajouleina".

## Shared issues
1. The reused figure fy3-7/melting-curve in Tutki is 324 px wide at 390, so its labels are about 13 px. This is inherited from the FY3 module and already noted in the source developer report.
