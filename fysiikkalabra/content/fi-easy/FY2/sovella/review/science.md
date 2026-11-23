VERDICT: PASS
CONTENT-HASH: 92e65712da6bbe51

## Blocking

## Polish
- [Minor] fy2-s1 c) Kaava: the general rows $E = Pt$, $P = E/t$ use $E$, and the last row uses $E$ for the city's annual consumption ($P_\text{k} = 0{,}31 E / t$). The same letter means two things in one block, which may matter more for an S2 reader. A subscript on the general row would fix it. It is not wrong (category 6).
- [Minor] fy2-s1 a) The Kaava block ends in $N = E/(kP_\text{n}t)$, but Sijoitus computes $E_1$ first. This is form only; the numbers are right.

## Checked
- Round 1, full packet. The Kaava steps of fy2-s1 a), b) and c) are the same as in the Finnish set:
  - $P_\text{keski} = kP_\text{n}$, then $E_1 = P_\text{keski}t$, then $N = E/E_1$;
  - the definition $e = m/E$, then $m = eE$, then the relative cut with $E$ cancelling;
  - $E = Pt$ applied to the winter shares.

  The algebra is right, the conditions are stated in Periaate, and everything is within FY2 scope.
- I recomputed every number with my own formulas: $14{,}016\,\text{GWh}$, $27{,}1 \to 28$; $3{,}116 \cdot 10^5$, $1{,}862 \cdot 10^5$ and $4{,}18 \cdot 10^3\,\text{t}$; $40\,\%$ and $99\,\%$; $58{,}1$ and $54{,}5\,\text{MW}$; $7$ and $73\,\text{MW}$; $7{,}1\,\text{MW}$ from the solar parks; for e) $252 + 88 + 40\,\text{GWh}$, $k = 0{,}11$, $1/6$ of the fuel, $1{,}4 \cdot 10^4\,\text{t}$, $95\,\%$, $65$ and $15\,\text{MW}$, $> 50\,\text{MW}$, $11\,\%$; the alternatives $473\,\text{GWh}$, $0{,}54$, $72\,\%$. All agree with answers.py.
- A script compared the numbers in fi-easy against fi. solutions.md and tasks.json hold identical sets of numbers, so splitting sentences into shorter ones changed no value.
- The physics in the shorter sentences was checked in d), e), the common mistakes and s2 d), and it is kept:
  - controllability is still a property with limits;
  - the nuclear plant's power can be lowered but not raised above its rated power;
  - no production method is called emission-free;
  - operational and life-cycle emissions are told apart;
  - the biomass factor is stated as an assumption.
- Rubric points add up to 18 and 14; the rubrics did not change.
- The hash was the same at the start and at the end.
