VERDICT: PASS
CONTENT-HASH: 34569735919c8d54

Round 2 (delta review of round 1 fixes; round 1 hash 1e35148179fc1f8f). Judged against docs/FY9_PLAN.md "Lesson 16: the mock exam".

## Round 1 Blocking findings: verified fixed
1. s9 b) Järkevyys (solutions.md line 597) now reads "Kallioperän lämpötila nousee Suomessa tyypillisesti noin 15–20 astetta kilometriä kohti, ja tulos on tällä välillä." It no longer cites the tiedote. The built page shows the same text.
2. teacher.md, Tukea tarvitsevat: now 70 p. Recomputed 20 + 2·15 + 20 = 70.

## Round 1 Polish: verified
3. s3 Yleisiä virheitä: 261 K instead of 12 K, about 20-fold (261/12 = 21,8). Correct.
4. s5 c): "Valaisimen vieressä altaan pohjalla oleva sukeltaja" adds the missing condition.
5. teacher.md, 75-min lessons: five sessions; every session now fits and covers 4 Osa II + 2 Osa III tasks.
6. s1 d) answer.value 3,12: left as it is (optional). Accepted.
7. s10 e): √2 ≈ 1,41 without the spring mass, and √(0,620 : 0,320) = 1,392 with it. Data ratio 0,990/0,713 = 1,388. Model check: T(0,300) = 0,711 s and T(0,600) = 0,990 s with k = 25,0 N/m and m_eff = 20,5 g. Consistent.

## Fixed by the reviewer in this round
- s10 e) Mallivastaus said "d-kohdan jousen massan vaikutus", but the spring mass is found in c) (d) is the static spring constant). Changed to "c-kohdan". This was a new small error from the round 1 fix.

## Rechecked
- answers.py output unchanged from round 1 (s1 5,30 MJ … s10 k = 25,0 N/m, m_eff 20,5 g, static k 24,9 N/m). s10 slope 4π²/k = 1,578 s²/kg matches the graph label 1,58, and the intercept 0,032 s² gives 0,032/1,579 = 0,020 kg.
- s8 d) is reworded ("c-kohdan kuvaajasta valitsemasi mallin"). The s8 d)/e) solutions still use the kv² model chosen in c), so the physics is unchanged.
- Build of fy9-harjoituskoe: OK.

## Blocking
(none)

## Polish
(none new)
