VERDICT: PASS
CONTENT-HASH: bf6c90e5e26557a0

## Blocking
None.

## Polish
- tests/sims/fy3-8.json — no assertion that the current-point marker or the per-material chart lines are drawn (canvas pixels, not in simState); low value, optional. If wanted, add `window.simState` fields for the plotted point and assert them.
- tests/sims/fy3-8.json — alpha is asserted only at T = 20 °C (dL = 0); the dL assertions cover steel, aluminium, borosilikaattilasi, copper and tavallinen lasi once each, so all five materials are covered, but no material is asserted for both signs of ΔT. Optional.

## Checked
- `test_sims.py fy3-8`: `PASS preview/fy3-8  [] []` (43 assertions, no console or page errors)
- `lint_lesson.py fy3-8`: 0 error(s), 0 warning(s); hash before and after the review: bf6c90e5e26557a0 (unchanged)
- Formula: sim.js `dL = alpha * L0 * dT`, `L = L0 + dL`, `dT = T - 20` match lesson.md (ΔL = αL₀ΔT, L = L₀ + ΔL); the five α values (12, 23, 17, 9, 3,3 · 10⁻⁶ 1/K) match spec and lesson table
- Every spec slider/control has an assertion: material select (5 options, labels, alpha per option), L₀ slider (range 1-100 step 1, value), T slider (range -40...120 step 1, value), run/pause button (stop, stay fixed, resume)
- Every simState field in the spec (material, alpha, L0, T, dT, dL, L) is asserted; also rel, spacing, amp (√T, two temperatures), chart axis (L₀ = 1, 10, 100 m) and E = 100
- Readout text asserted (decimal comma, Finnish minus, +/− sign, ΔT line, ΔL in mm, L with enough decimals, ΔL/L₀, axis); the nowrap spans did not change textContent, all readout and label assertions still pass
- Both round-1 additions are present and pass: controls (with the button) before readout; simState.E = 100
- Own sweep (node + Playwright): 5 materials × L₀ {1, 50, 100} × T {-40, 0, 20, 21, 120} at 360, 390 and 1280 px: every simState number finite, L = L₀ + ΔL and ΔL = αL₀ΔT hold, no console/page errors, no horizontal page scroll
- Determinism: vibration phase depends only on index and tAnim (no Math.random in sim.js); deltaTime clamped to 100 ms
- Units/g convention: sim contains no g or N/kg
