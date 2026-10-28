VERDICT: PASS
CONTENT-HASH: d5016cfcfdfdcdd5

## Blocking

## Polish
- review/checks.txt:4 — says `FAIL sims`, but `python3 scripts/test_sims.py fy3-1` now passes (29 assertions, KaTeX labels checked); the file is stale — rerun `check_lesson.py fy3-1` so the record matches.
- sim.js:1020 — the drawn settling oscillation has the same ω = 10 1/s for every mass and body; drawing only, simState holds rest values — optional.

## Checked
- Full review; hash d5016cfcfdfdcdd5 at start and end. Change since the last PASS (7036c6b~1..HEAD): sim.js labels and readout converted to TeX strings (new `tx()` gives `{,}` decimal comma) and four test assertions in tests/sims/fy3-1.json rewritten to read the TeX via simText.
- Test assertions: no physics check lost. Each rewritten assertion still checks the same numbers (g = 9,81 and G = 98,1 N at 10 kg on Maa; Mars 3,71 m/s² and 74,2 N at 20 kg; chart scale 49,6 N at 2 kg and 992 N at 40 kg); none removed. simState computation (G, stretch, arrow, bars, chartFull) is byte-identical.
- Sim screenshots (390, 1280 px): readout m = 10 kg, g = 9,81 m/s², G = mg = 98,1 N; bars 16,2 / 37,1 / 98,1 / 248 N; scale 0–248 N; ruler pointer ≈ 7,5 px below 0 (190·98,1/2480) — all right.
- answers.py and all 12 exercise answers recomputed with my own formulas: 39,24; 6,0; 48,6; 9,6; 62; 4,995; 0,5886; 1187,55; 5,886; 6,807; 133,2; 68,75 — match, within tolerance.
- solutions.md and worked example: unknown solved symbolically first; 1177,2 N / 445,2 N, ratio 0,38.
- lesson.md: 70 kg ≈ 690 N, 1,62/9,81 ≈ 0,17, g table, bathroom-scale reasoning; scope stays at G = mg, no Newton's laws.
- Figures: forcemeter x/2x and G/2G; force–extension slope 0,501 px ratio consistent with grid (points on the line); weight–mass end points 981/371/162 N at 100 kg, Jupiter line consistent with 24,8 m/s².
- inquiry.json: 6,0 km; 98,1/294 N (+196 N); 248 N (×2,53); 3,5 N (wrong 8,96); 4,905 N vs 4905 N; 72,7 N with mistakes 19,44/117,72/7,41; 8,8 m/s² with mistakes 0,114/44,9. exp-1 locks body, varies m; exp-2 locks m, varies body; simState gives m, g, G. Sim `model` states the constant-g assumption.
- Exit ticket: 29 N / 4,9 N, 7,5 cm, 15 N right.
