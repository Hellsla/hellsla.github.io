VERDICT: PASS
CONTENT-HASH: a4218abbc5a602f5

# Proofreader, fy3-1, second pass of the round (previous diff applied)

## Blocking
None.

## Polish
1. solutions.md:7 — "Yksi kilogramma painaa noin 10 N" uses the same loose "massa painaa voiman" phrasing as the two sanity checks already reworded in L2-01 and L2-02; optional: "Yhden kilogramman paino on noin 10 N, joten 4 kg:n massan paino on noin 40 N." Not applied, since it is understandable and not a terminology error.

## Diff
```diff
```
(empty: nothing is genuinely wrong)

## Checked
- lint_lesson.py: 0 errors, 0 warnings.
- Applied lesson.md:21 "Jupiterissa pilvien yläpinnan tasoa" and lesson.md:52 "sen lukema muuttuu, kun sama kappale viedään toiseen paikkaan": grammar and meaning correct, "se" ambiguity gone.
- Applied solutions.md:47 and :55 sanity checks ("5 kg:n massaa", "100 g:n kappaleen paino ... 60 g:n kappaleen paino"): inflection and paino-as-force correct.
- sim.js:92 label "asteikko 0–62 N (paino Jupiterissa)": unspaced en dash, decimal comma via fi(), space before unit, "paino" as force; it is also shrunk to fit now, so the earlier width concern is resolved.
- sim-spec.md, sim.js strings (lines 28, 35, 46-48, 82, 88, 92): glossary terms (massa, paino, voimamittari, vuorovaikutus) correct.
- Number-plus-unit cases in exercises.json, exit-ticket.json, solutions.md (4,0 N:n, 12 N:n, 0,20 kg:n, 22,0 kg:n, 29 N:sta, 4,9 N:iin, 5,0 kg:n): all inflected.
- Finnish quotes ”painan 70 kiloa”, minus signs (G_Maa − G_Kuu), decimal commas in prose: fine.
- Paino is a force and massa is kg throughout; no "aste"/unit confusion; reading level suits 16–19-year-olds.
- Hash checked at start and end: unchanged (a4218abbc5a602f5).
