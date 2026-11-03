VERDICT: PASS
CONTENT-HASH: bcb0030d6d5d7294

## Blocking

## Polish
- lessons/FY6/fy6-11/answers.py:15, :18 — comment and expression still read the line at (4,5 nC; 135 µN); the solution now reads (4,0 nC; 120 µN) — compute 120e-6 / 4.0e-9 so the script backs the shown reading (value unchanged).

## Checked
- Round 2 (diff HEAD~1..HEAD): L3-02 task adds "Levyt ovat tyhjiössä." and the Periaate states no other forces — round-1 B item resolved.
- solutions.md L1-02, L1-03, L1-04, L1-05, L2-01, L2-02, L3-03 now name "sähkökentän voimakkuus" — round-1 A item resolved.
- L1-05 reading: fitted line through the origin at slope 30 µN/nC passes the grid crossing (4,0 nC; 120 µN) → 3,0·10⁴ N/C; check point (3,0; 91) → 3,03·10⁴ N/C; the self-contradictory grid sentence is gone.
- L3-01 answer 3,4·10² V (337,5 V) with its rounding reason — correct.
- answers.py re-run: all 12 values agree with exercises.json; no other numbers changed.
