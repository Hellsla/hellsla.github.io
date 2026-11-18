VERDICT: PASS
CONTENT-HASH: feb3d9ff810a6f9a
SCOPE: delta caption-label,md-paragraphs,reflow,typography,wording from b294f169a9ddc0c5 base b5600a6

## Blocking

## Polish
- exercises.json:70 (L1-06, option "osa varauksesta muuttui lämmöksi") — the new feedback ("Varaus ei häviä eikä synny tyhjästä") no longer answers the option's own claim that charge turns into something else. It is still correct, but a student may not see why. A fix: "Varaus ei muutu miksikään muuksi eikä häviä." The wrong option's own words stay as they are (guardrail: a wrong option keeps its words).

## Checked
- The hash was feb3d9ff810a6f9a at the start and at the end. I judged only the diff: one feedback in exercises.json and paragraph splits in solutions.md.
- L1-06 feedback and model answer: the physics is right, since total charge is conserved and charge is not created or destroyed. The verdict on the "lämmöksi" option is still "wrong", and exactly one option is still correct. No option and no correctness flag changed.
- L2 (F vs 1 : r² fit), L3 three-charge line and L3 hanging spheres: the text was only split into paragraphs. Every sentence, number, sign and unit is the same and in the same order, so the earlier recomputation still holds. I rechecked q = 40,9 nC: r = 0,1042 m and F = 1,384 mN.
- In the hanging-sphere solution, part c) is now its own paragraph after the answer. Its content is the same and its physics is right: the third-law pair has equal forces and the masses are equal, so both threads make the same angle.
- No new "lämmöksi" or "liikekitka" phrasing appears in the changed text.
