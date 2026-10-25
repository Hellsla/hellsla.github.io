VERDICT: FAIL
CONTENT-HASH: e808e1517d619f4b

The lesson still meets its goals and tells one story: interaction, then force, then the voimamittari (proportional stretch, calibration), then G = m g, and back to the opening astronaut question. It stays inside FY3: no motion and no vectors. The exercises, the exit ticket and the misconception section (bathroom scale, followed up in L3-03) cover the same threads. The proofreader's wording changes (lines 45 and 76) leave the story unchanged, and the length suits a first lesson. One regression: sim-spec.md now says the bar chart is scaled to the current mass, but the sentence after it still says the bars grow with the mass. Bar height is g_i/24,8 · 220 px, which does not depend on m, so the spec contradicts itself and the sim.

## Blocking
- sim-spec.md:1 — "Siksi jousi venyy ja palkit kasvavat näkyvästi, kun massaa kasvatetaan" is false now that the chart's full scale is m · 24,8 N. — Rewrite as "Siksi jousi venyy ja nuoli pitenee näkyvästi, kun massaa kasvatetaan, ja paino-ero eri taivaankappaleiden välillä näkyy palkeissa; palkkien lukuarvot ja asteikko kasvavat massan mukana."

## Polish
- sim-spec.md:1 — the 2 px minimum bar height can no longer take effect (the smallest bar, Kuu, is about 14 px at every mass). — Drop it or call it a safeguard.
- lesson.md:57 — the voimamittari SVG sits under Esimerkki, which is about the robot. — Move it after line 32 in Ydinajatus.
- lesson.md:30-38 — Ydinajatus has five paragraphs where gold has three. — Merge lines 32-36 into one paragraph.

## Checked
- Lint: 0 errors and 0 warnings. The editor hash was the same at the start and the end of the review.
- meta.json goals match curriculum.json.
- The opening question is answered at line 38 and in the misconception section.
- Scope: g is given in N/kg, and the link to m/s² is deferred to FY4.
- No exercise repeats the worked example.
- Levels have 5/4/3 exercises and fit the CLAUDE.md definitions.
- The exit ticket covers mass versus weight, stretch and the "kiloa" misconception.
- Diff since 2f088fd in editor files: lesson.md lines 45 and 76, and the sim-spec.md bar-scale sentence.
- sim.js lines 50-51: the bar scale depends on mass; the spring and arrow use a fixed scale.
