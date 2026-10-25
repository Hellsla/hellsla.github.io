VERDICT: PASS
CONTENT-HASH: 570e52bc4aec7171

## Blocking

## Polish
- sim-spec.md:1 — still says the efficiency slider is "10–60 %" for every heat engine — add that the automoottori mode stops at 45 %.
- lesson.md:7 — "laajenevalle kaasulle se on $-p\,\Delta V$" holds only at constant pressure; the Kaava paragraph has the condition, Ydinajatus does not — consider "vakiopaineessa".

## Checked
- New Kaava formulas: $Q_\text{sisälle} = Q_\text{ulko} + W$ and $\varepsilon = Q_\text{sisälle}/W$ correct, all symbols named with units; consistent with L3-02 (ε = Q/W, Q_ulko = Q − W) and with sim.js (Pout = cop·Pel, Pambient = Pout − Pel).
- Sign sentence (Ydinajatus and Kaava): W = pΔV is work by the gas; in fy3-5's ΔU = Q + W the work on the gas is −pΔV — correct.
- "voima kertaa matka: W = Fs = pAs", As = ΔV, constant p — correct and inside FY3 scope (W = Fs).
- Heat-pump SVG: W 20 px + Q_ulko 40 px = Q_sisälle 60 px, ε = 60/20 = 3; arrows merge into the output; aria-label matches.
- Figure 1 (labels only): Q₁ 60 px = W 24 + Q₂ 36, η = 0,40 — unchanged physics (reused).
- Sim, Playwright (preview current, #sim-root in view): automoottori preset 60 kW/30 % → 18 + 42; slider max 45, setting 99 clamps to 45; 60 kW → 27 + 33, 200 kW/45 % → 90 + 110, residual 0, etaTotal = η. Lauhde max back to 60 after mode change. Pump 1 kW, cop 3 → 1 + 2 = 3. Shortened readout lines numerically right.
- Other sim modes, CHP cap, arrow scaling, speed independence — reused from round 1 (code unchanged there).
- All 12 answers, answers.py and solutions' numbers — reused (unchanged).
- Exit ticket (100 J; 18 + 42 kW; pump reasoning) — reused.
- Worked example (38 %/310 MW, 88 %/60 MW, symbolic first) — reused.
