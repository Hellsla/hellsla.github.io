VERDICT: FAIL
CONTENT-HASH: 7283af51ce18e15e

## Blocking
- exercises/solutions.md:58 (fy6-2-L2-01, Vastaus) — **A**: "noin $10\,\%$, yksi merkitsevä numero" breaks the rule being applied. 10,6 % begins with 1, so it gets two figures: 11 %. The rounded limit gives the same (0,04 A : 0,35 A = 11 %), and line 59 itself says "lähes $11\,\%$". Fix: "noin $11\,\%$, kaksi merkitsevää numeroa, koska ensimmäinen numero on 1". Also update the comment in lessons/FY6/fy6-2/answers.py:16 ("-> 10 %"). Tolerance 0,08 already accepts 11.

## Polish
- solutions.md (L1-05) — 0,009935 → 0,01 → 0,010 V applies "first digit 1" to the already rounded value. The step is explained and matches the lesson's example. Keep the same wording in both places.
- solutions.md (L1-04, L2-04, L3-01 Järkevyys) — the checks still cite the lesson's sim values. They are correct, but checks based only on the task data would stand apart from the lesson (carried over).

## Checked
- One script recomputed every answer: L1-01 0,0823 → 0,08 V; L1-02 1,663 → 1,7 mA; L1-03 0,75 → 0,8 %; L1-04 0,180 A; L1-05 0,009935 → 0,010 V; L2-01 10,57 %; L2-02 0,001075 → 0,0011 A; L2-03 3,20; L2-04 ≈ 9,0 V; L3-01 2,17 → 2,2 %; L3-02 0,1522 → 0,15 V. All agree with answers.py and exercises.json.
- Every rounded answer is inside its relative tolerance (tightest: L1-03 at 6,7 % of 7 %, L1-01 at 2,8 % of 3 %).
- The FY1 rounding reasons are right everywhere except L2-01.
- L3-02: limits 0,05 V and 0,11 V; intervals 4,97–5,07 and 5,03–5,25 V overlap; "cannot be shown faulty, not proven equal" follows the guardrail.
- L3-01: 1,0 mV/mA = 1,0 Ω burden; the task states an ideal battery.
- L2-02: the mA → A conversion is explicit, and the reasonableness check is real.
- L3-03: the causal chain is correct (short through the meter, fuse opens, lamp relights, display 0), and the criteria match the task.
- Notation $\Delta x = p \cdot x + n \cdot r$ matches the brief, and every formula is written symbolically before substitution.
- Content hash unchanged start/end.
