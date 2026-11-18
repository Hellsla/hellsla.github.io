VERDICT: PASS
CONTENT-HASH: b916fcbcac5a7c18
SCOPE: delta (work queue 8g round 2: L3-05 mean symbols, F_ka now defined from F_1, F_2, F_3) from previous PASS aed639aa12699893

## Blocking
None.

## Polish
- solutions.md, fy4-3-L3-05 Kaava — $F_1$, $F_2$, $F_3$ are not named as the three sensor readings at the point of use ("lukemien keskiarvo" only implies it); the Annettu line gives the values but not the symbols — fix: "Anturin kolme lukemaa ovat $F_1$, $F_2$ ja $F_3$, ja köyden voima on niiden keskiarvo $F_\text{ka} = \dfrac{F_1 + F_2 + F_3}{3}$."
- Same task, Sijoitus: the row shows $3{,}40\,\text{N}$ while the Vastaus says two significant figures ($3{,}4\,\text{N}$); fine, but the Sijoitus could end "$= 3{,}4\,\text{N}$" for consistency (recorded only).

## Checked
- Round 1 polish fixed: ΣF is no longer the sum of sensor readings; the mean is $F_\text{ka}$ with $F_1 + F_2 + F_3$, and ΣF means the net force again, as in every other Kaava of the set.
- Kaava order in L3-05: mean definition, then first law $\Sigma F = F_\text{ka} - F_\text{k} = 0$, then $F_\text{k} = F_\text{ka}$; symbolic to the end before substitution.
- Sijoitus: $3{,}4 + 3{,}5 + 3{,}3 = 10{,}2\,\text{N}$, divided by 3 gives $3{,}40\,\text{N}$; matches the answer b).
- Answer, unit, significant figures and tolerance unchanged; no task, id or figure changed.
- Finnish in the changed text correct ("Lukemien summa ... on", "ensimmäisen lain mukaan").
- Phone: text-only change; the layout checks (360-1280 px) already ran ok.
- Captures opened: none (text-only change).
