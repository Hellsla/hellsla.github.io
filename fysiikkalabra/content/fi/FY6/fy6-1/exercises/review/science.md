VERDICT: PASS
CONTENT-HASH: cf52e4c26916eaa1
ROUND: 2

## Blocking

## Polish
- solutions.md:149 (L2-06 Periaate vs Mallivastaus b) — the Periaate now says "lähes koko virta kulkee johdon kautta", but the Mallivastaus says "Lampun läpi ei kulje virtaa". Make them agree (guardrail 6): in b) write "Lampun läpi kulkee vain mitättömän pieni virta, joten lamppu ei pala."
- solutions.md:174 (L3-05 c) — the added sentence is right, but it gives no mechanism. Add the cause in one clause: "koska sähköinen vuorovaikutus eli työntö etenee piirissä lähes valon nopeudella, ja kaikki vapaat elektronit alkavat liikkua lähes samanaikaisesti."
- Plan drift (docs/exercise-bank/FY6.md fy6-1), carried over and extended: L1-07 asks about an imagined open switch, not "mikä kaavio vastaa kuvattua piiriä". L2-06 describes the circuits in words, not with two diagrams. L1-08 now uses 0,25 A, but the plan still says 2,5 mA. Update the plan so that it matches the tasks.

## Checked
- Hash cf52e4c26916eaa1 at start and end. Counts 8/7/5.
- Round-1 Blocking (L2-07 c, the "mittaus 4" inference) resolved: the solution now says that the differences go in both directions, are no larger than one display step and come from the reading's uncertainty.
- Round-1 Polish resolved: "resoluutio eli pienin näyttöaskel" in L2-07 task, answer and solution; "vapaat elektronit" in L3-05; the L2-06 Periaate no longer gives the current a will; L1-08 is no longer harder than L2-02 (no mA conversion).
- L1-08 recomputed: N = 0,25 A · 60 s : e = 9,36·10¹⁹, so 9,4·10¹⁹. The text, the solution, answers.py and exercises.json agree, and the reasonableness estimate (15 C · 6,2·10¹⁸) is right.
- I recomputed every answer from answers.py in one script and checked each new task with my own formulas: L2-05 22,8 C, L3-04 12,5 Wh, L3-05 0,0192 mm/s. All are within tolerance of exercises.json.
- L3-04: removing the "noin 13 Wh" clause leaves a consistent rounding reason.
- L2-06: "oikosulku" is now named, and the safety sentence about a real battery is exact.
- MC L1-06 and L1-07: still exactly one correct option each, with correct feedback.
