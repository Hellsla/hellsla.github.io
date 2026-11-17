VERDICT: PASS
CONTENT-HASH: eeccff04aba30fbe

## Blocking

## Polish
- exercises/solutions.md:313 (L2-10 Järkevyys): this is a language matter for the Selkeä suomi version, not physics. "suora interpolointi", "kupera" and "janan alapuolella" are hard words for an S2 reader. Possible wording: "Jos arvo luettaisiin suoraan välistä, se olisi noin $16\,\mu\text{Sv/h}$. Kuvaaja kaartuu tämän suoran alapuolelle, joten arvo on vähän pienempi."

## Checked
- The hash eeccff04aba30fbe was the same at the start and the end. I judged the diff: the L2-10 Järkevyys line (the L3-06 text and the answers.py comment were already judged in round 2).
- L2-10 Järkevyys: on the chord between (10 cm, 20) and (15 cm, 10), the value at 12 cm is $16\,\mu\text{Sv/h}$. The convex curve runs below it: $80 \cdot 0{,}5^{2{,}4} = 15{,}16\,\mu\text{Sv/h} < 16$. The reasoning is now correct, and the round-2 blocking item is fixed.
- "lähempänä $10\,\text{cm}$:ä" is correct (2 cm against 3 cm).
- Recomputed: L2-10 15,157 (answers.py 15,157166); L3-06 $5{,}0\,\mu\text{Sv/h}$, $t = 4{,}0\,\text{h}$. Both match answers.py.
- The changed line matches the fi version word for word.
