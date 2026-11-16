VERDICT: PASS
CONTENT-HASH: 0a743d1f79e88e55
SCOPE: delta added-exercise from 010cc9be0b649006 base 415cbc7c6bc3

## Blocking

## Polish
- exercises/solutions.md:183 — The rounding reason cites "noin $30\,\text{a}$", but b) and Annettu (line 174) fix $T_{1/2}$ as exactly $30\,\text{a}$. Say instead that the real half-life is about $30\,\text{a}$ (30,1 a gives 39,8 %), so two figures.
- exercises/solutions.md:176 — Periaate states as fact that Cs-137 "ei häviä ympäristöstä muuten kuin radioaktiivisesti hajoamalla". In mushrooms the concentration also falls as caesium sinks deeper in the soil, as c) itself says. Write "Tehtävän oletuksen mukaan …".

## Checked
- Hash 0a743d1f79e88e55 at the start and the end. Only fy8-9-L2-08 was judged.
- Recomputed: $(1/2)^{40/30} = 0{,}3969$, so 39,69 % and the box value 40 %. answers.py also gives 39,685. Tolerance 0,03 (relative) accepts 38,8–41,2 %, which covers 39,7 and 40.
- The table matches verified Table 9.2: Helsinki 14–413 Bq/kg (12 samples), Tampere 3,5–670 Bq/kg (13), Rovaniemi 76 Bq/kg (2). The caption names the source.
- The a) attributions (Chernobyl 1986, weapons tests of the 1950s–60s, the before/after-1986 split, the foods, the steady decrease) are all in the verified lines. The c) reasoning is marked as the solution's own, and only the Tampere fallout fact is attributed.
- d): $670 : 3{,}5 = 191$ is correct, and the sampling, species, small-sample and counting-statistics arguments are sound.
- The decay law is used with its condition stated in the task ("fysikaalista hajoamista lukuun ottamatta aine ei häviä"). The Järkevyys check (between 25 % and 50 %) is a real check.
