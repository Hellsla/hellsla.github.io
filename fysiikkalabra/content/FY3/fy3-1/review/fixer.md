VERDICT: DONE

Round 2 fixes for fy3-1. `build.py --all`, `check_latex.py content/FY3/fy3-1` (7 fragments) and `test_sims.py fy3-1` (19 assertions) all pass. Checked the canvas visually at 320 and 390 px.

1. physics-expert 1 (BLOCKING, sim.js): the weight arrow was `20 + 50*G/G_FULL`. Now `arrow = ARROW_FULL * G / G_FULL` with ARROW_FULL = 110 px (pure k*G, no offset, exposed as `simState.arrow`). The drawing applies only a 3 px floor (`max(3, arrow)`) and shortens the head for tiny arrows. Longest arrow (100 kg on Jupiter) starts at y = 276 and ends at 386, inside the 400 px canvas. Comments in sim.js and sim-spec.md updated (no offset, 110 px at full scale, 3 px floor). Computed: arrow(10 kg, Maa) = 4,35 px, arrow(10 kg, Kuu) = 0,72 px, ratio 6,06; arrow(100 kg, Maa/Kuu) = 43,5 / 7,19 px, ratio 6,06. Two assertions added to tests/sims/fy3-1.json: (a) arrow(10 kg, Maa) / arrow(10 kg, Kuu) = 9,81/1,62 within 5 % (on the simState value, which is below the drawing floor at 10 kg); (b) at 100 kg, above the 3 px floor, Maa/Kuu = 6,06 within 5 %, arrow/G is the same on Jupiter as on Maa, and the arrow is at most 120 px. Existing assertions untouched.
2. web-designer 1, 3 (sim.js, narrow canvas): mass-label block is now `max(36 + 40*sqrt(m/100), textWidth(label) + 16)`, measured with the scaled text size. The bar-chart title is shrunk to fit (`2*(600 - 420) - 10 = 350` canvas px) when wider; the title text itself is unchanged. Bar value labels are shrunk if wider than bar width + 12 so neighbours do not touch at 320-360 px (same cause, same fix). Screenshots at 320 and 390 px (100 kg, Jupiter) show no clipping.
3. web-designer 5 (sim.js): non-selected bars alpha 150 -> 200.
4. educator/editor (lesson.md, g paragraph): "yksiköt N/kg ja m/s² ovat sama yksikkö" replaced by "Luku 9,81 on sama kuin FY1:n putoamiskiihtyvyys 9,81 m/s². Tällä kurssilla g:lle käytetään yksikköä N/kg, ja syy lukujen yhtäsuuruuteen selviää FY4:ssä." Weight is still never described as the cause of motion.
5. educator/editor (lesson.md, calibration): "tunnettuja painoja" replaced by identical small bodies of about 1 N each, one marks 1 N, two bodies give double the stretch and 2 N, and so on (the doubling argument). "Punnus" is not in glossary.json, so the word "kappaleita" is used.
6. educator/editor (lesson.md, summary and bathroom scale): the summary bullet now reads "g = 9,81 N/kg: yhden kilogramman massan paino Maassa. Kuussa g = 1,62 N/kg ja Marsissa 3,71 N/kg." Bathroom-scale sentence continues "Kuussa tällainen vaaka näyttäisi vain noin kuudesosan massasta."
7. educator/editor (exercises.json, solutions.md): L1-02 (Moon task) replaced by a spring task: 4,0 N -> 2,0 cm, how far at 12 N; answer 6.0 cm, tolerance 0.02 (12/4,0 * 2,0 = 6,0 recomputed in Python). Solution rewritten in the same format. Ids and the 5/4/3 structure unchanged.
8. educator/editor (exit-ticket.json, Q2): 3,0 cm at 8,0 N, 20 N gives 7,5 cm (20/8,0 = 2,5; 2,5 * 3,0 = 7,5, recomputed in Python), with a one-line reason.

Not applied (outside the list): web-designer 2, 4 (CSS/template, not fixable here), web-designer 6, physics-expert 2/3 and all other optional suggestions. Default slider values, glossary, templates/CSS, meta.json and status fields untouched.

Files changed: content/FY3/fy3-1/{lesson.md, exercises.json, solutions.md, exit-ticket.json, sim.js, sim-spec.md}, tests/sims/fy3-1.json.

NEW HASH: python scripts/gate.py --hash fy3-1 = 8fb367b0d6fd83e0

Every edit changes the content hash, so all reviewers must run again.
