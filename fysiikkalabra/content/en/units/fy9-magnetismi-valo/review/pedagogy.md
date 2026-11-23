VERDICT: PASS
CONTENT-HASH: a73bb95a8b0fdfba

## Blocking
None.

## Polish
- Pysahdy box 3 (critical angle, Formula section): the question is answered word for word in the sentence directly above it ("the angle of refraction is larger than the angle of incidence"). It is only a recall of the previous line. Ask a question the text does not answer, for example "what is the angle of refraction at the critical angle, and what does that say about the ray?", or put the box before the sentence.
- Pysahdy box 2 (the magnetic force and speed): the preceding formula paragraph already says "The magnetic force does not change the speed", and the text above the box says the force is perpendicular to the velocity. The box is a light recall. It works as a pause, but "Why not?" could ask for the work-done reasoning.
- Pysahdy box 1 (Key idea) sits right after the sentence that states the answer. It is acceptable as retrieval, and it fits the exam hint below it ("ask first what changes").
- The three boxes are short, open on demand and add no clutter, so the page is not heavier. Their placement (after the paragraph they test, before the figure) is sound.
- Several task titles name the topic or model: s3 "The magnetic field of a straight wire", s8 "A laser experiment with an acrylic plate", s9 "Flux through a coil and the induced current". In a review unit this is tolerable, but a neutral title would demand more independent model choice. The part questions (s1 b "ratio of the numbers of turns of the transformer", s2 a) also name the device. Fine at FY9 review level.
- solutions.md keeps the Finnish headings "Yleisiä virheitä" and "Hyväksytään myös" in the English file. This is probably the fixed key the page parser expects; check that the page shows English labels.

## Checked
- New pysahdy boxes: placement, answerability from earlier text, no disclosure of an unattempted answer, relevance to the unit's goals (flux change, magnetic force, critical angle). Content in English is correct and consistent with the Finnish version that passed.
- Hero and figure change from inline SVG to webp images. The aria-labels and the LaTeX labels stay as foreignObject text. The aria-labels give the same data without the answer. I did not open the image captures.
- Task set s1-s9 read from the packet: authentic or sourced situations (invented but flagged, CERN source page for s7, a flawed student report in s5, measurement data in s3 and s8, a flux graph in s9). The parts rise in demand (calculate, explain, critique, plan). Points are 11 to 17 per task. Competencies vary: math, graph, experiment, transfer, communication. There is variety across the nine tasks. Workload is fitting for 75 min.
- Solutions (s1 read in full): all seven required parts are present, symbols come before numbers, and the reasonableness checks are real. Common mistakes are real ones (U^2/R loss, forgotten 2 pi, swapped currents). The accepted alternatives are fair. The rubric points are not awarded for irrelevant things.
- inquiry.json diff: only the paragraphing of the solution changed (reflow). Pedagogy is unchanged.
- Deterministic check: practice.py check OK. Hash at start and end: a73bb95a8b0fdfba.
