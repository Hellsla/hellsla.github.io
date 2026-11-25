VERDICT: PASS
CONTENT-HASH: ccb612016d41f41b

## Blocking

## Polish
- solutions.md:263–267 (L3-04): $\Delta T_\text{talvi}$ is defined only in the Taulukon lukeminen line. Repeating it under the Kaava block would make the sign of $g_\text{max} = g_\text{raja} - \alpha l_0\Delta T_\text{talvi}$ self-evident. This item is carried over from the last round.
- exercises.json L3-04 (`answer` 13.2, `tolerance` 0.03): the checker accepts about $12{,}8$ to $13{,}6\,\text{mm}$. A student who enters the safe rounded value $14\,\text{mm}$ that the Vastaus recommends is marked wrong. The stored value was kept by instruction, so this is not blocking. A fix would be a task sentence asking for the computed value, or a tolerance that includes 14.

## Checked
- The diff (solutions.md:275 Vastaus) restores the safe rounding: "alaraja pyöristetään ylöspäin: vähintään $14\,\text{mm}$". The statement that the results hold to two figures now has the explicit exception for the lower limit. This resolves the previous Blocking item and agrees with the guardrail that a "vähintään" value is rounded up.
- Recomputed: $g_\text{min} = 12\cdot10^{-6}\cdot25{,}0\cdot44 = 13{,}2\,\text{mm}$ and $g_\text{max} = 30 - 12{,}0 = 18{,}0\,\text{mm}$. Both agree with answers.py and with `answer` 13.2.
- A $13\,\text{mm}$ gap would close at $51{,}3\,{}^\circ\text{C} < 52\,{}^\circ\text{C}$, which is unsafe. A $14\,\text{mm}$ gap closes at $54{,}7\,{}^\circ\text{C} > 52\,{}^\circ\text{C}$, which is safe. So 14 mm is the correct two-figure minimum.
- $g_\text{max} = 18\,\text{mm}$ as an upper limit needs no rounding, because 18,0 is exact to two figures.
- Mallivastaus c) is unaffected: $13{,}2 < 15 < 18\,\text{mm}$, the summer margin is $1{,}8\,\text{mm}$, and the winter gap is $27\,\text{mm} < 30\,\text{mm}$.
- The hash was the same at the start and the end (ccb612016d41f41b).
