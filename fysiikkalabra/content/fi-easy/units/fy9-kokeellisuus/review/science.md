VERDICT: PASS
CONTENT-HASH: bfe9479ef3570ebe
SCOPE: full (as asked): the three new ```pysahdy boxes first, then the unit texts and the Sovella task set
Round 3: the version passed in round 2 (fc1b77921967a9ae) plus three Pysähdy ja mieti boxes in unit.md and a paragraph break in one inquiry.json model answer.

## Blocking
- (none)

## Polish
- (none)

## Checked
- Pysähdy box 1 (one variable at a time): its physics is the same as fi. If two variables change together, the cause of the change cannot be inferred. It sits after the same paragraph and agrees with that paragraph and with Yleisiä virheitä item 2.
- Pysähdy box 2 (hand timing with a 0,01 s display): the answer is "Ei ole". Resolution alone does not give the uncertainty, and reaction time makes it tenths of a second. This is the same as fi and agrees with the Virhe, epävarmuus ja resoluutio paragraph, Yleisiä virheitä item 3 and s3 a (about 0,1 s, about 13 % of 0,8 s). It is not an A or B finding.
- Pysähdy box 3 (slope compared with a single point): all points affect the slope, so one point's random error affects it less. This is the same as fi. It speaks of random error only, so it does not clash with the next paragraph, where a constant systematic error shifts the line but leaves the slope unchanged. It is not an A or B finding.
- fi and fi-easy both have 3 pysahdy blocks, in the same places. The inquiry.json diff splits the model answer into two paragraphs with every word unchanged.
- I recomputed all the numbers in one script of my own: s2 160 s; s3 t̄ 0,7867 s, g 9,695, gmax 10,67, gmin 8,923, Δg 0,872 m/s² (so 9,7 ± 0,9), 4,45 % and 12,5 %; s4 T² row, least-squares k 4,020 and b 0,103 s², read k 4,0125 giving g 9,839, d 4,98 cm, row by row 8,87 and 9,60, extreme lines 10,10 and 9,61; s5 2677 kg/m³, Δρ 78 kg/m³, 2,9 %; s6 v² 7,7…69,4, a 4,167, μ0 ≥ 0,4247, true a 3,779, 0,385; s7 ratios, mean 0,2152, Δμ 0,005, 14,3 %; s8 k 2,467 mT/A, n 1963 1/m, I 4,86 A, 3,08 % and 0,645 %. All of them match the solutions and answers.py.
- The physics of s1–s8 is unchanged since rounds 1–2: the model conditions (small swing angle, losses, no change of phase, static friction as an upper limit, extrapolation), the direction of each systematic error, and rounding with its reasons. The Hyväksytään myös ranges contain the recomputed values.
- The unit text (formulas for mean, half the range and ε; y = kx + b with its range of validity; the tare figure with b ≈ 52 g and k ≈ 0,91 g/cm³) is consistent and has no guardrail break.
- The hash is bfe9479ef3570ebe at both start and end.
