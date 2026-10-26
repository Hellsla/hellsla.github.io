VERDICT: FAIL
CONTENT-HASH: 1cebfd341ecec92d

## Blocking
- inquiry.json pred-3 feedback (all three options, "Selitä-vaiheessa", "Selitä-vaihe johtaa") — the page has no stage called Selitä; the stages are Pohdinta, Ennusta, Tutki, Teoriatiivistelmä, Sovella, Tarkista — the student is sent to a stage that does not exist — write "luvun Teoriatiivistelmä-osassa" (or "Ydinajatus-kappaleessa") in all three.

## Polish
- exit-ticket.json, exercises.json (texts such as "ρ = 1000 kg/m³", "p = F/A", "ρgh", "0,30 m²") — symbols, quantities and units are plain text, while the lesson, inquiry and example render them as maths (see the Exit ticket capture: "ρ = 1000 kg/m³" is plain) — wrap them in $...$ per the 2026-10-26 rule.
- Simulation 1280 capture — two closed boxes, "Mallin oletukset ja selitys" and "Mallin oletukset", say nearly the same — merge them. Canvas labels ("ilma, p₀ = 101 kPa", axis ticks) are small plain sans text, not LaTeX, and small at 390 px — consider LaTeX and a larger size.
- inquiry.json pred-3 and reflect — pred-3 has no experiment (the sim cannot vary the area), yet reflect asks the student to compare all three predictions with "mittauksiisi" — say pred-3 is answered by the derivation, or add a cross-section control.
- lesson.md worked example stage 3 — the aligned display puts "ρgh" and "p" alone on lines, so the step reads in fragments on a phone — write "ρgh = ..." on one line broken at "·".

## Checked
- Figures (pressure-area, water-column, pressure-depth): all labels are set as maths and legible at 390 px, forces are drawn equal-length, the graph shows p0 as a dashed line with the ρgh bracket, and the new simple figure for p = F/A is present.
- Layout: 1280 px top and Tutki captures work (experiments beside the sim, readout and boxes visible); 360 px tested by checks; 768 px has no capture.
- Learning path: prerequisites are stated by chapter name, with no lesson ids; the opening dam question is answered in the text; the slot's goals are covered.
- Predictions 1 and 2 can be refuted by the experiments; locked and varied parameters are right; the feedback repairs the misconception (constant term p0) and names the evidence.
- Worked example: 5 stages, symbolic first, check of sense. Solutions are in LaTeX, symbolic first.
- Exercise levels 1 to 3 are progressive (L3: snowshoe, lid and hose, two layers); none repeats the example; the exit ticket tests the core idea.
- Finnish: no case errors found after number plus unit; workload is about one hour.
