VERDICT: PASS
CONTENT-HASH: 1bb16197ef174c7b

## Blocking
- none

## Polish
- scripts/check_i18n.py does not list `detail` (a rubric criterion's specifics) in TEXT_KEYS, so it reports the translated check-3 criteria details as errors; the translation is right and the checker needs `detail` added (outside this review's scope; the content hash does not change when it is fixed).

## Checked
- Checked (full translation review): goals read "In this lesson, you will learn to" + bare verb (identify, tell apart, form); same demand as the Finnish in every prediction, check and transfer task; feedback and hints translated in full, with no hint or option giving the answer away; every model solution keeps the free-body-diagram step before the equations and all seven stages; the drawing task (check-3) stays gated at 360 px: the model diagram and rubric open only after the student ticks that the diagram is drawn, and the rubric details are now in English. The elevator task shows four unlabelled diagrams whose descriptions do not reveal the correct one.
