VERDICT: PASS
CONTENT-HASH: 4602df1a2aa26b6f

## Blocking
(none)

## Polish
- sim.js:100 — canvas label "välit +0,240 %" is terse; "hiukkasväli …" would be clearer (code string, not in diff).
- solutions.md:84 — "Fe" for steel: steel is an alloy; "teräs" would be clearer (not in diff).
- glossary.json — liikuntasauma and kaksoismetalliliuska are used in the lesson but not listed; add if wanted.

## Diff
```diff
(empty — the first-pass diff and the orchestrator's two wording changes are applied and correct; nothing further is genuinely wrong)
```

## Checked
- Lint clean (0 errors, 0 warnings); first-pass hunks (lesson.md, solutions.md, sim-spec.md) are present in the files.
- lesson.md:67 misconception now reads "vesi kutistuu 0 °C:n ja 4 °C:n välillä, ja jäätyessään se laajenee. Siksi jää kelluu ja järvet jäätyvät pinnalta." — correct Finnish, physics consistent with line 12.
- exit-ticket.json answer 3 "Tämä 4-asteinen vesi painuu pohjalle" — consistent with the question's "4-asteista"; earlier hyphen/compound polish item is resolved.
- Terms match glossary: lämpölaajeneminen, pituuden/tilavuuden lämpötilakerroin, kelvin, lämpötila.
- Case endings after number plus unit (°C:ssa, °C:seen, mm:n, mm:iin, m pitkä) in lesson, exercises, solutions and sim.js.
- Decimal comma in Finnish text, decimal point in JSON; U+2212 minus; thin-space unit style matches gold lesson; ”…” quotation marks.
- exercises.json texts and units (µm, cm³, mm, l) read: no errors.
- sim.js Finnish strings (buttons, labels, readout, canvas text) and sim-spec.md read: no errors.
- Reading level suitable for 16–19-year-olds; no new wording issues found.
