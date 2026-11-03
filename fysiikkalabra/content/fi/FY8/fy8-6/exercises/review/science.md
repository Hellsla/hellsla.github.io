VERDICT: PASS
CONTENT-HASH: 028a3512b6c4895c

## Blocking

## Polish
- exercises/exercises.json:48 (L2-01) — "kuinka suuri jännite LEDiin on vähintään kytkettävä" while solutions.md L2-01 says the measured threshold is usually about 0,1 V below this estimate; "Arvioi LEDin kynnysjännite" avoids calling a value a minimum that real LEDs go under.
- solutions.md L2-03 — Vastaus "noin 39 mW, kaksi merkitsevää numeroa" while exercises.json answer is 39.4; harmless with 2 % tolerance, but the stored answer could be 39.
- solutions.md L2-04 Järkevyys — "kuten fluoresenssissa aina": fine at this level (C); "tavallisesti" would be exact.

## Checked
- Recomputed all 12 answers in one script with own formulas: 3,124e-19 J; 2,362 eV; 4,612e14 Hz; 873 nm; 6,568e-34; 2,638 V; 6,304e-34; 39,36 mW; 0,541 eV; 6,748e-34 (LSQ k = 4,212e-15, b = −0,164 V); 2,403e-35; 22,08 % — all match answers.py and solutions.
- L3-01 data realistic (offsets −0,11…−0,13 V below hc/(eλ)); two-endpoint check 4,18e-15 V s right.
- L3-02 steepest/shallowest lines called an estimated range ("todennäköisesti"); (6,6 ± 0,2)·10^-34 J s, ≈4 %.
- L3-03 one photon per electron at most; 68 mW upper bound check real.
- L2-02 assumption $eU_\text{k} = hc/\lambda$ stated in the task; −4,9 % explained by the offset, consistent with the lesson.
- L2-03 and L3-03 assumptions (one escaping photon per electron) stated in the task.
- Units, conversions, symbolic solving first, rounding by the limiting datum in every solution.
- Notation (U_k, h = ek, 1240 eV nm) matches the brief; all within FY8 scope.
