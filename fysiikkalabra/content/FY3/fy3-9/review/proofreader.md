VERDICT: PASS
CONTENT-HASH: 2ce27b58d735ec2b

## Blocking
(none)

## Polish
(none)

## Diff
```diff
```
(empty: the seven first-pass wording fixes are already applied and nothing further is needed)

## Checked
- Lint run first: 0 errors, 0 warnings; not repeated.
- First-pass diff confirmed applied: lesson.md:52 (1,04 l sentence), exercises.json L2-04 (single question), L3-01 ("kuplan ilma liukene"), L3-02 ("20 °C:n tallissa"), solutions.md:63 ("Tulon pV arvot"), :79 ("kuin ympäröivä vesi"), sim.js:119 (”Tallenna mittaus”).
- Glossary terms (tilanmuutos, isoterminen, isobaarinen, isokoorinen, Boylen laki, kelvin, absoluuttinen nollapiste, ylipaine, ilmanpaine) used as defined; no invented synonyms.
- Case after number+unit (101 kPa:n, 22 °C:n, 20,0 m:n, 280 kPa:iin, 7 kN:n, 10 °C:sta ... 20 °C:seen, 280 K:stä 308 K:iin) correct in all files.
- Decimal comma in all text, decimal point only in JSON values; space before units and %; minus sign U+2212 in text and sim.js fi().
- Finnish quotation marks (”...”) in sim.js and sim-spec.md; no "N-voimalla" constructions.
- Sim strings (labels, options, readout, note, table, empty row) and sim-spec.md read for grammar and terminology; consistent with lesson.
- Exit ticket and solutions: language and sanity-check sentences read; numbers, formulas, LaTeX untouched.
- Reading level suitable for 16-19 year olds; lesson.md:10 and :12 long but clear.
- Hash re-run at the end: 2ce27b58d735ec2b (same as at start).
