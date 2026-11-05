VERDICT: PASS
CONTENT-HASH: f3f7dd18087405bc

## Blocking

## Polish
- exercises.json:311 fy5-14-L3-05 a) — the answer pattern "find f1, name the missing even harmonics" is the same as in the old L3-03 (clarinet). The cause and the timbre comparison are different (a node at the pluck point instead of a closed pipe end), so the two tasks complement each other. — Optionally add to c): "Vertaa tehtävän 14-18 (L3-03) klarinettiin: mikä aiheuttaa parillisten puuttumisen kummassakin?"
- solutions.md:176 fy5-14-L3-05 c) — "eikä solmukohta lähde värähtelemään" is loose wording, because the plucked point is the one that moves most. — Write instead: "keskeltä näpätty alkumuoto on symmetrinen, eikä värähtelytapa, jolla keskellä on solmu, voi tuottaa poikkeamaa juuri näpäytyskohdassa, joten sitä ei synny". This is a level-C simplification and not wrong.

## Checked
- Round-1 Blocking 1 is resolved. L3-05 is replaced by the plan's level-3 timbre task, and it no longer overlaps fy5-11-L2-05 or fy5-10-L2-07 (no s–t data, no device delay). I found no plucked-string task in any other FY5 chapter.
- L3-05 physics: an ideal pluck at the middle gives amplitudes ∝ sin(nπ/2)/n² = 1, 0, 0,111, 0, 0,040, 0. A pluck at d = L/10 gives 1, 0,476, 0,291, 0,192, 0,129, 0,085. Both match the table (0,47/0,30/0,19/0,13/0,09), so the example data are physically consistent. v = 2·0,650·196 = 254,8 → 255 m/s, and the tolerance is right. G3 = 196 Hz is right.
- Round-1 Blocking 2 is resolved. Recomputed the L2-05 rows: 30,77 / 29,32 / 31,48 / 30,05 m/s, so "29,3–31,5 m/s, hajonta noin 1 m/s" is correct.
- Round-1 Polish items applied: L1-08 rounding reason, the "Aineiston käsittely" headings, and the irrelevant sentence removed from L2-07.
- Recomputed in one script: L1-08 0,167 s; L2-05 30,41 m/s; L2-06 262 Hz; L2-07 548,4 Hz (student 544,1, too small); L3-04 0,4753 m/s; L3-05 254,8 m/s. All 20 values match answers.py and exercises.json.
- L1-06 and L1-07 (choices reordered): each has exactly one correct option, its answer text matches the correct choice, and the distractor feedback is right.
- Scope: the harmonic series, timbre and FFT spectrum are in the slot's täsmennys. Pluck position uses only the node idea from fy5-13. Level 3 fits (data interpretation plus a causal explanation). The kind "graph" is no longer used.
- Render: the L3-05 table and solution fit the card at 1280 px (L3 shots 6–7).
