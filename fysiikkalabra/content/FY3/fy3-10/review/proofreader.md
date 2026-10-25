VERDICT: PASS
CONTENT-HASH: b90850edfaa09776

## Blocking
(none)

## Polish
(none)

## Diff
```diff
```

## Checked
- Lint clean (0 errors, 0 warnings); not repeated.
- The eight first-pass edits are in place: lesson.md:49 (tulokseksi, tuhat- tai miljoonakertaisesti), exercises.json L1-04 (no "tyhjä"), L2-01 (autotallissa), L3-01 (no "keuhkoissa" repetition), solutions.md L1-05 (Grammat supistuvat), exit-ticket.json Q3 (oletuksia ideaalikaasun mikromalliin), sim.js readout (Suhde mitattu/ennuste (= pV/(NT) suhteessa vertailutilaan)).
- lesson.md:44 "Pyöristämätön ainemäärä on 0,207 mol, joten …" reads correctly; 0,207 mol and 0,83 g match 101 000 · 0,0050 / (8,31 · 293,15), and 0,21 mol / 6,0 g for air agree.
- Worked example display (three aligned rows) is LaTeX only; prose around it is intact.
- "yhdistetty kaasulaki" is in glossary.json and meta.json glossary; its use in lesson.md:6 and :27 matches the definition.
- Other glossary terms (ideaalikaasu, tilanyhtälö, ainemäärä, mooli, moolinen kaasuvakio, moolimassa, Avogadron vakio, ylipaine, ilmanpaine, kelvin) used consistently across all files.
- Case after number plus unit (37 °C:n, 250 °C:n, 1,00 l:n, 101 kPa:n, 20 °C:n, 2 s:n) correct; no "80 N voimalla" pattern.
- Decimal comma in Finnish text, decimal point only in JSON values; minus U+2212; sim.js fi() gives comma and U+2212.
- Sim strings and sim-spec.md agree with the lesson wording (Nollaa mittaus, mitattu, ennuste); reading level suits 16 to 19-year-olds.
- Hash unchanged at start and end of review (b90850edfaa09776).
