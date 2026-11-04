VERDICT: PASS
CONTENT-HASH: 3bdcdbebb2c499c3
Round 2: full review of the exercise set after the round-1 fixes (commit e6301a0ac); round 1 had no Blocking items.

## Blocking

## Polish
- solutions.md:160 (L2-06) — "kaksi merkitsevää numeroa kuten jännite-erotuksessa ... 0,5 V": 0,5 V has one significant figure, so it cannot justify two. Write "erotus 0,5 V on vain yhden desimaalin tarkka, joten tulos 1,5 Wh on likiarvo (noin 2 Wh)", or give the voltages as 4,20 V and 3,70 V in the task.
- docs/exercise-bank/FY6.md:55 — still says "virta kulkee akun sisällä $-\to+$" during charging, which is the discharging direction (L1-07, + → −, is right). The plan's CC–CV graph and error claim are still listed though L2-07 and L2-06 replaced them. Update the plan.

## Checked
- Hash 3bdcdbebb2c499c3 at start and end. Diff since 048b5f229 read in full: only option reordering, wording and the round-1 Polish items changed.
- Round-1 Polish fixed: L3-04 now states "ladattiin täyteen samasta tyhjästä tilasta"; answer 77.45 matches the solution's 77,45 %; L3-05 rounding now cites R_kok = 0,40 Ω.
- L3-04 recomputed: W = 8,52 / 9,62 Wh, η = 77,45 % (87,5 % at 0,50 A), R_s = 0,10 Ω.
- L2-06 recomputed: (4,2 − 3,7) V · 2,0 A · 1,5 h = 1,5 Wh; 11,1 + 1,5 = 12,6 Wh; the added a) answer is right.
- L1-06, L1-07 after reordering: exactly one correct option (index 2 and 3), the `answer` text equals it, every distractor and its feedback still right.
- answers.py re-run: all 18 numeric answers agree with exercises.json.
- Levels, scope and notation unchanged from round 1; no duplicate of an existing task.
