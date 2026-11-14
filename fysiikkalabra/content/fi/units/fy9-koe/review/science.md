VERDICT: PASS
CONTENT-HASH: 0a325fe3bad4c4ff
Delta review (hero calculator removed, Part II source-material sentence, 2026-11-14) of the version passed at 33fcccd3aae0531c.

## Blocking
None.

## Polish
- The fi review/developer.md cites https://tiedostot.ylioppilastutkinto.fi/kokeet/2026-03-25_FF_fi/grading-instructions.html for the 5/7 count; FF is the philosophy exam. The physics exam is 2026-03-25_FY_fi (checked: 5 of 7 Part II questions carry Aineisto). The student-facing sentence is right; only the source line in the log needs the FY URL.

## Checked
- Hero figure: all calculator elements (body, display, 12 keys) are removed from the SVG in unit.md and from figures.py; no path or rect of the calculator is left (grep `M930,440`, `M948,452`). The aria-label and the figures.json alt text no longer mention a calculator, and no other "laskin"/"calculator" is left in the unit. This agrees with YTL Reaaliaineiden kokeiden määräykset §3 (fetched 2026-11-14): "ei saa käyttää apuvälineinä erillisiä laskimia eikä erillisiä taulukkokirjoja"; the English test-specific regulations say the same.
- Part III bullet, new sentence (source material in most Part II questions, 4 or 5 of 7 in recent exams): checked against the Board's grading instructions. Spring 2026 (2026-03-25_FY_fi): Tuulivoimala, Hiilidioksidikapseli, Jouset, LED, Carringtonin tapaus have Aineisto, Lentokone kiitoradalla and Radioaktiiviset lähteet do not, so 5/7. Autumn 2025 (2025-09-17_FY_fi): Kuula putkessa, Maalämpö, Jalkaprässi, Aaltoja have Aineisto, the other three do not, so 4/7. "Most" and "four or five of the seven" are both right, and they agree with the Part II bullet (4 of 7, 15 p).
- fi, en and fi-easy say the same thing.
- Hash checked at the start and the end with `python3 scripts/units.py hash fy9-koe --lang fi`.
