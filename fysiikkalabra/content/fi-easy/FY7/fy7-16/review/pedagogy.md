VERDICT: PASS
CONTENT-HASH: 5d90832ff9c66085
## Blocking
(none)
## Polish
- lesson.md:134-138 (Pysähdy, laturi) — the answer repeats the paragraph just above and stops at "vuo pienenee, joten jännite pienenee". Optionally add the causal step the question sets up (current and frequency stay the same, so only $\Phi_0$ changes: $e_0 = N \cdot 2\pi f \cdot \Phi_0$). Not blocking: the answer is correct and answerable from the text.
- lesson.md:160-164 (Pysähdy, liesi) — fine as is; optionally name that the field does pass through the glass, so the student separates "field reaches it" from "current can flow".
## Checked
- Round 2's blocking item is fixed: the vaimennus answer now shows $\lg (P_0 : P) = A : 10\,\text{dB} = 0{,}90$, then $P_0 : P = 10^{0{,}90} \approx 7{,}9$, then about $13\,\%$. A student who has only read the preceding formula section can follow it.
- Pysähdy 3 recomputed: $0{,}18 \cdot 50 = 9{,}0\,\text{dB}$, $10^{-0{,}90} = 0{,}126$, about $13\,\%$; significant figures fine; does not repeat the worked example (80 km, 0,20 dB/km).
- Pysähdy 1 and 2: physics matches the lesson text; each is answerable from the paragraph just read; one per idea, one to two sentences each, no field, lock or storage.
- The blocks sit in Teoria, after the predictions are committed (Ennuste 3 and 4 reveal only after teoria-osa), so they give nothing away early.
- Finnish: case after number+unit right ($3\,\text{mm}$:n, $50\,\text{km}$), glossary terms (pyörrevirta, vaimennus, vuo) used, S2 reading level fine.
- Old content that could stop the blocks working: none found.

## Vanhan sisällön löydökset
(Not Blocking, not fixed in this PR.)
- "Miksi etäisyys ratkaisee": "Siksi laturin ja puhelimen väli on vain muutamia millimetrejä." follows a figure description, so "Siksi" has no cause to refer to.
- "Induktioliesi": "Pohjaan ei kuitenkaan synny yhtä tavallisen käämin kierrosta." is awkward for an S2 reader; e.g. "Pohjaan ei synny yhtä silmukkaa kuten käämiin, vaan virtoja kiertää monta reittiä."
- inquiry.json koe-1 and koe-2: `measure` label "e_0 (V)" and `names` "lähetinkäämin säde R_1" are plain text, not LaTeX.
- The packet says check_lesson.py had not been run, so the deterministic checks are unconfirmed.
