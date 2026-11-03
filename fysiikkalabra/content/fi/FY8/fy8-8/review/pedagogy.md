VERDICT: FAIL
CONTENT-HASH: c43174dd158bac10
## Blocking
- inquiry.json activity `gammaspektri` (interpret, figure `fy8-8/spectrum`) — the figure is not needed to answer: the text already gives both peak energies (`1173,2 keV` and `1332,5 keV`) and the question only asks to add them, so the student never reads the spectrum — remove the two numbers from the text and let the labelled peaks (and the figure description) be the only source; keep "peräkkäin".
## Polish
- inquiry.json `ennuste-2` prompt — "ydin jää yhtä raskaaksi kuin ennen lähes kokonaan" gives away that $A$ stays and removes a distractor before the student commits — delete the clause.
- inquiry.json `johtopaatos` / `koe-1` — the prompt and criterion ask where the series ends (Pb-206, 8 alpha, 6 beta), but the experiment requires only rows $k = 0$–$5$ — add "kirjaa myös vaihe $14$" to the intro of `koe-1`.
- lesson.md "Ytimen energiatasot ja gammaspektri" — "Ero on mittakaavassa." is unclear, and "kymmeniä keV … satojatuhansia kertoja" does not match (tens of keV is about $10^4$ times an eV) — "Mittakaava on aivan toinen: atomin siirtymät ovat elektronivoltteja, ytimen satoja keV tai MeV, eli tuhansia tai satojatuhansia kertoja enemmän."
- inquiry.json `tarkistus-1`, second option feedback — "Fotoni ei ole hiukkanen, joka sisältäisi protonin" can be read as "photon is not a particle" — "Fotoni ei sisällä nukleoneja: sen massaluku ja varaus ovat nolla."
## Checked
- Learning path: hook, retrieval, two predictions, series, spectrum, theory, staged Cs-137 example, transfer, checks; the hook's gamma half is answered in theory and revisited in `pohdi`.
- Example: seven stages, one step each; unit conversion and sanity check separate.
- Figures (hero, isotopes, chart, decays, levels, shifts) legible in captures, each beside its paragraph.
- Simulation at 390 and 1280 px: chart, readout and legend readable, controls usable.
- Experiment: rows $k=0$–$5$ show alpha and beta steps; consecutive rows let the student compute the changes; predictions can be refuted by the data.
- Option feedback repairs misconceptions (electron in nucleus, gamma changing the element).
- Exit ticket tests the equation and the isotope idea.
- Workload about one lesson plus 12 exercises; optional items trimmed.
- Finnish: no case or glossary errors found beyond the polish above.
