VERDICT: FAIL
CONTENT-HASH: a261e297b6f6d732

## Blocking
- lesson.md:623 — B: the summary says "Positiivinen juuri on kohtaamishetki, ja negatiivinen juuri ei kuulu tilanteeseen" as a general rule for every uniformly accelerated case. Case 5 / exp-3 has two positive roots (1,55 s and 6,45 s), and both are meetings. — State the condition: "Jokainen positiivinen juuri on kohtaaminen (niitä voi olla kaksi); negatiivinen juuri on ennen lähtöä eikä kuulu tilanteeseen."
- lesson.md:624 and inquiry.json:3 (contribution) — B: "Etumatka on suurimmillaan, kun nopeudet ovat yhtä suuret" is stated as universal. It holds only when the one ahead is faster at first, as with a chaser starting from rest. The misconception section already says "suurimmillaan tai pienimmillään". — Add the condition, e.g. "kun takana oleva lähtee hitaampana", or write "välimatka on suurimmillaan tai pienimmillään".
- inquiry.json:545 (check-3) — A: "Auto lähtee levosta pyöräilijän edestä" puts the car ahead of the cyclist (as "bussi lähtee juoksijan edestä" does in sim-spec). The model answer and criteria assume the cyclist is ahead with a lead that grows. With the car ahead, the gap closes first. — State the start: "Auto lähtee levosta, kun pyöräilijä on sen edellä (tai ohittaa sen)."

## Polish
- lesson.md:385 — "eivät kohtaisi": add "jos ne lähtevät eri paikoista".
- lesson.md:401 — units "(m)", "(m/s²)" are plain text; the standing rule wants every symbol in LaTeX: $\text{m/s}^2$.
- inquiry.json:178,246,307 — the measure label "x_B − x_A" has no unit "(m)".
- sim.js:103 — case 5 draws the bus as a car and the runner as a cyclist (howto explains it).

## Checked
- One script recomputed every lesson, inquiry and exit-ticket number and each mistake value. All agree.
- The figures are to scale and match the text (vt areas are 9 m each).
- sim.js implements x = x0 + v0 t + at²/2. The simState keys exist in every experiment, and its limits are stated.
- Experiments: tapaus is locked and t is varied, which isolates the parameter. 8,0 s can be reached on the slider.
- Every prediction, Etsi virhe and check-1 has exactly one correct option, and its distractor feedback is right.
- Standing rules: \cdot is used throughout and × never appears. Vectors are written \overline{v} and \overline{a}. Velocity arrows are blue and acceleration arrows orange. Body colours are green and brown, so they never use a quantity colour. No forces are drawn.
- The scope stays within FY4 tasainen/tasaisesti kiihtyvä liike.
