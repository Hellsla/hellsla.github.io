VERDICT: DONE
Round 1 fix.
- inquiry.json: new Tutki item `data-viikko` (an invented, rounded winter week of consumption, nuclear and wind as daily mean powers, wind's nominal power about $8\,\text{GW}$, labelled as an example) with a numeric task (other sources on Thursday, $9{,}9\,\text{GW}$) and a complete solution, before the conclusion; the conclusion's prompt, model and criterion now use it. data-fi: "muut lähteet 0,8" row instead of "rounding"; answer $2{,}31\,\text{GW}$ with three figures; 2306 feedback says MW only. Virhe: "kymmeniä kertoja koko maailman voimaloiden keskiteho". Quantities in LaTeX (ennuste-1, data-yksikko table, siirto, tarkistus-3), conversions by substitution (data-fi, siirto, tarkistus-2). tarkistus-3 (criteria comparison) is on the core path now.
- lesson.md: blank line before the criteria list; clearer Kuljetettavuus; "kapasiteettikerroin" dropped; LaTeX $80\,\text{TWh}$ and $5\,\text{MW}$; the group table shortened so all columns show at 360 px; the log-scale text no longer speaks of a "ruutu".
- figures.py: plants redrawn (reactor vs boiler, generator G, solar without G, grey resource arrows, dark electricity arrows, labelled orange heat arrows); unit-power uses dots instead of bars; fi-bars aria says two fifths.
- lesson-answers.py: the new numbers (muut, week, world mean power ratio 36).
- exit-ticket.json: conversion by substitution.
Not fixable here: the source-note pill (shared component).
