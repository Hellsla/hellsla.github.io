VERDICT: PASS
CONTENT-HASH: 848b3b84e36daf0e

## Blocking

## Polish

## Checked
- Round-1 blocker, solutions.md:8 (L1-01): the answer is now 0,098940 u, "kuusi desimaalia kuten annetuissa massoissa". This is a correct reason (a subtraction keeps the data's decimals). exercises.json 0.09894 is the same value.
- Round-1 polish: L1-03 now gives 7,570 MeV with the 931,5 reason, and the answers.py L2-03 comment now says 2,04479e-11 J. Both fixed.
- All 12 answers recomputed in one script with my own formulas, and all match answers.py: 0,098940 u; 127,62 MeV; 7,5702 MeV; 8,988e13 J; 2,3875e-3 u; 8,7904 MeV; 4,8708 MeV; 2,04479e-11 J; 3,6817e14 kg; 20,578 MeV; 23,848 MeV; 2,797e-12 kg.
- The L2-03 check, 2,045e-11 J / 1,602e-19 = 127,7 MeV, is consistent with the 931,5 route (127,6 MeV).
- L3-01: He-3 E_B is 7,72 MeV, 2,57 MeV per nucleon. The ratio 20,58/28,3 = 73 % is right.
- L3-02: the mass route gives 23,847 MeV.
- L2-04: 4,26e9 kg/s.
- The electron bookkeeping is right in every alpha decay and in He-4 → He-3 + n.
- No new error was introduced. Scope, units and tolerance are fine.
