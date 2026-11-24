VERDICT: FAIL
CONTENT-HASH: 4c5a23b8baf24e5f

## Blocking
- solutions.md:275 (fy3-8-L3-04, Vastaus a) — **A, significant figures and a limit value (guardrail "a limit value is rounded to the safe side").** Because the diff removed "käytännössä vähintään $14\,\text{mm}$", the Vastaus now says that, since $\alpha$ has two figures, "tulokset kelpaavat kahteen numeroon pyöristettyinä". For a) that gives $13\,\text{mm}$. This is a "vähintään" value rounded down, onto the unsafe side. A $13\,\text{mm}$ gap closes at $8 + 13/0{,}30 = 51{,}3\,{}^\circ\text{C}$, which is below the summer maximum of $52\,{}^\circ\text{C}$. This is Round 1's Blocking item again. The pedagogy reviewer's point was the clash between "14 mm" and "two figures", not the 14 mm itself. — Fix: restore the safe rounding and resolve the clash in the same sentence, for example: "a) $g_\text{min} = 13{,}2\,\text{mm}$; alaraja pyöristetään ylöspäin, joten kahdella numerolla vähintään $14\,\text{mm}$. b) $g_\text{max} = 18\,\text{mm}$ (ylärajana alaspäin)." The Finnish solutions.md:277 has the same change, and the same fix applies there.

## Polish
- solutions.md:263–267 (L3-04): $\Delta T_\text{talvi}$ is defined only in the Taulukon lukeminen line. Repeating it under the Kaava block would make the sign of $g_\text{max} = g_\text{raja} - \alpha l_0\Delta T_\text{talvi}$ self-evident. This item is unchanged from the last round.

## Checked
- Recomputed: $g_\text{min} = 12\cdot10^{-6}\cdot 25{,}0\cdot 44 = 13{,}2\,\text{mm}$ and $g_\text{max} = 30 - 12{,}0 = 18{,}0\,\text{mm}$. Both agree with answers.py, `answer` 13.2 and `tolerance` 0.03.
- A $14\,\text{mm}$ gap closes only at $54{,}7\,{}^\circ\text{C} > 52\,{}^\circ\text{C}$, so 14 mm is the safe two-figure minimum.
- Mallivastaus c) is unaffected: $15\,\text{mm}$ lies between $13{,}2$ and $18\,\text{mm}$, the summer margin is $1{,}8\,\text{mm}$, and the winter gap is $27\,\text{mm} < 30\,\text{mm}$.
- Nothing else in the set changed. The hash was the same at the start and the end.
