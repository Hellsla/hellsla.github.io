VERDICT: PASS
CONTENT-HASH: d1e3f3544f8c599a

## Blocking

(none)

## Polish

- inquiry.json "data" question (tolerance 0.03 m/s) — reading a second point off a 340 px graph to within about 0,05 m/s means reading x to about 0,5 m of 15 m; a phone student will land at 1,4 or 1,6 and be told "wrong" — widen tolerance to about 0.1, or give the end point of the line in the text.
- inquiry.json pred-1..3 feedback — each wrong option's feedback already quotes the exact model values (B 40 m at 10 s, A and D both at 12 m at 6 s) that the experiment is meant to produce. They show only after commitment, so this is not disclosure, but exp-1..3 then partly repeat what the student was told; consider "B:n suora on jyrkempi" without the numbers in the wrong-option feedback.
- Workload — 3 predictions, 3 experiments, 2 interpret items, example, error item, transfer task, 12 exercises, 3 checks and an exit ticket is more than one lesson hour if done in full; exercises 2 and 3 are already marked optional, and the fitted-line item could be marked optional as well.
- inquiry.json exp-2 question — "Laske kummankin kärryn nopeus taulukosta. Mitä huomaat?" gives the student no chance to refute prediction 2 on the displacement claim (the prediction speaks of siirtymä, the question of nopeus); add "ja siirtymä" to the question.
- sim legend (390 px) — the A/B legend sits in a narrow right margin and the plot area is only about 230 px wide on a phone; legible but small. A legend row under the plot at phone width would give the graph more room.

## Checked

- Packet read in full; hash identical at start and end (d1e3f3544f8c599a).
- Learning path: pyöräilijä hook -> ala-asteen nopeus retrieval -> three predictions -> experiments -> data -> theory -> reflect -> example -> error item -> transfer; the opening question (matka 4 km, siirtymä 0) is answered in the theory, reflect and check 3. Scope stays on the slot's goals (no acceleration).
- Experiments can refute their predictions: varied t only, case locked, the numeric or choice question is answerable only from the recorded rows; sign and starting-position misconceptions are repaired in feedback.
- Simulation canvas at 390 and 1280 px (captures plus Playwright, case 4 mid-run): all KaTeX labels (axis ticks, A/B/D/E badges, legend, x (m), t (s)) are 10,8 px at 390 and 11 px at 1280, so at least 10 px; no overlaps or clipping, cart badges, arrows, graph markers and the dashed t-cursor stay apart.
- Readout under the canvas is LaTeX and reads well; Käyttöohje, Mallin oletukset and Laskennan selitys are closed boxes; the visible lead text is under 30 words.
- 1280 px: the simulation sits beside the experiments, buttons and table next to each other.
- Figures 1-6 (siirtymä, edestakainen, kulmakerroin, robotti, hölkkääjä): labels in LaTeX, legible on a phone, colour never alone (signs and arrows are labelled).
- Worked example: five stages, symbolic first, then substitution, then a sanity check; not repeated in the exercises.
- Exercises: 5/4/3, each one formula, two steps, reasoning; answers verified by hand (L3-01 4,0 m/s, L3-02 50 m, L3-03 0,25 m/s); exit ticket tests the core ideas in vector notation.
- Finnish: glossary terms correct (keskinopeus vs keskivauhti kept apart), case after number+unit fine, no spelling errors found.
