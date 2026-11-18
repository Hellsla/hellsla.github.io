VERDICT: PASS
CONTENT-HASH: ae9268d2c79b7c5f
Mode: full

## Blocking
None.

## Polish
1. exercises.json, fy4-13-L1-08: "Piirrät kärryn voimakuvion." is the wrong form. Corrected: "Piirrä kärryn voimakuvio." (or "Olet piirtämässä kärryn voimakuviota.").
2. solutions.md, fy4-13-L3-01 Vastaus: "19000 N ... kaksi merkitsevää numeroa, koska massat on annettu sadan kilon tarkkuudella" conflicts with the house rule that trailing zeros of 800 kg and 1200 kg are significant. Give $18\,800\,\text{N}$ (three figures) or state the task's own reason. The box answer 19000 stays inside tolerance.
3. solutions.md, fy4-13-L2-02 and L3-02 Kaava: the algebra between the two motion equations and the final form is skipped. L2-02: show $T = m_1\!\left(g + \dfrac{(m_2-m_1)g}{m_1+m_2}\right) = \dfrac{2m_1m_2}{m_1+m_2}\,g$. L3-02: show $T_\text{max}m_1 + T_\text{max}m_2 = m_1m_2 g \Rightarrow m_2(m_1 g - T_\text{max}) = T_\text{max}m_1$.
4. fy4-13-L2-05, L2-06, L3-04, L3-05 prose and Annettu lines carry "esimerkkiaineisto". The 2026-11-13 rule drops provenance on example data; cut it, keep the tables.
5. solutions.md, fy4-13-L2-05 Kuvaajan lukeminen: "sovitussuora osuu viimeisen pisteen kohdalla arvoon $4{,}9\,\text{m/s}^2$" reads the fit off a value the student does not yet have. Say: paper fit through the origin gives about $4{,}9$ at $250\,\text{g}$; the last point $4{,}84$ gives $g = 9{,}7$, also accepted.

## Checked
- Opened exercises.json and solutions.md whole (8 + 9 + 6 tasks; counts met) and the packet's Kaava, Esimerkki and Tiivistelmä.
- Recomputed: 2,0; 4,7 N; 2,8 N; 29 N; 4,0; 3,9; 880,8 N; 6,54 N; 8,0 N; 0,907 kg; 9,8 (fit 19,5-19,6 x 0,5); 3,41 N; 1,96; 1,6 N; 18 835 N; 0,44 kg; 0,857 s; 15 kN and 21 kN (20 kN limit exceeded); mean mass 0,909 kg; 1,21 kg. All match, including the table-derived numbers in L3-05 and L3-04.
- Every Kaava opens with $\Sigma F = ma$ for each body separately, then adds equations; none opens with $a = m_2 g/(m_1+m_2)$.
- Every force task asks for the diagram first and each solution gives the diagram as a voimakuvio block with arrows that match the equations (T below G for the accelerating weight; K12 > K23).
- L1-06, L1-08, L2-08 are conceptual choices with distractor-specific feedback; L2-08's second step (reasons) targets the "T = m2 g" misconception and a true-but-irrelevant option.
- L2-07 error analysis: the student's mistake is localised to the substitution step and the units of the check agree.
- Level mix: L1 single body or one pair, L2 conversion, data, error, L3 limit, kinematics link, reordering wagons and two data tasks; none repeats the worked example (1,5 kg + 0,60 kg).
- Finnish: case after number+unit correct ("$3{,}0\,\text{N}$:n", "$20\,\text{N}$:n"); glossary terms (jännitysvoima, voimakuvio, liikeyhtälö) consistent.
- Captures not opened: text and formula order only.
- Hash the same at start and end.

## Scores
Level fit 5/5. Task clarity 4/5. Solution completeness 4/5. Finnish 4/5. Feedback quality 5/5.
