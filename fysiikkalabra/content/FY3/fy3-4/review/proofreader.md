VERDICT: PASS
CONTENT-HASH: df8f771931cfbeb4

## Blocking
(none)

## Polish
- lesson.md:51 — "Se vastaa noin 180 kg:n massan painoa pienellä ikkunalla" is slightly ambiguous ("pienellä ikkunalla" could attach to the wrong noun). Optional: "Se vastaa noin 180 kg:n massan painoa, vaikka ikkuna on pieni." Not applied; meaning is clear.

## Diff
```diff
```
(empty: round-1 diff confirmed applied; nothing further is genuinely wrong)

## Checked
- Round-1 diff applied in full: exercises.json L1-05 and L3-03, exit-ticket.json q1 and q3, lesson.md "vesi ulottuu" and "nastan", sim-spec.md "Kuolleenmeren", sim.js:34 "ρg:n verran".
- New example (lesson.md:45-51, underwater observation-room window): grammar, spelling and case endings correct ("12 m:n syvyydessä", "180 kg:n massan").
- The old physics contradiction (the diver not feeling the force on the palm) is resolved: the window has room air on the inside, and the diver's body is described separately.
- Decimal comma in prose and LaTeX (0{,}015, 1{,}8 kN); units with thin space inside LaTeX; kPa, cm², kN used correctly.
- Terminology matches glossary.json: paine, hydrostaattinen paine, ilmanpaine, ylipaine, kokonaispaine, tiheys.
- Reading level suitable for 16-19-year-olds; sentences short, no unexplained terms.
- No leftover "kämmen" or "palm" in lesson.md, exercises.json, solutions.md, exit-ticket.json or sim files.
- lint_lesson.py fy3-4: 0 errors, 0 warnings. Hash unchanged between start and end of review.
