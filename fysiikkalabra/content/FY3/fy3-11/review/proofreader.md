VERDICT: PASS
CONTENT-HASH: 10f5b276749a35a6

## Blocking
(none)

## Polish
- exercises.json L2-01 and solutions.md L2-01: "3 830 MWh" uses a space group while other four-digit values do not ("4300 MW", "1200 kW", "3600 s"); pick one style. Not in the diff because the lint may read the number from the text.
- solutions.md L1-03: **Vastaus:** 37 % while exercises.json has answer 37.2 and Sijoitus gives 37,2 %; for the producer or physicist to decide which significant figures to show (not a language matter).
- solutions.md L3-03: "12 040 W" and "54 kWh" are fine, but the space group in "12 040" is the same style question as above.

## Diff
```diff
```
(empty: the 12 hunks of the first pass are already applied; nothing further is genuinely wrong)

## Checked
- First-pass diff confirmed applied: lesson.md (3 hunks), solutions.md (3), exercises.json (3), exit-ticket.json (1), sim-spec.md (1), sim.js "mekaaninen teho" (1); no remaining "mekaaninen työ" in the lesson folder or tests/sims/fy3-11.json (line 501 expects "mekaaninen teho 18,0 kW").
- glossary.json has hukkalämpö, kaukolämpö, lauhdevoimalaitos (fy3-11, valid fields, definitions in correct Finnish); meta.json glossary lists all three.
- Decimal comma, space before units and %, case after number-plus-unit (480 kPa:na, 125 kPa:na, 100 %:n, 30 %:n, 90 %:n, 80 km/h:n, 480 kW:n) consistent in all text files; no decimal points in Finnish text.
- Minus sign U+2212 and en dash in ranges (85–90 %, 10–60 %, 1,5–5,0) correct; litre written as "litraa"/"l" consistently.
- Terminology matches glossary (lämpövoimakone, hyötysuhde, kaasun tekemä työ, lämpökerroin, lämpöpumppu, jäähdytyskone, yhteistuotanto, lämpöarvo); "teho" for kW values, "työ" for J values.
- sim.js Finnish strings (menu, labels, legend, readout, note, "Energia säilyy" lines) and sim-spec.md: grammar and wording fine.
- exit-ticket.json and exercises.json texts: no case or inflection slips; levels read at 16-19 reading level.
- No numbers, formulas, LaTeX or JSON values touched; five `<!-- vaihe -->` stages and both SVGs intact; lint 0 errors, 0 warnings.
- Hash unchanged at start and end of review (10f5b276749a35a6).
