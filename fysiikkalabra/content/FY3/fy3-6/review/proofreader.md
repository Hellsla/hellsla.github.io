VERDICT: PASS
CONTENT-HASH: b649f8347a2b2968

## Blocking
(none)

## Polish
- lesson.md:8 — "kuumenee samalla energialla moninkertaisesti enemmän" is slightly pleonastic — "kuumenee samalla energialla moninkertaisesti" (optional, not in diff).

## Diff
```diff
```
(empty: the round-3 first-pass hunk at lesson.md:102 is applied and correct; no further language errors found)

## Checked
- lesson.md:102 — "kappaleen lämpökapasiteetti 0,200 kg · 374,6 J/(kg·K) ≈ 75 J/K" is now present; sentence compares heat capacities with heat capacity, correct case and spacing
- lint_lesson.py fy3-6: 0 errors, 0 warnings (not repeated)
- lesson.md: decimal comma, spaced units, inflected units (24,6 °C:seen, 0,200 kg:n, 3,0 kg:aan, 80-asteista), no "80 N voimalla" patterns
- lesson.md:100-102, 115 — idiomatic Finnish ("jaettu puolittain", "kerrottu auki", "selittyy lukematarkkuudella"); no meaning errors
- exercises.json — all 12 task texts: grammar, case after number-plus-unit, minus signs (−22 °C, −4,0 °C), "negatiivinen Q" wording fine
- solutions.md — all 12 solutions: terms (lämpömäärä, lämpökapasiteetti, tasapainolämpötila) consistent with tasks; minus U+2212; no numbers/formulas judged
- exit-ticket.json — 3 checks: correct Finnish, "kuumaa on kolme kertaa enemmän ... (65 °C)" consistent with the lesson
- sim-spec.md and sim.js strings (Upota, readout, intro paragraph, axis labels): Finnish and non-breaking spaces before units correct
- Terms vs glossary.json: ominaislämpökapasiteetti, lämpökapasiteetti, kalorimetri, lämpötasapaino, tasapainolämpötila, lämpömäärä all match
- Proofreader hash identical at start and end (b649f8347a2b2968)
