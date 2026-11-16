VERDICT: PASS
CONTENT-HASH: ffd2c67e70d46b4c
SCOPE: delta added-exercise from 179ff8f7abefc16c base abdc9e095e4f
## Blocking

## Polish
- exercises.json fy4-9-L2-09 and solutions.md — the source date reads "luettu 16. marraskuuta 2026", while this review ran on 15.11.2026. Fix: confirm the reading date before publication.
- solutions.md fy4-9-L2-09 c) — method 1 does not say that the pusher is fixed to the station, so that the velocity change is measured relative to the station. Fix: one clause.

## Checked
- Only fy4-9-L2-09 judged (added exercise); the other tasks are as passed.
- Source: the task and solution state only what the coordinator's record of NASA's pages gives (SLAMMD, Andreas Mogensen of ESA, a known force on an astronaut attached to the arm, mass from the resulting acceleration by Newton II). No scene of the video is described; b) tells the student to compare with the video.
- a) The scale measures the supporting force, which is zero when station and astronaut are in the same free fall; mass unchanged and gravity still acts (it keeps them in orbit). Correct, no "no gravity" claim.
- b) $m = F/a$ and $m = F\,\Delta t/\Delta v$ are the same law since $a = \Delta v/\Delta t$; condition stated (the push is the only significant force along the motion, so it is the total force).
- c) The solution says there are many right answers and gives a method with example values labelled as such, not measured data. Recomputed: $20{,}0 \cdot 0{,}50 / 0{,}125 = 80\,\text{kg}$ (two figures as $0{,}50\,\text{s}$); method 2: $p_1 = 4{,}0\,\text{kg}\cdot\text{m/s}$, $m_2 = 4{,}0/0{,}050 = 80\,\text{kg}$. Method 2 rests on Newton III and the impulse principle, which this chapter teaches.
- d) $\Delta v = 0{,}130\,\text{m/s}$ is $+4{,}0\,\%$ and gives $76{,}9 \approx 77\,\text{kg}$, $-3{,}8\,\%$: "likimain yhtä suuri suhteellinen virhe" holds. Error sources and remedies are physical and belong to the example method.
- Every part is solvable with the source and FY4 knowledge; answers.py asserts the same numbers; the answer is a string, no numeric field.
- Notation ($\overline{I} = \Delta\overline{p}$, $\Sigma\overline{F} = m\overline{a}$) as in the chapter.
- Hash ffd2c67e70d46b4c at the start and at the end.
