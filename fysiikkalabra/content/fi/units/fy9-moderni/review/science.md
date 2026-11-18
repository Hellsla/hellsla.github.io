VERDICT: PASS
CONTENT-HASH: 876c08f6ee47b4ec
SCOPE: delta: round 2, the fixes of round 1 in fy9-moderni-s8, -s9; older tasks s1-s7 and the intro untouched
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
None. The three round-1 items are fixed in the fi text:
- s8 d Oletukset: the activity clause is gone; it now says scattering adds dose and "tulos on liian pieni, jos lähde vaihdetaan vahvempaan tai oleskeluaika pitenee". Both reasons really raise the dose, so "paksummaksi" follows.
- s8 d criterion 4: the part text now asks "Mainitse myös yksi mallin oletus, joka voi tehdä tuloksesta liian pienen, ja sen vaikutus", and the criterion's examples (sironta, vahvempi lähde, pidempi oleskelu) are not the given "annosnopeus on vakio". Points still 4 = 1+1+1+1.
- s9 c: part text "galaksien väliset etäisyydet olivat nollia ... etäisyydet ovat kasvaneet koko ajan samalla nopeudella", Periaate "galaksien väliset etäisyydet ovat kasvaneet nollasta", criterion 1 "etäisyys d on kasvanut nollasta". No start-from-one-place picture left; consistent with d and fy8-16.

## Polish
- s8 Yleisiä virheitä, a-kohta: "μ = 16 / 20 cm = 0,80 1/cm" is left over from the old reading point (20 cm; 5,0 µSv/h). With the new points (0; 80) and (10; 20) the quotient error is 4 / 10 cm = 0,40 1/cm. Newly inconsistent, not wrong physics.
- Round-1 polish taken: s9 task text no longer gives the grid point; s8 a uses (10 cm; 20 µSv/h) (a ±0,5 µSv/h reading now gives µ = 0,136-0,141 1/cm, inside 3 %); s9 d criterion 2 now accepts "muulla yhtä pätevällä tavalla".

## Checked
- Read the s8 and s9 tasks.json entries and solutions.md sections (current packet-science.md matches them).
- One script recomputed from the figures' data (80 µSv/h, half-value 5,0 cm; H0 = 72): µ = ln 4/10 = 0,1386 (also ln 8/15), 6,60 µSv/h, 330 h, 2,18 mSv, 3,03 µSv/h, d 23,61 cm, 23 cm -> 3,30 µSv/h, 24 cm -> 2,87 µSv/h ("noin 2,9"), error value 31,6 cm; 116,7 Mpc, 8640 km/s at 120 Mpc, 2,333e-18 1/s, 4,286e17 s, 1,358e10 a. All agree; results rounded to the data's two significant figures, d rounded up with reason.
- Calculation chains are aligned rows; unit fields (1/cm, µSv/h, mSv, cm, km/s/Mpc, Mpc, a) language-neutral; part texts reveal no solution structure beyond what is asked.
- practice.py check units/fy9-moderni OK (9 tasks, 136 points), units.py check OK; shots.md is for this hash; hash the same at start and end.
