VERDICT: PASS
CONTENT-HASH: 4b435403c5d88a78
SCOPE: delta md-paragraphs,numbers,reflow,teacher-figure,typography,wording from a1cac1a76ad996ac base 5b3ca4f

## Blocking

## Polish
- solutions.md (fy2-7-L2-10 c)) — "nettovienti oli $2142\,\text{MW}$" reads as if it were derived from $12\,791 - 10\,647 = 2144\,\text{MW}$. — Fix: "Fingridin mukaan nettovienti oli $2142\,\text{MW}$".

## Checked
- L3-01, the round-2 fix: the English subscripts $E_\text{sent,…}$ are gone from both the fi-easy and the Finnish solutions.md. The Sijoitus now substitutes into the Kaava's final form: $\Delta E = E_\text{perille}(1/\eta_1 - 1/\eta_2) = 600(1/0{,}910 - 1/0{,}940) = 21{,}0\,\text{MWh}$, a single aligned chain that starts from the quantity.
- Every rewritten Kaava line starts from a basic relation: conservation $E_\text{lähtö} = E_\text{perille} + E_\text{häviö}$ (or the same with powers), $\eta = E_\text{perille}/E_\text{lähtö}$, $p = E_\text{häviö}/E_\text{lähtö}$, or $P = E/t$. Each solves symbolically and substitutes into the final form.
- Recomputed in one script: 150 MWh, 10,96 MW, 1200 kWh, 21,0 MWh, 13,0 MWh, 65,7 houses, 4,8 %, 6,593 MWh, 12,5 MWh and 72 MJ. All agree with the solutions.
- Heat-plant improvement: $\Delta E_\text{laitos} = rP_\text{häviö}t/\eta$ is right. The house's saving is energy that arrives, and the loss is taken from the energy sent.
- `fy2-7/sankey`, the figure the teacher approved: it shows only 96/4 % and 91/9 %, drawn to scale, and the alt text agrees.
- The paragraph splits (L3-02, L3-03, L3-04, L3-05) change no claim or number.
- answers.py matches all 21 numeric answers within tolerance. No answer changed.
- Hash 4b435403c5d88a78 at the start and at the end.
