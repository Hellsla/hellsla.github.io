VERDICT: FAIL
CONTENT-HASH: 311b8a552540fc24

## Blocking
- inquiry.json hook (and lesson.md hero, `aria-label`) — the hook says the biggest source is "näkymätön ja hajuton kaasu, joka nousee kallioperästä kotien kellareihin", and the hero shows radon rising into the house. That answers ennuste-3 ("Mistä lähteestä ... suurimman osan") and the opening question before the student has committed to anything; ennuste-3 then only repeats it and no experiment can refute it. — Fix: let the hook state only the 5,9 mSv average and that nuclear power and X-rays are small, and ask where the rest comes from; drop the gas description (and the "Miksi" blockquote's implied answer) or move it behind the prediction's reveal. Keep the hero neutral until the reveal, or make ennuste-3 a real choice between plausible sources by removing the clues.

## Polish
- inquiry.json hook — "työntekijä ... saa pienemmän annoksen kuin moni saa kotonaan kuukaudessa" is an unsupported claim with no number; either give figures (annosnopeus, aika) or drop it.
- inquiry.json ennuste-2 — the prompt already gives 40 -> 20 for 6 mm, so the pattern is almost handed over; a prediction at a non-multiple (e.g. 9 mm) would be more arguable.
- inquiry.json pohdi/tarkistus-3 are optional; tarkistus-3 (radon explanation) is the only check on the lesson's main idea, so keep it non-optional.
- lesson.md Esimerkki — covers only dose weighting; distance, time and shielding (two of three goals) are practised only in "siirto" and the exercises. Acceptable, but mention in the example's Järkevyys that the next task uses the other tools.
- lesson.md, section "Mistä suomalaisen säteilyannos tulee" — the table and the bar chart (lahteet) carry the same data; fine for access, but say once that the chart shows the table.

## Checked
- Packet: course goals, slot, glossary, checks, full lesson text, inquiry.json (all activities).
- Hash at start and end: 311b8a552540fc24.
- Captures: sim-390 (controls, readout and the three boxes OK, legible at 390 px), fig-1-390 (hero: clear, uncluttered, colour not alone), fig-12-390 (graph for tarkistus-2: axes, units and grid legible; answer 5 cm not given away).
- Experiments koe-1/koe-2 can refute their predictions (values 40/10/2,5 and 40/20/10/5 differ from the wrong options).
- Finnish, term use and levels: no blocking problems; staged example, Etsi virhe and siirto (3 hints, mistakes) are sound.
