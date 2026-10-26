VERDICT: PASS
CONTENT-HASH: 34d62791171a8af6

## Blocking

(none)

## Polish

1. inquiry.json `data` mistakes[0] feedback — "19,1 m − 4,2 m" uses 4,2 m, but the line starts at 4,1 m everywhere else — write "$\Delta x = 19{,}1\,\text{m} - 4{,}1\,\text{m}$".
2. Simulation canvas and its DOM readout ("A: paikka x = 0,0 m, matka s = 0,0 m", axis labels, "Nuolen suunta...") — plain interface text, not maths; per NOTES.md §1 it stays until the teacher decides.
3. inquiry.json exp-1..3 — the sim only evaluates x = x0 + vt, so the experiments confirm arithmetic the prediction states; the real inquiry is the `data` activity (round 2, unchanged).
4. exp-2 question — the correct option is the longest and the only one with value and reason; length is a cue (round 2, unchanged).
5. `data` figure — the equation of the fitted line appears only in the solution, not on the line (round 2, unchanged).

## Checked

- Hash at start 34d62791171a8af6; end check same.
- Hint 1 now says to read the point from the line, not the table; this repairs the earlier mismatch and still leaves the choice of point to the student.
- Solution reads the line at (10 s; 19,1 m), matching the drawn line and the figure text; 15,0 m / 10 s = 1,5 m/s, inside tolerance 0,03.
- Hints 2 and 3 (about 19 m, 15 m) are consistent with the line.
- Mistake values 1,9 / 1,3 / 0,67 still match the data.
- Nothing else in the lesson changed since the round-2 PASS; goals, workload, exercises, exit ticket and phone fit stand as approved.
