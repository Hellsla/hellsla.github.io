VERDICT: PASS
CONTENT-HASH: 77d0c5813b2c4c1b

## Blocking
(none)

## Polish
- lesson.md:338 — "Kohtaamishetkellä kappaleiden kuvaajat leikkaavat toisensa." still only repeats the previous sentence (round 1 item, not applied) — delete it.
- lesson.md:338 — the new negative-direction sentence is correct and answers my round-1 point. It still leaves the figure's own case (A moves +x, B moves -x) without a rule; one clause would close it: "Jos kappaleet liikkuvat eri suuntiin, vertaa suoraan paikkakoordinaatteja." Optional.
- inquiry.json:317, 330 (exp-3 Tarkista feedback) — "Etumatka $x_\text{B} - x_\text{A}$" still names the difference "etumatka", while the sim's calc text now calls it "paikkojen ero" and says it is an etumatka only for +x motion. Both bus and runner do move in +x there, so it is true, but "Paikkojen ero $x_\text{B} - x_\text{A}$" would be uniform with the hints and solution.

## Checked
- Diff is lesson.md:338 (one added sentence), sim `calc` text, hints 2-3 and the solution of the transfer task; no number, formula or figure changed.
- "Negatiiviseen suuntaan liikuttaessa edellä on se kappale, jonka viiva on alempana": physically right (ahead = more negative x = lower line). Finnish correct.
- Sim `calc`: "paikkojen ero ... nolla kohtaamishetkellä; positiiviseen suuntaan se on B:n etumatka" removes the false "positive = B ahead" reading and is accurate for the sign convention.
- Transfer task: hint 2 and 3 values agree (60 m, falls 6,0 m/s = 4,0 + 2,0, zero at 10 s); solution's "Annettu" and "Periaate" lines follow, answer 50 m unchanged and still not given away by hints 1-2.
- Using neutral "paikkojen ero" in the task hints reduces the misconception that etumatka must be positive; no new jump for the student.
- Other "etumatka" uses (opening, Ennuste 3, cyclist and car) concern +x motion and stay valid.
- Hash unchanged at the end (77d0c5813b2c4c1b).
