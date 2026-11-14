VERDICT: PASS
CONTENT-HASH: 74b50c2bb09b776e
## Blocking

## Polish
- content/fi/FY4/fy4-9/exercises/solutions.md (L3-02 Kaava) — Earlier note still stands: "$F\,\Delta t = mv_0 - 0$" writes the momentum change the wrong way round (initial minus final). Fix: write $-F\,\Delta t = 0 - mv_0$, which matches L2-01.
- solutions.md (L2-07 Vastaus) — Earlier note still stands: $1{,}50\,\text{m/s}$ has three significant figures, so it does not limit the result. Fix: name only the mass $0{,}50\,\text{kg}$ as the limiting datum.

## Checked
- The diff (fi and fi-easy exercises.json, L1-03 only) changes "kohtisuoraan ylöspäin" to "pystysuoraan ylöspäin". "Pystysuoraan" is the correct term for a vertical throw. "Kohtisuoraan" needs a reference surface, which the text did not name. The en text already says "vertically upwards".
- The premise holds. A ball thrown vertically upwards is momentarily at rest at the top, so $v_0 = 0$ follows from the throw. A non-vertical throw would leave a horizontal velocity at the top. The new wording makes the rest at the top exact. (A)
- fi, fi-easy and en say the same thing: vertical throw, struck at rest at the top, leaves at $18\,\text{m/s}$, weight neglected during the strike.
- solutions.md in each language does not use the word that changed, so no solution needs to change. Its $v_0 = 0$ and $I = mv - mv_0 = mv$ still match the task.
- Recomputed: $I = 0{,}27\,\text{kg}\cdot 18\,\text{m/s} = 4{,}86\,\text{N}\cdot\text{s}$, which rounds to $4{,}9\,\text{N}\cdot\text{s}$ (two significant figures). answers.py gives `0.27*18 - 0.27*0` = 4.86. The answer, unit and tolerance (0.02) are unchanged.
- Hash 74b50c2bb09b776e at start and end.
