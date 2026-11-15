VERDICT: PASS
CONTENT-HASH: 6f158dcc37c616a5

## Blocking

## Polish
- solutions.md fy7-2-L2-05, L2-06 — the stage is headed "Reading the graph" but the task gives a table — "Reading the table".
- exercises.json fy7-2-L1-09 — `answer` 2.84 (three figures) while the data has two and the solution answers $2.8\,\text{cm}$; 2.8 is within the tolerance, so this is consistency only — 2.8 with tolerance 0.03 would match the solution.
- exercises.json fy7-2-L2-09 — `answer` 3.35 against the solution's $3.4 \cdot 10^{-27}\,\text{kg}$; both are within the tolerance — keep it, or align it with the solution.
- packet — the exercise brief's lesson excerpt is empty, so the notation could not be checked against the lesson's Kaava and Esimerkki. The set's notation ($F_\text{m}$, $\overline{F}_\text{m}$, $r = mv : (qB)$, $T = 2\pi m : (qB)$) matches the glossary and the scope notes.

## Checked
- All 18 numeric answers recomputed in one script from the task text with my own formulas. Each agrees with answers.py and exercises.json within tolerance.
- L3-05 (the proofreading fix): the data $0.200\,\text{m}$, $60.0\,\text{kV}$ and $1.00\,\text{T}$ now carry three figures, matching the answer $1.05\,\mu\text{s}$. I recomputed $v = 1.92 \cdot 10^{7}\,\text{m/s}$, $E_\text{k} = 3.07 \cdot 10^{-13}\,\text{J} = 1.92\,\text{MeV}$, $n = 31.9 \approx 32$ and $T = 65.6\,\text{ns}$. Using the unrounded $n$ also gives $1.05\,\mu\text{s}$. $v/c = 0.064$. The relativistic estimate $\tfrac34\beta^2 \approx 0.3\,\%$ is correct, as is the remark that the period grows at higher energy (only mentioned in passing, as the plan asks).
- L3-04: a least-squares fit through the origin gives $22.8\,\text{u}$ and a free fit gives $22.7\,\text{u}$ (intercept $0.5\,\text{cm}^2$), so a line fitted by hand stays within the 4 % tolerance. Sodium-23 at $400\,\text{V}$ gives $r = 6.9\,\text{cm}$. The slopes quoted for Li-7 and K-39 are correct. The reason the line passes through the origin is physical.
- Directions: L2-05 has $\overline{v}$ to the right and $\overline{B}$ into the page, so the force on a positive ion is up. L2-08 has the electron moving up with $\overline{B}$ out of the page, so the force is to the left (diagram C). $F_\text{m} = 2.4 \cdot 10^{-16}\,\text{N}$ and $mg = 8.9 \cdot 10^{-30}\,\text{N}$. Each wrong diagram (A, B, D) has exactly the one error its feedback names.
- L1-06 and L2-07: exactly one option is correct in each, and every distractor's feedback gives the right physics.
- L2-06: $d \propto m$ holds because the velocity selector gives every ion the same speed. The masses $25.1\,\text{u}$ and $25.9\,\text{u}$ and the share 78.9 % are correct, and the data resemble the natural abundances of magnesium.
- L3-01 and L3-03: $r \propto \sqrt{m/q}$ at the same $U$, giving $4.0\,\text{cm}$ and $1.41$.
- Figure r-points: the line is generated from the deuteron's mass. At $1.5 \cdot 10^{6}\,\text{m/s}$ it gives $r = 15.65\,\text{cm}$ (the solution reads it as 15.7), and the figure does not give the mass away.
- Magnitudes in the reasonableness checks: L1-01 $r \approx 1.25\,\text{cm}$, L1-02 a proton circle of about $14\,\text{m}$, L2-04 a magnetic force of about $10^{8}$–$10^{9}$ times the weight at $10^{6}\,\text{m/s}$, L2-05 about $210\,\text{eV}$.
- Scope: everything is inside FY7's charged-particle contents and the scope notes. Each solution derives symbolically before substituting, states its conversions, and justifies its rounding by the limiting datum.
