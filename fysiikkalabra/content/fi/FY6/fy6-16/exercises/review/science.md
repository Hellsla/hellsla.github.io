VERDICT: PASS
CONTENT-HASH: 314a764bcc4556f0

## Blocking

## Polish
- exercises.json:13 (L1-02) — the cable limits the current to 10 A on an ordinary socket, while the lesson says "yleensä noin 8 A". Consider 8 A, or say the cable is set to 10 A.
- solutions.md:79 (L2-03) — a maximum of 11,96 A is rounded up to 12 A, which puts the phase at 25,04 A. Consider "enintään noin 12 A (11,96 A)".

## Checked
- Round 2, judged from the diff HEAD~1..HEAD: solutions.md and the lataus-ex figure code.
- Round-1 blocking item (L3-02) is resolved: 156 % is now justified as an exact result because 10 A and 16 A are the charger's exact settings. The answer 156 and the tolerance 0,02 are unchanged and consistent.
- L3-01's reasonableness check now names its bases (3260 kWh and 3660 kWh): 397,7 : 3660 ≈ 11 % and 397,7 : 3260 ≈ 12 %, so "10–12 %" holds.
- L3-01's 82 % and 92 % now lie inside the lesson's stated typical range of 80–95 %.
- lataus-ex: the y gridlines are now at 2, 4, 5,5, 8 and 11 kW, placed linearly (render checked at 1280 px). The values 11 kW and 5,5 kW can be read directly; the description states the same gridlines and values; no energy is written on the figure.
- answers.py re-run: all 12 answers still match my own recomputation (41,6; 2,3; 15,94; 6,30; 88; 27,5; 10,87; 11,96; 6,528; 59,65; 156; 7,157).
- The €/kWh notation edits in L1-04 and L3-01 change no number.
