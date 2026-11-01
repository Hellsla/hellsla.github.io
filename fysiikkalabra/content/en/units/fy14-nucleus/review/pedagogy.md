VERDICT: PASS
CONTENT-HASH: 32e35f45c81f307f

Pedagogy review of fy14-nucleus (2026-11-01). Page built with `python3 scripts/build.py fy14-nucleus` and tested in Playwright at 390 px. `check_layout.py --width 360` is all OK, and there are no console errors and no raw `$`.

## Blocking
None.

## Polish
1. `inquiry.json` `pred-heavy`: the correct option ("More neutrons than protons, $N > Z$.", 33 characters) is about half as long as the distractors (58 and 61). This is outside the ±30 % rule, and a short answer can stand out as well as a long one. Lengthen it, for example "More neutrons than protons, $N > Z$, to add attraction without repulsion."
2. `inquiry.json` `builder-text`: task 6 (two protons, no neutrons) is the only builder evidence about what holds the nucleus. It cannot separate the strong force from "neutrons cancel the charge", so `pred-glue` depends on the theory alone, which the design allows. To give the students something to argue from, add one sentence to the task's `done`: "Neutrons have no charge, so they cannot cancel anything; they add attraction."
3. `inquiry.json` `find-error`: the correct option is the shortest here. That is fine, but across the unit the correct option is the longest (or tied) in `review`, `pred-glue` and `check-3`. This is not a pattern a student could use; the note is only for balance.

## Shared issues
None found for this unit.

## Checked
- Predictions:
  - `pred-neutron`, `pred-glue` and `pred-heavy` lock on commit with no feedback.
  - They open only when `theory-main` (`pred-neutron`) or `theory-forces` (the other two) comes on screen.
  - Nothing before them answers them: the hook, the Why line, the hero (carbon-12, $N = Z$), the review feedback and the learning goals.
- The model answers of `builder-conclusion` and `check-explain` stay closed until the student has written something.
- The staged worked example (iron-56) has all seven stages.
- The Isotope Builder at 390 px is usable, and its tasks have their own Check buttons.
- Learning path: review → three predictions → builder and table → theory (about 510 words) → example and Coulomb task → three misconception checks and a transfer explanation.
- CLIL:
  - a word bank and sentence starters next to both writing tasks;
  - a pair task for the builder and the conclusion;
  - B1–B2 English with key terms in bold;
  - the French corner compares *eu* with the Finnish *ö*, has the `say` component and has `lang="fr"`.
- `teacher.md`: 75-minute timing, a plan for fast pairs and a plan for running out of time.
