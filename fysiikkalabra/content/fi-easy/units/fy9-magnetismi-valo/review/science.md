VERDICT: PASS
CONTENT-HASH: 92d38a396fa55df5
SCOPE: full: the fi-easy unit (unit.md, inquiry.json, exit ticket, teacher.md) with its Sovella task set; the three new ```pysahdy boxes judged first against the Finnish unit (PASS e8fc07600488a929).

## Blocking
None.

## Polish
- s9 Yleisiä virheitä, line 1: this is carried over from the last round. It names only "$5{,}0 - 3{,}0\,\text{mWb}$". The Finnish text also names using only the final value $3{,}0\,\text{mWb}$. This is the one number in the fi text that is not in fi-easy. The physics is right.
- teacher.md "Arviointi" ("muut viisi", $95$ points, "kaikki aineistot keksittyjä") is out of date in the same way as in the Finnish text. There are 9 tasks and $137$ points, and s7 uses CERN data. This is teacher-facing text, not physics.
- "Kun tanko liikkuu kentässä, sen jännite on $e = vBl$" does not say that $v$, $\overline{B}$ and the rod must be perpendicular to each other. The same is true of the Finnish text, so this is not blocking.

## Checked
- `units.py hash --lang fi-easy` gave 92d38a396fa55df5 at the start and at the end. `practice.py check` is OK in fi, en and fi-easy (9 tasks, $137$ points).
- **Pysähdy boxes.** Each one matches the Finnish box in physics:
  - Box 1: a voltage needs a changing flux; with constant flux there is none.
  - Box 2: the force is always perpendicular to the velocity, so it changes only the direction. This agrees with the johda box.
  - Box 3: the refraction angle is larger than the incidence angle, so the ray bends away from the normal. "Silloin" refers back to $n_1 > n_2$ in the question.
  - The selkosuomi wording splits only the "joten" sentences and adds no condition or claim.
- **Other changes since 43b392b3:**
  - The hero, ympyra and rajakulma figures are now the same webp files as in the Finnish unit. I viewed them. In ympyra, the charge is positive, $\overline{B}$ points into the page, the motion is counterclockwise and $\overline{F}_\text{M} = Q\overline{v} \times \overline{B}$ points to the centre at all four points. In rajakulma, $\alpha_2 = 90^\circ$ at the critical angle, there is a weak reflection, and the reflection is total when $\alpha_1 > \alpha_\text{r}$.
  - The inquiry change only splits paragraphs. Each part matches word for word.
- **Same as the Finnish unit:**
  - Every number in unit.md, inquiry.json, teacher.md, exit-ticket.json, tasks.json and solutions.md, outside the SVGs, matches the Finnish files (multiset comparison). The only difference is the s9 line above.
  - Every non-text field matches the fi files: correct options, answers, tolerances, units, points, figures and kinds.
- **My own formulas in one script, side by side with answers.py; all agree:**
  - s1: $565{,}5$ and $399{,}9\,\text{V}$; $375$ and $7{,}5\,\text{A}$; $0{,}225\,\%$
  - s2: $81{,}81^\circ$; $68{,}6$ and $0{,}707\,\mu\text{s}$; $0{,}897\,\text{mW}$
  - s4: $24{,}0^\circ$ and $103\,\text{nm}$
  - s5: $533{,}0$ and $532{,}2\,\text{nm}$
  - s6: $18{,}29\,\text{MHz}$; $3{,}914 \cdot 10^7\,\text{m/s}$; $0{,}341\,\text{m}$; $80$ turns; $4{,}37\,\mu\text{s}$
  - s7: $2{,}9978 \cdot 10^8\,\text{m/s}$; $1{,}089\,\mu\text{J}$; $436\,\text{MJ}$; $753$ cars
  - s8: $1{,}5$; $0{,}75\,\text{ns}$; $41{,}8^\circ$
  - s9: $2{,}4$ and $1{,}8\,\text{V}$; $0{,}369\,\text{J}$; $0{,}25\,\text{s}$
  - the unit's own numbers:
    - hook: $174\,\text{A}$ and $15{,}1\,\text{kW}$
    - Tutki: $18{,}7$ and $34{,}6\,\text{mW}$
    - siipi: $0{,}391\,\text{V}$; Sirius: $9925\,\text{K}$
    - ikkuna: $3{,}42\,\text{m}$; öljy: $580\,\text{nm}$
    - virhe-siirto: $826\,\text{kW}$; muuntaja: $12{,}0\,\text{V}$
    - timantti: $2{,}42$; lt-wire: $0{,}40\,\text{mN/m}$
- **Unit prose read in full.** Every condition is stated: the formula conditions, the long wire and long coil, $|Q|$, $v \ll c$, the ideal transformer, $P_\text{h} = RI^2$ and not $U^2/R$, and angles measured from the normal. The text uses "muuttuu sisäenergiaksi" (P1). No later-course physics.
