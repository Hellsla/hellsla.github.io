VERDICT: PASS
CONTENT-HASH: eaff5be82b3b554c

## Blocking
(none)

## Polish
1. inquiry.json, `johtopaatos` criteria[2] — asks the student to say that the petrol engine's losses are large and heat, but the question and the model answer are about koe 2 (lamp), `after` is only koe-2, and koe-1 is optional; a student who skipped it cannot meet the criterion — replace with a lamp criterion (e.g. "Sanoin, että loput 95 % oli häviöitä, pääosin lämpöä") or drop it.
2. inquiry.json, `koe-1` — varies only t, while ennuste-1 asks about the size of eta; the sim returns the typed-in model value (disclosed honestly in intro and feedback), so the experiment illustrates the prediction rather than testing it. Optional, so acceptable; a better design would compare several devices at one fixed time.
3. inquiry.json, `ennuste-2` / `koe-2` — the model fixes eta, so the "eta decreases" option can only be refuted by the calculation, which the feedback says openly. Fine for the core path; consider having ennuste-2 ask the student to predict the ratio E_a:E_o as a number.
4. lesson.md:126 — the paragraph under "Hyötysuhde kertoo hyödyn osuuden" is about 125 words and holds three ideas (limit 100 %, real devices, heater); split it at "Sähkölämmittimessä hyöty on itse lämpö".
5. lesson.md:185 — the 4,0 cm / 5,0 cm arrow example is an invented extra that does not match the lamp figures; use the 5 % / 30 % arrows of the figure above so the student reads it from the picture.

## Checked
- Path: prior (fy2-3, E = Pt) retrieved with the lamp from the hook; the opening question is answered in Ydinajatus and "Kahden lampun vertailu" only after the student commits.
- Slot goal eta = E_a/E_o = P_a/P_o with derivation that time cancels; no chains, no FY3 content.
- Core path is light (one prediction, key experiment, explain, two checks); an hour's work.
- Figures (3 theory figures, 390 px captures): arrow widths to scale, green/orange with text labels, legible; the pair figure supports the lamp comparison and does not hide the answer.
- Simulation (1280 px capture): lead short, Käyttöohje/Mallin oletukset/Laskennan selitys closed, readout in LaTeX, model values named as such.
- Worked example: seven stages, symbolic first, conversions, sanity check; differs from the exercise set in context.
- Misconception feedback: energy lost, power vs efficiency, heater heat as benefit, inverted ratio; each repairs rather than restates.
- Etsi virhe, siirto (panel) and numeric mistakes are specific; exit ticket tests the core idea (calculation, power form, power is not efficiency).
- Finnish: terms match glossary (hyötysuhde, hyötyenergia, häviöt); no case slips found.
- Exercises not judged (reviewed apart).
