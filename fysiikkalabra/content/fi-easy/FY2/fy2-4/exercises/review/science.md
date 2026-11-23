VERDICT: PASS
CONTENT-HASH: 1cbb64c4124fa188
SCOPE: delta md-paragraphs,numbers,reflow,teacher-figure,typography,wording from 290ca9ff5936acc5 base a5182aa

## Blocking

## Polish
- solutions.md:276 and :282 (fy2-4-L1-09) — the hint names MAFY's table *Polttoaineiden LHV-lämpöarvoja*, but Annettu and Vastaus say "polttoaineiden lämpöarvot". — Fix: use the table's exact name in both places.

## Checked
- Every rewritten Kaava line now starts from one of these: the definition $\eta = E_\text{a}/E_\text{o}$ (or $P_\text{a}/P_\text{o}$), conservation $E_\text{o} = E_\text{a} + E_\text{h}$ (or the same with powers), or $E = Pt$ at steady power. Each line solves for the unknown in symbols before any number goes in.
- LED task: $\eta = P_\text{a}t/(P_\text{o}t) = P_\text{a}/P_\text{o}$ holds at steady power, the condition the Periaate states.
- Recomputed in one script:
  - $0{,}30 \cdot 9{,}0/0{,}050 = 54\,\text{W}$
  - $t = 500\,000/(0{,}20 \cdot 1200) = 2083\,\text{s}$
  - `fy2-4/grid`: $(6/8) \cdot 240 = 180\,\text{J}$
  - $0{,}95 \cdot 0{,}060 \cdot 4{,}0 = 0{,}228\,\text{kWh}$
  - L3-04: $6{,}0 \cdot 32/3{,}6/17 = 3{,}14$
  - L1-09: $80/(40{,}6 \cdot 2{,}5) = 78{,}8\,\%$
  - $\eta_\text{A} : \eta_\text{B} = 1{,}5$
  - $650/2160 = 30\,\%$

  All agree with the solutions.
- LED-lamp error-analysis task: $E_\text{h,v} = (E_\text{h}/E_\text{o}) \cdot E_\text{o,v}$ rests on a constant share, and the Kaava now states that.
- `fy2-4/grid`, the figure the teacher approved: 8, 2 and 6 squares, matching the task, the alt text and $\eta = 0{,}25$. It does not give the answer away.
- The paragraph splits (120 % claim, motor comparison, lamp table, both error analyses, L3-04) change no claim or number.
- answers.py matches all 20 numeric answers within tolerance. No answer changed.
- Hash 1cbb64c4124fa188 at the start and at the end.
