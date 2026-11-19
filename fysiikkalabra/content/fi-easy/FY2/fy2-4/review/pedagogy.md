VERDICT: FAIL
CONTENT-HASH: 4be5418ea1b3935c

## Blocking
- inquiry.json (ennuste-1 / koe-1 / simulaatio `model`) — Ennuste 1 asks for a fact (a petrol engine's efficiency) that a student cannot argue to a number. Koe 1 only returns the stipulated 25 %, and the sim's closed "Mallin oletukset" box lists every device's η, so the experiment cannot refute the prediction; it reads back an input. The only prediction a student can argue (ennuste-2, "aika supistuu") and its koe-2 are `optional`, and the sim cannot test it either (η is constant by assumption). — Make the core prediction the arguable one: promote ennuste-2 (the ratio E_a : E_o when t doubles) to the core path, with koe-2 using unequal rows. Let ennuste-1 be an estimate with the reasoning "which devices get hot?" and keep the η list out of the sim's visible text until the prediction is revealed. Alternatively, let the student compare η across several devices from the data and rank them before the numbers are shown.

## Polish
- lesson.md:114 — the paragraph "Hyötysuhde kertoo hyödyn osuuden" is about 170 words and holds four ideas (definition, upper limit, why real devices lose, heater). Split it at "Sähkölämmittimessä" and before the table.
- inquiry.json koe-1 question — the student computes E_h : E_o and gets 75 %, then must flip it to η, although the lesson is about η. Ask for E_a : E_o (25 %) directly.
- Selkeä suomi — "verrannollinen" (lesson.md:102) and "Hyötysuhteen arvoon vaikuttaa, mikä määritellään hyödyksi ja mitkä osat lasketaan kuuluviksi laitteeseen" (lesson.md:105) are abstract for S2 readers. Explain "verrannollinen" at first use ("nuolen paksuus kasvaa samassa suhteessa kuin energia") and give an example for the second sentence.
- inquiry.json ennuste-1 prompt — "Vihje: muista Pohdinnan kuuma hehkulamppu" steers students towards the distractor "noin 5 %". Drop the hint or ask the question without it.
- lesson.md:165 — "Valotehoon 3 W": write "Valotehon 3 W saamiseen".

## Checked
- Path: prior lessons (energy conservation, joule, power) → η = E_a/E_o = P_a/P_o → energy balance; within the slot, with no chain efficiencies or heat-engine cycle.
- The opening question is answered only in the theory, after the prediction. Retrieval (E = Pt) fits the phenomenon.
- The misconception that energy "disappears" is repaired in the Pysähdy items, check 1, the Etsi virhe item and the exit ticket.
- Feedback for every wrong option names the error (inverted ratio, 330 %, "heat is always a loss", power taken for efficiency).
- Worked example: seven stages, one step per stage, symbolic first, includes a plausibility check. It does not repeat the exercises.
- Transfer task (solar panel) has three hints and mistake feedback, and its solutions are complete.
- Three checks plus an exit ticket: concept, heater (heat as the benefit) and calculation. Explain criteria are observable.
- Workload: one lesson; extras are optional.
- Not opened: captures (the visual reviewer's job); the exercise set.
