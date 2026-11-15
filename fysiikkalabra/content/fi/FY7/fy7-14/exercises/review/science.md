VERDICT: FAIL
CONTENT-HASH: 5ddb545be9a5be70

## Blocking
- exercises/solutions.md:210 (fy7-14-L3-04 c) — A: "Kalvo on siis tummempi kuin yksikään väri paksummassa kohdassa." is false. At $d = 450\,\text{nm}$ the cancelled wavelengths ($661{,}5\,\text{nm}$ and $441\,\text{nm}$, the ones named in part a) reflect about $2{,}0\,\%$, the same as the thin film. The two-beam model gives $(0{,}19 - 0{,}05)^2$ for both, and the full Airy formula gives $2{,}006\,\%$ for both. The thin part is darker than the thick part's strongest colour and darker on average over the spectrum, not darker than every wavelength there. — Fix: change it to "Kalvo on siis tummempi kuin paksumpi, värikäs kohta, jossa vihreä heijastuu lähes kolminkertaisesti." or delete the sentence.

## Polish
- solutions.md:210 (L3-04 c) — $5{,}8\,\%$ is the two-beam estimate $(0{,}19 + 0{,}05)^2$. With the multiple reflections in the denominator it is $5{,}67\,\%$. The estimate is consistent with the amplitudes the text quotes, so it is a fair simplification (C). "noin $5{,}7\,\%$" or "noin $6\,\%$" would hold under both models.
- solutions.md L1-04 and L2-01 — The reasonableness checks cite the simulation's $103\,\text{nm}$ and the chapter's $200\,\text{nm}$ film. Both numbers are correct ($550 : (4 \cdot 1{,}33) = 103{,}4$ and $2 \cdot 1{,}33 \cdot 200 = 532$), but the exercise brief does not contain them. Check that the lesson still has them.

## Checked
- I recomputed all 18 numeric answers in one script with my own formulas: every one matches answers.py and exercises.json, and every unit and tolerance fits the significant figures of the data. For L2-05 and L3-05 I used least squares (slope $5{,}26$, giving $n = 1{,}315$; $\Delta x = 1{,}896\,\text{mm}$, giving $D = 12{,}42\,\mu\text{m}$). The answers in the solutions ($1{,}3$ and $12\,\mu\text{m}$) are inside the tolerances of $4\,\%$.
- Focus item, L2-08: the cause of the residual reflection is correct. $|r_1| = 0{,}160$ and $|r_2| = 0{,}048$ are unequal because $1{,}38 > \sqrt{1{,}52} = 1{,}23$. In the coating-curve figure the minimum is $1{,}26\,\%$ at $497\,\text{nm}$ and bare glass is $4{,}26\,\%$, so $70{,}4\,\%$ is removed. Reading $1{,}3$ and $4{,}3$ gives $69{,}8\,\%$, inside the tolerance of $3\,\%$.
- L2-07: the table matches the Airy reflectance of a $97{,}83\,\text{nm}$ MgF₂ layer on glass to every digit.
- L3-06 soap-curve ($d = 350\,\text{nm}$): minimum at $465{,}5\,\text{nm}$, maximum at $620{,}7\,\text{nm}$ with $R_\text{max} = 7{,}7\,\%$, which agrees with the solution. The figure does not give the thickness away.
- Phase-shift counting is right in every task: soap film, oil on water ($1{,}00 < 1{,}47 > 1{,}33$), MgF₂ (two shifts), TiO₂ on glass (one shift), and the air wedge, where the lower surface inverts and the contact line is dark.
- L3-03: only the orders $k = 2$ and $k = 3$ are visible ($1050\,\text{nm}$ and $350\,\text{nm}$ are outside the visible range). L3-04: $529{,}2\,\text{nm}$ is the only visible maximum, and the first destructive thickness is $360\,\text{nm}$.
- L1-05: $n_\text{p} = \sqrt{n_\text{s}}$ is the equal-amplitude condition at normal incidence. The ratio form in the solution is equivalent.
- L1-06 and L1-09: exactly one option is correct in each, and every distractor's feedback is physically right ($\lambda/(4n)$ is the first bright ring).
- L3-02: $0{,}987^8 = 90{,}06\,\%$. Uncoated, $(1 - 0{,}04258)^8 = 70{,}6\,\%$.
- Scope: every task stays inside the FY7 contents on light interference and inside what the brief teaches, with normal incidence throughout. Every solution solves symbolically before substituting.
