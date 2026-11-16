VERDICT: FAIL
CONTENT-HASH: 448904a798abd326

## Blocking
- solutions.md:208–209 (fy6-9-L2-09, Kohta d) — the model answer attributes specific claims to the Tukes page, and nobody has checked them against it (the page could not be opened). The claims are: "Ohjeiden mukaan akku ladataan vain sen omalla tai laitteelle varmasti sopivalla laturilla"; "ohjeiden mukaan akkua ei pidä ladata yöllä eikä silloin, kun kotona ei ole ketään, ja akku ladataan palamattomalla alustalla"; "Ohjeiden mukaan viallinen laturi tai akku voi aiheuttaa palon … paloa on hyvin vaikea sammuttaa"; "Muita ohjeita ovat, että kylmää akkua ei ladata, koska se vaurioittaa akkua, ja että akkua ei pidetä jatkuvasti latauksessa". The last one also gives the source as the cause ("koska se vaurioittaa"). Class A: a claim with no checked basis is presented as the source's words. — Fix: check each instruction on the page and keep only those it states. Otherwise reword them as examples of typical instructions the student may find ("esimerkiksi ohje ladata akku vain sille tarkoitetulla laturilla…"), with the physics kept as the solution's own reasoning. Drop the unchecked reason "koska se vaurioittaa akkua", or explain it as physics.

## Polish
- solutions.md:207 (fy6-9-L2-09, Kohta c) — the task says the charger delivers 120 W *into the battery*, so the losses that lengthen the charge are those in R_s (and the drop in power). The charger's and wires' R lie before that point. Naming R_s alone, or saying "laturin ottama teho", would keep the two consistent.

## Checked
- One independent script recomputed all 19 numeric answers and compared them with exercises.json (L1-05 is read from the figure, 4,0 Ah, as answers.py has it): all are inside tolerance.
- L2-09: W = UQ = 36 V · 14 Ah = 504 Wh = 1,81 MJ; t = UQ/P = 4,2 h, solved symbolically. The cross-check through I = P/U is a real check. Two significant figures are justified.
- L2-09 c): the mechanisms match the brief. They are RI² losses with only EI stored, and E rising so that I = (U_lat − E)/(R + R_s) falls, plus the Li-ion charger's voltage limit and taper (the brief's Tiivistelmä).
- L2-09 d), physics: a slightly high charger voltage gives a large I because R_s is small; R_sI² quadruples when I doubles; an internal short releases the stored energy as internal energy. All of this is correct and presented as physics, not as the source's words. The safety wording ("jos se onnistuu turvallisesti") is not unsafe.
- Reflowed chains (L2-08, L3-04, L3-05): same numbers, signs and units in the same order.
- Notation (W, E as source voltage, R_s, U_lat) matches the brief. Everything is within FY6 scope (akut ja latauspiiri).
- Hash read at start and end: unchanged.
