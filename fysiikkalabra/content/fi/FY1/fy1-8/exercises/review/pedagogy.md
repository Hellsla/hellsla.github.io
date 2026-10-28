VERDICT: PASS
CONTENT-HASH: f4fca3b182c3189f

Round 2 and 3: re-check of round-1 Blocking items against the fix diffs.

## Blocking
- none. L3-02 Sijoitus now reads $\dfrac{80{,}0\,{}^\circ\text{C} - 68{,}0\,{}^\circ\text{C}}{5{,}0\,\text{min}} = \dfrac{12{,}0\,\text{K}}{5{,}0\,\text{min}} = 2{,}4\,\text{K/min}$ (and the same for $r_2 = 1{,}0\,\text{K/min}$): temperatures in °C, the difference in K, correct and consistent with the Muunnokset line.

## Polish
- exercises.json fy1-8-L2-03 — "90 cm" and "342 cm" are still plain text beside LaTeX times; write `$90\,\text{cm}$` and `$342\,\text{cm}$`.
- solutions.md fy1-8-L3-02 Kaava — $\Delta t$ and $\Delta r$ stand for an interval and a rate difference where elsewhere $\Delta$ is an uncertainty; use "viiden minuutin aikana" and "laskunopeuksien erotus".
- solutions.md L2-01 and L3-01 — the added sentence "Vastauskenttä hyväksyy kummankin" is interface talk inside a solution; say "kumpikin pyöristys kelpaa" or drop it.
- solutions.md L1-01 Vastaus — "$5\,\%$ (laskimen arvo $5{,}0\,\%$)" is the same number twice.

## Checked
- Tolerances now 0.21 (L2-01, answer 2.5, accepts 2,0–3,0 so the reported 3 % passes) and 0.1 (L3-01, answer 0.033, accepts 0,030–0,0363 so 0,03 passes); consistent with the relative-tolerance rule and with the solutions' rounded reports.
- Rest of the set unchanged; earlier checks (L2-02, L1-03 Järkevyys, L3-01 argument) still hold.
- Round 3: L2-01 tolerance 0.21 on answer 2.5 accepts 1,975–3,025, so both 2,5 and the reported 3 pass.
- Hash unchanged at the end.
