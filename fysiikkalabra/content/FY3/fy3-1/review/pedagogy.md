VERDICT: FAIL
CONTENT-HASH: 590742e6e82795d0

## Blocking
- sim.js (canvas, review/shots/fy3-1-sim-390.png, fy3-1-lab-1280-1.png) — the spring scale in the simulation is labelled kN with ticks 0 to 2.5, but every weight in the lesson is 16-248 N. The 10 kg box on Earth (98,1 N) therefore reads about 0, and the lesson's central unit, the newton, is not on the instrument. This undoes "voimamittari mittaa newtoneina" and the calibration story — fix: label the scale in N, sized so that 98,1 N and 248 N are readable (for example 0-250 N), or drop the numbers and keep only the stretch.
- sim readout and experiment text (sim-390.png, exp-exp-2-390.png) — "Massa m = 10 kg", "g = 9,81 m/s²", "G = m · g = 98,1 N" and the experiments' "Alkutila: ... massa m = 10 kg" are set as plain sans text, while the example and theory use maths. The teacher's rule 2026-10-26 (symbols in prose as maths) is not met where the student looks most — fix: render the readout and the experiment initial-state lines through KaTeX, with non-breaking spaces between number and unit ("10 kg" breaks across lines at 390 px).

## Polish
- sim canvas labels (G (N), kN, Kuu, Mars, "asteikko 0-248 N", the legend) are plain canvas text, not LaTeX like the three figures; at 390 px the bar and axis labels are about 8 px. Enlarge them, and set G and N in the same maths typeface at least.
- Hook/lesson.md:104 — "Tässä vaiheessa kiinnostaa vain voiman suuruus, ja kuvissa nuoli näyttää suunnan" is slightly cryptic for a first paragraph; say "Nuoli kuvassa näyttää, mihin suuntaan voima osoittaa."
- Fig. 3 — the Jupiter line leaves the frame with no value; add the label "Jupiter, 100 kg: 2480 N (kuvan ulkopuolella)" or extend the axis.
- Fig. 2 — the label "suora origon kautta" is plain text inside the plot; it is fine, but "x = kF" with the slope as a number would link to the formula $G = mg$ afterwards.
- check-1 option "Marsin ohut ilmakehä..." and pred-2 option on Jupiter's gas surface are good distractors, but the feedback in pred-2 could name the experiment's reading, not only the model value.

## Checked
- Figures 1-3 (fy3-1-fig-1/2/3-390.png): labels in LaTeX, uncluttered, colour with labels; fig. 1 shows 1 and 2 bodies with x and 2x clearly; legible at 365 px. Rule 2026-10-26 on figures met.
- Opening question is answered by the Kuu paragraph and g table; scope held to G = mg (no Newton's laws).
- Prediction, experiment pairs can refute (Koe 1 varies only m, Koe 2 locks m, varies body); the sim computes the formula but the spring/bar views make the comparison concrete.
- Example is staged in six steps and does not repeat any exercise; solutions in LaTeX with sanity checks.
- Exercise levels ascend; L3 tasks need reasoning; exit ticket tests mass vs weight and proportionality.
- Finnish: case after number+unit correct; no lesson ids in prose (only course names FY1, FY4).
- Layout at 1280 px: hook and prerequisite item sit two by two and read standalone; lab view beside simulation fine.
