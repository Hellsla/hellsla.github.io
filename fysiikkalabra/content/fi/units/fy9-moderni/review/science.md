VERDICT: PASS
CONTENT-HASH: e27ea8539b46773c
Delta review, work queue items 18 and 19 (2026-11-16), against the version previously passed.

## Blocking
- (none)

## Polish
- A: s7 a: the lasers both compress and heat the fuel; "kuumensi ja puristi polttoaineen" would match the principle line ("kuumassa ja tiheässä aineessa").
- C: s7 d: "noin sata kertaa enemmän" is 95-fold; fine at the precision of "noin 300 MJ".

## Checked
- Item 18 hunk (s6 common mistakes): "Δm lasketaan sähkötehosta lämpötehon sijaan" agrees with s6 b, which uses the thermal power 4300 MW.
- s7 recomputed in one script: ratio 1,537; difference 1,10 MJ (54 %); inverse 0,651; m = 3,15e6 J / 335 200 J/kg = 9,397 kg; 3,15/300 = 1,05 %; 2,05/300 = 0,68 %; 1,05 MJ = 0,35 %; Δm = 3,50e-11 kg = 35 ng. All agree with tasks.json answers, solutions.md and answers.py; `practice.py check` OK (7 tasks, 110 points; s7 2+3+4+3+3).
- Physics: the system-boundary argument (fuel against the whole facility) is the right one; the 300 MJ is given in the task and marked as not from the article; energy conservation is explained through binding energy and E = Δm c^2 (products more tightly bound, smaller mass), within FY8 scope; "kiehauttaa" read as heating to the boiling point is stated. Rubric criteria ask only what the parts ask and the solution shows.
