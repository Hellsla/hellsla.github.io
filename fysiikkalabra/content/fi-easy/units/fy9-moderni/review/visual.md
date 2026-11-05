VERDICT: PASS
CONTENT-HASH: 99d9cf49a3fb1eb9

Visual and editorial review of the Selkeä suomi (fi-easy) translation of fy9-moderni. The preview was built with `python3 scripts/build.py fy9-moderni` (preview/fi-easy/fy9-moderni.html). I checked it in Playwright at 390 px and 1280 px with every details element opened.

Results: there is no horizontal page scroll at 390 px (scrollWidth 390), no KaTeX errors, no raw `$` text and no page or console errors. All figures are drawn in the language with a decimal comma: hero, kartta, fotonit, puolitus, the two reused binding-energy graphs, s3-p and s3-fit. They are 358 px and 298–324 px wide at 390 px, and their labels are readable, the same as the source that passed. Every aria-label description is translated into plain sentences. The tables (three sources, photocell, Ba-137m data) fit at 390 px. The key-concepts block renders correctly at both widths, with a KaTeX `$E = hf$`. LaTeX is used for every number and unit, and decimal commas are `{,}` throughout.

## Blocking
None.

## Polish
1. inquiry.json activities[7].text (Tutki): "Tee näin:" with steps 1–4 renders as one paragraph at both widths because there is no blank line before the list. Fix: "Tee näin:\n\n1. Päättele …".
2. sovella/solutions.md, s2 Järkevyys of c): "Tasot ja syaani viiva sopivat siis yhteen". Correct form: "syaanin viiva".
3. sovella/solutions.md, s2 Yleisiä virheitä: "c-kohdassa syaaniin viivaan lisätään". Correct form: "syaanin viivaan".
4. inquiry.json activities[19].solution: "Lähteessä on satojatuhansia becquerelejä". Better: "Lähteen aktiivisuus on satojatuhansia becquerelejä" (also science Polish 2).
