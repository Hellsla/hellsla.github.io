VERDICT: PASS
CONTENT-HASH: 314e222bbcc3a430
Round 2: full review of the exercise set after the round-1 fixes (commit f8abf016e, diff from d0ea57642). Round 1 had no Blocking items; three of its Polish items are fixed.

## Blocking
(none)

## Polish
- solutions.md:140 (L1-08) — the new rounding reason "kolme merkitsevää numeroa, koska ... 18 V määräävät tuloksen riittävän tarkasti" does not follow the rule: 6,0 V and 18 V have two significant figures, so a student who answers 1,4·10² mJ (2,8 % off) is marked "Lähellä". Fix: keep 144 mJ in the box, set `tolerance` to 0.03, and write "kaksi merkitsevää numeroa kuten jännitteissä, eli noin $1{,}4 \cdot 10^{2}\,\text{mJ}$; vastauslaatikkoon käy myös 144 mJ".
- Plan deviation, carried from round 1 (not physics): the plan's error analysis was "nettovaraus on Q"; L2-07 tests QU vs ½QU instead, and L2-06 has only a charging curve, no discharging curve. Physics fine; the planning side decides, or updates docs/exercise-bank/FY6.md.

## Checked
- Hash 314e222bbcc3a430 at start and end.
- Round-1 Polish fixed: L2-05 and L3-04 now read the slope from the origin and a far point of the fitted line ((12 V; 566 µC), (12 s; 1200 V)), which matches the least-squares 47,21 µF and 100,0 V/s; L2-06 distractor moved to 1–2 s (3,5→5,5 V brackets 4,5 V) and its feedback says 2,0 V.
- One script recomputed every new answer: L1-08 144 mJ; L2-05 3,40 mJ; L2-07 63,4 mJ; L3-04 C = 150 µF, W = 243 J, P = 48,6 kW, 18 s; L3-05 ratio 6,89. answers.py and exercises.json agree.
- L2-06 steps 3,5/2,0/1,4/0,8/0,5/0,3 V match the solution and every feedback; the new correct-option text ("jännite kasvaa silloin nopeimmin") equals `answer`.
- L1-06, L1-07, L2-06 after the reorder: exactly one correct option each, `answer` equals its text, every distractor's feedback right.
- L3-05 c: W = ⅛ε₀ε_rE_max²Ad and the ratio (2,1·60²)/(5,6·14²) agree.
- Levels 8/7/5, units, symbols as in the brief; no duplicate of an existing task.
