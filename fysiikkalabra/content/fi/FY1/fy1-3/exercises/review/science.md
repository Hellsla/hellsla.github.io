VERDICT: FAIL
CONTENT-HASH: 674ef574eb28d802

Delta review over the audit's PASS (f6ea8ce2311e052c): L1-03 now reads five pendulum times off fy1-3/pendulum-dots; LaTeX in L1-02, L2-03, L2-04, L3-03.

## Blocking
- exercises.json:24–26 with solutions.md:29 — (B, assessment) L1-03, now rewritten: the range 12,9 s − 12,2 s = 0,7 s has one significant figure (NOTES §2, difference of readings), and this chapter reports an uncertainty to one figure; the solution itself says the reported estimate is 0,4 s, but tolerance 0,02 (0,343…0,357) rejects 0,4. Fix: accept both, e.g. answer 0,35 with tolerance 0,15 (0,30…0,40), and change "kaksi merkitsevää numeroa; jakaja 2 on tarkka" to say 0,35 is the exact half and 0,4 its one-figure rounding, both accepted.
## Polish
(none)
## Checked
- Figure (shot and code): axis 12,0–13,0 s, gridlines and ticks every 0,1 s, numbers every 0,2 s; dots on 12,2, 12,4, 12,6, 12,7, 12,9 s, no stacking (distinct 0,1 s bins); description matches.
- Kuvaajan lukeminen is right (12,9 one gridline right of 12,8); (12,9 − 12,2)/2 = 0,35 s; answers.py 0,35; midpoint 12,55 ± 0,35 covers all dots.
- LaTeX conversions: 20,3 − 20,0 = 0,3 cm; L2-03 mean (12,4 + 12,5 + 12,3)/3 = 12,4 cm; L2-04 0,2/0,02 = 10; L3-03 mean 8,26 − 8,00 = 0,26 cm. Values unchanged.
