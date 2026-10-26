VERDICT: FAIL
CONTENT-HASH: 9bc1f95d58539988

## Blocking
- inquiry.json pred-3 (prompt, both feedbacks) — refers to "Selitä-vaihe" / "Selitä-vaiheen kuva", but the page has no such stage (Pohdinta, Ennusta, Tutki, Teoriatiivistelmä, Sovella); the student is sent to a place that does not exist, and the repair of the misconception hangs on it — fix: "Teoriatiivistelmän kuvaan ja malliin" / "Palaa tähän Teoriatiivistelmässä".
- sim.js (capture fy3-2-sim-390.png, fy3-2-lab-1280-1.png) — the simulation figure breaks the teacher's 2026-10-26 rule: canvas labels ("F = 60 N", "F (N)", "s (m)", "W = pinta-ala") and the readout ("W = F · s = 600 J", "P = W / t", "Voima F = 60 N", experiment lines "Alkutila: F = 60 N, s = 10 m") are plain sans text, while the same symbols in the prose are LaTeX maths; at 390 px "W = pinta-ala" touches the top edge of the canvas — fix: render symbols and units as maths (italic symbols, thin space before units) in canvas and readout, and give the label room.

## Polish
- The two experiments only reproduce W = Fs and P = W/t from a program that computes them, so they confirm arithmetic, not physics; Joule's table (3 rows, no graph) carries the empirical weight. Let the student plot or fit W against Q, or add a spring (rising force) option to the sim so the area under the curve is found, not given.
- pred-2 option 3 feedback says "mittausten mukaan"; elsewhere these are mallin arvot ("Mallin arvojen mukaan P = W/t pienenee 120 W:sta 30 W:iin").
- pred-3 cannot be tested in the sim and its correct feedback ("Juuri näin ...") appears at once; fine as a model comparison, but say in the prompt that the evidence is the figure and Joule's table, not the sim.
- Figure text at 390 px is about 10 px ("kanto sivulle", "liike", "A₁"); enlarge labels or the figure fonts for phones. Power has no figure, although P = Fv is a goal of the lesson.
- Joule figure: the weight carries no force arrow G, so the link to W = Gh (h only) is left to the text.

## Checked
- Learning path from fy3-1 to W = Fs, area under (s,F), P = Fv; opening question answered by pred-3 and reflect.
- Five theory figures: legible, LaTeX labels, uncluttered, colour not alone (arrows labelled), spring graph in scale.
- Worked example staged one step per stage, with a sanity check; the error-spotting item targets the 8 J slip.
- Exercises: three levels, no repeat of the example; solutions in LaTeX, numbers verified (250 kJ, 590 J, 45 min).
- Exit ticket tests perpendicular force, area as work, work versus power.
- Finnish: case after number+unit correct; terms match the glossary.
- Wide layout at 1280 px: sim beside the experiments; phone captures: nothing clipped except the label noted.
- Workload fits one lesson.
