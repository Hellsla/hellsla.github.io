VERDICT: PASS
CONTENT-HASH: b04487bcb547a68a

## Blocking
(none)

## Polish
(none; the first-pass polish items are all applied, see Checked)

## Diff
```diff
```
(empty: nothing further to change)

## Checked
- Lint run first: 0 errors, 0 warnings; not repeated.
- First-pass diff confirmed applied, all six hunks present: lesson.md "kaasun kokonaispainetta", "Molemmissa tapauksissa", aria-label "Kaasutilan korkeudet"; solutions.md "lämpötilat on käytettävä kelvineinä", "renkaassa, jonka lukema on 0, on silti ilmaa"; sim.js "sitä suurempi paine on". The old wordings no longer occur anywhere in the lesson folder.
- The applied lines read correctly in context; no numbers, LaTeX or JSON values changed. (Hash differs from the first-pass report only because those edits changed the files.)
- Re-read lesson.md, exercises.json, solutions.md, exit-ticket.json, sim-spec.md, sim.js strings: spelling, decimal comma, U+2212 minus, space before units, case after number+unit (101 kPa:n, 10 °C:sta, 20 °C:seen, 20,0 m:n, −18 °C:n) all correct.
- Terms match glossary.json (tilanmuutos, isoterminen, isobaarinen, isokoorinen, Boylen laki, kelvin, absoluuttinen nollapiste, ylipaine); no invented synonyms.
- Finnish quotation marks ”Piirrä p 1/V:n funktiona” and ”Tallenna mittaus” correct; the heading "Yleinen virhekäsitys" is the fixed section name and stays.
- Reading level suits 16-19-year-olds; no paragraph over 91 words.
- Hash re-run at the end: b04487bcb547a68a (unchanged from start).
