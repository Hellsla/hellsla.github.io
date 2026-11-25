VERDICT: FAIL
CONTENT-HASH: ec997ed6c12a6814

Delta review of the new `hints` in `sovella/tasks.json` (work queue 11c), against each part's rubric, answer and `sovella/solutions.md`.

## Blocking

1. **s3 a, hint 2 (fi), A.** "…ja katso, mihin se osuu pystyakselilla." The fitted line meets the vertical axis at $\Delta m \approx -9\,\text{g}$, below the zero-based scale the same hint asks for. So in the student's graph it never meets the vertical axis. The rubric (criterion 4) and the solution point at the horizontal-axis intercept ($P_\text{h} \approx 70\,\text{W}$) and say the line must not be forced through the origin. The hint sends the student to the wrong axis. Replacement: "…Sovita pisteisiin suora, joka kulkee pisteiden lomitse, ja katso, kulkeeko se origon kautta."
2. **s6 d, hint 2 (fi), B.** "Kumpi kohde pystyy luovuttamaan sisäenergiansa ilmaan?" This presupposes that only one of them can. Brake discs do pass energy to the air: part c of the same task finds that about $40\,\%$ of it does. The rubric's point is that the engine's cooling system can carry a large power to the air for a long time. Replacement: "Kumpi kohde pystyy luovuttamaan sisäenergiansa ilmaan suurella teholla koko pitkän mäen ajan ylikuumenematta?"

## Polish

3. **s3 b, hints 1–2 (fi).** "Kuumennin tuottaa energiaa, jonka vesi ottaa höyrystyessään" and "kuumennin antaa energiaa $P\,t$. Kirjoita energian säilyminen" lead to $Pt = r\,\Delta m$, which is the very one-point model that part d criticises. The slope still comes out as $t/r$, but the hint should use the solution's balance. Suggest for hint 2: "Höyrystymiseen tarvittava energia on $Q = r\,\Delta m$. Kuumentimen energiasta $P\,t$ osa $P_\text{h}\,t$ johtuu huoneeseen: $(P - P_\text{h})\,t = r\,\Delta m$. Päättele, mitä suoran kulmakerroin kertoo."

## Checked

I recomputed every number a hint states or implies, using my own formulas:
- s1: $m = 54\,000\,\text{kg}$, $Q = 21{,}9\,\text{GJ}$, $t = 17{,}4\,\text{h}$; phase shares $16/82/2\,\%$ and times $2{,}7$ and $14{,}3\,\text{h}$.
- s2: $86\,400\,\text{s}$, $\Delta T = 31\,\text{K}$, $4650\,\text{W}$, $35{,}8\,\%$.
- s3: least-squares slope $0{,}1326\,\text{g/W}$, $r = 2{,}26\,\text{MJ/kg}$, intercept $69\,\text{W}$; the d percentage is $12{,}6\,\%$.
- s5: $370{,}8$ and $333{,}0\,\text{kJ/kg}$; hint b3's "energy the group counted for melting" is $Q_\text{v} - c_\text{v} m_\text{j} T$, which is correct.
- s6: $31{,}5\,\text{K}$, $133{,}7\,\text{K}$, $40{,}2\,\%$, with the $0{,}85$ share applied correctly in c.
- s7: $0{,}222\,\text{K/s}$, $900$, $360\,\text{s}$, $0{,}4\,\%$.
- s8: $2083$, $333$, $270\,\text{kJ}$, $0{,}30\,\text{kg}$.

Every conversion stated in a hint is right. Symbols match the solutions ($c_\text{v}$, $c_\text{j}$, $m_\text{p}$, $m_\text{k}$, $m_\text{l}$, $P_\text{h}$, $Q_\text{jarrut}$), and so do the sign conventions. No hint states a part's final answer. Numbers with units are LaTeX with a decimal comma. The physics of s4 (density maximum, latent heat conducted through the ice, snow as an insulator) and of s7 d (loss power growing with the temperature difference) matches the rubrics.
