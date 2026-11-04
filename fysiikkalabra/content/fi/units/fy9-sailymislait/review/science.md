VERDICT: PASS
CONTENT-HASH: c2716084d9c1d0b9

Round 2 (delta review of round 1 fixes; round 1 hash 82147d0c9120ddde)

## Verified
1. Blocking 1 fixed: the tarkistus-3 model now ends "tai törmäys, jossa oma keula rypistyy lyhyemmän matkan, koska se
   lyhentää pysähtymisaikaa". It no longer contradicts the rigid-wall case, which it calls equally dangerous.
2. unit.md, Yleisiä virheitä: "samalla nopeudella kimpoavalle pallolle $\Delta p = -2mv$". Fixed.
3. s1 c (tasks.json and solutions.md): "jarrun vaunuun kohdistama", and the system is named as laskija, valjaat ja
   vaunu (82,0 kg). Fixed.
4. s6 d: Periaate and the rubric's equation detail use $\Delta U = cm\Delta T$, and the no-change-of-state condition is kept. Fixed.
5. tarkistus-2 mistake 7.11: recomputed (784,8 − 729)/784,8 = 7,11 %. The answer is 53,56 % and the complementary
   mistake 46,44 %. Fixed.
6. s2 b Vastaus: the precision is now justified by the difference and the 0,05 m/s reading (about ±0,01 m/s).
   I recomputed 0,57 m/s and the 85,2 % kinetic energy share. Fixed.
7. teacher.md 15–25 min: "lähes vain" and "lähes $m_B:(m_A+m_B)$". Fixed.
8. tormays now prints numbers. I recomputed them: 32 t × 1,6 m/s = 51 200 kg·m/s, 40,96 → 20,48 kJ (41 and 20 kJ). The
   kartta notation now uses vector bars and is correct.

In Python I recomputed every number that changed or was newly printed. No fix brought a new physics error.
`practice.py check`: OK, 6 tasks, 95 points. `units.py check`: 38 units OK.

## Polish
None remaining.
