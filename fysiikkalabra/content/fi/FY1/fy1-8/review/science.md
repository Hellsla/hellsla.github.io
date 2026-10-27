VERDICT: PASS
CONTENT-HASH: 42fa021ae8b29ad2

## Blocking
None.

## Polish
- inquiry.json `suunnittele` model — a ball rolling on a level floor slows slightly from rolling friction, so over 1,6–3,2 m the s = vt hypothesis may fail. The model now says that the hypothesis is refuted if the time grows faster than the distance, so this is a legitimate, falsifiable example. A note that a real ball slows a little would make the example richer.

## Checked
- Round-1 blocking 1 (`suunnittele`): the ball now rolls on a level floor after a launch ramp, and timing starts past the ramp. At 0,4 m/s, 1,6 m gives 4 s, and 0,2 s / 4 s = 5 % ("enintään 5 %"). The range 1,6–3,2 m gives five equally spaced values. The model states a falsification criterion. Fixed.
- Round-1 blocking 2 (lesson.md:155): the text now says that a shorter distance makes the relative uncertainty exceed ε_max. Correct. Fixed.
- Polish items: the hook now matches the Tutki table (five distances × 3 repeats, mean 4,73 s); "noin 6 % tai alle" matches the 6,1 % row; the cross-reference names the right section; L2-02 now gives "3,0 m". All fixed.
- New L1-05: ε = 0,15 s / 4,73 s = 3,17 % → 3,2 %, which matches answers.py, exercises.json, the solution and the table row. The 2 % tolerance covers rounding. Its solution is symbolic first and complete.
- Recomputed all 12 answers again in one script; all agree with answers.py and exercises.json.
- Graph text: Δs/Δt = v needs t on the horizontal axis. Correct.
- Reworded `reilu-koe` options and their feedback are physically right; the Ennusta correct option's feedback (20 %, 0,50 ± 0,10 m/s; B ±0,01 m/s) still holds.
- Content hash matched the packet at start and end.
