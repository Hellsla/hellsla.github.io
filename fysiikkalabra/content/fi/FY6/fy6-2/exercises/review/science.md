VERDICT: PASS
CONTENT-HASH: d98092f0c14ecbc1

## Blocking

## Polish
- solutions.md (L1-05) — 0,009935 → 0,01 → 0,010 V applies "first digit 1" to the already rounded value. The step is explained and matches the lesson. Keep the same wording in both places (carried over).
- solutions.md (L1-04, L2-04, L3-01 Järkevyys) — the checks cite the lesson's sim values. They are correct, but checks based only on the task data would stand apart from the lesson (carried over).

## Checked
- Round-1 blocker fixed: L2-01 Vastaus is now "noin 11 %, kaksi merkitsevää numeroa, koska ensimmäinen numero on 1". Recomputed: ΔI = 0,020 · 0,35 A + 3 · 0,01 A = 0,037 A, and 0,037 A : 0,35 A = 10,57 %. The rounded limit gives the same: 0,04 A : 0,35 A = 11 %.
- The Vastaus, the Järkevyys ("lähes 11 %") and the answers.py:16 comment ("-> 11 % (first digit 1: 2 sf)") now agree.
- exercises.json L2-01 has answer 10.57 and tolerance 0.08. The answer 11 is 4,1 % off, so it is accepted.
- The diff touches only L2-01 in solutions.md and the answers.py comment. All other answers are unchanged and were recomputed in round 1 (L1-01 to L3-02 all agree).
- The content hash is the same at the start and the end.
