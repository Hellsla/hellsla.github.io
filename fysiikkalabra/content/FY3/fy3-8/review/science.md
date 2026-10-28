VERDICT: PASS
CONTENT-HASH: 59f4726db9209370

## Blocking

## Polish
- content/FY3/fy3-8/sim.js:1033 — the axis range renders as "−20–30 mm": an en dash right after a negative number reads like a second minus — write `${tx(yMin,dec)}\text{ … }${tx(yMax,dec)}` or "−20 mm … 30 mm".
- content/FY3/fy3-8/sim.js:1099 — `fi` is now unused (every value goes through `tx`) — delete it.
- content/FY3/fy3-8/sim-spec.md:1 — the spec still lists α beside each material in the select; the options now name the material only and α is in the readout — say "α näkyy lukemissa".
- content/FY3/fy3-8/sim.js:1071 — `p.textWidth('$\\Delta L$')` measures the TeX source, not the rendered label; harmless at x ≤ 590, but use a fixed half-width.

## Checked
- answers.py and all 12 exercises recomputed independently (2,88; −51,75; 0,85; 0,84; 0,3375; 52,08; 3,024; 36; 23; 120; 20; 457): all match, every key inside its 2 % tolerance; solutions are symbolic first, units and signs right (L1-02 negative, L2-03 rail-gap reasoning, L3-02 bends toward steel, L3-01 hole grows).
- Worked example 0,0864 m ≈ 86 mm, 0,07 %; exit ticket 0,021 m.
- inquiry.json numbers: pred-1/pred-2 6,00 mm and 12,0 mm, 0,0600 %; olomuodot table 0,36 / 2,1 / 11 / 34 cm³; virhe 28 mm vs 1,8 mm (×15); siirto 44 mm, mistakes 0,044 and 110, with glass 42,9 ≈ 43 mm, ethanol/glass γ ≈ 41; check-2 α = 23, mistakes 46 and 15,3; check-3 air/steel γ ≈ 94 ("noin sata"). Correct options all right; Bea's asymmetric-potential model and the feedback on Cem's symmetric one are sound physics.
- Experiments: exp-1 locks material and L₀, varies T, measures dT, dL; exp-2 locks material and T, varies L₀, measures dL, rel; all keys exist in simState.
- Coefficient tables (α: 12, 23, 17, 9, 3,3; γ: 0,21, 1,1, 0,95, 3,4 · 10⁻³) realistic; water 4 °C anomaly and L1-04's γ(T) remark correct.
- Scope: ΔL = αL₀ΔT, ΔV = γV₀ΔT, γ ≈ 3α with the small-change condition and ~100 K validity, inside FY3 "lämpölaajeneminen".
- Figures: d > d₀ with equal particle sizes, ΔV above the cold level, ΔL at the free end; all marked as exaggerated.
- Sim LaTeX pass: the sim.js diff changes only labels and formatting; the physics lines (dT, dL, L, rel, spacing, amp ∝ √T, chartRange) are unchanged. Screenshot at 1280 px renders the KaTeX readout and canvas labels correctly; the chart axis −20…30 mm matches simState.
- Test diff (tests/sims/fy3-8.json): every readout assertion keeps the same numbers (50 K, +6,00 mm, 10,0060 m, −60 K, −138 mm, 99,8620 m, 3,3, +0,330 mm, 1,00033 m, +0,0600 %, axis −20…30), now read as TeX through simText. The only loosened check is α in the option labels, and the five simState.alpha assertions and the readout α check still cover it. No physics check was lost.
- The sim's limits (constant α, symmetric drawn vibration, spacing set from the formula, ×100 exaggeration, < 0,3 %) are stated in howto/model; max real change 0,23 %.
