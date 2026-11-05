VERDICT: PASS
CONTENT-HASH: 2410c9996b853823
Round: 2

## Blocking

## Polish
- [Minor] L3-05 Sijoitus — the radicand is now dimensionless with "A" after the root (the numerator unit N·m and the denominator unit Vs/A are given on the lines above); acceptable, but a short note "yksikkö $\sqrt{\text{N}\cdot\text{m} : (\text{Vs/A})} = \text{A}$" would let the pupil follow the units.
- [Minor] L2-05, L2-07, L3-04 tables — long captions with "(esimerkkiaineisto)" make 2 tables scroll at 360 px (check_layout notes "2 wide table, scrolls", status OK); shorten the captions if wanted (carried over, now only a note).

## Checked
- Round 1 Blocking (L3-05 Sijoitus overflow at 360 px) is resolved: the chain is split into Nimittäjä, Osoittaja and a short root chain; `check_layout.py fy7-4 --width 360` is OK for fi, en and fi-easy. Capture L3-1280-7/8 shows no clipping or red source.
- Round 1 Polish: L1-08 Periaate now "kulman siniin $\sin\alpha$ eikä itse kulmaan $\alpha$" (resolved); L2-06 pupil's calculation is in ”…” (resolved); L2-07 Järkevyys uses the lesson's radius 1,3 cm, 65 turns (resolved).
- Recomputed L3-05: numerator 1,849·10^-3 N·m, denominator 6,283·10^-7 Vs/A, I = 54,25 A, F = 0,0294 N = mg; L2-06 (3,04·10^-3 N, 0,041 T), L2-07 (l = 5,3 m): the answers match the solutions. L3-05 b) now says the arrangement is unstable sideways, which is correct.
- L1-06 option wording changed only in the correct option and its answer text.

## Scores
illustrations 4 · typography 5 · Finnish 5 · accessibility 4
