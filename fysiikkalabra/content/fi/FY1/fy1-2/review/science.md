VERDICT: PASS
CONTENT-HASH: 5ed8a5d3bb13d878

## Blocking

## Polish
- solutions.md fy1-2-L3-01 — "63 250 AU, neljä merkitsevää numeroa" has an ambiguous trailing zero by the lesson's own new rule — write $6{,}325\cdot10^{4}\,\text{AU}$.
- solutions.md fy1-2-L2-03 / L2-02 — "240 ha" and "500" are said to have two figures; adding $2{,}4\cdot10^{2}\,\text{ha}$ (as L2-02 already shows $5{,}0\cdot10^{2}$) would model the rule.
- solutions.md fy1-2-L1-01 — the Kaava line ($1\,\mu\text{m} = 10^{-6}\,\text{m}/10^{-3}\,\text{m/mm}$) is clumsy; "$1\,\mu\text{m} = 10^{-6}\,\text{m} = 10^{-3}\,\text{mm}$, joten $l_\text{mm} = x\cdot10^{-3}$" is enough.

## Checked
- Round-1 blocking 1 fixed: lesson.md now says trailing zeros of a whole number are ambiguous (384 400 → $3{,}844\cdot10^{5}$); L1-02 justification cites it; L3-02 answer 674,4 with four figures, 1920 px exact (exercises.json, answers.py, solution agree).
- Round-1 blocking 2 fixed: prefix figure symbols n, µ, m, k, M, G, T and nm…Tm upright (screenshot checked).
- Round-1 polish: L2-04 comment 1,3255; voyager-malli correct option says the signal time is from the Sun.
- All 12 exercise answers recomputed independently, answers.py and exercises.json agree (≤ 0,2 %).
- siirto 3,236 AU/a, tarkistus-2 3,22 min (mistakes 193 s, 0,0536 h), Neptune example 4,50·10⁹ km and 4,17 h.
- Voyager 2 table and 1.1.2026 values (142,9 AU, 19,8 h) recomputed from d0, v, t0; mid-Feb 2026 ≈ 143 AU matches JPL.
- Prediction/experiment feedback numbers: 1 h ≈ 7,2 AU, week ≈ 1212 AU, 33,4/334/3340 s, 1 AU = 499 s = 8,32 min.
- Every solution's reasonableness check verified numerically (L1-03, L1-04, L2-04, L3-02, L3-03).
- sim.js unchanged in physics: scale, ruler, pulse timing, Voyager model; limits stated.
- FY1 scope: only conversions, sig figs, t = s/c as given uniform motion.
