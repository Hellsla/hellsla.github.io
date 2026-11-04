VERDICT: PASS
CONTENT-HASH: d66b07866727f253

Full review of the 8 new tasks (L1-06..08, L2-05..07, L3-04..05) and set coherence; old tasks unchanged.

## Blocking
(none)

## Polish
- solutions.md:144 (L2-05) — "Lisää toistoja ja tarkempi ajanotto voisivat näyttää sen" suggests that a mass effect exists to be found; for two balls of the same shape rolling without slipping, the rolling time does not depend on mass — "voisivat näyttää, onko eroa".
- exercises.json:46 (L1-06) and L2-05/L3-05 — "riippumaton/riippuva muuttuja": the lesson brief and glossary use "muutettava / mitattava / vakioitavat" — add the lesson's word once, e.g. "riippumaton (muutettava) muuttuja".
- exercises.json:106 (L1-08) — "luettelee, mitä kukin lause kuuluu kertoa" is not grammatical — "Työselostuksen kirjoittaja miettii, mihin osioon kukin lause kuuluu."
- exercises.json:347 (L3-05) — one rate, 2,0 K/min, is assumed for all three materials, although the slowest-cooling container (plastic) gives the smallest drop and so sets the needed time — say "hitaimmin jäähtyvässäkin astiassa alun nopeus on noin 2,0 K/min".
- exercises.json:314 (L3-04) — a multiple-choice item at level 3, where the plan asks for "paranna perustellen" — consider an open model answer (pedagogy's call).

## Checked
- One python script recomputed every new answer: L2-05 means 3,12 s and 3,08 s, half-ranges 0,04 s each, ratio 100 %; L2-07 (2,40−0,60)/(8,0−2,0) = 0,30 m/s, least-squares slope of the table 0,2995 m/s, inverse 3,33 s/m matches the student's 3,3; L3-05 1,0/0,050 = 20 K, 20/2,0 = 10 min. All match answers.py.
- L2-05: overlapping ranges → difference cannot be shown, and it is explicitly not proof of no effect (guardrail wording kept). Half-range is called a simple scatter estimate, not the uncertainty of the mean.
- L2-07: s = vt with t horizontal gives slope v; swapped axes give 1/v; the slope is read from line points, not raw neighbours.
- L3-05 mirrors the lesson's ε = Δ/x ≥ … method; the solution says that 10 min is a lower bound because cooling slows.
- L1-06, L1-07, L1-08, L2-06, L3-04: exactly one correct option each; every distractor's feedback is right. Outlier removal is worded as in the guardrails, and the hypothesis is "not proven certain".
- No duplicate of existing tasks; levels fit; kinds and data tables match the plan.
