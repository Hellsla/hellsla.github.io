VERDICT: PASS
CONTENT-HASH: d49bab5db8078c49

## Blocking
(none)

## Polish
(none) The first-pass diff is confirmed applied (lesson.md :31 "Loppu imeytyy", :52 "Tätä sanotaan ilmastonmuutokseksi", :78 "se siirtää vuorokaudessa"; solutions.md :47 "Kylmemmällä säällä", :79 "vielä noin 70 °C:n lämpöistä"; exercises.json L3-01 "Minkä kautta", L3-03 "lämmityskaudella keskimäärin 2,8"). Nothing further is wrong.

## Diff
```diff
(empty: no further changes needed)
```

## Checked
- lint_lesson.py fy3-12: 0 errors, 0 warnings (not repeated)
- First-pass diff present in lesson.md, solutions.md and exercises.json and reads correctly in context
- Decimal comma in prose, U+2212 minus, plain space before units (same as content/_gold, which has no thin spaces)
- Case after number+unit: 96 W:n, 210 W:n, 3,5 kW:n, 1,4 W:n, 30 %:sta, 30 %:sta/29 %:iin, 238 W/m²:stä, 241,4 W/m²:iin, 0,35 W/(m²·K):sta all correct
- Terms vs glossary.json: johtuminen, konvektio, lämpösäteily, energiatasapaino, kasvihuoneilmiö, U-arvo, lämpökerroin, ominaislämpökapasiteetti consistent; no invented synonyms
- No Finnish quotation marks needed (none used); numbers, LaTeX, JSON values and stage markers untouched
- exit-ticket.json, exercises.json (all 12 texts), solutions.md (all 12) and lesson.md read through; no sim.js or sim-spec.md in this lesson (sim false)
- SVG aria-labels and visible labels (heijastuu, takaisin, eriste, sisällä, ulkona) are correct Finnish
- Reading level and paragraph length fine for 16-19 year olds
