VERDICT: PASS
CONTENT-HASH: 17e8bd95a6baa0ea

## Blocking

None.

## Polish

- Mistake "Liitetyt luvut eivät ole lukuja" names the cause (decimal separator) but not the fix; add one, e.g. change the separator in the phone app's export or replace it before pasting.
- Step 4 says to leave a point out of the fit without deleting the row, but no guide says how in GA Pro (see tvt-suoran-sovitus polish).
- Step 6: degrees → radians has no example; e.g. `"θ"*3.14159/180` (or the verified way) would save students a dead end with sin/cos.
- Sensor runs produce columns with the program's own names; add one line to step 5 that the name in quotes must be exactly the column's name as shown, also for sensor columns (mistake 1 covers it after the fact).
- Checklist does not check goal 3 (cumulative sum / area); add e.g. "Kertyvän summan tai pinta-alan sarakkeen viimeinen arvo vastaa **View Integral** -tulosta."
- The folder id *taulukkolaskenta* no longer matches the content (GA Pro table); students never see it, so leave it, but the title is right.

## Checked

- Read guide.json, guide.md and the figure's labels in full; ran the hash. Menu names (Manual Entry, Sensor Data Collection, Column Options, Add Manual Column, Add Calculated Column, Data Set Options, Add New Data Set, Rename Data Set, Delete Column, Export data as csv) and expression syntax ("T"^2, sqrt, delta, sum, integral, no A/B parameters, radians, Pro for custom expressions) match the verified facts.
- Order works for a student alone: new experiment → name/unit → type data → keep raw data → calculated column → constants → delta/sum → integral → import → save/export. Each step says what to click and why.
- Goals match steps; mistakes are real ones (column name, paste not numeric, missing unit, degrees, overwriting raw data).
- Figure: table with measured and calculated columns, labelled *esimerkkiarvoja* / "keksityin esimerkkiarvoin"; 1,27² = 1,6129 correct and shown unrounded on purpose.
- Finnish grammatical around bold names ("valikosta **Data Set Options** valinnalla **Add New Data Set**"). Cross-links to mittausohjelma, nopeus-datasta, kuvaaja, suoran-sovitus sensible. No Excel/spreadsheet formula leftovers (no cell references, no =SUM).
