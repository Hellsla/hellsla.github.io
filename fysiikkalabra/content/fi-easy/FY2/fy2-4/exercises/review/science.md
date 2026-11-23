VERDICT: PASS
CONTENT-HASH: 1cbb64c4124fa188
SCOPE: delta md-paragraphs,numbers,reflow,teacher-figure,typography,wording from 290ca9ff5936acc5 base a5182aa

## Blocking

## Polish
- solutions.md:276 and :282 (fy2-4-L1-09): the round-1 point is still open. The task's hint names MAFY's table *Polttoaineiden LHV-lämpöarvoja*, but Annettu and Vastaus say "polttoaineiden lämpöarvot". Fix: use the table's exact name in both places.
- solutions.md:379 (L1-09), :199 and :325: "joka on jo ratkaistu kysyttyyn muotoon" and "sieventämistä ei tarvita" are correct. They are only wordy; this is a style point and blocks nothing.

## Checked
- Every rewritten Kaava line now starts from the definition $\eta = E_\text{a}/E_\text{o}$ (or $P_\text{a}/P_\text{o}$), from conservation $E_\text{o} = E_\text{a} + E_\text{h}$ (or the same with powers), or from $E = Pt$. It solves for the unknown symbolically before any substitution.
- LED power ratio: $\eta = \dfrac{P_\text{a} t}{P_\text{o} t} = \dfrac{P_\text{a}}{P_\text{o}}$ is valid at steady power, the condition the Periaate states.
- Both-lamps task: same useful power, $P_\text{o,hehku} = \eta_\text{LED} P_\text{o,LED}/\eta_\text{hehku}$, so $0{,}30 \cdot 9{,}0/0{,}050 = 54\,\text{W}$.
- Device B, solar panel and arrow-thickness tasks: the chains are correct. $\eta_\text{A} : \eta_\text{B} = 0{,}75 : 0{,}50 = 1{,}5$. $t = E_\text{a}/(\eta P_\text{o}) = 500\,000/240 = 2083\,\text{s}$. In `fy2-4/grid`, $E_\text{h} = (6/8) \cdot 240\,\text{J} = 180\,\text{J}$, and thickness proportional to energy is stated as the premise.
- L3-04: $192\,\text{MJ}/3{,}6 = 53{,}3\,\text{kWh}$, and $53{,}3/17 = 3{,}14 \approx 3{,}1$. The useful energies 15,3 and 13,3 kWh are unchanged.
- LED-lamp error-analysis task: $E_\text{h,v} = (E_\text{h}/E_\text{o}) \cdot P\,t_\text{v}$ correctly assumes that the share stays the same as on every row. $650/2160 = 30\,\%$.
- L1-09: $E_\text{o} = Hm = 101{,}5\,\text{MJ}$ and $\eta = 78{,}8\,\%$.
- The paragraph splits in the 120 % claim, the motor comparison, the lamp-comparison table, the LED-lamp error analysis and the kettle-row error analysis change no claim or number.
- `fy2-4/grid`, the figure the teacher approved: the 8, 2 and 6 squares match the task, the alt text and $\eta = 0{,}25$ in the generator, and the figure gives no answer away.
- answers.py matches every numeric answer in exercises.json within its tolerance. No answer changed. Hash 1cbb64c4124fa188 at the start and at the end.
