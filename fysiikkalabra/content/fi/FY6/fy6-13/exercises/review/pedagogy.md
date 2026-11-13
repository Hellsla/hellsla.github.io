VERDICT: PASS
CONTENT-HASH: 33d51071fa114751
SCOPE: delta added-exercise from 6f38db9cc5bb5b1e base 8f23aa7ae3bd

## Blocking
(none)

## Polish
- exercises.json (fy6-13-L1-10) — the question is not the last sentence: "Laske ... nanofaradeina. Käytä sähkövakiota ... ja hae ... MAFY-taulukosta." Put the data instruction first and end with "Laske kondensaattorin kapasitanssi nanofaradeina."
- exercises.json (fy6-13-L2-08) — "toisen kondensaattorin" has no referent in a task read alone; write "erään kondensaattorin". Also end with the question: "Selvitä kapasitanssi kuvaajasta ja vastaa mikrojouleina. Kuinka paljon energiaa ...?" order, question last.
- solutions.md (fy6-13-L1-10, Vastaus) — "vastaus hyväksytään noin ±5 % tarkkuudella" is checker talk, not for the student; drop it.
- fy6-13-L1-10 overlaps L1-04 (plate capacitor from A and d); the new part is the lookup of ε_r, which is the point, but keep a third such Level 1 task out.

## Checked
- Text only (no render) of the added exercises.
- L1-10 recomputed: 8,854·10^-12 · 2,3 · 0,025 : 1,0·10^-4 = 5,09 nF; three conversions (cm², mm, nF) are named and shown; one formula plus a hinted MAFY lookup: level 1, a little heavy but acceptable.
- L2-08 recomputed: C = 120 µC : 8 V = 15 µF; W = ½ · 15 µF · (7,0 V)² = 367,5 µJ; matches answer and tolerance.
- L2-08 is genuinely level 2: C from the slope, then a voltage (7,0 V) that is not on the graph, so area-under-graph shortcut of L1-05 does not apply.
- Figure ex-qu2: line from the origin to (120 µC; 8 V), grid 20 µC and 1 V; the description gives the same data and no C or W.
- Solutions follow the seven parts; reasonableness check by W = ½QU and W < QU is meaningful.
- Finnish and case after number+unit correct; no repeat of the worked example.
- Hash unchanged at the start and end.
