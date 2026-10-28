VERDICT: PASS
CONTENT-HASH: e7319904009dc653

Delta review over the audit's PASS (f67273566e2625ad): L1-03 (t = s/v from given values) replaced by a reading task on fy1-5/line-read; numbers with units elsewhere turned into LaTeX.

## Blocking
(none)
## Polish
- solutions.md:30 and the task text — 2,5 m/s = 9 km/h is jogging, not walking ("kävelijä"); the solution even says "hidas hölkkä". Call the person "hölkkääjä" or halve the slope (e.g. 25 m at 20 s) if the walker is kept.
## Checked
- Figure: line from origin to (10 s; 25 m) on a 1 s × 5 m grid, passing exactly the crossings (2; 5), (4; 10), (6; 15), (8; 20), (10; 25); description matches.
- Recomputed v = 20 m / 8 s = 2,5 m/s, t = 150 m / 2,5 m/s = 60 s; answers.py 60; tolerance 0,03 (58,2…61,8 s) accepts every crossing-based reading and the 6 × 10 s proportion; rejects reading the graph's last time (10 s) or v misread as 2,0 or 3,0 m/s (75 s, 50 s).
- LaTeX conversions keep all values (110 m, 8,0 m/s, 45 m, 3,5 m/s, 210 m, 450 s, 2,4 km, 1,7 km, 3420 vrk, 41,6 h, 90 m recomputed from answers.py).
