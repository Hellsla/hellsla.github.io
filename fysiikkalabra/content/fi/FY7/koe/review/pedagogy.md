VERDICT: PASS
CONTENT-HASH: d63f5c2e6544c73f

## Blocking
None. The exam fits the brief: 10 concept-based Osa 1 items with misconception distractors, four Osa 2 tasks covering graph and uncertainty (k2, k5), explanation and the main model, and two Osa 3 tasks of different kind (k6 societal, k7 data-driven). No part names its model. Rubrics sum to the points. The workload fits 120 min.

## Polish
Kaava step (queue 8g). The basic law comes first and the derived formula follows everywhere, but "simplify symbolically to the end, then substitute" is not done in four places:
- k4-c: `I_1 = I_2 U_2 / U_1` with `I_2 = P/U_2` should reduce to `I_1 = P/U_1` before substitution.
- k6-a: `I = P/U` and `P_h = RI^2` should combine into `P_h = R(P/U)^2`. The asked share `P_h/P` is not in the Kaava block either.
- k6-c: `S = (E_A - E_B)p` is substituted in pieces.
- k3-c: `P = Fv` is not reduced to `e^2/R` or to `P = I^2R`.

"Every chain shows what it computes": the k6-c Muunnokset rows begin with a bare numeric expression (`&1,728 MW · 4000 h`). In k7-c the first sentence is `(2,898 - 2,76)/2,898 = 0,048`, a bare fraction. Start each with `E_A =` or `\delta =`.

Task design:
- k6-a to k6-c are routine `P = UI`, `RI^2` and chained arithmetic. They repeat item k1-g (100-fold loss) and k4-d. The choice and evaluation sit only in k6-d. Making the choice harder would raise the transfer demand, for example a cable resistance that depends on cross-section, or a second route.
- The k6 statement says the calculation assumes constant resistance and a DC-like transmission. That names part of what k6-d asks the student to find. Leave the assumptions out of the statement.
- k7-a is the hardest step (choosing `1/T`) and comes first, and k7-b depends on it. Osa 3 should open accessibly. Swap the order, or give the data pairs in b so a student who fails a can still continue.
- k3 has no figure of the rails and the field. A simple figure would help and would not give an answer away. The question "ylöspäin vai alaspäin" depends on the orientation.
- k5-b solution: it says the results "sopivat yhteen" within 0,8 %, but later notes that the k=2 and k=3 spread (0,026 µm) exceeds the summed reading uncertainties (0,018 µm). Align the rubric's conclusion with this.
- k1-e: the wrong option "kuparin tiheys, joten ilma vastustaa enemmän" is a contrived distractor and not a real student error. Replace it with, for example, "kupari on paramagneettista" (not in FY7 scope, so use a different one) or "magneetti kuumenee ja menettää magneettisuutensa".
- k1-c solution: "Johtimen toisen johtimen kohdalla aiheuttama kenttä" is awkward.

## Checked
tasks.json: structure, sections, selection rules, criteria against the framework, whether the text discloses the method. solutions.md: every Kaava block (order and derivation), the sequence of steps, common mistakes (real ones), "Hyväksytään myös" and the k1 distractor feedback. Figures were not opened (the packet omits them); the page layout and the coverage doc are not in this packet.
