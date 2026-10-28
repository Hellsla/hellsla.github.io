VERDICT: PASS
CONTENT-HASH: a0884c77f1e7ec8a

## Blocking

## Polish
- inquiry.json:92 — pred-2 feedback still calls the simulation's output "mittausten" — "mallin arvojen mukaan".
- inquiry.json reflect — "Vertaa ennusteitasi mittauksiisi": the student recorded model values — "kirjaamiisi mallin arvoihin".
- inquiry.json exp-1/exp-2 — the sim computes W = Fs directly, so these experiments confirm arithmetic; the Joule table is the evidence — say so at the point of use (e.g. in exp-1 intro).
- sim.js:2–3 header comment — "plain DOM text" is now KaTeX-rendered TeX in the DOM; the comment is stale (code comment only).

## Checked
- Test diff since 46aa00b (last PASS): only three assertions changed, all to read TeX via simText. The label test still requires units N, m, s on the three sliders; the readout tests still require W = 600 J and P = 120,0 W at F = 60 N, s = 10 m, t = 5 s, and W = 640,5 J at 61 N × 10,5 m. Same numbers, same tolerance 0 — no physics check lost or loosened.
- sim.js diff: only label strings (fi → tx with {,}), graph box y/h (50/200 → 70/180, used consistently in yF and xS) and caption position. W = F·s, P = W/t, Wdone = W·u, speed handling and simState keys unchanged.
- Screenshots 390 and 1280 px: readout shows W = Fs = 600 J, P = W/t = 120,0 W; F = 60 N arrow, s = 10,0 on the graph; the old caption/axis overlap is gone.
- Model limits (constant speed, friction = pull, work → heat) are in the Mallin oletukset panel; howto says speed changes only the pace — correct for the code.
- All 12 answers recomputed in one script: agree with answers.py and exercises.json within 2 % (250,155 → 250 kJ, 588,6 → 590 J, 45,4 → 45 min).
- Inquiry numbers: 98 N; 600/1200 J; 120 → 30 W; siirto 240 W (mistakes 9,6, 0,24); check-2 180 J (mistakes 240, 120); check-1 ratio 3; virhe 4,0 J; exit 98 J and 20 J; Joule table Q/W ≈ 0,99 (19,6 J/drop ≈ 2 kg × 1 m).
- exp-1 locks F, t and varies s; exp-2 locks F, s and varies t; simState gives W and P.
- Worked example symbolic before substitution; spring figure to scale; solutions all formula-first.
- Formulas W = Fs, area under (s,F), W = Gh = mgh, P = W/t = Fv: conditions stated, within FY3 scope.
