VERDICT: PASS
CONTENT-HASH: 37c379ba50e81e4a

Visual & editorial review of the English translation of fy9-koe. Preview built with `python3 scripts/build.py fy9-koe` (preview/en/fy9-koe.html), checked in Playwright at 390 and 1280 px with every details element open.

Results: no horizontal page scroll at 390 (scrollWidth 390) or 1280; no page errors or console errors; 0 KaTeX errors and no raw `$` in the rendered text; no decimal comma left in any formula or figure label (all figures drawn with the decimal point: 1.0 s, 2.48 m, 0.62 m/s, 0.900 m, 3.68 s², 4.03 s²/m); no Finnish text on the page apart from the language menu's "Suomi" / "Selkeä suomi"; the solutions' structural headings render in English. The command-word table wraps cleanly at 390 (358 px); the pendulum data table fits. Figures: hero (no text), seven-step cards, x(t) graph and T²(L) graph all translated, aria-labels translated, readable at 390 (358 px wide; the T²(L) figure 298 px). Language: natural, consistent British physics English (metres, tyre, lorry, programme, "work–energy principle", "significant figures", "free-fall acceleration").


Re-review (2026-11-04) after the "fold" tags were translated: rebuilt with `python3 scripts/build.py fy9-koe` and checked preview/en/fy9-koe.html in Playwright at 390 and 1280 px with all 85 details open: scrollWidth 390 / 1280, no page or console errors, 0 KaTeX errors, no raw `$`, the 24 question summaries carry the pill "REVIEW TEST FY1" … "FY8" (CSS uppercase) followed by the question title, fitting on one row with the title at 390 px; no "Kertaustesti" anywhere in the HTML. No earlier Blocking finding existed; nothing regressed.

## Blocking
None.

## Polish
1. Seven-step figure at 390 px: the grey right-hand descriptions ("an estimate or a comparison") are about 11 px and come close to the step name on row 7; legible but tight. Same as the Finnish figure (shared figures.py), so a change belongs in lessons/units/fy9-koe/figures.py, not in the translation.
2. T²(L) graph in solutions s2 is drawn at 298 px at 390 (smaller than the other figures); point labels are small. Shared figure, as in the source.
3. unit.md Worked example: "*Given and find* is Given and Find" reads as a repetition (see pedagogy.md Polish 1).
4. tasks.json s3 "at $13.00$": a clock time typeset as a math number; plain "at 1 pm" reads better.
5. Colon as a division sign ($20 : 3.6 : 5$, $15.0 : 1.68$, $x : t$) is Finnish usage; acceptable in Answer A as a student's notation, elsewhere / or ÷ is more natural in English.
