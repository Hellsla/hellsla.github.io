VERDICT: DONE

Unit fy12-energia, "Energia, teho ja hyötysuhde" (FY12 chapter 2, order 1). Developer report 2026-11-03.
Content hash at hand-over: d64ab1c8503f8cb7 (round 1; was 34d0e6d4b7d16344) (`python3 scripts/units.py hash fy12-energia`).

## Files
- `content/fi/units/fy12-energia/unit.json`: course FY12, chapter 2, order 1, kind review, 75 min, subjects physics; `sources` empty (no real statistics or facts that change are used).
- `content/fi/units/fy12-energia/unit.md`: Why question (EV charging vs ten litres of petrol), hero, `## Ydinajatus` (concept map), `## Kaava: Energia, teho ja hyötysuhde` (E_alussa = E_lopussa, P = ΔE/Δt, kWh by substitution, η = E_a/E_o = P_a/P_o, E_o = E_a + E_h, η = η1η2η3, E = Hm, W = Fs, W = mgh, each with symbols and conditions; Sankey figure), `## Yleisiä virheitä {Virheet}`, `## Kertaa tarvittaessa {Kertaa}` (chapter links). About 470 words.
- `content/fi/units/fy12-energia/inquiry.json`, `exit-ticket.json` (2 questions), `teacher.md`.
- `content/fi/units/fy12-energia/sovella/tasks.json`, `solutions.md`; `lessons/units/fy12-energia/sovella/answers.py`, `figures.py` (model graph of s3).
- `lessons/units/fy12-energia/figures.py`: `hero`, `kartta` (concept map), `ketju` (Sankey to scale, 500 MW plant).

## Counts (as the plan table)
- Pohdinta: 1 hook. Ennusta: 6 choice (diagnostic, each option names the chapter). Tutki: 1 interpret (reuses `fy3-15/chain-bars`, `source: example`, numeric question η2 = 43 %).
- Teoriatiivistelmä: 1 theory activity (4 sections).
- Sovella: 4 choice (kWh error-spotting, reading Sankey `fy2-4/grid`, CHP claim, charging power vs energy), 4 numeric (sauna 43 MJ, EV chain 51 kW, pellets 3,7 t, lift 8,4 kW), each with solution, ≤3 hints, mistakes.
- Tarkista: choice, numeric (phone 68 kJ), explain (CHP vs condensing); `practice` links on all three; exit ticket.
- Tehtävät: 6 tasks, 90 points: s1 Mökin aurinkosähkö (calc, 13), s2 Hakevoimala (calc, 15), s3 Pakkanen ja sähkölasku (data → graph → fit → interpret, 18), s4 Saaren sähkö (word, 13), s5 Vedenkeittimen hyötysuhde (experimental report critique + design, 14), s6 Kaivoksen pumppuvoimala (cross-module with FY4 mgh, 17).

## Numbers (computed in Python: answers.py, scratch generator for inquiry)
s1 1,54 kWh; 1,84 kWh (η 0,837). s2 P0 110,8 MW; η_s 27,1 %, η_kok 90,2 %; separate production 156,7 MW → 59,4 t/h. s3 fit k = −4,893 kWh/(vrk·°C), b = 92,79 kWh; read slope −4,9 → 204 W/K; E(−28 °C) 230 kWh; balance 16,5 °C. s4 wind 5,26 GWh/a, battery 1,7 h, diesel 2100 t CO2. s5 η 83,4 % (2100 W → 87 %, 1,05 kg → 88 %, 0,95 kg → 79 %, 100 °C → 88 %). s6 Ep 245,3 MWh; 36,0 MW; grid 288,5 MWh; η 74,8 %. Inquiry: chain 0,729; EV 50,76 kW; pellets 3,737 t; lift 8371 W; phone 67,5 kJ; Tutki 150/350 = 42,9 %.

