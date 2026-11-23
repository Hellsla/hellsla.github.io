VERDICT: PASS
CONTENT-HASH: efd3289961c2953a

## Blocking

## Polish
- [Minor] fy2-s1 c) Formula: $E = Pt$ and $P = E/t$ are written as the general law, but the last row uses $E$ for the city's annual consumption ($P_\text{c} = 0.31 E / t$). The same letter means two things in one block. A subscript on the general row would remove this. It is not wrong (category 6).
- [Minor] fy2-s1 a) The block ends in $N = E/(kP_\text{n}t)$, but Substitution works out $E_1$ first and then $N$. This is a matter of form; the numbers are right.

## Checked
- Round 1, full packet. The change is the Formula steps of fy2-s1 a), b) and c). They now start from $P_\text{avg} = kP_\text{n}$ and $E_1 = P_\text{avg}t$; from the definition $e = m/E$ (with $E$ cancelling in the relative cut); and from $E = Pt$. Each step is algebraically right, its conditions are stated in Principle, and everything is within FY2 scope.
- Every number was recomputed with my own formulas: a) $14.016\,\text{GWh}$, $27.1 \to 28$. b) $3.116 \cdot 10^5$, $1.862 \cdot 10^5$ and $4.18 \cdot 10^3\,\text{t}$; $40.2\,\%$ and $98.7\,\%$. c) $58.1$ and $54.5\,\text{MW}$; $7$ and $73\,\text{MW}$. d) $9.636\,\text{GWh}$ and $7.1\,\text{MW}$. e) $252.3 + 87.6 + 40.1\,\text{GWh}$, $k = 0.114$, about $1/6$ of the fuel, $1.41 \cdot 10^4\,\text{t}$, $95\,\%$, $64.5$ and $15.5\,\text{MW}$, $55.5\,\text{MW}$. Alternatives: $473\,\text{GWh}$, $4.6 \cdot 10^3\,\text{t}$, $0.54$, $8.7 \cdot 10^4\,\text{t}$, $72\,\%$. All match answers.py and tasks.json.
- A script compared the numbers in en against fi: solutions.md and tasks.json hold identical sets of numbers.
- Physics wording in d), e), the common mistakes and s2 matches the Finnish version:
  - controllability is treated as a property, not a category;
  - no production method is called emission-free;
  - operational and life-cycle emissions are told apart;
  - $11\,\text{g/kWh} = 11\,\text{t/GWh}$;
  - IPCC AR5 medians and onshore wind's range $7\text{–}56$ are right.
- Rubric points add up to 18 and 14; nothing in the rubrics changed.
- The hash was the same at the start and at the end.
