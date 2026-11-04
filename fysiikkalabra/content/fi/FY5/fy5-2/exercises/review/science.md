VERDICT: FAIL
CONTENT-HASH: ea5bc4173fe3ad0e

## Blocking
- content/fi/FY5/fy5-2/exercises/exercises.json:255 (fy5-2-L3-05) and solutions.md:188 — **B**: the model puts the person's whole weight on the chair, which is true only if the person's feet do not touch the floor. A seated person with feet on the floor cannot tip a chair forward by leaning (the feet take the load), so as written the task and c) ("kurkottelu kaataa tuolin") leave a wrong picture. The task never states the condition. — Fix: add to the task "Henkilön jalat eivät ylety lattiaan, joten koko hänen painonsa on tuolin varassa" (or make it a person kneeling or standing on the chair, and adjust the data and the 0° value to fit), and say the same in the Periaate. The numbers stay: x_h,max = 42,2 cm, θ ≈ 53°.

## Polish
- exercises.json:82 (L1-08) — this is the same common-centre-of-gravity formula as L1-05 (two masses on a rod); the only new step is the plank's own mass at its middle. Acceptable, but close to a duplicate.
- exercises.json:74 (L1-07) — the seesaw is the same light beam with one moment on each side as L1-02, with masses instead of forces.
- Plan (docs/exercise-bank/FY5.md) lists "kaatuvan kappaleen raja-aineisto" at level 2; L2-07 (metre-stick mass) is done instead, and the tipping data moved to L3-05. Update the plan or note it.

## Checked
- All 8 new answers recomputed independently: 0,98 m; 1,6 m; least-squares slope −202,4 N/m → 61,9 kg (intercept 657 N vs theory 656 N); 209,9 N; 108,5/111,3/109,6/111,4 → 110,2 g; ladder s = 4,575 m; x_h = 42,22 cm, θ = 52,97°; all match answers.py and solutions.
- L1-06: exactly one correct option (equal and opposite forces on different lines turn the free rod; both moments clockwise); distractor feedbacks correct.
- L2-05 tolerance 0,05 covers the 59–65 kg the solution accepts for an eye fit; L2-07 0,03 and L3-05 0,04 fit their data.
- L2-06: the student's 141,3 N is reproduced; the forgotten bench weight (arm 1,00 m) is the real error; the check about the right leg closes.
- L3-04: friction toward the wall, smooth wall horizontal, f = μN at the limit; c) correctly argues N constant while the required friction grows; second-point check closes. Friction is FY4, a valid level-3 combination.
- Scope: ΣF = 0, ΣM = 0, centre of gravity, tipping: inside "tasapaino kiertymisen suhteen". Levels fit; plan +3/+3/+2 met.
