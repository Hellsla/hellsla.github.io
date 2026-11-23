VERDICT: PASS
CONTENT-HASH: 83530c0cd8777982

## Blocking

## Polish
- [Minor] fy2-s1 c) Kaava: the first rows use $E = Pt$ and $P = E/t$ as the general law, and the last row uses $E$ for the city's annual consumption ($P_\text{k} = 0{,}31 E / t$), as in Annettu. The same letter means two things in one block. It is not wrong (category 6, no wrong picture), but $E_\text{talvi}$ / $P_\text{keski}$-style subscripts or "$P = \Delta E / \Delta t$" for the general row would remove the ambiguity.
- [Minor] fy2-s1 a) The Kaava block ends in $N = E/(kP_\text{n}t)$, but Sijoitus works out $E_1$ first and then $N$. The numbers are right, but this does not quite follow the "substitute into the last symbolic form" rule. It is a matter of form, not physics.

## Checked
- Round 1, judged in full. The change is the Kaava steps of fy2-s1 a), b) and c) (git diff ce7c397be2..eda9e57628). Each now starts from its basic relation: a) $P_\text{keski} = kP_\text{n}$, $E_1 = P_\text{keski}t$, $E = NE_1$; b) definition $e = m/E$, then $m = eE$, then the relative cut with $E$ cancelling; c) $E = Pt$, then the winter shares. Every derivation step is algebraically right, the conditions are stated in Periaate (average power, the same energy in every option), and no formula is outside FY2 scope ($P = E/t$, emission factor, no FY3 content).
- I recomputed every number in one script with my own formulas: $E_1 = 14{,}016\,\text{GWh}$, $N = 27{,}1 \to 28$ ($27$ turbines give $378\,\text{GWh}$), and the nominal-power mistake gives $43{,}8\,\text{GWh}$, which leads to $9$ turbines. b) $3{,}116 \cdot 10^5$, $1{,}862 \cdot 10^5$ and $4{,}18 \cdot 10^3\,\text{t}$; cuts $40{,}2\,\%$ and $98{,}7\,\%$. c) $392{,}4\,\text{GWh}$, $58{,}1$ and $54{,}5\,\text{MW}$, calm $7\,\text{MW}$, gap $73\,\text{MW}$, year averages $44{,}8$ and $43{,}4\,\text{MW}$. d) $9{,}636\,\text{GWh}$, $385\,\text{GWh}$, $15{,}4\,\text{GWh}$, $7{,}1\,\text{MW}$. e) $252{,}3$, $87{,}6$ and $40{,}1\,\text{GWh}$; $k = 0{,}114$; fuel $0{,}16 \approx 1/6$; share $10{,}6\,\%$; $2775 + 2102 + 9226 = 14\,103\,\text{t}$; cut $95{,}5\,\%$; peak $64{,}5$, so $15{,}5\,\text{MW}$ is bought; without biomass $55{,}5\,\text{MW}$. Alternatives: $473\,\text{GWh}$, $4{,}56 \cdot 10^3\,\text{t}$, $k = 0{,}54$, $8{,}74 \cdot 10^4\,\text{t}$, $72\,\%$. All agree with answers.py and tasks.json.
- Emission factors match IPCC AR5 WGIII Annex III medians, and onshore wind's range $7\text{–}56\,\text{g/kWh}$ is right. The s2 unit conversion $11\,\text{g/kWh} = 11\,\text{t/GWh}$ is right.
- Rubrics, points (3+3+4+3+5 = 18 and 3+3+4+4 = 14), significant-figure reasons and Hyväksytään myös are unchanged and still match the solutions.
- The hash was the same at the start and at the end.
