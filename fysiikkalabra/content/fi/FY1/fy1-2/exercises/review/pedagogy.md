VERDICT: PASS
CONTENT-HASH: 2afc0aba92faf652
Delta scope: only this diff judged.

## Blocking
- none

## Polish
- solutions.md (L1-10 Vastaus) — the reason for three figures ("etäisyys on keskiarvo keskipisteestä keskipisteeseen") is physical, while the lesson's rule is "as many figures as the least accurate factor"; a student may wonder why four-figure data gives three. Fix: add "Tässä tehtävässä tulos annetaan kolmella merkitsevällä numerolla, koska Kuun etäisyys vaihtelee kuun kiertoradalla (noin 356 000-407 000 km)." or keep as is.
- solutions.md (L1-10 Vastaus) — "noin ±4 %" but tolerance 0,04 s on 1,28 s is about 3 %; write "noin ±3 %".

## Checked
- exercises.json answer 1.28 s matches solutions.md Vastaus and answers.py (round to 2 decimals); the Sijoitus line shows 1,282 s ≈ 1,28 s so the rounding is visible.
- Solution steps, the conversion km to m and the Järkevyys line are unchanged and still consistent with 1,28 s.
- Tolerance 0,04 accepts 1,282 and 1,28 alike, so a student who keeps four figures is not marked wrong.
- Task text unchanged: situation, lookup, hint t = s/c, question last.
- Finnish of the new sentence is correct ("kolmella merkitsevällä numerolla").
