VERDICT: PASS
CONTENT-HASH: 8d806aafb6c72eb4

## Blocking
None.

## Polish
- fy6-s1 text is long, and it names the error source (warming, creep, a falling voltage) before part d asks the student to find it. Part d then rewards "naming" a source the text has already given. Trim the text, or let the student notice the drift from the 0.10 A re-reading alone.
- fy6-s1 part a: "choose a suitable model" is good, but the 4.5 V marking and the figure's internal-resistance symbol (if shown) make the model obvious. Check that the figure does not draw R_int.
- fy6-s3 part a (4 p) and fy6-s4 part a (3 p) are single-formula calls (E = U : d, F = qE; E = 1/2 C U^2). Part a of s3 does carry an evaluative reasonableness criterion. For s4 a, either ask for the energy comparison early or make the part smaller.
- fy6-s3 part a's heading "Evaluate which other forces act" and part d's "what does the result tell" are well built. Part b's criterion "strength of the field or the acceleration is not needed" works as a hint for the student, but it is a marking note and should not appear in the student's text.
- fy6-s4 has no figure and no source material to interpret. A short table or a graph of the discharge (U(t)) would raise the demand on interpreting sources, which is the weakest of the six competencies in this task.
- fy6-s2 part d asks for four things in one prompt (current, protection, basis for the fuse rating, voltage) and the order of the criteria does not follow the order in the prompt. Reorder the criteria so they follow the question.
- Variety: s1 is graph and experiment, s2 is a circuit, s3 is fields and energy, s4 is a capacitor and safety. Semiconductors, diodes and LEDs and Kirchhoff's junction rule are not applied anywhere. Check that the coverage document records this as a deliberate gap (docs/coverage/FY6.md was not in the packet, so it could not be judged).
- Workload: 15 parts, 15 to 16 points per task, about 60 points. This is a little heavy for a 2 op course. Accept it, or mark s4 as the optional task.

## Checked
- Each task is an unfamiliar, authentic situation. Headings and prompts do not name the formula: s1 "Choose a suitable model", s3 b "State your assumptions", s4 b "compare with the voltage decrease".
- Parts rise in demand: calculate, then evaluate, then justify and interpret. Every task ends in a word part with a conclusion.
- Rubrics are specific and fair. Points go to relevant content, and tags match what is demanded.
- Numbers checked against answers.py:
  - s1: slope -1.19, E 4.60 V, 13 %, 0.08 and 0.06 ohm.
  - s2: 2.5 A, 16.7 W, 4.3 A.
  - s3: 1.8e-7 N, 13.4 m/s, 3.2e-9 N with 0.8 times the weight.
  - s4: 14.85 J, 6.86 J, 46 %, 26.4 A.
  All are consistent in solutions and criteria.
- Worked solutions are model-based (Given, Find, Principle, Formula, Answer, Reasonableness). The "Hyväksytään myös" sections and the common mistakes are real (broken-line fit, slope read from adjacent points, ignoring the internal resistance, 0.01 V quoted as the uncertainty).
- Safety part s4 d is responsible: it states that the current is an idealised estimate and sends servicing to a professional.
- Scope: s4 treats the capacitor only as energy and charge, with no exponential function and no capacitor connections.
