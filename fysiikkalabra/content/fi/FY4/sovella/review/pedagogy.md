VERDICT: PASS
CONTENT-HASH: 78c0faf56737d1db

Delta review: since the last PASS the diff is one ```voimakuvio block (solutions.md, fy4-s1 c-step "Voimakuvio:"), the only "Voimakuvio:" step in the file apart from the b-step's hand-made figure. Nothing else changed, so the earlier judgement of the three tasks, rubrics and variety stands.

## Blocking
None.

## Polish
- The to-scale diagram at 4,0° (390 px render) is hard to read. G_y lies on top of G and G_x is a stub under the weight arrow, so the dashed components do not show that "G_x is larger than friction"; the G_x label sits at the body's right edge, away from its arrow. Friction (21 N) is drawn longer than scale (alt text says so) but the rest of the figure then looks as if friction ≈ G_x. The b-step's exaggerated model figure teaches the same point better. Consider dropping `komponentit G` from this block, or saying in one sentence that the 4° slope makes the components short and the picture is to scale.
- The block uses only wax A's friction (21 N), but c) asks for both A and B. Add "(voide A)" to the sentence, or leave friction unlabelled by value; the page shows no numbers, so this is only a wording matter for a reader of the source.
- The c-step now shows a second diagram right after the first ("b-kohdan kuvio"); the sentence could say "samassa mitoituksessa kuin b-kohdassa, nyt mittakaavassa" so the student sees why it is drawn again.

## Checked
- practice.py check OK; fbdspec.py check: every Voimakuvio step drawn.
- Spec physics: G = 72 kg·9,81 = 706 N; N = G cos 4° = 704,6 N; friction = G sin 4° − m·0,39 = 21,2 N up the slope; a down the slope, forces sum that way.
- Diagram comes before any equation in the step; accessible text alternative present and honest about scale.
- Does not give away the task: it sits in the solution, after the student's own drawing in b).
- Rendered the preview at 390 px; the figure fits and is legible apart from the points above.
