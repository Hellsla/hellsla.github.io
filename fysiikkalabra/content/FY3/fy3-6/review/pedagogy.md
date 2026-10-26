VERDICT: PASS
CONTENT-HASH: a38128ef6919c113

## Blocking
(none)

## Polish
- sim.js canvas texts (T (°C), t (s), "vesi 20,0 °C", "T 24,6 °C") and the DOM readout (C = cm, Q, "Lämpömittarit nyt") are plain interface text, not typeset maths; NOTES.md §1 records this as pending the teacher's decision, so polish only.
- lesson.md Ydinajatus, 1st paragraph — one dense block of ~9 sentences before the first figure — split after "lämpömäärä riippuu aineesta" and place the water-sand figure beside the second paragraph.
- lesson.md Esimerkki, "Järkevyys" stage — four ideas in one stage (copper comparison, sim rerun, 0,1 K gap, heat-capacity ratio) — move the heat-capacity comparison into its own short stage.
- Experiment tables at 390 px: the Mittaukset table is narrow and its header row is small (aine, c / T (°C) / C (J/K)); legible, but a wider table would help once rows accumulate.
- inquiry.json "kertaus" — the "kylmyys siirtyy" distractor has no link to today's topic; low priority.

## Checked
- Learning path unchanged since round 1: hook, retrieval, two predictions, sim and two experiments, theory, reflection, example, error-spotting, transfer, checks, exit ticket. Goals covered, nothing extra; opening question answered only after commitment.
- New Nopeus control (390 and 1280 px captures): labelled, sits with the other controls, and the howto says it changes only the animation's pace, not temperatures or heat amounts, so it cannot mislead.
- New Lisätietoja boxes (Käyttöohje, Mallin oletukset, Laskennan selitys): closed by default, readable, no clipping at 390 px; the model box states the simplifications and that values are model values.
- Activity texts now carry symbols as maths (m_v, T_v, c_k, T in howto and calc); consistent with the prose.
- Experiment Alkutila line and table headers render symbols as maths (c, T (°C), C (J/K)); koe-1 and koe-2 still lock the controlled parameters and can refute their predictions (hiekka 26,8 vs vesi 44,0 °C; 40,0 / 55,0 / 63,1 °C).
- Figures, exercises, solutions in LaTeX, exit ticket and Finnish unchanged from round 1 (PASS); numeric answers recomputed then.
- Layout: 1280 px lab shows experiments beside the sim, readable; 390 px sim nothing clipped.
