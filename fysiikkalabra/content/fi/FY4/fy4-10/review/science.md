VERDICT: FAIL
CONTENT-HASH: c2ac57b9f030fafa

## Blocking
- content/fi/FY4/fy4-10/lesson.md:396 (Tiivistelmä) — (B) the summary still says "osat saavat yhtä suuret vastakkaissuuntaiset liikemäärät" for any explosion from rest. The changed theory (line 230) now limits this to two parts, with a vector sum of zero for more parts. — Fix: "...pysyy nollana: kahdeksi osaksi hajotessa osat saavat yhtä suuret vastakkaissuuntaiset liikemäärät, ja liike-energia kasvaa."

## Polish

## Checked
- batch delta review: the two-part condition and the vector-sum statement are right. In the perfectly inelastic case, "liike-energia pienenee eniten: suurin mahdollinen osa muuttuu muiksi energiamuodoiksi" is right, since the centre-of-mass KE remains and "häviää" no longer appears in the theory. The lesson-answers.py comment now correctly names velocity Verlet (checked against the code); model.js uses RK4. The exercises text dropping the level-policy sentence carries no physics. The only "hävisi" left is a wrong option (check-1), and its feedback is right.
