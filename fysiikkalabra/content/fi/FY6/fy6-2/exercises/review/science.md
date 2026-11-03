VERDICT: PASS
CONTENT-HASH: b33c56a990dea99a

## Blocking

## Polish
- solutions.md (L1-04, L2-04, L3-01 Järkevyys) — the checks cite the lesson's simulation; the values (4,50 V, 97,8 mA, 0,10 A) agree with the model, but a set reviewed apart from the lesson is safer with checks that stand on the task data alone.

## Checked
- Round 1 Blocking fixed: L3-03 now says the lamp goes dark for a moment and relights, display stays 0; model answer and criterion explain the short through the meter, the blown fuse opening the meter's path and the lamp relighting — causally correct.
- Round 1 polish done: L2-01 Järkevyys (350 mA exceeds 200 mA, so 10 A is the smallest fitting range), L2-04 Periaate (lamp voltage = resistance × almost zero current).
- One script recomputed every answer from the task text: L1-01 0,0823 V, L1-02 1,663 mA, L1-03 0,75 %, L1-04 0,180 A, L1-05 0,009935 V, L2-01 10,57 %, L2-02 0,001075 A, L2-03 3,20, L2-04 ≈ 9,0 V, L3-01 2,17 %, L3-02 0,1522 V — all agree with answers.py and exercises.json; tolerances fit.
- L3-02 intervals 4,975–5,065 V and 5,033–5,247 V overlap; conclusion "cannot be shown faulty, does not prove equal" follows the guardrail.
- L3-01 1,0 mV/mA = 1,0 Ω burden, ideal battery stated in the task.
- Rounding: error limits to two significant figures with reasons; L2-02 conversion explicit; symbolic formula before substitution throughout.
- Notation (Δx = p·x + n·r, r resolution) matches the lesson brief.
- Content hash unchanged start/end.