## Checks
- `units.py figures fy12-energia`, `practice.py figures units/fy12-energia`: up to date. `practice.py check units/fy12-energia`: OK. `units.py check`: no errors for this unit.
- `build.py fy12-energia` writes `preview/fy12-energia.html`, then crashes in mixer.py (Shared issues). Because `preview/index.html` is then missing, `check_layout.py` falls back to site/; I ran it against preview with an unmodified copy whose OUT points at preview: 360 px OK (wide tables scroll); 1280 px only the teacher box (preview only) fails line length (Shared issues).
- Playwright (`_browser.launch`), 1280 and 390: every choice answered correctly with its feedback, every numeric answered ("Oikein."), explain model shown, all details/solutions opened: no console errors, no `.katex-error`, no raw `$`. Looked at hero, theory, Tutki, Sankey, concept map and s3 graph at 390 and 1280; fixed label overlaps and raised figure labels to 24 px (≥ 14 px at 390).

## Open questions
- No real Finnish statistics are used: stat.fi was not reachable from this session, so every dataset is marked as an invented example (`source: example`, `source_note`). A reviewer may want one real Tilastokeskus/Energiavirasto item with a checked date.
- Heating value of moist forest chips 9,5 MJ/kg and diesel emission factor 700 g/kWh are stated as typical/rounded example values.

## Shared issues
1. `scripts/mixer.py` `_entry`: `{own_module} | {…} - {None}` subtracts None only from the skills set; for unit tasks own_module is None and the sort key crashes (`TypeError: 'NoneType' object is not subscriptable`). Fix: `({own_module} | {…}) - {None}`. This breaks `build.py <unit>` after the unit page is written, and so no `preview/index.html` gets written.
2. No `assets/units/fy12/units.css`: FY14's `units.css` limits `.unit-teacher` (and credits/sources) to `--measure`. Without it, the teacher box on FY12 previews is 1152 px wide, and `check_layout.py --width 1280` fails on line length.

## Round 1
Visual Blocking:
- The s1 table now has three short columns (Laite | Teho | Käyttö/vrk), with the fridge note below it. The s4 table has two columns (Vaihtoehto | Teho), and the other facts are three bullets under it. At 390 px every column shows: table width ≤ container.
- `kartta` is redrawn 380 px wide and stacked vertically: hub, a spine, three boxes of laws, a grey word beside each, and slash fractions. `ketju` is redrawn 420 px wide, with η above the bounds, stage names in a key under the figure, "häviöt:" on the row of loss values, and losses in grey. Labels render at about 17–20 px at 390.

Polish:
- Science items 1–6: the s1a line now reads 1,54 · 3,6 MJ. In s5b, the late reading lowers the result and the nameplate power can shift it either way; the rubric detail now gives directions. The s3b check is (191 − 12) kWh : 24 h ≈ 7,5 kW. The s3b range is 192–216 W/K in both the rubric and Hyväksytään. `lataus` now says the power stays constant.
- The Tutki bars are now a unit-drawn bar chart (`tehot` in figures.py, pasted into the inquiry text by running figures.py), with the same data as fy3-15/chain-bars in sand and green. The Sankey and the map hub no longer use orange.
- Text: all straight quotes are now ”…”. The kWh conversion is a display formula. E = Hm now states its condition. Unit fractions in solutions and tasks are inline (kg/m³, J/(kg · K)). The circled s3 points are explained in a caption and in the alt text.
- `yhteistuotanto` is now a heat-pump claim, so tarkistus-3 is no longer a repeat. `lataus` uses e-bike numbers. lt-3 distractors are longer, and the correct option has moved in `virhe-kwh` and `kuvio`. The Tutki text asks only for η₂. The hook is answered at the end of Ydinajatus. The teacher plan now has only parts a–b of a long task in class. fy1-4 was added to the s5 skills and fy2-1 to the s6 skills.

Checks: practice.py check OK; units.py check finds 33 units OK; build OK; check_layout passes at 360, 390 and 1280. In Playwright, every item is answered correctly, with no console errors, no katex errors and no raw `$`. Figures and tables were looked at at 390 px.
