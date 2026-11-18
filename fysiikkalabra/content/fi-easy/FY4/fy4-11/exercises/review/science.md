VERDICT: PASS
CONTENT-HASH: 0d9f6781a76891b9

## Blocking

## Polish
- content/fi-easy/FY4/fy4-11/exercises/solutions.md:204 (L3 two cars, Kaava) — "Autot eivät törmää, jos $d$ ja edellä ajavan pysähtymiskohta yltävät takana ajavan pysähtymiskohtaan" is hard to parse; say "Takana ajava ei törmää, jos se pysähtyy viimeistään edellä ajavan pysähtymiskohtaan, eli $d + s_1 \ge s_2$; rajatapauksessa $d + s_1 = s_2$."
- solutions.md:87 (Kaava) — "Lisäksi Jarrutusmatka" has a capital mid-sentence.
- solutions.md:215 (L3-04 Kaava) — the new derivation is followed by "$t_\text{r}$ = leikkauskohta" as a bare fragment; "Suoran leikkauskohta pystyakselilla on $t_\text{r}$ ja kulmakerroin $\tfrac{1}{2a}$" ties it to the line just derived.
- solutions.md:135, 152 — two equations run together with only a full stop or "joten … joten"; a linking word ("Siksi") reads better.
- Earlier polish (L3-04 51–52 km/h; L2-10 air resistance) still open; not part of this change.

## Checked
- Hash 0d9f6781a76891b9 at the start and the end; since 062f457c28^ only solutions.md changed: `**Kaava:**` lines plus two Sijoitus lines (L3 airbag/crumple 0,600 m and the μ = 0,8 braking task) reordered to substitute into the final symbolic form; numbers, answers, tolerances, tasks, ids, exercises.json and answers.py unchanged.
- Recomputed the two reordered Sijoitus lines: $70{,}0 \cdot 13{,}89^2 / 1{,}200 = 11\,253\,\text{N}$, $\Delta t = 0{,}08640\,\text{s}$; $22{,}22^2/(2 \cdot 0{,}8 \cdot 9{,}81) = 31{,}5\,\text{m}$, $a = 7{,}85\,\text{m/s}^2$: as before.
- Braking distance now derived from $s_\text{j} = \tfrac12 v_0 t_\text{j}$ and $t_\text{j} = v_0/a$ as in the brief's lesson; $a = \mu g$ from $\Sigma F = ma$, $F_\mu = \mu N$, $N = mg$ (level road stated in the tasks).
- Impulse steps start from $I = F\Delta t$, $p = mv$, $I = \Delta p$; $F_\text{ka} = m\Delta v/\Delta t$ as the lesson.
- L3 30 km/h task: $v_0^2/(2a) = (d - v_0 t_\text{r}) + v^2/(2a)$ correctly reasoned (constant deceleration); consistent with Sijoitus.
- L3-04 quadratic $\tfrac{1}{2a}v^2 + t_\text{r} v - d = 0$, positive root right.
- Data task: $\Sigma F = ma$, $a = \Delta v/\Delta t$ → $F = m\Delta v/\Delta t$ per interval; valid.
- Two-cars rajatapaus $d = v_0 t_\text{r} + v_0^2/(2a_2) - v_0^2/(2a_1)$ unchanged and matches Sijoitus.
- Every Sijoitus substitutes into the last symbolic form shown.
- Captures: none opened (fi-easy judged from text and the packet).
