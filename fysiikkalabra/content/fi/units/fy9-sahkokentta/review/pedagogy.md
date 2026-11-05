VERDICT: PASS
CONTENT-HASH: 9c10b36b9630971c

## Delta review
Delta review, 2026-11-04 (previous PASS hash 29b45f18108766eb). `git diff HEAD -- content/fi/units/fy9-sahkokentta lessons/units/fy9-sahkokentta` shows one changed line: `sovella/tasks.json`, s1 b rubric criterion `calculation` (1 p). The long formula with the fraction inside the square root is now three formulas: $F_\text{s} = 4{,}93 \cdot 10^{-4}\,\text{N}$ ja $k = 8{,}988 \cdot 10^{9}\,\text{N}\cdot\text{m}^2/\text{C}^2$, joten $q = 0{,}080\,\text{m} \cdot \sqrt{F_\text{s}/k} \approx 1{,}87 \cdot 10^{-8}\,\text{C}$ ja $n \approx 1{,}2 \cdot 10^{11}$. Nothing else changed in the unit.
- The criterion keeps its meaning and its 1 p; the rubric total is unchanged. Naming $F_\text{s}$ and $k$ first is clearer for the grader, and it uses the same symbols as the preceding criterion ($q = r\sqrt{F_\text{s}/k}$). Nothing is given away to the student, because this is the model rubric.

## Previous review

Round 2 (delta review of round 1 fixes; round 1 hash 63bd93568ec525b8). Pedagogy review of fy9-sahkokentta, 2026-11-04.

## Blocking from round 1
1. **s1 a model force diagram: fixed.** `sovella/solutions.md` s1 a has a new **Voimakuvio:** line with the figure `fy9-sahkokentta-s1-fbd`. It comes right after Kysytty and before the Periaate and any equation, as docs/force-diagrams.md requires. The figure has a situation picture and the right ball's force diagram: a body rectangle, red $\overline{G}$, $\overline{T}$ along the thread and $\overline{F}_\text{s}$ away from the other ball, and the angle α. The caption says that the angle is drawn larger than in the task. I opened it at 390 and 1280 px. The force diagram criterion in the rubric now has a model to compare against.

## Polish from round 1, verified
2. oljypisara: retitled "Mikä kuvaus". It still has no figure options, which is acceptable as Polish.
3. aineisto: hint 1 is about reading the graph, hint 2 asks for the energy principle in words, and only hint 3 gives the formula. The task text asks first what the slope says and which way the electron moves.
4. tarkistus-1: the option 1 and option 2 feedback now say that each plate gives a field that does not depend on the distance.
5. tarkistus-2: one final value, 0,11 J (about 110 mJ).
6. teacher.md: the Sovella window names the two calcs done in class (*Pölyhiukkanen sähkösuodattimessa*, *Defibrillaattorin kondensaattori*) and the two left for home.
7. s1 set-up: not changed. The developer's reason is acceptable: the d part, r = r₀/∛2, is the original twist.
- The s4 fix makes the task richer, because the phase versus earth voltage links back to the chapter *Sähköturvallisuus kotona ja työssä*. The new Yleisiä virheitä item targets that misconception.

## Checked again
- Task counts are unchanged: hook 1, Ennusta 6, Tutki 1, Sovella 4 + 4, Tarkista 3, 6 long tasks.
- Rubric sums: 95 points (`practice.py check` OK).
- Feedback names chapters, not ids.

## Shared issues
None.
