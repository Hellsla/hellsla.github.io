VERDICT: PASS
CONTENT-HASH: aa93c04b647589b2

## Blocking

## Polish
- inquiry.json (sim, koe-1) — the transformer, half of the slot (U₁:U₂ = N₁:N₂ = I₂:I₁), is never acted on: the sim only shows $N_2:N_1$ as a readout, and ennuste-dc is revealed by reading the theory — add a transformer control (N₁, N₂ → U₂, I₂) or an experiment, or at least a line in the sim howto that links the readout to the formula.
- lesson.md "Jännite lasketaan vaiheittain" — one dense paragraph that also brings in the switch-mode charger (beyond the slot, and it makes exercise L2-02 "ideaalinen muuntaja" look inconsistent) — shorten to the stepping-down chain and move the charger to one sentence ("yksinkertaistettuna laturia voi pitää ideaalisena muuntajana").
- lesson.md same section — "(luku *Sähköturvallisuus*)" refers to a chapter I could not verify in FY7's plan — confirm it exists or drop the reference.
- lesson.md "Yleinen virhekäsitys" — "johtimien ja maan tai johtimien keskinäinen jännite" is hard for a 17-year-old (three-phase detail) — write "siirtojännite on johtimen ja maan välinen jännite, ei johdon päiden välinen".
- inquiry.json koe-1 — the sim computes $I = P:U$ and $P_h = RI^2$, i.e. the formula the student predicts, so the experiment confirms arithmetic more than physics; acceptable here since losses are the topic, but the howto says it ("Malli laskee ...") only in the model box — fine to leave, noted.

## Checked
- Path: induction → core/turn ratio → DC fails → power conserved → I² loss → high voltage; opening question ("miksi ei generaattorin jännitteellä, miten jännitettä muutetaan") answered in both parts; slot goals only.
- Ennuste 2 is refutable (four options, each feedback cites model values 6,0 → 1,5 MW and repairs "U²:R" and "half" misconceptions); koe-1 locks P and l, varies U, min 3.
- Sim at 390 px readable: bars, readout ($I$, $R$, $N_2:N_1$ = 20, 0,75 %) match the model text; sim-spec numbers agree with feedback numbers.
- Example staged one step per stage, sanity check via power conservation; siirto has 3 hints and real mistake values (U²:R, R·I, MW vs kW).
- Etsi virhe and check-1/2 distractors are misconception-based; check-3 criteria observable and match the question.
- Exit ticket tests turn ratio and the square law; figures (transformer, grid, loss graph) described with data in aria-labels.
- Finnish and glossary terms (ensiö-, toisiokäämi, muuntosuhde, siirtohäviö) correct.
- Hash unchanged at end (aa93c04b647589b2).
