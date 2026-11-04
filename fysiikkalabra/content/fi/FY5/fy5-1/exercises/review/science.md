VERDICT: FAIL
CONTENT-HASH: bff64d6a912010ad

## Blocking
- content/fi/FY5/fy5-1/exercises/exercises.json:272 (fy5-1-L3-04) and solutions.md:172 (Periaate) — **B**: a) needs "pedal moment = chain moment about the crank axle", i.e. moment balance of the crank and chainring (ΣM = 0). That is the content of the next chapter (fy5-2), the brief's lesson does not teach it, and the task does not state the condition (only "Kitka jätetään huomiotta"). The solution asserts "sama momentti on ketjun voiman momentilla" with no reason. — Fix: add to the task text "Kampi ja etuhammaspyörä pyörivät tasaisesti, joten polkimen voiman momentti ja ketjun voiman momentti kammen akselin suhteen ovat yhtä suuret (ja vastakkaissuuntaiset)." and cite that sentence in the Periaate. Numbers are right: F_k = 787,5 N, M = 70,9 / 47,3 / 31,5 Nm.

## Polish
- solutions.md:132 (L2-07) — the answer is given to three significant figures "kuten varressa 0,240 m", but F = 90 N has two; 22 Nm (the tolerance already accepts it), or state that 90 N is taken as exact.
- exercises.json:146 (L2-05) — the plan asks for a (1/r, F) graph; the task uses the products Fr instead. That is a valid method, but no graph task covers the inverse proportionality in this chapter.
- solutions.md:172 (L3-04, Järkevyys) — "Takahammaspyörän säde on 0,90-kertainen etuhammaspyörän säteeseen nähden" checks only the ratio; a check of the magnitude (a 9 cm sprocket is a large MTB cog) would make it a real check.

## Checked
- All 8 new answers recomputed independently in one script: −9,0; 25,1→25; 0,1177→0,118; 21,6; 70,875; 166 (A 240 N, C 200 N); all match answers.py and solutions.
- L1-06, L1-07: exactly one correct option; every distractor wrong and its feedback right (zero arm when the line of action passes through the hinges).
- L1-08, L2-06: sign convention counterclockwise positive, as in the lesson; left weights turn the stick counterclockwise, left end goes down: right.
- L2-07: arm measured from the axis, 0,270 − 0,030 = 0,240 m; error magnitude 2,7 Nm agrees.
- L3-05: r = d sin α used with α to the arm's extension as the lesson defines; "longest wrench not best" correctly argued from the arm.
- Scope: moment, arm, sign, oblique force only (FY5 "momentti ja kappaleen kiertyminen"), except the L3-04 item above. No duplicate of an existing task; levels fit; plan +3/+3/+2 met.
- Tolerances 0,02 fit the data's significant figures; units Nm/N/m.
