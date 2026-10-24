VERDICT: PASS

Tester report for fy3-2 (headless Chromium, `PW_CHROMIUM=/opt/pw-browsers/chromium-1243/chrome-linux64/chrome`).

1. Load: no console errors or page errors; `window.simState` exists after 1.5 s (`scripts/test_sims.py`, console/pageerror lists empty).
2. W = F s: `content/FY3/fy3-2/sim.js:32` `const W = F * s;` matches lesson.md:15 `W = F s` exactly; asserted at default and at several slider settings (100x10=1000 J, 40x5=200 J, maxima 100x20=2000 J, F=0 gives W+P=0).
3. P = W/t: `sim.js:33` `const P = W / t;` matches lesson.md:29 `P = W/t`; asserted (1000 J / 4 s = 250 W, 2000 J / 20 s = 100 W).
4. Animation: `sim.js:26` Vedä resets u=0 and starts; `sim.js:34` advances u by deltaTime/t, clamps at 1 and stops. Tests press the button via DOM (short t=1 s): u == 1 after 1.2 s, running == false, Wdone == 400 J == W (50 N x 8 m). Mid-run: with t=2 s, u ~ 0.5 at ~1 s (tol 0.1); with t=20 s, 0 < u < 0.1 and running right after press; Wdone == W*u during the pull (`sim.js:35`).
5. Work bar / area: `sim.js:64` shaded area width ∝ u, `sim.js:75` bar width barW*u; both driven by u, which is tied to Wdone (checked through simState; drawing itself not pixel-tested).
6. Sliders labelled with units: labels read "Voima F = 60 N", "Matka s = 10,0 m", "Aika t = 5,0 s" (`sim.js:37`); ranges 0-100 / 1-20 / 1-20 match sim-spec.md. Asserted.
7. Canvas is 600x400 (`sim.js:20`); asserted.
8. Added to tests/sims/fy3-2.json (4 assertions, no duplicates): canvas 600x400, slider labels end in N/m/s, slider ranges per spec, exactly one Vedä button. Previously present assertions (14) kept.
9. Minor, non-blocking: the sim is intentionally limited to constant force along motion (lesson also shows variable force/spring triangle at lesson.md:51; sim does not show that, consistent with sim-spec.md). Note test_sims tolerance is relative to max(1,|expected|), so the "u == 1" check has effective tol 1e-6 and the half-way check effective tol 0.1.

Raw test_sims output:
```
PASS preview/fy3-2  [] []
```
Build output: `built fy3-2 (draft)` / `built index + FY3 -> preview`.
