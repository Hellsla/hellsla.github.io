VERDICT: PASS
CONTENT-HASH: 8e3ef3e145da510f
## Blocking
(none)
## Polish
- solutions.md:L2-02 Sijoitus — "160 kJ + 0 = 160 kJ" — "+ 0 kJ", as the first pass did for L1-02 (consistency only; not applied)
- lesson.md:11 — "kaksi eri lämpötilassa olevaa kappaletta koskettavat" — "koskettavat toisiaan" reads more smoothly (not applied)
## Diff
```diff
```
(empty: the first-pass diff is applied and confirmed; nothing else is wrong)
## Checked
- First-pass diff present: ”…” quotes in lesson.md (lines 6, 46, 50), "sisäenergiaa", "kuuman kipinän lämpötila", Tiivistelmä wording, "−8,4 kJ + 0 kJ" in solutions.md L1-02
- Hash re-run before and after: 8e3ef3e145da510f, unchanged during review
- Lint: 0 errors, 0 warnings, not repeated
- Glossary terms (sisäenergia, lämpö, lämpömäärä, systeemi, termodynamiikan ensimmäinen pääsääntö) used consistently and match definitions; no "lämpöenergia"; the working-tree glossary.json change (fy3-6 terms) does not touch fy3-5 entries
- Unit inflection in all 12 exercises (0,20 m:n, 300 N:n, 2,0 kW:n, 250 W:n, 5,0 kg:n, 0,15 m:n) and solutions correct
- Decimal comma in text, decimal point in JSON; true minus sign (−) in Finnish text; spaces before units; no N/kg
- exit-ticket.json and exercises.json: no straight quotes in Finnish text, cases and punctuation fine
- Reading level suits 16–19-year-olds; no sim.js or sim-spec.md in this lesson
