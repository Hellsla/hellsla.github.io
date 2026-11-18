VERDICT: PASS
CONTENT-HASH: 0fb7773df145af69
SCOPE: delta: Sovella itsenäisesti tasks s8 (Skeittari half-pipessä) and s9 (Kaksi laitetta energiamittarissa) with solutions, answers.py and the changed intro sentence ("Kaksi viimeistä tehtävää lukevat tiedot kuvasta"); s1-s7 not re-judged.

## Blocking
- (none)

## Polish
- s8, figure `fy2-1/kitka-pylvaat`: its alt text ends "Lämpöenergiaa kuvassa ei ole", while the task and solution say sisäenergia (the figure is FY2's and keeps MAOL's lämpöenergia). Harmless, since the figure shows no such bar, but a student using a screen reader meets two names for one thing.
- s9 c: the solution takes the useful energy as mgh, i.e. the load is at rest before and after (or its kinetic energy is negligible). The task does not say so; one clause ("nostaa ... tasaisella nopeudella") would make the model explicit without revealing the method.
- s9 a, criterion units_precision: also carries the observation "A:n suora on kolme kertaa jyrkempi". It is a good reasonableness check but is not about units or precision; `reasonableness` would fit.
- s9 b: a lift motor running 3,0 h a day at constant 0,50 kW is a stretch but is consistent with the task's own premise (the rated power from the graph); fine for practice.

## Checked
- Intro: nine tasks, s7 the source task, s8 and s9 the only two with a figure (`figure` field in tasks.json); the sentence is true and reveals nothing of the solutions.
- s8: figure values (A 700/0 J, B 300/300 J, C 0/500 J) match answers.py, criteria and solution. Chain 700 -> 600 -> 500 J gives 100 J and 200 J; v = 4,7 m/s (4,71), friction 59 N (58,8), v without friction 5,6 m/s (5,58); 29 % = 200/700. Rounding follows the data (45 kg, 3,4 m: two figures; read energies exact on a 100 J grid). Tolerances cover the unrounded values.
- s8 text states the situation, figure and zero level, and asks last; it names friction (given in the situation) but not the energy-conservation method, "three phases" or the like. Part d asks both the value and the why (2 concept points). Energy-into-heat rule respected: sisäenergia, siirtyy lämpönä; the "katoaa/muuttuu lämmöksi" misconception is named only under common mistakes.
- s9: graph reading A 120 kJ and B 40 kJ at 80 s equals the figure's alt text; P 1,5 and 0,50 kW; cost 21,6 -> 22 EUR and 7,2 EUR (two figures, 3,0 h data); eta = 29,4/40 = 74 %; loss 0,13 kW = 26 %. The ratio check (3 : 1) is a good internal consistency.
- Alt text names (A, B, C; laitteet A ja B) equal the task's names. Figures carry no answer values beyond what the student must read ("safe" in REUSE).
- Calculation chains in the solutions are aligned rows; the 360 px captures of the stage were opened, but the capture set shows the guided Sovella stage and no s8 or s9 card (not found in shots.md), so open-solution layout of the new tasks is left to the visual reviewer and `check_layout.py`.
- Skills and links (fy2-1, fy4-7, fy4-8; fy2-3, fy2-4) fit the tasks; unit remains language-neutral (answers and figure ids identical across languages).
- Hash identical at start and end.
