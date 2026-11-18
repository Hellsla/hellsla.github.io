VERDICT: PASS
CONTENT-HASH: 43cb3edae017c63d
SCOPE: delta: round 2, the fixes of round 1 in fy9-moderni-s8, -s9; older tasks s1-s7 and the intro untouched
Round 2: delta against the version round 1 reviewed (fix round 1).

## Blocking
None. The three round-1 items are fixed in the fi-easy text:
- s8 d Oletukset: "Lähteen aktiivisuuskaan ei pysy vakiona" is gone; now "Tulos on liian pieni myös, jos lähde vaihdetaan vahvempaan tai oleskeluaika pitenee", after the scattering reason. Both raise the dose.
- s8 d criterion 4: part d now asks "Mainitse myös yksi mallin oletus, joka voi tehdä tuloksesta liian pienen, ja kerro sen vaikutus"; the criterion's examples are not the given "annosnopeus on vakio". Points 4 = 1+1+1+1.
- s9 c: part text "kuinka kauan sitten galaksien väliset etäisyydet olivat nollia. Oleta, että etäisyydet ovat kasvaneet koko ajan samalla nopeudella", Periaate "galaksien väliset etäisyydet ovat kasvaneet nollasta", criterion 1 "etäisyys d on kasvanut nollasta". Consistent with d and *Maailmankaikkeuden kehitys*.

## Polish
- s8 Yleisiä virheitä, a-kohta: "μ = 16 / 20 cm = 0,80 1/cm" is left from the old point (20 cm; 5,0 µSv/h); with (0; 80) and (10; 20) the quotient error is 4 / 10 cm = 0,40 1/cm. Same as in fi.
- s9 c criterion 1 "Galaksin etäisyys d on kasvanut nollasta vakionopeudella v. Aika on ..." reads as a fact, not as the assumption; "Jos ..., aika on" (as in fi) keeps the condition in one sentence.
- Round-1 polish taken as in fi.

## Checked
- Read the fi-easy s8 and s9 tasks.json entries and solutions.md sections. Every number, unit and rounding is the same as in fi (0,14 1/cm, 6,6 µSv/h, 330 h, 2,2 mSv, 3,0 µSv/h, 23,6 -> 24 cm rounded up; 72 km/s/Mpc, 120 Mpc, 2,33e-18 1/s, 4,29e17 s, 1,4e10 a); the short-sentence split keeps every reason (why the wall is made thicker, why d rounds up, the distance-growth assumption).
- The same script as for fi recomputed every value: all agree; two significant figures as the data.
- Aligned calculation rows; unit fields language-neutral; part texts reveal no structure.
- practice.py check --lang fi-easy OK (9 tasks, 136 points); hash the same at start and end.
