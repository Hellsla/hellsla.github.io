VERDICT: PASS
CONTENT-HASH: c01ae7b7fd2c9a4c
SCOPE: full: the three new pysahdy boxes first (against the Finnish unit.md), then unit.md (hero, geo and tilanteet now WebP image bases), inquiry.json, teacher.md and the Sovella set s1-s9 (tasks, solutions, rubrics, answers.py).

## Blocking
- None.

## Polish
- Second pysahdy box (Uniform circular motion) says "normal acceleration", but the paragraph right above it and the formula name say "centripetal acceleration". The physics is the same, but use one term on the page, whichever the glossary gives.
- teacher.md "Assessment": "the other five ... $95$ points in all". The set has nine tasks: s3 has 20 points, s9 has 17 and the other seven have 15 each, 142 in all. The Finnish teacher.md has the same error, so fix both.
- s3 d: tasks.json `answer` is 0.4948 s, but answers.py and the solution give 0.4937 / 0.494 s. The difference is inside the tolerance.
- geo image: the grey radius line from the Earth's centre stops at about 70 % of the orbit radius. It does not reach the dashed orbit next to the label $r \approx 6.6\,R$. The radii are to scale: about 6.4 measured against 6.6. The Finnish page uses the same image.

## Checked
- pysahdy 1 (net force points to the centre because the acceleration does), pysahdy 2 (velocity along the tangent, acceleration to the centre) and pysahdy 3 (doubling $r$ gives a quarter, $F \propto 1/r^2$) say the same physics as the Finnish boxes, sentence by sentence.
- The new images are the same files as the Finnish unit's. Every label foreignObject is still there. Force, velocity and acceleration arrows in tilanteet: plank $N_2 > N_1$ with the closer support carrying more; hump $N < G$, $a$ down; satellite has one force only. In geo, $\overline{v}$ is tangent and anticlockwise, $\overline{F}$ points to the centre, and after 6 h the line of sight has turned a quarter.
- I recomputed every number in one script with my own formulas (geo: $r = 42\,157$ km, $h = 35\,786$ km, $v = 3.074$ km/s; GPS $T = 12.0$ h; inquiry lid, pedal, shovel, phone, science satellite, barrow and all mistake values; s1-s9 every part, including s3's fit $k = 1.950$, intercept $0.034$; s7 e shadow at $\theta = 70.2^\circ$, 39 %, 36 min). All of them agree.
- Every choice item has exactly one correct option, and the distractor feedback is right. The weightlessness text says normal force zero with gravity present. Centrifugal force is never drawn.
- Rubric points add up to each part's total. Hyväksytään myös covers the other correct methods. The model answers in the explain tasks are sound, and the sig-fig reasons hold. s7 cites its NASA source. The other tasks are labelled as invented.
- Hash c01ae7b7fd2c9a4c was the same at the start and at the end.
