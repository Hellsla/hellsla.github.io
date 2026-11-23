VERDICT: PASS
CONTENT-HASH: d3918dbf39dfd275
SCOPE: delta caption-label,md-paragraphs,numbers,reflow,typography from 8a4aaa9b86ce5839 base b5600a6

## Blocking
- none

## Polish
- solutions.md fy6-8-L3-05 Annettu — still says "(esimerkkiaineisto)" although the same marker was taken out of the captions; harmless for physics.

## Checked
- Rewritten Kaava blocks start from $U = E - R_\text{s} I$ or the loop equation $E - R_\text{s} I - RI = 0$ (Kirchhoff, a prerequisite) and derive $I_\text{k} = E : R_\text{s}$, $I = E : (R + R_\text{s})$ and the two-point slope; every row is algebraically right.
- Battery groups: series $E = 2E_1$, $R_\text{s} = 2R_{\text{s}1}$; parallel $1 : R_\text{s} = n : R_{\text{s}1}$ with $E = E_1$ and $I_1 = I : 2$; reversed cell $E = E_1 + E_1 - E_1$ with $R_\text{s} = 3R_{\text{s}1}$. All match the brief.
- L3-05: wire resistance in the slope, $U = E - (R_\text{s} + R_\text{j})I$, then $R_\text{s} = 1{,}10 - 0{,}30 = 0{,}80\,\Omega$, $I_\text{k} = 6{,}11\,\text{V} : 0{,}80\,\Omega = 7{,}6\,\text{A}$ at the battery's terminals. Correct.
- L2-06: the crossing current from $U_\text{A} = U_\text{B}$ is $0{,}11\,\text{V} : 0{,}28\,\Omega = 0{,}39\,\text{A}$ (answer 0,4, tolerance 0,13). Correct.
- Recomputed in one script (my formulas vs answers.py vs exercises.json): 32,5 A; 0,15 Ω; 1,0 Ω; 5,5 V; 3,0 W; 1,0 A; 0,75 A; 0,316 A; 1,6 V; 0,38 Ω; 0,56 Ω; 7,6 A; 0,020 Ω. All agree within tolerance.
- Paragraph splits (L1-06/L2-07 model answers, L3-04 check) change no claim; the slope-to-$R_\text{s}$ reasoning and "the power maximum is flat" are right.
- Content hash checked at start and end: unchanged.
