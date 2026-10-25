VERDICT: PASS
CONTENT-HASH: 49e851e9a8306b78

# Proofreader, fy3-1, round 5 (second pass)

## Blocking
None.

## Polish
None.

## Diff
```diff
```
Empty: nothing is genuinely wrong.

## Checked
- First-pass diff confirmed applied: exercises.json L3-03 and solutions.md "Annettu" now read "näyttää kilogrammoina luvun, joka saadaan jakamalla voima arvolla 9,81 m/s²"; same wording matches lesson.md:50 style (jakamalla voima arvolla 9,81 m/s²).
- solutions.md L3-03 sanity check reworded: "3,71/9,81 ≈ 0,38 kertaa Maan g ... noin 2,6-kertainen eli vajaat 70 kg" is grammatical and consistent with 68,75 kg; the rounded-ratio product is gone.
- lesson.md (all 55 lines): decimal commas, thin-space units, ”…” quotes, N:ksi / 1 N:ksi inflections, "kuudesosa", "painaa" colloquialism explained; the Kuu paragraph (line 22) and the summary are grammatical.
- Glossary terms (voima, voimamittari, vuorovaikutus, paino, massa, newton, putoamiskiihtyvyys) used correctly; g only in m/s²; no "N/kg".
- exercises.json: all 12 texts (4,0 N:n voima, 0,20 kg:n kappale, 22,0 kg:n massan) correct inflection and unit spacing.
- solutions.md: all 12 entries, minus sign and decimal commas fine; exit-ticket.json (N:sta, N:iin, kg:na, ”vesi painaa puolitoista kiloa”) correct.
- sim.js Finnish strings (Taivaankappale, Massa m = ... kg, asteikko 0–... N, Sama massa, paino eri paikoissa, note paragraph) and sim-spec.md correct.
- lint_lesson.py: 0 errors, 0 warnings. Hash at start and end: 49e851e9a8306b78.
