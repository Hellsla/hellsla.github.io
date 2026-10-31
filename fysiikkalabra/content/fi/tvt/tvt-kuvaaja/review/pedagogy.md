VERDICT: PASS
CONTENT-HASH: 13d584b07162e849

## Blocking

None.

## Polish

- Step 5: error bars are a goal ("merkitsemään kuvaajaan mittausten epävarmuuden") but the guide can only say "kysy opettajalta, jos et löydä asetusta". Fine while the menu path is unverified; once Lauri confirms where GA Pro sets error bars (and that the student enters the value Δy per point or per column), add that path here and in tvt-epavarmuus.
- Step 1 assumes the data is already in GA Pro. One clause pointing to tvt-taulukkolaskenta / tvt-mittausohjelma for getting the data in would help a student who opens this guide first (it is order 1).
- Step 6: **Graph Legend** is under **Graph Tools**; saying so (as step 3 does for **Edit Graph Options**) saves a search.
- The good/bad comparison paragraph sits inside step 5 but illustrates steps 1–5; a short lead-in or moving it after step 5 would make that clearer.

## Checked

- Read guide.json, guide.md and the figure's labels/aria-label in full; ran the hash. All bold menu names (Column Options, Graph Tools, Edit Graph Options, Automatic, Always Show 0, Manual, Zoom to all Data, Points, Lines, Both, Point Symbols, Plot Manager, Graph Legend, Export graph as png) are in the verified GA facts.
- Steps in a workable order: axes (click axis label to choose column) → names/units (Column Options) → scale → Points → error bars → several series → title and PNG export. Each step says what to click and why (e.g. why not a polyline, when to show zero).
- Finnish around English names reads correctly ("valinnassa **Column Options**", "**Plot Manager** -näkymässä", "Graphical Analysis Prolle").
- Goals match steps 1–5; checklist covers units, scales, points, error bars and caption. Mistakes are real ones (missing units, polyline, wrong column, T vs T², axes swapped for the model, bad scale), each with symptom and fix.
- Figure contrasts exactly the listed mistakes; data labelled *esimerkkiaineisto* / "keksitystä esimerkkiaineistosta". Units in LaTeX ($l\ (\text{m})$, $T^2\ (\text{s}^2)$, 60–80 °C).
- Cross-links to suoran-sovitus, kulmakerroin, taulukkolaskenta, epavarmuus, tyoselostus are where the next step needs them. Investigation titles named in the text exist. No spreadsheet/Excel/Tracker leftovers.
