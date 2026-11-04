VERDICT: FAIL
CONTENT-HASH: cb63d082dd31e069

## Blocking
- exercises.json:104 (L1-08). **A, duplicate.** "Lepakko, ultraääni, λ = v/f ilmassa" is the same task as fy5-14-L1-02 (a bat at 45,0 kHz, λ in air, answer in mm). It also repeats the method of this chapter's own L1-02, λ = v/f, and the brief says this chapter applies and does not revise. Because a near-duplicate across chapters counts against the later chapter, this task has to go. Fix: put a level-1 multiple-choice item from the plan in its place, for example on the lesson's misconception about why the highest frequency is not always used (it gives a sharp image but is absorbed quickly, so deep scans use a lower frequency), or on which A-scan peak belongs to which interface. Update answers.py:39 to match.
- solutions.md:150 and :152 (L2-05). **A, arithmetic.** d₂ = 1540 m/s · 58,9 µs / 2 = 4,535 cm, which rounds to **4,54 cm**, not 4,53 cm. The check line then gives 8,41 − 4,53 = 3,88 cm and blames rounding for the gap. With the correct d₂ the difference is 8,41 − 4,54 = 3,87 cm, the same as the answer. Fix: write 4,54 cm in both lines, and in the check write "8,41 cm − 4,54 cm = 3,87 cm on sama kuin …". Drop the rounding remark.

## Polish
- exercises.json:318 (L3-05). **B.** The task assumes "aallonpituus yli 10 km", but on stretch 1 (h = 4 km) that is not much larger than the depth. Write "noin 200 km valtamerellä (yli 10 km myös rannikolla)" or similar, in line with L3-03.
- solutions.md:147 and :184 (L2-05, L3-05). The step is headed "Kuvaajan lukeminen", but both tasks give a table. Use "Taulukon lukeminen".
- exercises.json:69 (L1-06, fourth feedback). "eikä aallon suunta vaikuttaa siihen" should read "eikä … vaikuta siihen".
- L2-06 vs fy5-14-L1-01. Both get the speed of sound from an echo, v = 2L/t. They differ in medium, apparatus and averaging over four rows, so this is not a duplicate. To make L2-06 clearly different, it could ask how the spread of the four values compares with the error in reading t.
- Plan deviation (docs/exercise-bank/FY5.md). The plan puts the gel at level 2 (experiment) and "why S-waves do not cross the outer core" at level 3. The set has both as level-1 multiple-choice items (L1-07, L1-06), and level 3 has a tsunami task (L3-05) instead. Both levels fit, so update the plan.

## Checked
- One script recomputed all 20 answers from the task texts. All agree with answers.py and with exercises.json within tolerance.
- L2-05: d₁ 1,65, d₂ 4,54, d₃ 8,41 cm; layer 3,873 cm.
- L2-06: 1481, 1474, 1481, 1477 m/s; mean 1478,6 m/s, given as 1480 m/s. There is no hidden delay: t is proportional to L, with an intercept of about 0.
- L2-07: 8,4 km/s · 16,0 s = 134 km. The travel times 22,4 s and 38,4 s differ by 16,0 s. The 56 km distractor is correct as a wrong answer. The explanation (P has already covered the whole path before Δt starts) gives the direction of the error: the student's answer is too small.
- L3-04: d = 84,0, 63,0 and 49,6 km. The two candidates are (72,9; ±41,8). Distance to C is 49,9 km against 132,4 km, so +41,8 km is right. Part c's mirror-image argument is correct.
- L3-05: travel times 1514, 1010 and 903 s, total 57,1 min. The ratio 0,60 and the speed ratio of about 9 are both correct.
- L1-06 and L1-07: each has exactly one correct option, and every distractor and its feedback are right. The 99,9 % and 0,2 % reflections agree with acoustic impedances.
- The new tasks stay inside FY5 scope: echo depth, v = fλ, P and S waves, and √(gh) as the lesson gives it. Notation matches the lesson.
- The 1280 px captures of L2-05, L2-06 and L3-04 render cleanly. There are no 360 px captures of the new tasks.
- The hash was the same at the start and at the end.
