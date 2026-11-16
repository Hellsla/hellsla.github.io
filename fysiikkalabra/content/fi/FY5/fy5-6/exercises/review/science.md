VERDICT: PASS
CONTENT-HASH: 7cc36b31da39ce67

## Blocking

## Polish

## Checked
- The hash was the same at the start and at the end. Round 2. `git diff 09d57eb5ac..HEAD` changes only L2-09 (the task text: `*…*` changed to `<em>…</em>`, same words; the solution's Vastaus split into paragraphs, and the outer-planet sentence rewritten) and one sentence in L2-04's Vastaus (why the heights are exact model values). No line of answers.py changed.
- Round-1 Polish (Uranus outside the "1–3 %" range) is fixed. I recomputed T²/a³ against Earth from the NASA values in the source notes: Mercury +0,15 %, Venus +0,06 %, Mars −0,04 %, Jupiter −0,20 %, Saturn −1,26 %, Uranus −0,33 %, Neptune −2,46 %. The spread of the five-planet table is 0,35 %. The text now says "noin 0,2 %", "alle 0,4 %", 1,3 %, 0,3 % and 2,5 %, and these are right.
- L2-09 d is unchanged: 365,2 d · (228,0/149,6)^1,5 = 687,12 d, and with 227,9 it is 686,67 d. The difference from 687,0 d is 0,02 %. The physics (Kepler III holds for ellipses with the semi-major axis; the planet's mass is negligible) is unchanged and right.
- L2-04: Δv = 1,13 m/s is unchanged. The new reason (the task gives the heights no uncertainty) is consistent with the one-figure remark that follows it.
- The unchanged exercises rest on the round-1 recomputation of all 23 numeric answers (round-1 report, hash fcb321d5570d6cec), in which every answer was within 0,4 % of my value.
