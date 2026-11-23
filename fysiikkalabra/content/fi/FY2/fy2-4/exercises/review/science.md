VERDICT: PASS
CONTENT-HASH: 47ad0bab5c624779
SCOPE: delta md-paragraphs,numbers,reflow,teacher-figure,typography,wording from 6c7acbf24ababf6e base a5182aa

## Blocking

## Polish
- solutions.md L1-01, L2-05, L2-06 Kaava — "kysytty $\eta$ on jo yksin, joten sieventämistä ei tarvita" / "ratkaistavaa ei tarvitse sieventää" is a process remark, not physics; it can be dropped (C).
- fy2-4-L2-09: $\eta = 25\,\%$ is low for an electric motor; "pieni leikkimoottori" in the task would make it plausible (C, still open from my previous report).

## Checked
- Hash 47ad0bab5c624779 at the start and the end; only solutions.md changed since base a5182aa, plus the teacher-approved figure fy2-4/grid (category teacher-figure; the solution still reads 8, 2 and 6 squares, as the figure description states).
- Every rewritten Kaava now names its starting law: the efficiency definition $\eta = E_\text{a}/E_\text{o}$ or $P_\text{a}/P_\text{o}$, energy conservation $E_\text{o} = E_\text{a} + E_\text{h}$ (or with powers), $E = P\,t$ at constant power, $E_\text{o} = Hm$, and the proportionality of arrow width to energy; each is then solved symbolically before substitution.
- L1-02: the power form is derived correctly, $\eta = P_\text{a} t / (P_\text{o} t) = P_\text{a}/P_\text{o}$, with its condition (constant power) stated.
- L2-02: one useful power $P_\text{a}$ for both lamps (same light output) is the right model; $P_\text{o,hehku} = 54\,\text{W}$.
- L3-05: $E_\text{h,v} = (E_\text{h}/E_\text{o}) \cdot E_\text{o,v}$ rests on the constant loss share the table shows; the new wording says so.
- Recomputed every numeric answer in one script with my own formulas: 85, 30 %; 3,0 W; 2000 J; 4,0, 9,0 kJ; 200 kW; 78,8 %; 96 kJ; 54 W; 0,228 kWh; 45 kW; 4,3; 79 %; 25 %; 1,5; 2083 s; 180 J; 3,14; 6,89 kWh: all agree with answers.py and exercises.json within tolerance; no unit or tolerance changed.
- The md-paragraph splits (L1-06, L2-05, L2-06, L2-07, L2-08, L3-04, L3-05) move no number and change no claim.
