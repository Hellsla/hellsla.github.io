VERDICT: PASS
CONTENT-HASH: 59c94115b15b2cf7
Round: 3

## Blocking
(none)

## Polish
- solutions.md L3-04 c) Vastaus and exercises.json L3-04 c) — "Kokonaiskulutus voi pysyä samana, koska energiaa ei synny eikä katoa" presents the conservation law as the cause of a constant total, but a constant total is the task's assumption (real totals usually fall when combustion losses go away). Also "lisää energiaa saman verran kuin fossiilinen vähenee" reads as if total energy grows. Fix: "käytöt tarvitsevat saman energian, eikä sitä synny tyhjästä, joten vesi- ja tuulivoiman on tuotettava se, minkä fossiilinen tuotti (mallissa kokonaiskulutus oletetaan samaksi)".
- exercises.json L1-07 third option feedback "Ympäristö kuuluu systeemiin" — the task names no system. Write "Kun ympäristö otetaan mukaan systeemiin, ...".

## Checked
- Round-2 item L3-05 resolved: the reflection remark is gone from the task text and from Periaate, so the model "loppu energia muuttuu lämpöenergiaksi" matches a), b), c) and the check 0,14 + 4,86 = 5,00 MJ. The earlier Polish about heat versus reflection no longer applies.
- Recomputed L3-05: stage differences 4,20 / 0,16 / 0,08 / 0,42 MJ, sum 4,86 MJ, panel share 86,4 %, light share 2,8 %. All match the key and solutions.md.
- Diff since round 2 touches only that sentence (exercises.json and solutions.md); no other task changed, and L3-04 (470/1200 = 39,2 %, 218 GJ, over 70 PJ) is still correct.
- FY2 scope holds (no W, no c·m·ΔT, no product of efficiencies).
- Hash 59c94115b15b2cf7 vs. reported value was the same at start and end.
