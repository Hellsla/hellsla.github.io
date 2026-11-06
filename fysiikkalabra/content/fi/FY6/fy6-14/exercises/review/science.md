VERDICT: PASS
CONTENT-HASH: dd712fc8e155ee45
Round 1, science, mode full. Scope: the new YO-skill task fy6-14-L2-08 (two-stage, type 1); the rest of the set was PASS and is unchanged. Checked from text only, no renders.

## Blocking

## Polish
- fy6-14/exercises/exercises.json:291 (and solutions.md) — "Diodi johtaa vain anodi plusnavan puolella" is clumsy Finnish — write "Diodi johtaa vain, kun sen anodi on plusnavan puolella, ja …".
- fy6-14/exercises/exercises.json — none of the distractors carries the chapter's own warned mistakes (R = U : I, a diode as a fixed resistor). They carry the anode/cathode mix-up and the series-vs-parallel mix-up from the glossary and Tiivistelmä instead, which is acceptable physics. Pedagogy may want one of the warned mistakes in.

## Checked
- Physics: branch 1 is forward-biased (4,5 V − 2,0 V = 2,5 V across the resistor), so LED A lights. LED B and the silicon diode in branch 3 are reverse-biased, so B and C stay dark. The parallel branches are independent, so "Vain LED A" is right. A red LED reverse-biased at 4,5 V is below the usual 5 V reverse rating, so the task is realistic.
- The stem says that lamp C lights on its own, which removes any doubt about the lamp.
- The correct choice's feedback ("Oikein: vain LED A palaa.") does not give away the reason stage.
- Form: the four reasons are 84–103 characters long, and the correct one is not the longest. One reason is true but does not explain the answer (the series resistor), as type 1 asks.
- The terms (päästösuunta, estosuunta, anodi, katodi, etuvastus) are the lesson's and the glossary's, and the task stays within fy6-14 and its prerequisites.
- The solution is complete, takes each branch with its reason, and contrasts the series case.
- All numeric answers of the set were recomputed from answers.py in one call: no mismatch.
