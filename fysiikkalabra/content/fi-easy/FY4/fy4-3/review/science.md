VERDICT: PASS
CONTENT-HASH: e37e5b90dd1278d1

## Blocking
None.

## Polish
- Figure systeemit, right panel: the arrows for G_A+G_B and N_A+N_B are drawn 108 px long, exactly as long as G_A and N_A alone in the left panel. The combined weight is larger than A's weight alone, so a student who compares panels at one scale may read the arrows as the same size. The panels are separate diagrams, but the figure does not say so. Draw the right arrows longer, or add "eri mittakaava" to the figure description or text (class C, not blocking).
- "Vasta nyt voimat kuuluvat samaan systeemiin" is vague. Say it plainly: "Nyt molemmat voimat ovat saman systeemin sisäisiä voimia, ja niiden summa on nolla."
- Optional addition, not required by the slot: the net external force on A+B is zero (friction ignored), so the pair as a whole does not start to move even though A and B do. This would link the subsection to the first law.

## Checked
- Subsection "Kaksi tapaa valita systeemi". Definition of system, external versus internal forces, F_AB + F_BA = 0 and "internal forces are not drawn in the system's force diagram" are correct. The condition "friction ignored" is stated. The pair is never summed inside one body's diagram, which agrees with the preceding paragraph and with the summary.
- Directions in the figure: F_BA to the left on A, N up, G down. The system boundary on the right encloses both skaters, and the right panel has only external forces (combined weight and normal force). This is correct.
- The figure's description matches its drawing. Third-law pairs, the object choice and the absence of velocity drawn as a force all pass the force-diagram checklist.
- Recomputed in a script: worked example F_v = 2·48 = 96 kN. Sim values with m = 10 kg and friction 40/20/10 N give s = 1,125/2,25/4,5 m, t = 0,75/1,5/3,0 s and a lane time of 4,0 s at 3,0 m/s. F·s = 45 N·m, so a 5,0 N friction gives s = 9,0 m (answer and mistakes 2,25/4,5/5,625 are right). Push force on wood 110 N. Trailer 420 + 260 = 680 N (mistake 160 is right).
- inquiry.json: pred-1 and pred-2 each have exactly one correct option, and every distractor's feedback is physically right. Experiment 1 locks v0 = 3,0 m/s and varies only the surface. The conveyor belt check, the book and table pair, and the lamp diagram are correct.
- Scope fits FY4 (Newton 1 and 3, no complete force diagrams). The curling stone has no forward force. The sim states its model limits (constant friction, no air resistance, frictionless surface as a thought experiment).
- Not verified: the anturit figure data (only the 4 N peak and the 0,10 s contact time in lesson-answers.py were checked); the rest of sim.js (draw code) was not read.
- Hash is unchanged at the start and the end.
