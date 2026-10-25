VERDICT: DONE

Round 1 fixes for fy3-1 (orchestrating session acting as the fixer). lint 0/0, build --all, check_latex (7 fragments) and test_sims fy3-1 (26 assertions) pass.

1. editor Blocking 1, physics-expert Polish 1 (sim-spec.md): the sentence "jousi venyy ja palkit kasvavat näkyvästi" replaced by the editor's wording (spring and arrow grow with the mass; the bars show the weight ratio and their values and scale grow with the mass). The 2 px bar floor is now called a safeguard (editor Polish 1, physics-expert Polish 3).
2. physics-expert Polish 2 (sim.js header): the comment now says the bars are proportional to G at the current mass.
3. mathematician Polish 1 and 2, proofreader Polish 1 (solutions.md:7 and :63): "1 kg:n massan paino on noin 10 N, joten 4,0 kg:n massan paino on noin 40 N" and "Kuussa paino on 1,62 / 9,81 ≈ 1/6 Maan painosta, joten se pienenee noin 5/6 eli 83 %".
4. web-designer Polish 3 and 4 (sim.js): the canvas scale line is now the short "asteikko 0–2480 N", drawn higher (BARS.y − 2) with the title at BARS.y − 15, so it never shrinks below 10 px and no longer touches the top value label; the explanation "Palkkikaavion asteikko 0–… N on tämän massan paino Jupiterissa" moved to the DOM readout, where it is legible on a phone.
5. tester Polish 1 and 2 (tests/sims/fy3-1.json): the Mars readout assertion and the 40 kg chartFull assertion added, plus one that the readout states the scale. Tester Polish 3 (tests depending on earlier state) not done: reordering 26 assertions is larger than a polish fix.
6. web-designer Polish 1, 2 and 5 (templates, not part of the lesson): lesson.js now picks the last section whose top passed 35 % of the viewport, pins the tapped tab briefly and scrolls the active tab into view; site.css removes the solution indent and narrows list padding under 600 px. Applied in the templates because the orchestrating session may edit them.

Not applied: educator Polish 1–5 (calibration wording, FY1 link, Moon mass, rewriting L1-02/L1-04 and exit ticket 3) and mathematician Polish 3 (SVG arrow position) are larger rewrites that need the human's decision; the educator and editor listed them as non-blocking. Default slider values, meta.json and status fields untouched.

Files changed: content/FY3/fy3-1/{sim-spec.md, sim.js, solutions.md}, tests/sims/fy3-1.json, templates/{lesson.js, site.css}.

Stale reviewers after these edits (python scripts/gate.py fy3-1): tester, physics-expert, mathematician, proofreader, editor, web-designer. The educator's verdict stays valid.
