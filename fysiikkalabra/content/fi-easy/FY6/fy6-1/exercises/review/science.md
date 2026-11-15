VERDICT: PASS
CONTENT-HASH: f2d06e99ef2be864

## Blocking

## Polish
- exercises/solutions.md:9 (L1-01 Järkevyys) — the comparison $21\,\text{W} : 12\,\text{V} = 1{,}75\,\text{A}$ uses $P = UI$, which this chapter does not teach yet — compare with the brief's table values (taskulamppu $0{,}3\,\text{A}$, laturi $2\,\text{A}$) instead.
- exercises/solutions.md:149–150 (L2-06) — Periaate says "lähes koko virta kulkee johdon kautta", Mallivastaus b) says "Lampun läpi ei kulje virtaa" — write "lähes ei lainkaan virtaa" in b) so the two agree (C-level otherwise).
- exercises/solutions.md:173–174 (L3-05) — $5{,}2 \cdot 10^{4}\,\text{s} = 14{,}5\,\text{h}$ is followed by the answer "noin $14\,\text{h}$"; reads like double rounding ($14{,}46\,\text{h}$ → $14\,\text{h}$) — show $\approx 14{,}5\,\text{h}$ as an unrounded intermediate ($14{,}46$) or give the rounding reason.

## Checked
- All 16 numeric answers recomputed independently in one script (I = Q/t, U = E/Q, Q = Ne, areas under the (t, I) graphs, trapezoids, ΣUIt): every one agrees with exercises.json and answers.py to within 0,04 %; a student's 2-sf answer stays inside the tolerance (L2-01 $110\,\text{C}$: +1,9 %).
- L2-05 b) $0{,}38\,\text{A}$, c) $0{,}37\,\text{A}$ from the table; L2-07 means $0{,}310$ / $0{,}306\,\text{A}$, differences never over one display step; L3-04 $Q = 3{,}35\,\text{Ah}$, $U_\text{ka} = 3{,}73\,\text{V}$, $45\,\text{kJ}$, estimate +7,2 %.
- L3-05: $n = 1{,}3 \cdot 10^{23}\,\text{1/m}$ realistic for a ~1,5 mm² copper wire; $v = 1{,}92 \cdot 10^{-2}\,\text{mm/s}$, $14{,}46\,\text{h}$ per metre; explanation of instant lighting matches the brief's misconception section.
- Figures virta-kuvaaja and lataus-kuvaaja: polylines carry exactly the values the solutions read (0,40/0,10 A; 0,50 A then linear to 0 at 100 s); alt texts give the same values; neither shows the charge.
- kaavio-malli: both cells plus-up, upper − to lower +, IEC symbols (long thin plate +, lamp circle with cross, A meter), current arrow from + along the top: matches the model answer.
- Choice tasks L1-06, L1-07 and statements L1-09: exactly one correct option; every distractor really wrong and its feedback correct (electron direction, no current "used up", drift vs. signal, open switch zero current everywhere, air gap an insulator).
- Significant figures per P7: 150 C (3), 3000 mAh (4), 30 s (2) etc.; every stated limiting datum is the really limiting one.
- Magnitudes realistic (starter 150 C, 9 V/AA capacities, phone 12,5 Wh, LED 20 mA); scope inside FY6 fy6-1 and the brief; notation (I, Q, t, U, E, N, e) as in the brief.
- Solutions all seven parts, symbolic before substitution; L2-03 check $mgh = 40 \cdot 9{,}81 \cdot 100\,\text{J} \approx 39\,\text{kJ}$ is right.
- Hash identical at start and end.
