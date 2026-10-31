VERDICT: PASS
CONTENT-HASH: 80e44fd6110c09bb

## Blocking

None.

## Polish

- Step 4: GA Pro's Linear fit box labels the slope and intercept with its own letters (y = mx + b as far as I know; verify). A student told "kulmakerroin ja vakiotermi" who sees an "m" may read it as metres. One sentence ("ohjelma merkitsee kulmakerrointa kirjaimella …") would remove the doubt; same in tvt-kulmakerroin step 3 and tvt-tyoselostus step 4.
- Step 6 and the mistake "Poikkeava piste on poistettu kertomatta" tell the student to leave a point out of the fit but not how to do it in GA Pro without deleting the row (tvt-taulukkolaskenta step 4 forbids deleting it). Either name the verified way (fit only a selected region) or say to ask the teacher.
- Step 7 repeats the Linear-first advice already given in step 3; could be merged so the student does not fit twice.
- Checklist does not check goal 2 (linearisation); add e.g. "Jos riippuvuus oli kaareva, olet linearisoinut sen ja sovittanut suoran uuteen kuvaajaan."

## Checked

- Read guide.json, guide.md and both figures' labels in full; ran the hash. Menu names (Graph Tools, Apply Curve Fit, Linear, Proportional, Points) match the verified facts; region selection by dragging, RMSE and r in the fit box are verified facts.
- Order: model → what least squares does → fit → read box → residual pattern → outliers → origin or not → linearise. Each step says why (r alone does not prove the model; Proportional only with a physical reason).
- Goals (fit and judge the model; linearise via a new quantity) match steps; four linearisation examples come from real investigations whose titles exist.
- Mistakes are real ones (line through first/last point, polyline, forced origin, straight line on curved data, silent outlier removal, extrapolation), each with symptom and fix.
- Figures: least-squares residuals and curved v(h) vs straight v²(h); no numbers, so no invented data. Units in LaTeX.
- Finnish clear, short sentences; cross-links to kuvaaja, kulmakerroin, taulukkolaskenta sensible. No spreadsheet/Excel/Tracker leftovers.
