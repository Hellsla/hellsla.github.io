VERDICT: PASS
CONTENT-HASH: ec5a3cef43ec5a85

## Blocking

## Polish
- lesson.md:188 — "Kysytään sitä mekaanista energiaa $E_\text{lämpö}$, jonka kitka muuttaa" gives the converted mechanical energy the thermal-energy symbol. Prefer "Kysytään lämpöenergiaa $E_\text{lämpö}$, joksi kitka muuttaa osan mekaanisesta energiasta".
- inquiry.json:244 data — "Pallo ja lattia muodostavat eristetyn systeemin". The air also warms (and the lesson's check-3 model counts it), so "pallo, lattia ja ilma" would match check-3 and exercise L3-02.
- inquiry.json simulaatio.model — the friction force is a constant μmg along the track, not μN. The model box says "jokaisella liukumetrillä yhtä paljon", which is a fair simplification (C). Optional addition: "todellinen kitka riippuu myös siitä, kuinka lujasti lauta painaa rampin pintaa".
- lesson.md Seitsemän energialajia — the lesson defines lämpöenergia through motion and interactions (FY3-compatible), while the glossary says "satunnaiseen liikkeeseen". The two are not contradictory, but one wording everywhere would follow the guardrail rule.

## Checked
- I ran lesson-answers.py, which ports the sim's model independently of sim.js. Frictionless h₀ = 2,0 m: 981 J total; (E_p, E_k) = (63, 918), (862, 119), (424, 557) J at 1, 2 and 3 s. μ = 0,04: mechanical energy 981 → 469 → 143 J and thermal energy 0 → 512 → 838 J at 0, 8 and 16 s. These match the johtopäätös model answer and the exp-2 feedback.
- Plausibility of the sim numbers: the small-amplitude quarter period of the parabola (ω = √(gA) = 1,71 s⁻¹) is about 0,9 s, so "lähellä pohjaa" at 1,0 s is right. The 838 J of thermal energy corresponds to about 43 m slid at 19,6 J/m.
- sim.js implements the same equation of motion (a bead on a parabola, tangential friction μmg, RK4 with a 2 ms step, friction work as the thermal energy). Its three energies are computed independently; the adapter params and simState keys Ep, Ek, Eth and Ekok exist.
- Worked example: 840 − 720 = 120 J, symbolic first, rounding to tens of joules justified, 14 % share plausible. Other numbers: data 0,29 J (mistakes 0,31/0,60/0,12; about 20 % lost per bounce); siirto 335 kJ (mistakes 505/85/420; about 20 % muscle efficiency); check-2 2380 J → 2,4·10³ J inside the tolerance (about 5 % visible light for a bulb); exit 3,8 kJ.
- Figure "sailyminen": bars at 0,16 px/J (800/300+450+50/700+100 J). The skater's middle position is 3/8 of the start height on the drawn parabola, which matches E_p = 300 J.
- Each choice item has exactly one correct option, and each distractor's feedback names the physics. Brakes, nuclear and the half-pipe items are consistent with the theory.
- Heat versus thermal energy and net transfer follow the guardrail wording. Friction "ei luo energiaa" appears consistently in the theory, misconception, summary and exit ticket.
- Scope: no expressions for E_k or E_p (FY4), and no Q = cmΔT or first law (FY3).
- Hash identical at start and end.
