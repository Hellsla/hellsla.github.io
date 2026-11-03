VERDICT: PASS
CONTENT-HASH: c394fcead04f076c

## Blocking

## Polish
- inquiry.json ennuste-2 prompt — the added sentence "Kapasitanssi kertoo, kuinka paljon varausta kondensaattoriin tulee jännitettä kohti" is correct but hints at the answer before the prediction. A pedagogy matter, not physics.

## Checked
- Round 2. I reviewed the diff from commit f3bb2adf and re-checked the full packet.
- Round-1 blocker resolved: lesson.md now states the conditions after C = ε0εrA/d (small gap compared with the plates, homogeneous field, edges ignored, dielectric fills the gap). The dielectric section says "eristelevy, joka täyttää välin".
- ennuste-2 feedback now reads "5,6-kertaisesti pienemmäksi": 1,0 kV : 5,6 = 0,179 kV, correct.
- tarkistus-1 distractor now says "kun levyjen väli pysyy samana", so it is unambiguously wrong and its feedback is right.
- Esimerkki Tulos: W comes from C and U, and P from t. 6,75 J and 6750 W are unchanged.
- ennuste-1 distractor "kondensaattori ei muutu" is still wrong and its feedback correct. Energy 11 → 44 µJ.
- siirto prompt: dropping "Paristo siirtää koko varauksen" leaves the task well defined ("ladataan ... kunnes virta lakkaa"). 190 µJ is unchanged.
- koe-5 is no longer optional. Its setup (1,0 mm air, connected, U0 varied) isolates U0, and breakdown occurs above 3,0 kV in the sim.
- The εr / E_max table is unchanged and accepted (standard textbook values, stated as approximate). Units are now upright.
- Round-1 recomputation of all lesson numbers still holds. No new errors in the changed lines.
