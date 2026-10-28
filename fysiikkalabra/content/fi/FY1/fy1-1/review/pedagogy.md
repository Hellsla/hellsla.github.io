VERDICT: PASS
CONTENT-HASH: f4e6eeab469a347c

## Blocking
- none.

## Polish
- inquiry.json (whole core path) — workload: my estimate for the non-optional path is 75–90 min (2 predictions, 2 experiments with 7 table rows, Miksi koot on saatu selville, about 1100 words and 8 figures of theory, reflect, a 7-stage example, 2 Sovella items, level 1 with 5 exercises, 2 checks, 3 exit questions). That is about a third over one lesson. Cheapest cuts: make `reflect` and exp-2's `question` optional (exp-2's rows still reveal pred-2), and have `tunnista` or `vuorovaikutukset` carry the "Sovella" load, not both. Do not cut Ennusta, exp-1 or the example.
- inquiry.json:15 hook — the opening question has three parts and the core path never answers the third ("kuinka monta kymmenpotenssia pienimmän ja suurimman koon välillä"). Only optional exp-3 computes -35…27. Add one line to `reflect` or to Ydinajatus: protoni–maailmankaikkeus ≈ 42 kymmenpotenssia, Planck–maailmankaikkeus ≈ 62.
- inquiry.json:356 vuorovaikutukset — items 1, 2 and 4 are exactly the examples in the theory text (Maa–Aurinko, ilmapallo ja paperi, beetahajoaminen), so the task is recall, not transfer. Replace 2 and 4 with new phenomena (e.g. "kompassin neula kääntyy", "Aurinko puristaa vetyä heliumiksi"), keeping 3 (heliumydin).
- inquiry.json:116 sim `model` — "…havainnollistuksia. ja ytimien, atomien ja Kuun…" has a stray full stop and a lowercase start; fix: "…havainnollistuksia. Ytimien, atomien sekä Kuun ja Jupiterin koot ovat pyöristettyjä taulukkoarvoja." Also `learn` (line 4) has no goal for slot goal 1 (fysiikka mallintavana, kokeisiin nojautuvana tieteenä): e.g. "Osaat selittää, miksi malli testataan mittauksella."
- exercises.json:28 L1-04 — same method, nearly same context as the worked example (atom/nucleus ratio); swap for a non-atomic pair (e.g. hius/virus) so the example is not repeated.

## Checked
- Learning path follows Pohdinta → Ennusta → Tutki → Teoriatiivistelmä → Sovella → Tarkista; prerequisites suffice; slot goals covered, no quantum/particle classification/cosmology maths.
- pred-1 and pred-2 are arguable before evidence; each wrong option's feedback repairs its misconception; both can be refuted by the table rows (n values), none disclosed before commitment.
- Sim at 390 and 1280 px: readable, labels in LaTeX, text in closed boxes; experiments' rows (L, n) match the intro.
- Figures 2–8 at 390 px: legible, labelled "ei mittakaavassa" where needed, colour not alone; each follows its paragraph; no paragraph over about 120 words.
- Example has seven stages, one step each; solutions in exercises and tasks are complete and numerically right (spot-checked L2-01, L2-04, L3-01, check-2).
- Physics facts checked: Sgr A* horizon 2,5·10^10 m, neutron star 20–25 km, 93 mrd ly, Neptune 10^13 m.
- Finnish: glossary terms used; no case errors after number+unit found.
- Exit ticket tests the core idea (suuruusluokkaero, malli-testi, vahva vuorovaikutus).
- Hash at start f4e6eeab469a347c; at end re-checked below.
