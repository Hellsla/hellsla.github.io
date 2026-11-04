VERDICT: FAIL
CONTENT-HASH: 20c2600b9b6fb2ac

## Blocking
- solutions.md:242 (L2-05, Järkevyys) — A. "Jos köysi kiihtyisi, lukemien pitäisi erota selvästi" is wrong. For a rope whose mass is neglected, as the task states, the end forces are equal even while the rope accelerates. For a light real rope they differ only by m·a. This undercuts the point of the plan item, that the forces are equal at every moment. The same sentence also says "alle 0,1 N", but four of the five differences are exactly 0,1 N. Fix: "Lukemien erot ovat enintään 0,1 N, ja vuoroin A, vuoroin B on suurempi, joten erot ovat satunnaisvaihtelua eivätkä systemaattisia."
- solutions.md:271 (L3-04, Järkevyys) — A, causality. "Kitka … vie eteenpäin, vaikka se tavallisesti vastustaa liukumista" suggests that here friction does not oppose slipping. It does: the hoof pushes back on the road, and friction opposes the hoof slipping backwards, so it points forward (guardrail J). Fix: "Tien kitka vastustaa kavion liukumista taaksepäin, joten se osoittaa eteenpäin, liikkeen suuntaan."

## Polish
- solutions.md:276, :282 (L3-05) — "kärry vetää köyttä ja oppilasta" is wrong as written, because the cart does not act on the student. Write "kärry vetää köyttä, ja köysi vetää oppilasta". Also, the Vastaus lists b) before a). Put them in task order.
- solutions.md:226 (L1-08) — "osoittaa lapsesta kelkkaa kohti eli lasta vastaan" is unclear. Write "osoittaa lapsesta kelkkaa kohti (köysi vetää lasta taaksepäin)".
- exercises.json L2-06 b) — The table covers 0–5 s, but the distance is asked "ajassa 6,0 s". That is a 1 s extrapolation the solution does not name, and six readings can be misread as 6 s. Either ask for 5,0 s or say that the motion is assumed to continue the same way. At solutions.md:253, "pieni ilmanvastus on hyvin pieni … kokonaisvoima on nolla" should say "likimain nolla".
- solutions.md L3-04 c) — Explain also why the cart starts: the rope's force on the cart is larger than the cart's resistances. The text gives this only for the horse.
- docs/exercise-bank/FY4.md — The plan has a "väärin piirretty voimapari" error task and an L3 "törmäävät kärryt → kevyempi kiihtyy enemmän". The set has L2-07 (verbal fist/wall) and L3-05 (pull data) instead. The swap keeps out the second law, which is right for this chapter. Update the plan to match.

## Checked
- I recomputed all 17 numeric answers in one script. All agree with exercises.json and answers.py: L1-08 38 N, L2-05 4,8 N, L2-06 3,0 m, L3-04 450 N / 480 N, L3-05 3,40 N. The old answers are unchanged.
- L3-04: cart T = 410 + 40 N, horse F_t = T + 30 N. Each body has its own diagram, and no third-law pair is on one diagram.
- L3-05: v is constant (0,70 ± 0,01 m/s) from 4 s on, and the mean force is 3,4 N. Only the first and third laws are used, so the chapter's scope holds.
- MC items L1-06, L1-07, L2-07 each have exactly one correct option, and every distractor's feedback is right. L1-07 separates the support force's partner from the weight, as the lesson does.
- Notation follows the lesson: \overline{F}_{AB} = −\overline{F}_{BA} and magnitudes plain. No new figures, so there are no arrow-colour issues.
- The L2-05 and L2-06 captures (1280 px) render without overflow.
- The hash was the same at the start and at the end.
