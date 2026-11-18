VERDICT: PASS
CONTENT-HASH: 6e26a08a08a64312
SCOPE: delta (round 2), s7 Two loudspeakers / Kaksi kaiutinta pihalla, s8 standing wave on a string, changed intro; s1-s6 not re-judged; language: en

## Blocking
None. Round-1 blocking items (significant-figure reasons in s7 a, s7 b, s8 a; en decimal points) were verified in the current text and are fixed: s7 a two sf from the 0,50 m square, s7 b three sf from 343 Hz, s8 a three sf from 1,20 m, with exact counts stated as exact. No decimal commas in the en s7/s8 text.

## Polish
- s7 task text says the loudness difference from unequal distances is ignored, yet the c model answer says P is "not completely silent because the farther loudspeaker is heard more weakly". Drop that sentence or rephrase it as outside the stated model.
- s7 c "Perustele a- ja b-kohdan tuloksilla" points at the path-difference versus wavelength comparison; acceptable scaffolding, a bare "Justify" would be more exam-like.
- s7 d: tasks.json value 687 Hz, solution and rubric state about 690 Hz; tolerance covers both, but keep one form.
- s8 c: the units_precision row also carries the reasonableness check; label it accordingly.
- s8 d: "nodes cannot be at both ends" and "small amplitude" are loose; "no resonance, small amplitude, no clear nodes" is more exact.
- The solutions heading 'Yleisiä virheitä' stays Finnish in en; it is the file-wide parser convention (8 of 8 tasks), not a defect.

## Checked
- Task texts name no solution structure (no interference condition, no L = n lambda/2); grid reading, wavelength, comparison and next maximum emerge from the parts.
- Solutions follow rule 7: given, find, principle, formula first, conversions, substitution, rounded answer with sf reason, reasonableness; figure reading shown; common mistakes realistic.
- Rubrics fair: points sum to part points (s7 4+2+3+3, s8 3+3+4+3), alternative routes listed under accepted answers, wrong-model answers not rewarded.
- Figures fy5-12/ruudukko-tehtava (0,50 m squares, S1 to P 12, S1-S2 5) and fy5-13/kuvio-tehtava (1,20 m, four loops) match the numbers, symbols and names in text and solutions; answers.py values agree (6,0; 6,5; 0,50; 1,00; 687; 0,600; 30; 37,5; 12,5, 25).
- Changed intro: eight tasks, correct scope (oscillations, waves, sound), clear exam-style instructions.
- Translation fidelity checked against fi for s7, s8 and intro: numbers, criteria and points identical.
