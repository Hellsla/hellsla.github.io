VERDICT: PASS
CONTENT-HASH: c28f74ef54584ec7

The lesson does what its goals promise and tells one story. It goes from interaction to force, then to the voimamittari, then to G = m g with the g table, and ends back at the opening astronaut question. It stays inside FY3, with no motion and no vectors. The exercises, the exit ticket and the sim follow the same threads: weight on different bodies, proportional stretch, and mass versus weight (the bathroom scale in the misconception section returns in L3-03). The round-1 blocking issue is fixed. sim-spec.md now says that the spring and the arrow grow with the mass while the bars show the weight ratio, and this matches sim.js lines 45-52. The bar floor is now a safeguard ("varmuuden vuoksi"). lesson.md is unchanged, and its length (about 670 words) suits a first lesson.

## Blocking
(none)

## Polish
- lesson.md:33-43 — The voimamittari SVG sits under Esimerkki, but the example is about the robot. — Move the SVG to the end of Ydinajatus, after line 8. Left for the human in round 1; the line numbers given then were wrong.
- lesson.md:6-14 — Ydinajatus has five paragraphs, while gold asks for three. — Merge lines 8, 10 and 12 into one voimamittari paragraph. Left for the human in round 1.
- sim-spec.md:1 — "Tekstinä kankaan alla" does not mention the readout line that explains the bar scale (sim.js:50). — Add "sekä palkkikaavion asteikon selitys".

## Checked
- Lint: 0 errors, 0 warnings. The editor hash was the same at the start and the end.
- The only change in editor files since 9e1104c is the sim-spec.md sentence, which uses my round-1 wording.
- The sim-spec statements match sim.js: the fixed scale is 2480 N with a 110 px arrow, the chart's full scale is m · 24,8 N, there is a rest length, and the floors are 2 px for bars and 3 px for the arrow.
- The bar floor never takes effect: the smallest bar (Kuu) is 1,62/24,8 · 220 ≈ 14 px at every mass.
- meta.json goals match curriculum.json. FY1 covers putoamiskiihtyvyys (fy1-6), so the reference at line 21 is valid.
- The g values in the sim match the table at lines 25-28.
- The levels have 5, 4 and 3 exercises, and none repeats the robot example.
- The exit ticket covers mass versus weight, stretch and the "kiloa" misconception.
