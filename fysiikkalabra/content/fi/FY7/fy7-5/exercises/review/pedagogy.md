VERDICT: PASS
CONTENT-HASH: 5cd62b0183fa3d77

## Blocking
(none)

## Polish
- exercises.json fy7-5-L1-09 — five full calculations plus a ranking is level-2 work (several steps, a trap in C), not "one formula or one step". Move it to level 2 or cut it to three situations (A, C, D); level 1 would still have 8 tasks.
- exercises.json fy7-5-L3-03 — "Kuinka suuri magneettivuo kulkee keskimäärin yhden kierroksen läpi" is ambiguous (average over time? over turns?). The task asks the flux at the moment the pulse ends. Fix: "Kuinka suuri on yhden kierroksen läpi kulkeva magneettivuo hetkellä, jolloin pulssi on päättynyt ja magneetti on käämin keskellä?" Solution's "keskimäärin" goes too.
- exercises.json fy7-5-L3-01 — the task hands over "pystykomponentti", so the one insight that makes it level 3 (only the vertical component drives a horizontal axle) is given away; with unit conversions it is level 2. Ask for the Earth's field only as "Maan magneettikenttä, suunta kallistunut" with B and inclination, or accept as a hard level 2.
- docs plan for fy7-5 asks a task where the student draws e(t) from a piecewise-linear Φ(t) with a changed N ("kuvaajat" is the chapter's core). The set only reads Φ(t); none has the student produce the voltage graph. Add one level-2 drawing task (`"draw": true`-style, model figure) in a later round.
- solutions.md fy7-5-L1-05 Järkevyys — "hidasta kävelyä hitaampi vauhti" reads clumsily; write "Puoli metriä sekunnissa on rauhallista kävelyä hitaampi vauhti".

## Checked
- Levels and counts: 9/8/5 (minimum 5/4/3); L1 one formula or one rearrangement; L2 conversion, graph or table with data; L3 unfamiliar context, data modelling (L3-02 Δφ = 2BA, L3-03/L3-05 area under e(t)). None repeats the worked example (coil in an electromagnet) or the flashlight transfer task.
- Mix is varied: concept choice (L1-06), error analysis (L2-07), ranking, two graph figures (flux-task, flux-task-2: values and descriptions suffice, no voltage drawn, no answer given away), data tables with line fit (L2-06) and kinematics link (L3-04).
- Distractors in L1-06 and L2-07 are real misconceptions (large flux gives large voltage; voltage needs current; acceleration needed) and each feedback names the error and repairs it.
- Solutions follow CLAUDE.md rule 7: given, asked, principle with reason, symbolic formula before numbers, conversions (cm², mWb, km/h, µT), substitution, rounded answer with s.f. reason, reasonableness; graph tasks show how values are read (L2-02, L2-05, L2-08, L3-05).
- Lenz deferred to the next chapter consistently (L2-03 and L3-05 avoid directions; L3-05 only notes opposite signs).
- Data: L2-06 and L3-04 numbers are consistent with their answers; tolerances (2–5 %) fit the data's precision; L1-07's 2,25 V rounds to 2,3 V inside 3 %.
- Finnish and glossary use (induktiojännite, magneettivuon tiheys, käämi) are correct; units in LaTeX.
