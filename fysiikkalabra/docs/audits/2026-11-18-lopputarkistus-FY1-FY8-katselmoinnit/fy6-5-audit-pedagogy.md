VERDICT: PASS
CONTENT-HASH: 2dde1d7403e54d9e

## Blocking
(none)

## Polish
1. inquiry.json tarkistus-1 (Minor) — the only graded concept check is the series-current misconception; no check tests the lesson's new core (current law at a junction, loop law, branch voltage). The explain check (tarkistus-3) that does is optional. Fix: make a branching-circuit item (e.g. "branch current from I1 and the other branch") the graded concept check, or make tarkistus-3 core.
2. lesson.md "Kierros silmukassa" (Minor) — "Kuvan piirissä on kaksi silmukkaa" refers to the circuit figure placed one section earlier, after the potential paragraph, so it is not right after the paragraph it explains. Fix: repeat the figure here or write "kuvan 2 piirissä".
3. lesson.md "Esimerkki", stage "Kaava ratkaistuna" (Minor) — V_B = U − R_1 I_1 is not simplified symbolically before substitution, and the loop law is only used in the check, not named in "Periaate". Fix: name Kirchhoff's voltage law as the step that gives V_B.
4. inquiry.json koe-1/koe-2 (Minor) — the sim only evaluates the formulas the prediction is about; the model note says so, but koe-3 (optional) is the only one where the student could see a surprise (zero shift). Fix: consider letting the student set R_3 so that the branch current ordering flips, or a short "what if R_1 = 0" question.
5. inquiry.json workload (Minor) — 2 predictions, 3 experiments, explain, error-finding, transfer, exercises, 3 checks and exit ticket is near the upper limit of one lesson; optional markers keep the core path within it.

## Checked
- Opening question (bird) is answered in "Lintu johdolla" and the transfer task; no answer is disclosed before commitment (hook and predictions pose it neutrally).
- Both predictions can be refuted by their experiments (koe-1 varies R3 with U, R1, R2 locked; koe-2 varies only the probe).
- Option feedback names the misconception (consumed current, whole source voltage on a branch, "voltage only in the source").
- Sim at 390 px: picture, graph, sliders and readout legible; text is behind Käyttöohje / Mallin oletukset / Laskennan selitys; colour is paired with labels.
- Worked example has seven stages, one step each; "Järkevyys" checks both laws.
- Etsi virhe distractors are real errors; transfer task has three progressive hints and mistakes with value-specific feedback.
- Exit ticket tests the current law and the voltage law directly.
- Finnish reads correctly; glossary terms, "lämmöksi" only in a wrong option, "sisäenergiakseen" is correct.
- Prerequisites (parallel same voltage, U = RI) are used and cited by chapter name.

## Scores
- 2 Learning design: 4 — predictions, sim, explain and transfer fit the goals; check coverage of the core is thin.
- 3 Lesson form: 4 — staged example, figures with sources, no wall of text; one figure reference is distant.
- 4 Exercises/exit ticket/checks: 4 — good error-spotting and transfer; one graded concept check misses the new content.
- 5 Finnish: 5 — no faults found.
- 6 Phone usability: 5 — nothing clipped in the 390 px sim capture; readout clear.
Findings: all Minor; no Critical or Major.
