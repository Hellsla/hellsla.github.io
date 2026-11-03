VERDICT: PASS
CONTENT-HASH: 6e962ba765f93e9c

## Blocking

## Polish
- exercises/exercises.json (L2-01) — "kuinka suuri jännite LEDiin on vähintään kytkettävä" while solutions.md L2-01 says the measured threshold is usually about 0,1 V below the estimate; "Arvioi LEDin kynnysjännite" avoids calling it a minimum.
- solutions.md L2-03 — Vastaus "noin 39 mW, kaksi merkitsevää numeroa" while exercises.json stores 39.4; harmless within 2 % tolerance.
- solutions.md L2-04 Järkevyys — "kuten fluoresenssissa aina": fine at this level (C); "tavallisesti" would be exact.

## Checked
- One-script recompute of all 12 answers with own formulas: 3,124e-19 J; 2,362 eV; 4,612e14 Hz; 873,2 nm; 6,568e-34; 2,638 V; 6,304e-34 (stored 6,3e-34, within tolerance); 39,36 mW; 0,541 eV; 6,748e-34 (LSQ k = 4,212e-15, b = −0,164 V); 2,403e-35; 22,08 % — all match answers.py and solutions.
- L3-01 data realistic (offsets −0,11…−0,13 V below hc/(eλ)); two-endpoint check 4,18e-15 V s right.
- L3-02 steepest/shallowest lines as an estimated range; (6,6 ± 0,2)·10^-34 J s, ≈ 4 %.
- L3-03 at most one photon per electron; 68 mW upper-bound check real.
- L2-02 assumption eU_k = hc/λ stated in the task; −4,9 % explained by the offset, consistent with the brief.
- L2-03, L3-03 assumptions (one escaping photon per electron) stated in the tasks.
- Units, conversions, symbolic solving first, rounding by the limiting datum throughout.
- Notation (U_k, h = ek, 1240 eV nm) matches the brief; within FY8 scope.
