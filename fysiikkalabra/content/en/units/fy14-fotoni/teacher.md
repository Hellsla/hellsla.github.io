## Shape of the unit

The unit has three parts: a 75-minute lesson before the visit, the visit to Fotoni, and a 75-minute lesson after it. The page follows that order: *Think about it*, *Predict* and *Investigate* are the lesson before; the worksheet in *Investigate* is used at Fotoni; *Theory summary*, *Apply* and *Check your understanding* are the lesson after. The visit itself is not part of the 150 minutes.

What Fotoni offers was checked in its material bank and its work instructions on 2026-11-01 (sources at the end of the page). The page describes only what those instructions confirm. Agree the stations, the group sizes and the timetable with Fotoni when you book, and check on the day that the equipment matches the worksheet (for example the LED colours, the coil data and the slit data).

## Lesson 1, before the visit (75 minutes)

- **0–10 min, Think about it.** Read the hook together; the review question on the stopping voltage; pairs discuss what makes a measured number trustworthy (sentence starters on the page).
- **10–20 min, Predict.** Predictions 1–3 individually, each committed with a short reason. Prediction 4 (hot filament) only for the groups that will do that station. The feedback stays closed until the closed box *Lesson 2: after visit* (in *Theory summary*) is opened after the visit.
- **20–40 min, Investigate: the physics of each station.** Fotoni requires the double-slit video (7:25) before the visit and recommends the photoelectric video (5:30); both are linked on the material bank page. Show the double-slit video here if a group will do that station, and give the photoelectric video as homework (or show it here instead). Then each group reads the station it will do and reports it to the class in one minute; the matching task on what each station measures.
- **40–60 min, Planning and safety.** Read *Planning a measurement*; the safety match; pairs write the plan for the photoelectric station with the word bank.
- **60–75 min, the worksheet.** Hand out the printed worksheet. Each group reads the tables for its stations and writes its research questions; decide who records and who reads the meters.

## At Fotoni

- Fotoni (second floor of the Physicum building, Kumpula campus) describes an upper-secondary visit as an introduction of about 15 minutes, about 60 minutes of lab work and a visit to a research department of 30–60 minutes. Students choose their works in advance and should bring laptops if possible.
- Stations in the material bank: photoelectric effect 3 stations of 1–3 students, e/m 2 stations of 1–3, double slit 1 station of 1–4, Millikan (qualitative) 1 station of 1–4, hot filament 1 station of 1–4, spectra 3 stations of 1–5. In about an hour a group can do two stations; plan the rotation with Fotoni so that as many students as possible measure Planck's constant, which the lesson after needs.
- Fotoni asks you to tell them if you want to use the short version of the photoelectric instruction. Its videos (photoelectric effect, 5:30, recommended before the visit; double slit, 7:25, to be watched before the visit) are linked on the material bank page: show the double-slit video in lesson 1 if a group will do that station.
- Students fill in the worksheet at the station, with units and uncertainties. Photograph the completed tables, or let students type them into a spreadsheet on their laptops before they leave.

## Printing the worksheet

Print the worksheet from the separate file `docs/fy14/fotoni-worksheet.md` in the repository (also `fy14/fotoni-worksheet.md` in the project files): open it in a Markdown editor or viewer, export it as PDF and print one copy per student, leaving out the stations a group will not do. Check the print preview: the empty cells should be large enough to write in by hand. The section *During the visit: lab worksheet* on the page has the same tables and is meant for reading on screen or for typing results on a laptop; printing the page itself also prints the tasks around it, and its tables keep their narrow screen width.

## Lesson 2, after the visit (75 minutes)

- **0–15 min, Theory summary.** Read *What the stations show* and the key idea; every group compares its own worksheet with it; *Back to your predictions*; the vocabulary match.
- **15–40 min, Apply: the fit.** The formula and the worked example step by step; then each pair analyses its own photoelectric data in a spreadsheet (pairs without photoelectric data use the example table). The e/m task is optional.
- **40–50 min, Connect to modern physics.** Groups of three: each student explains one station, then each writes the answer.
- **50–65 min, the report.** Read *Writing a lab report in English*; put the report in order; each student writes the discussion of the report.
- **65–75 min, Check your understanding.** Three checks individually, the explanation task and the summary. The French corner if time allows.

**Fast pairs.** The optional e/m task and the optional task on the spacing of the bands; a full fit for $e/m$ from their own table ($2U$ against $B^2r^2$, through the origin); a second discussion for another station.

**Running out of time.** In lesson 1, give the planning text as homework and keep the predictions and the safety match in class. In lesson 2, give the whole lab report (all seven parts) as homework and keep the fit, the discussion paragraph and the checks in class. The French corner can move to the next lesson or be done at home.

## Preparation

- Book the visit through Fotoni's booking instructions on the University of Helsinki pages; agree the stations and tell Fotoni which instruction versions you want.
- Print the worksheet (above). Have spreadsheets ready on the students' laptops for lesson 2 (scatter chart and linear trendline).
- Keep the predictions on the students' devices or on paper: the page keeps them in the browser of that device only.

## Assessment

- Written answers are self-assessed with the criteria shown after the student has written something. For a grade, use the same criteria.
- **Worksheet and analysis:** complete tables with units in every heading and an uncertainty for each measured quantity; a graph with labelled axes and a fitted line; $h = e\,k$ with $\Delta h$ from the steepest and least steep lines; a percentage difference and a correct statement about agreement within the uncertainty.
- **Lab report (English):** the seven parts in order; present tense for the theory, past tense for the method; numbers with units; at least two concrete sources of uncertainty, called random or systematic correctly; one improvement linked to a named source.
- **Modern physics:** for two stations, the classical expectation and what the measurement showed instead; one correct link to fusion research or another application.

## Common difficulties

- Students confuse the uncertainty with a mistake, or think that a result different from the accepted value is wrong. *Common misconception* and checks 1 and 4 target this.
- The radius of the electron beam is easy to read wrongly (diameter or radius, parallax against the scale). Ask each group how it read $r$ and what $\Delta r$ is; the e/m task has the diameter mistake.
- Frequencies in $10^{14}\ \text{Hz}$ and slopes in $\text{V} \cdot \text{s}$: remind students to write the power of ten in the spreadsheet's units or to convert before fitting.
- The intercept of the photoelectric line is far from the points (the Fotoni instruction says so too): the graph needs a scale that reaches $f = 0$ if students want to read $W$.
- The double-slit station is mostly a demonstration with analysis; if students did not collect counts themselves, they use the counts the instructor shows, and say so in the report.

## Extension ideas

- Fit $2U$ against $B^2r^2$ for all six e/m readings and compare the uncertainty of the slope with that of one reading.
- Use the filament temperatures from the software and Wien's law to calculate $\lambda_\text{max}$, and compare with the peak of the measured curves. Why might they differ (the prism, the sensor's sensitivity)?
- Read about how ITER uses spectroscopy to measure its plasma, and present one diagnostic in English.
- A short oral report: each group presents its result $x \pm \Delta x$ in English to the class in one minute.
