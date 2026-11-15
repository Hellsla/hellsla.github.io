VERDICT: FAIL
CONTENT-HASH: 049190184f7fdbd1
SCOPE: delta round 2, L2-03 key and tolerance

## Blocking
- L2-03: answer 11.956522 with relative tolerance 0.09 accepts 10.88-13.03 A. That passes 13 A, which with the sauna's 13.04 A is 26.04 A per phase and trips the 25 A main fuse; it also contradicts the solution ("12 A would exceed"). The teacher's decision (11 A and 12 A both pass) needs only about 10.9-12.1 A. Fix: answer 11.5 (midpoint of 11 and 12), tolerance 0.05 (10.93-12.08 A); then 11, 11.96 and 12 pass, 13 and 10 fail. Update the answers.py comment to match.

## Polish
- The question does not say the limit is a maximum to round down; the solution explains it, and since both roundings now pass, no student is penalised.

## Checked
- Intent of the change (a limit rounded in either direction accepted, model answer 11 A with the reason stated) is pedagogically sound and consistent across the three languages.
- 25 - 9000/(3*230) = 11.96 A; Järkevyys sum 13.0 + 11 = 24 A and 7.6 kW unchanged and correct.
- Tolerance semantics: relative (docs/inquiry.md), so 0.09 is +-1.08 A.
