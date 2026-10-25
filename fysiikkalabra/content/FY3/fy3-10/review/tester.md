VERDICT: PASS
CONTENT-HASH: c0868da3fd4fed5e

## Blocking
(none)

## Polish
1. content/FY3/fy3-10/sim.js:52 (sync) and :109 (readout) — after any slider change the 2 s average still contains the old state, so the ratio readout jumps: measured by simAdvance 0,5 s after (200 K/600 K/25 %) -> (N=20, 100 K, 100 %) gives ratio 182,79 (0,5 s), 7,50 (1,5 s), 0,86 (3 s), 1,03 (25 s); 100->100 K/300 K/25 % -> 100 % gives 1,43 right after. It settles within about 3 s and the "Nollaa mittaus" button fixes it, but the student sees "pV/(NT) = 182,79" when the spec says it should stay near 1,00. Fix (optional): in sync() call clearAvg() when n, t or lx changed (keeps the spec's behaviour, only drops the stale bins), or leave as is and mention the 2 s settling in the lesson.
2. tests/sims/fy3-10.json — N = 20 is never tested for the measured ratio (smallest case is N = 50). Scatter is largest there: ratio 1,12 at (20, 100 K, 100 %) after 10 s, 1,11 after 30 s, whereas the 20 s case gives 1,014. Ready-to-paste (tol 0,15, deterministic):
   {"setup": "{ const r=document.querySelectorAll('#sim-root input[type=range]'); r[0].value=20; r[1].value=100; r[2].value=100; }", "expr": "(() => { window.simRestart(); window.simAdvance(20); return window.simState.ratio })()", "expected": 1, "tol": 0.15, "note": "low corner N = 20, T = 100 K, V = 100 %: few wall hits, measured/predicted still within 0,15 of 1"}
3. tests/sims/fy3-10.json — the canvas bars (measured, predicted, ratio text) have no assertion; they are not in simState, so this cannot be fixed without changing sim.js. Acceptable as is.

## Checked
- python scripts/test_sims.py fy3-10 -> `PASS preview/fy3-10  [] []` (29 assertions, no console or page errors at 1280 px and 360 px; no horizontal overflow at 360 px).
- lint_lesson.py fy3-10: 0 errors, 0 warnings.
- Spec quantities all asserted: N, T, Vrel, pPredicted (6 points incl. corners), pMeasured/ratio (5 cases), vrms (sqrt T scaling), tAvg (about 2 s window, reset by button), slider ranges and steps, labels, readout text with decimal comma, button, DOM order, canvas 600x400.
- Ratio sweep with simAdvance from simRestart, N in {20,100,200} x T in {100,300,600} x V in {25,50,100} % at 10, 20, 30 s: every ratio in 0,937-1,122; for N >= 100 within 0,937-1,046; N = 200 within 0,96-1,014; no drift with time.
- Dynamic change sequences (6 slider jumps): ratio back to 0,95-1,03 within 1,5 s, and 0,98-1,03 after 25 s (only the transient above deviates).
- Determinism: simRestart + simAdvance(5) gives identical pMeasured on repeat runs and across fresh page loads at 1280 and 360 px (0,99669...); 5 s in one call equals 50 calls of 0,1 s (frame-rate independent).
- Formula in sim.js (p/p_ref = (N/100)(T/300)(100/V), P_REF = N kT/A from pA = NkT, impulse 2m|v_perp| per perimeter) agrees with the lesson's pV = nRT; ratio = pMeasured/pPredicted verified to 1e-12.
- Hash c0868da3fd4fed5e unchanged at start and end of the review.
