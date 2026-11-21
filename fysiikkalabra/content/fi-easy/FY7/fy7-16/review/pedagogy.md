VERDICT: FAIL
CONTENT-HASH: 4a4e565124fa326c
## Blocking
- lesson.md:322-324 (Pysähdy, vaimennus) — the answer jumps from "Tehosuhde on" straight to $P/P_0 = 10^{-0{,}90}$. The inverse of the definition ($\lg(P_0:P) = A:10\,\text{dB}$, so $P:P_0 = 10^{-A:(10\,\text{dB})}$) is first shown in the later Esimerkki, so a student who cannot yet solve it cannot follow the step, and the block is placed before the example. Fix: add the step, e.g. "Määritelmästä $\lg (P_0 : P) = A : 10\,\text{dB} = 0{,}90$, joten $P_0 : P = 10^{0{,}90} \approx 7{,}9$ ja $P : P_0 \approx 0{,}13$ eli noin $13\,\%$."
## Polish
- lesson.md:144-148 (Pysähdy, laturi) — it repeats the scenario of Ennuste 1 (3 mm to 20 mm) and the paragraph just above, and its answer stops at "vuo pienenee, joten jännite pienenee". Add the causal step the text stresses: the current and frequency stay the same, so a smaller flux amplitude means a slower change of flux, and the voltage depends on the rate of change ($e_0 = N \cdot 2\pi f \cdot \Phi_0$). Or ask for the reason the lines turn back.
- lesson.md:231-235 (Pysähdy, liesi) — the question opens with "ei ole kuuma ennen kuin kattila on kuumentunut"; the answer is fine. Consider also naming that the field does pass through the glass, so the student separates "field reaches it" from "current can flow".
## Checked
- Round 1's blocking item (korkeudelta/korkeudelle) is fixed in the laturi block.
- Pysähdy 1: physics right, wording and case after number+unit right, S2 reading level fine.
- Pysähdy 2: physics matches the lesson text (glass does not conduct, warms only from the pot); no clash with Ennuste 3, which was committed before.
- Pysähdy 3: $A = aL = 9{,}0\,\text{dB}$ and $10^{-0{,}90} = 0{,}126 \approx 13\,\%$ recomputed; significant figures fine.
- The blocks sit in Teoria, after the student's predictions are committed, so they give nothing away early; one per idea, none repeats the worked example (80 km, 0,20 dB/km).
- Old content not judged for Blocking (see Vanhan sisällön löydökset).

## Vanhan sisällön löydökset
(Not Blocking, not fixed in this PR.)
- lesson.md, "Miksi etäisyys ratkaisee": "Siksi laturin ja puhelimen väli on vain muutamia millimetrejä." follows a figure description, not the cause; "Siksi" has nothing to refer to.
- "Induktioliesi": "Pohjaan ei kuitenkaan synny yhtä tavallisen käämin kierrosta." is awkward Finnish for an S2 reader; rewrite, e.g. "Pohjaan ei synny yhtä silmukkaa kuten käämiin, vaan virtoja kiertää monta reittiä."
- inquiry.json koe-1 and koe-2 `measure` label "e_0 (V)" and `names` "lähetinkäämin säde R_1" are plain text, not LaTeX (house rule: symbols and units in LaTeX).
- check_lesson.py had not been run according to the packet; the deterministic checks are therefore unconfirmed.
