VERDICT: PASS
CONTENT-HASH: cc0a19c351929d5f

# Proofreader, fy3-1, round 2

## Blocking
None.

## Polish
1. solutions.md:23 — "Maassa laite painaisi noin 294 N" still uses "laite painaisi voiman" phrasing; optional: "Maassa laitteen paino olisi noin 294 N". Not applied: understandable, no terminology error.

## Diff
```diff
```
(empty: nothing is genuinely wrong)

## Checked
- lint_lesson.py: 0 errors, 0 warnings.
- sim-spec.md rewritten sentence ("Palkkikaavion palkit ovat verrannollisia painoon valitulla massalla: asteikon täysi arvo ... m · 24,8 N ..."): grammar, case endings and paino/massa terminology correct.
- solutions.md:7 "1 kg:n massan paino on noin 10 N, joten 4,0 kg:n massan paino on noin 40 N": inflection (kg:n) and paino as force correct.
- solutions.md:63 "Kuussa paino on 1,62 / 9,81 ≈ 1/6 Maan painosta, joten se pienenee noin 5/6 eli 83 %": correct, space before %.
- sim.js:50 readout "Palkkikaavion asteikko 0–… N on tämän massan paino Jupiterissa.": grammatical, en dash, decimal comma via fi(), space before unit.
- sim.js:93 canvas label "asteikko 0–… N": short, correct, matches the readout.
- Other sim.js strings (note line 35, title line 89, readout line 48) and exercises.json / exit-ticket.json: unit inflections (N:n, kg:n, N:sta, N:iin), Finnish quotes, minus signs fine.
- Glossary terms (massa, paino, voimamittari, vuorovaikutus) consistent; reading level suits 16-19-year-olds.
- Hash checked at start and end: unchanged (cc0a19c351929d5f).
