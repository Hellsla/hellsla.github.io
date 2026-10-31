VERDICT: FAIL
CONTENT-HASH: 5e3d91121ea79e92

## Blocking
- lesson goals ("Tällä tunnilla opit", first screen at 390 px, inquiry.json `learn`[0]) — states the answer to the opening question and to pred-1 before the student commits: "selittämään, miksi samassa paineessa, tilavuudessa ja lämpötilassa kaikissa kaasuissa on yhtä monta moolia" — reword without the result, e.g. "päättelemään, mitä paine, tilavuus ja lämpötila kertovat kaasun määrästä, ja selittämään, miksi kaasut painavat eri verran".

## Polish
- inquiry.json check-2 solution "Periaate" — "pV = NkT" uses k, which the lesson never introduces; a student cannot follow it — write "tilanyhtälön mukaan p ∝ NT/V (pV = nRT, n ∝ N)".
- lesson.md Ydinajatus, "mikromalli" paragraph — "kelvinlämpötila on suoraan verrannollinen hiukkasten keskimääräiseen liike-energiaan": E_k is FY4 scope (CLAUDE.md FY3 scope) — say "kelvinlämpötila kuvaa hiukkasten liikkeen keskimääräistä voimakkuutta: mitä korkeampi lämpötila, sitä nopeammin hiukkaset liikkuvat".
- inquiry.json punnitus text — the mole and "m/M" are used before the theory defines n = m/M; the task says only "laske m/M" with no reason — add one sentence: "Moolimassa kertoo yhden moolin massan, joten m/M kertoo, montako moolia kaasua pallossa on."
- sim first load (capture #2): "Mitattu paine = 1,35 (keskiarvo 0,0 s:n ajalta)" reads as a measurement of an unaveraged moment and misleads at the reference state — show "–" until the averaging window has data.
- Figures: hero (#3) shows blue and yellow balloons without labels, and fig 5 (hot-air balloon, end of Tiivistelmä) teaches nothing — label "helium"/"ilma" in the hero or drop fig 5. Workload: Tutki holds nine items before theory (about 1.3 lessons); consider making taulukko optional.

## Checked
- Path: Boyle retrieval → prediction → weighing → emergent-pressure sim → R from data → theory; prerequisites sufficient; slot goals met without extras.
- pred-n can be refuted by exp-1 (T, V locked, reveal min 2); each option's feedback repairs its misconception; pred-1 feedback is distinct per option.
- exp-2 forces T-dependence from the student's own row N = 100 (p doubles), answer 50 is reachable; mistakes 200/71/25 are real.
- Numbers verified: m/M values, R ≈ 8,3, taulukko pV/(NT) column, check-2 3,0, siirto 2640 kg, exit ticket 0,601 mol, virhe 1,2 mol.
- Solutions step through given/principle/formula/units/substitution/sanity; significant figures stated.
- Check 2 (Kelvin) and Etsi virhe test real misconceptions (Celsius, units).
- Finnish: no grammar errors found; case after number+unit correct.
- Phone: sim, controls, locked sliders ("vakio") and experiment tables readable at 390 px; 1280 px lab layout has sim beside experiments, single reading column.
- Exit ticket tests the slot skill (solve n from pV = nRT, Kelvin conversion).
