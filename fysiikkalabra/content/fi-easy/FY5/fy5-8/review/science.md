VERDICT: PASS
CONTENT-HASH: 08fbb7bd52ff00b7

## Blocking

## Polish
- inquiry.json `mittaus` solution, Järkevyys — "Pienin venymä 1,7 cm on lyhyt, joten sen mittausvirhe on suhteessa suurin": the error itself is unknown (guardrails, Measurement terms). Fix: "sen suhteellinen mittausepävarmuus on suurin".
- lesson.md Ydinajatus, last paragraph of "Jousen voima ja jousta venyttävä voima" — "Voimamittari näyttää…" brings in a force meter that the cart situation does not have. Fix: say "Jos kärryä pidetään voimamittarilla, se näyttää…", or drop the sentence.

## Checked
- Definitions: harmoninen voima, jousivakio, jousen potentiaalienergia and lepopituus/tasapainoasema match glossary.json. The text says that the rest-length point is the equilibrium position only for a horizontal spring, and it states the condition "ei liikaa" (Hooke's range) where the law is used.
- Newton III: F_v acts on the spring and F on the body, the same in lesson.md, the `pari` and `suunta` figures, the sim calc box, kertaus, virhe, check-3 and the exit ticket. The `virhe` figure's one error is exactly the one the task means (F₂ drawn on the block).
- Force diagrams: the worked example's fish (G and F equal, y up) and malli-laatikko (G=N, F=F_μ, v drawn apart and in blue, at the right points of action) agree with the motion. The equations come from the diagrams.
- Ep = ½kx² is derived as the triangle area under (x, F_v) with stretching done slowly. The pinta-ala figure shows that 2x gives 4E_p. The unit check is right. Zero energy is at the rest length.
- One script recomputed every number of the lesson and the inquiry with my own formulas, and all of them agree with lesson-answers.py: spring B ±2,5/5,0/10 N and 0,0625/0,250/1,00 J; k_C = 80 N/m; k = 40 N/m from the figure line; the example 392,4 N/m and 0,1766 J (2 s.f. from 3,0 cm, which is right); a through-origin least-squares fit of 29,95 N/m vs the read 30 N/m (7 % tolerance); siirto 3,354 m/s and its mistakes 4,743/0,1061/335,4; check-2 +10 N; check-3 0,15 m and N ≈ 59 N; exit 1,0 J.
- Figures: the kulmakerroin points (slopes 38,8–42,5 N/m) lie around a line of slope 40 through (0,025; 1,0) and (0,100; 4,0). The mittaus points are mg of the table's masses, and no line is drawn.
- Sim code: F = −kx, F_k = kx, F_v = kx and E_p = ½kx². The arrows point the right way at the right faces (pull vs push) at 6 px/N as the calc box says. The F_v range of ±16 N fits the ±17 N axis. The simState gives x, jousi, F, Fk, Fv, Ep. Its limits are stated in Mallin oletukset.
- Experiments: exp-1/exp-2 lock the spring and vary x, and exp-3 locks x = 0,10 m and varies the spring. The slider step of 0,01 m reaches every position asked for.
- Predictions and checks: each has exactly one correct option, and every distractor's feedback is right and quotes the model values.
- Siirto states its assumptions (no friction, massless plunger, level field, the ball leaves at the rest length). 12 km/h is a reasonable result.
