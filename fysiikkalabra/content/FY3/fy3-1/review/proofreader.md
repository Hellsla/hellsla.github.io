VERDICT: PASS
CONTENT-HASH: a2b4617ad8b2da13

# Proofreader, fy3-1, review round 3 (second pass)

## Blocking
None.

## Polish
1. lesson.md:29 — "putoamiskiihtyvyys" is not in glossary.json (glossary has "kiihtyvyys", FY4-4) — optional: add the term or write "g (m/s²)"; not a language error.
2. lesson.md:8 — the calibration paragraph is long (about 170 words); optional split after "...2,5 N venyttää sitä 1,0 cm."
3. lesson.md:3, 22 — "astronautti painaa Kuussa" is colloquial verb use while line 48 warns against "painan 70 kiloa"; correct here (force, no unit), optional: "astronautin paino Kuussa on vain kuudesosa".

## Diff
```diff
```
(empty: the first-pass diff is applied and nothing else is wrong)

## Checked
- First-pass diff confirmed in place: sim-spec.md "m · 24,8 m/s²" (twice, both occurrences), lesson.md:52 "Massa kertoo, kuinka paljon ainetta kappaleessa on", lesson.md:8 "joiden kunkin massa on", lesson.md:48, exercises.json L3-03 and solutions.md L3-03 "arvolla 9,81 m/s²".
- lint_lesson.py: 0 errors, 0 warnings.
- No N/kg for g anywhere (lesson, table, exercises, solutions, exit ticket, sim.js strings, sim-spec); g values 1,62 / 3,71 / 9,81 / 24,8 m/s² consistent.
- Decimal comma, space before units, inflections (1 N:ksi, 5,0 N:n, 8,0 N:n voima, 29 N:sta, kg:n, g:n) correct in all files.
- Finnish quotation marks ”…” in lesson.md:48 and exit-ticket.json Q3; no minus-sign slips.
- Terminology paino/massa/voima/vuorovaikutus/voimamittari/newton matches glossary.json; "paino" always a force.
- sim.js Finnish strings (labels, note, readout, title, scale text) correct; reading level suits 16-19-year-olds.
- Hash at start and end: a2b4617ad8b2da13 (first-pass report had 5c94e4e4c798d64e; changed only by the applied diff).
