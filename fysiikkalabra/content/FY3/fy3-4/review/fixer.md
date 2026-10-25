VERDICT: DONE

Round 1 fixes for fy3-4. Proofreader diff was empty, nothing to apply.

## Blocking
1. mathematician 1 (lesson.md SVG p axis not linear): one scale, about 1 px/kPa from y = 250. p₀ = 101 kPa now at y = 150 (line start, dashed line, circle, label "101" at y = 157); 199 kPa stays at y = 52.
2. web-designer 1 (SVG "10" and "h (m)" overlap): "h (m)" moved above the axis end (x = 575, y = 238, end-anchored).
3. web-designer 2 (SVG "p = p₀ + ρgh" crossed by the line): label moved under the line, between it and the dashed p₀ line (x = 310, y = 132). "ilmanpaine p₀" moved below the dashed line (y = 178). This also covers mathematician polish 1 and 2.
4. web-designer 3 (sim: "101 kPa" reading on top of the grey p₀ label at h = 0): sim.js works out the reading's position and box first. The p₀ label then goes to the right end of the dashed line (below it, else above, else one line higher) when h ≤ 10 m, and to the left end below the line when h > 10 m, so it stays clear of the reading and the red guide lines. Near h = 0 the reading sits just under the dashed line, so no line crosses it.
5. web-designer 4 (sim: "0 kPa" over the x tick labels with "Näytä vain ylipaine" at h = 0): the reading's baseline stays above the h axis. The label moves right until the rising line clears its top edge.
   I checked items 4 and 5 with canvas screenshots at 390, 360 and 1280 px: h = 0 with both checkbox states, h = 1, 2, 3 and 4 m, ρ = 700 and 1300, h = 12 and 18 m. No text overlaps.
6. editor 1 (dam hook never answered): I added a closing paragraph at the end of Ydinajatus. Air pressure acts on both sides of the wall, so only the overpressure loads it. The overpressure is zero at the top and about 290 kPa at 30 m (294 300 Pa), which means about 290 kN on each m² of wall, so the base must be thick. This also covers educator 1.

## Polish applied
7. physics-expert 2: the example now reads F = ρgh·A = 117,72 kPa · 0,015 m² ≈ 1,8 kN.
8. physics-expert 3: "padon pystysuoraan seinään", and "sukeltajan kehoon joka puolelta" replaces the eardrum.
9. physics-expert 4: the derivation now says "Levossa olevassa nesteessä". Line 10 says it too.
10. mathematician 3: the example rounds only at the end: ρgh = 117 720 Pa = 117,72 kPa, then 101 kPa + 117,72 kPa ≈ 219 kPa.
11. mathematician 4 and editor: the misconception paragraph now says "pelkkä ρgh antaa vain ylipaineen".
12. mathematician 5 and editor (p_h never named): line 25 now names the overpressure Δp = p − p₀, and solutions.md uses Δp in place of p_h everywhere (L1-02, L1-05, L2-02, L2-03, L3-03). L3-02 already used Δp.
13. educator 2 (reason for sideways pressure): added "Jos paine sivulle olisi pienempi kuin alaspäin, vesi valuisi sivuun eikä pysyisi levossa", plus the bottle with the lowest side hole spurting hardest. I wrote "voimakkaimmin", not "kauimmas", because the range of the jet also depends on the outlet's height.
14. educator 3: the derivation names V = Ah and m = ρV, then G = mg = ρAhg.
15. editor polish (diver line 51) and proofreader polish: "vaikka ikkuna on pieni". The body is not crushed because the pressure acts on it from every side and the body fluids carry it inside; only air spaces such as the ears need equalising.
16. educator 5: added "ylipaine" to glossary.json (two Finnish sentences) and to the meta.json glossary list.
17. tester 1 and 2: added the slider-range assertion and the "Kuolleenmeren vesi" label assertion to tests/sims/fy3-4.json (28 assertions now).
18. web-designer polish: the chart's "h (m)" title is drawn 8 px left of the h = 20 m guide line.

## Not applied
- editor polish (rebuild L2-03 around slope and intercept): this would rewrite the task, its answer, answers.py and the solution, and the single-answer format needs two outputs (ρ and p₀). The instruction was to skip it unless quick, so I skipped it. No numbers changed, so answers.py is untouched.
- educator 4 (L2-04 too heavy for level 2): this is a judgement on difficulty and was not in the requested list. Left for the reviewers.
- tester 3 (optional readout check at h = 8 m): optional, and slope and readout are already asserted elsewhere.
- web-designer polish (the controls row wraps at 1280 px): this is controls/CSS layout, not a defect. Not changed.
- web-designer polish (31–34 character column at 390 px): template property, not fixable here.

## Checks
lint_lesson.py fy3-4: 0 errors, 0 warnings. check_latex.py: all LaTeX ok (8 fragments). build.py --all: fy3-4 built. test_sims.py fy3-4: PASS with no errors. answers.py output unchanged.

## Files changed
content/FY3/fy3-4/lesson.md, content/FY3/fy3-4/solutions.md, content/FY3/fy3-4/sim.js, content/FY3/fy3-4/meta.json (glossary only), glossary.json, tests/sims/fy3-4.json.

Stale reviewers to run again: tester, physics-expert, mathematician, educator, proofreader, editor, web-designer (all seven, per `gate.py fy3-4`).
