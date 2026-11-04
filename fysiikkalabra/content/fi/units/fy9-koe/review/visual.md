VERDICT: PASS
CONTENT-HASH: b2f0b8b8cd894742

Delta review: unit.md "Sähköinen koe", paragraph after the Osa list (new sentence: "Tämä on kokeen yleinen rakenne: tehtävien kysymysmuodot ja Osan I kohtien määrä vaihtelevat kokeesta toiseen, joten tarkista ajantasainen rakenne ylioppilastutkintolautakunnan ohjeista."). Previous PASS hash: 8cf0da264f14bed3.

## Blocking
(none)

## Polish
1. [Minor] unit.md "Sähköinen koe", same paragraph — "tarkista ajantasainen rakenne ..." and two sentences later "Tarkista ne ajantasaisina ..." repeat the verb and adjective; fix: merge into one sentence at the end, e.g. "Sallitut apuvälineet ja ohjelmat sekä kokeen ajantasainen rakenne on kerrottu ylioppilastutkintolautakunnan ohjeissa; tarkista ne ennen koetta ja harjoittele kokeen ohjelmilla etukäteen."
2. (Carried over, not re-judged) the earlier Polish items in the unit's other stages.

## Checked
- Built preview (python scripts/build.py, then scripts/screenshot.py fy9-koe; 138 captures). Opened the paragraph at 390 px (koe-390-0): wraps cleanly, no formulas in the new text, no clipping, no horizontal scroll. Read the diff (one paragraph; the rest of the unit is unchanged).

## Scores
illustrations 5 · typography 5 · Finnish 4 · accessibility 4

## Follow-up (4.11.2026, hash 4ff9fa1cddf8ae89)

Delta: one bullet deleted from teacher.md "Kertaustestin käyttö" (FY7 caveat; b6de518c4). Captures retaken (`python scripts/screenshot.py fy9-koe --if-stale`, 138 captures). Opened teacher-390-2 and teacher-1280-1.

### Blocking
(none)

### Polish
1. [Minor] teacher.md "Kertaustestin käyttö", first bullet: "palaute nimeää sen [luvun]" is now untrue for the FY7 items, whose feedback still reads "Kertaa tämä moduulissa FY7." without a chapter link (inquiry.json testi-19/20/21). Editorial consistency only here; the fix belongs to the content (see pedagogy.md Follow-up).

### Checked
- The list now has three bullets; spacing between bullets and the headings "Kertaustestin käyttö" and "Parityö" is even at 390 and 1280 px, no gap or orphan marker where the bullet was. Wording flows: diagnostic use → collect hard modules → nothing stored.
- grep "FY7" over the unit: teacher.md and unit.md no longer mention FY7; no remaining text says the chapters are missing.

## Follow-up 2 (4.11.2026, hash b2f0b8b8cd894742)

Delta: FY7 feedback links (inquiry.json testi-19/20/21) and developer.md line 17. Built preview and rendered the FY7 folds at 390 px in Playwright (scratch script; answered testi-19 = 58,75, testi-20 option 3, testi-21 = 30, and for comparison testi-24 = 91,2). Captures opened: fb-19, fb-20 (scratchpad), contact-3 (#34–#36, FY7 folds closed-state layout).

### Blocking
1. [Major, pre-existing, not FY7-specific] Numeric common-mistake feedback displays Markdown links literally. site/inquiry.js §4 sets `out.textContent = m.feedback`, so testi-19 shows "… Kertaa luvussa [\*Valon heijastuminen ja taittuminen\*](fy7-10.html)." with the brackets, asterisks and file name visible, and the same goes for testi-21 → fy7-4. This affects 29 mistake feedbacks in 12 numeric items of this unit (FY1–FY8, e.g. testi-24 → fy8-3). Other units whose mistakes carry links probably have the same problem. The new FY7 text repeats an existing pattern rather than introducing a new one. Still, the link does not render where the coordinator asked to check it. Fix (code, not content): render the mistake feedback's Markdown at build time (scripts/inquiry.py, as choice feedback already is) or in inquiry.js. It can wait only if accepted as a known site-wide issue.

### Checked
- Choice feedback (testi-20, all 4 options): renders a real link `<a href="fy7-5.html"><em>Sähkömagneettinen induktio</em></a>`, italic, underlined, wraps cleanly at 390 px, no horizontal scroll (scrollWidth 390).
- Titles and targets match meta.json for fy7-4, fy7-5, fy7-10; files exist in site/.
- KaTeX in the testi-19/21 mistake feedback renders.

## Follow-up 3 (4.11.2026, hash b2f0b8b8cd894742)

Re-check after the code fix: scripts/inquiry.py gives a Markdown mistake feedback an `html` field, and templates/inquiry.js uses it via innerHTML. Content hash unchanged. Rendered the rebuilt preview at 390 px in Playwright (testi-19 = 58,75, testi-20 option 3, testi-21 = 30, testi-24 = 91,2) and opened fb-19 and fb-21 (scratchpad captures).

### Blocking
(none). Follow-up 2 item 1 is resolved. The numeric mistake feedback now shows real links: fy7-10 for testi-19, fy7-4 for testi-21 and fy8-3 for testi-24, alongside the fy7-5 choice links. The links are italic and underlined, KaTeX is typeset, there is no raw Markdown, and scrollWidth is 390.

### Polish
1. site/inquiry.js does not have the change yet; only templates/ and preview/ do. A full build is needed before the fix reaches the published site.
