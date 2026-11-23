VERDICT: PASS
CONTENT-HASH: a087415b76d715f9
SCOPE: delta md-paragraphs,numbers,reflow,teacher-figure,typography,wording from d678f4eb5ef3254a base 5b3ca4f

## Blocking

## Polish
- solutions.md L2-09 Vastaus — with 9 % and 4 % rounded to whole percents, the 5 % difference is uncertain by about ±1 percentage point (C; still open).
- solutions.md L2-10 c) — add "ja sähkövarastojen" to the balance sentence (C; still open).

## Checked
- Hash a087415b76d715f9 at the start and the end; diff judged against base 5b3ca4f (passed as d678f4eb5ef3254a): solutions.md plus the teacher-approved figure fy2-7/sankey (its 96/4 % and 91/9 % shares are what L1-02 and L2-09 read); exercises.json and answers.py untouched.
- L3-01 (my round-1 Blocking item): the undefined $E_\text{sent,1}$, $E_\text{sent,2}$ are gone; the Sijoitus substitutes into the Kaava's last form, $\Delta E = E_\text{perille}(1/\eta_1 - 1/\eta_2) = 600\,\text{MWh}(1/0{,}910 - 1/0{,}940) = 21{,}0\,\text{MWh}$; symbols agree with the Kaava and the lesson ($E_\text{lähtö}$, $E_\text{perille}$).
- Every other rewritten Kaava starts from $E_\text{lähtö} = E_\text{perille} + E_\text{häviö}$ (or with powers), $\eta = E_\text{perille}/E_\text{lähtö}$, the loss share $p = E_\text{häviö}/E_\text{lähtö}$ or $P = E/t$, and combines symbolically before substitution; each combination is algebraically right, and the loss percentage is always taken of the energy sent.
- L3-04: plant saving $r P_\text{häviö} t/\eta$ is right (house saving is delivered energy).
- Recomputed in one script with my own formulas: 32,4 MWh; 120 MW; 150 MWh; 10,96 MW; 1200 kWh; 21,04 MWh; 13,0 MWh; 65,7 houses; 4,8 %; 72 kW; 6,59 MWh; 72 MJ; 12,5 MWh: all agree with answers.py and exercises.json within tolerance; units unchanged.
- The md-paragraph splits (L2-05, L3-04, L3-05, L2-10) move no number and change no claim; L3-05 keeps the correct reason (loss grows faster than the current).
