VERDICT: PASS
CONTENT-HASH: b5ff0600214c4eda

## Blocking

## Polish
- solutions.md:224 (L2-08) — "Molemmissa unohtuu, että sekä ilmakilogramman liike-energia että sekunnissa virtaava ilman massa kasvavat" is only true of the $v$ option. The $v^2$ option forgets only the mass flow, as its own feedback correctly says. Fix: "Verrannollisuudessa $v$ unohtuvat molemmat, neliössä $v^2$ vain sekunnissa virtaavan ilman massan kasvu."
- exercises.json (L2-08, the 20 kW feedback) — "kerroin $v^3$ on 100 kertaa suurempi kuin $v$" compares quantities with different units. Write "lukuarvo $10^3$ on 100 kertaa $10$".

## Checked
- Scope: only the new task L2-08 (order of magnitude, type 5). The rest of the set was PASS before and is unchanged. Checked from the text only, no renders.
- Recomputed: $v$ = 10 m/s, $A$ = 7854 m², $P = \tfrac12\eta\rho Av^3$ = 1,963 MW → "2 MW". The distractors are 19,6 kW ($\propto v$), 196 kW ($\propto v^2$) and 91,6 MW (36 not converted, ×46,7). They are a factor 10 or more apart, and each feedback names the reasoning that gives it.
- Conditions: the task states "ei saavuta nimellistehoaan", so the formula with a constant η holds (brief: power curve and rated power). η = 40 % < 50 % as in the Tiivistelmä. 2 MW for a 100 m rotor at 10 m/s is realistic.
- Distractors: the 20 kW option catches the chapter's warned mistake ("kaksinkertainen tuuli antaa kaksinkertaisen tehon"). The correct option cannot be told apart by its form (all four are bare values).
- Notation ($P$, $\eta$, $\rho$, $A = \pi r^2$, $v$) is the same as in the lesson.
- solutions.md L2-08: the conversions are shown and the formula is stated before substitution. The reasonableness check is real (wind power 4,9 MW; scaling from the lesson's example (100/120)²·(10/9)³·(0,40/0,45)·2,32 MW ≈ 1,96 MW agrees). The aligned lines are split short; checked from text only.
- answers.py: no line is needed. All 19 numeric answers in the set were recomputed in one call and match.
