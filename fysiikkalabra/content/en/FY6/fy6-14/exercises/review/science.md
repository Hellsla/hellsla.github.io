VERDICT: PASS
CONTENT-HASH: 375cd36a93d31bad
SCOPE: delta md-paragraphs,numbers,paragraphs,reflow,typography,wording from 38b2c5ddb83972d4 base 98218de

## Blocking

## Polish
- solutions.md:124 (fy6-14-L1-05) — the Formula row is labelled with the Finnish word `\text{osuus}` in the English set. — Write `\text{share}` (language only, not physics).
- solutions.md (fy6-14-L1-06) — "(at most about $1\,\text{V}$)" holds for a silicon diode, not for an LED (carried over from the earlier report).

## Checked
- Every new Formula step starts from the basic relations the lesson teaches. These are Kirchhoff's voltage law $U = U_R + U_\text{D}$ (or $+\,2U_\text{D}$, $+\,3U_\text{D}$) with Ohm's law $U_R = RI$, the efficiency $\eta = \tfrac{P_\text{useful}}{P_\text{in}}$ with $P_\text{in} = GA$, $P = UI$, $\eta = \tfrac{E}{HA}$ and the load line. Each solves for the asked quantity in symbols before substitution. The notation ($U_\text{D}$, $U_R$, $G$, $H$, $E_\text{kul}$) is the same as in the glossary and the tasks.
- L1-04 (reverse direction): with $I = 0$, $U_\text{D} = U - RI = U$ is correct.
- L3-05: the load line $I = \tfrac{U - U_\text{D}}{R}$ against the table curve $I_\text{LED} = f(U_\text{D})$ is the right model for the operating point.
- One script recomputed every number in the diff: 95 Ω, 8.3 mA, 250 Ω, 20.3 %, 36 %, 49.3 W and 5.86 Ω, 25 %, 16.7 %, 207 Ω, 387 Ω, 4683 kWh and 87.7 %, and 13.8 mA. All agree, and no number changed.
- In exercises.json only the presentation changed. The paragraph splits in solutions.md keep the numbers, signs and units in the same order.
- The scope is unchanged: components only, no p–n microphysics.
- The hash was read at the start and at the end and did not change.
