VERDICT: PASS
CONTENT-HASH: 4c5aa43d224fa957
## Blocking
## Polish
- inquiry.json kertaus title "Kertaa edelliseltä tunnilta", its feedback ("Tänään tutkitaan"), ennuste-1 feedbacks ("Edellisellä tunnilla", "edellisen tunnin tulokseen") — the prerequisite is the chapter *Termodynaaminen systeemi, tilanmuuttujat ja lämpötila*, not the preceding lesson. Use "Kertaa aiemmalta tunnilta" and "luvussa *Termodynaaminen systeemi, tilanmuuttujat ja lämpötila*" (as fy3-12 does).
- inquiry.json prior item 2 and kertaus feedback — chapter name lacks the italics the house form needs: "(luku *Termodynaaminen systeemi, tilanmuuttujat ja lämpötila*)".
- inquiry.json `suora` solution "Vastaus" — "lopuksi vähennys $20{,}0 - 296$ antaa tuloksen kokonaisina asteina" refers to a subtraction that is not in this solution (it computes $-p_0/k = -275{,}8$); replace with "tulos $-275{,}8\,{}^\circ\text{C}$ pyöristetään kolmeen numeroon, $-276\,{}^\circ\text{C}$".
- Investigation uses simulated data (honestly labelled), so the slot's "kokeellisesti" is met on paper only; if the teacher has a gas thermometer, a line in the lesson suggesting a real run would make the lesson an experiment.
- lesson.md Kaava — five formulas with two different meanings of $p_0$/$p_1$ in a row; a one-line pointer "tässä $p_0$ on paine lämpötilassa $0\,{}^\circ\text{C}$" before the last formula would help a first-time reader.
## Checked
- Round 2: re-check of round-1 Blocking items against the fix diff (none were open); fy3-13 inquiry.json: the pointe feedback on the mutka option now says 'satunnaisia mittausvirheitä, jotka mahtuvat mittausepävarmuuden rajoihin' (consistent with the guardrail; the option stays wrong, one correct option unchanged). No new wording problems.
- Opening question (how to find the lowest temperature from ordinary-range data) is answered by suora, epavarmuus and the Esimerkki; the slot's three goals (straighten data, extrapolate, estimate uncertainty) are all practised.
- Predictions precede the evidence; ennuste-2 (tens of degrees) is genuinely refutable by the epavarmuus table; each wrong option has repairing feedback.
- Recomputed: both bounding lines touch exactly the stated uncertainty bars (10 and 85 °C; 25 and 100 °C), θ0 −276,0, −258,7, −294,8, Δ 18,08; suora −276, siirto −277, tarkistus-2 −283, distractors −296/−307/−298, exit ticket 0,36.
- `aariviiva` feedback matches the figure description (s2 misses 10, 70, 85, 100 °C); one correct option per choice.
- Example has seven stages; the 0 °C reading is flagged as extrapolation.
- Uncertainty wording follows the guardrail (not an absolute bound); ± results consistent in lesson, conclusion, checks and exit ticket.
- Figures judged from alt texts and source; no captures were provided.
