VERDICT: PASS
CONTENT-HASH: 40177a99521db833

Full review, round 2: I judged the changes in L1-07, L2-05…07, L3-04 and the rewritten L3-05, and recomputed every answer.

## Blocking

## Polish
- solutions.md:195 — L3-05 Järkevyys: the end-point speed 0,55 m/s comes from the same two raw points as the steepest line, so it equals k_max by construction. That is no check. — Compare with the best line instead: about 0,51 m/s, which lies inside 0,40–0,55 m/s.
- solutions.md:189 — L3-05 Periaate states "arvo on välin keskikohta" as a rule, but the best-fit slope is 0,51 m/s, not 0,475. — Write "arvioidaan välin keskikohdaksi".
- solutions.md:194 — L3-05 rounding reason "kuten pisteiden koordinaateissa" does not fit an uncertainty. — "Epävarmuus ilmoitetaan yhdellä tai kahdella numerolla."
- solutions.md:183 — L3-04 still says "kuten venymissä", but most extensions have three figures. This is the reason L2-05 already had corrected. — Give the by-eye fit as the reason. Also soften "pätee … kuormattomaan jouseen asti" to "todennäköisesti", because it is an extrapolation.
- solutions.md L2-07 Periaate — says "m = kV", yet the lines read start at 0,3 g and 0,5 g. — "m = kV + b, jossa b ≈ 0".

## Checked
- All 18 answers recomputed with numpy polyfit, separately from answers.py; all agree. L2-05: 0,0797. L2-06: b = 0,829 m. L2-07: 2,707 and 7,835 → 2,89. L3-04: 0,0802 (residuals ≤ 0,24 mm; 3,5 and 12,6 mm at 600 and 700 g). L3-05: 15,8 %; the pupil's 31,6 % → 32 %.
- L3-05 data: steepest-line residuals −0,35…+0,1 m and shallowest −0,25…+0,5 m, so both are plausible bounds. The lines cross at about 2,7 s, inside the data, and the least-squares slope lies between them. The pupil's error (whole range instead of half) is real, and the interval is called an estimate, not a guarantee.
- L1-07: "saman metallin" makes the slope a density. Exactly one option is correct, and every feedback is right.
- L2-07: "tasalaatuisesta / saman aineen" is correct, the two-figure reason is the by-eye fit, and the densities match Al and Fe.
- L3-04: the range 100–500 g has its extrapolation named, and the cause (beyond the elastic range, possible permanent stretch) is right at FY1 level.
- Tolerances fit: 5 % and 10 % for by-eye fits, 3 % for the exact L3-05.
- FY1 scope kept; the notation matches the lesson.
- The hash was identical at start and end.
