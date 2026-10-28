VERDICT: PASS
CONTENT-HASH: b726ca376903e1f8

Delta review over the audit's PASS (52aa6a2eb19695e1): new choice check-c2 (heat pump 1,0 kWh electricity, 3,0 kWh delivered) from the exit ticket, checks renumbered, exit text "kaksi", lesson-answers.py added.

## Blocking
- none
## Polish
- inquiry.json:429 — "Sähkövastus muuttaisi 1,0 kWh sähköä täsmälleen 1,0 kWh lämmöksi": the guardrail and exercise L3-02 say the resistor turns the electrical energy into internal energy that passes on as heat, efficiency "käytännössä 100 %". Suggest "…muuttaa käytännössä kaiken sähköenergian sisäenergiaksi, joka siirtyy lämpönä huoneeseen".
- inquiry.json:433 — "Kitka ja häviöt muuttavat osan sähköstä lämmöksi": same wording point (sisäenergiaksi).
## Checked
- Q_ulko = 3,0 − 1,0 = 2,0 kWh; ε = 3,0 (symbol ε as in the lesson); energy balance Q_sisälle = Q_ulko + E_s right.
- Distractor "luo energiaa" wrong; feedback right (energy conserved, taken from outdoor air).
- Distractor "kolminkertainen hyötysuhde" wrong; feedback follows the guardrail (η ≤ 100 %, COP is not an efficiency).
- Distractor "kitka" wrong; losses are part of the 1,0 kWh, cannot give 2 kWh more; right.
- Exactly one correct option; lesson-answers.py reproduces 2,0 and 3,0.
- Removed exit question is the one converted; two remain; "kaksi" matches.
