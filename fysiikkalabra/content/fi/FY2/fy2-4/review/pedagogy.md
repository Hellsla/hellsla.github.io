VERDICT: PASS
CONTENT-HASH: 9afe1413fb973d68

## Blocking

## Polish
1. inquiry.json ennuste-2 / koe-2 (and feedback "Simulaation malli kumoaa tämän") — the sim has constant η by construction, so the experiment cannot test the claim "lamppu kuumenee, hyötysuhde pienenee"; it only returns the assumption. A student who reasons physically is "refuted" by program arithmetic. Keep the item, but let the feedback say that the model assumes constant η and that the reason is E = P · t (aika supistuu), not that the simulation shows it. Ennuste-1 likewise returns the table's 25 %; fine as a guess to correct, but say so ("mallin arvo").
2. lesson.md:126 (and every solution) — "sijoittamalla 1 = 100 %" reads as a false equation to a 16-year-old. Fix: "Suhdeluku muutetaan prosenteiksi kertomalla se luvulla 100 %, esimerkiksi 0,30 · 100 % = 30 %."
3. Simulation canvas — labels (hehkulamppu, sähkö, P_o, η) are about 11 px at 390 and 1280 px, clearly smaller than the 17 px text under it; enlarge them toward print size, since the arrows have room.
4. Workload — hook, retrieval, two predictions, two three-row experiments, conclusion, Etsi virhe, transfer, 12 exercises, three checks and exit ticket is more than an hour for weaker students. Mark ennuste-2/koe-2 (or the conclusion's second half) optional; the core path stays ennuste-1, koe-1, johtopäätös.
5. inquiry.json ennuste-1 — nothing before the evidence lets a student argue the percentage (no clue besides "moottori kuumenee"). Add one hint to the prompt that links back to the hot lamp of Pohdinta, e.g. "Kuumenevatko moottori ja pakoputki?"

## Checked
- Path: Pohdinta question (where does 60 W go, how to measure goodness) is answered by Ydinajatus plus the pair figure; prerequisite retrieval is the right one (E = P · t); no FY3 content (no chain, no heat engine).
- Figures 1 and 2 are print quality at 390 px, labels LaTeX, colour plus text (valo/lämpö), arrow widths to scale, right after the paragraph; at 1280 figure 1 sits beside its paragraph.
- No text wall; subsections short; table fits 360 px with η header.
- Worked example: seven stages, one step each, symbols before numbers, units, sig-figure reason, double check.
- Sim at 390 and 1280: controls clear, readout understandable, three explanation boxes closed; at 1280 the sticky card scrolls inside (max-height 816 px), so Laskennan selitys is reachable.
- Experiments lock and vary one quantity; reveal after 3 rows; mistakes feedback repairs (osuus väärin päin, 0,25 vs 25 %).
- Etsi virhe and transfer task (panel, MJ to W) have progressive hints and model solutions.
- Finnish: glossary terms hyötysuhde, hyötyenergia, häviöt used consistently; chapter names not ids; case forms correct.
- Exit ticket tests the core idea (share, P vs η, loss is not vanishing).
- Hash unchanged at end: 9afe1413fb973d68.
