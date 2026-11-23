VERDICT: PASS
CONTENT-HASH: 37809b21af7c6c0d
SCOPE: delta numbers,photo,teacher-figure,wording from 73014f45720e9c2d base b3ee786

## Blocking

## Polish
- content/en/FY8/fy8-9/lesson.md:58 (Geiger caption): the caption still says the counter "counts the ionising particles". The Activity paragraph now says "ionising particles and photons". To keep the claim the same in both places (consistency guardrail), write "ionising particles and photons" in the caption too.
- lessons/FY8/fy8-9/lesson-answers.py:70–71 (comments): the comments read 0,17750 and 97,62 MBq. The computed values are 0.177542 and 97.648 MBq. The page's 0.17754 and 97.6 are right, so only the comments are off.

## Checked
- Worked example: A = 550 MBq · (1/2)^(20.0/8.02), with 20.0/8.02 = 2.49377 and (1/2)^2.49377 = 0.177542, gives 97.648 MBq. The new last row "≈ 97.6 MBq" rounds this correctly to three figures. It now agrees with the Result and Reasonableness stages (97.6 MBq, between 138 and 69 MBq), with the Finnish text (97,6) and with lesson-answers.py `ex-A`. The old 97.65 was a four-figure intermediate.
- Activity paragraph: a Geiger–Müller counter registers ionising particles (α, β) and also gamma or X-ray photons. "Ionising particles and photons" is correct, and it removes the vague "quanta of radiation" without implying that only particles are counted. The added background caveat is unchanged and right.
- Geiger caption: "the count rate, after the background is subtracted, is proportional to the activity" is a type B condition that is now stated. It is consistent with the following paragraph and with the background subtraction in the exercises. Dead-time losses at high rates go unmentioned, which is a fair simplification at this level (C).
- The pictures fy8-9-hero.webp and fy8-9-ydin.webp and the figure blocks are teacher-approved. The packet carries no number or text change in them for me to judge.
- The rest of the lesson is as I approved it; no other line of the diff touches physics.
- The hash was 37809b21af7c6c0d at the start and at the end.
