VERDICT: DONE

Round 2 fixes for fy3-6. The proofreader's diff was empty, so there was nothing to apply. No number and no step of the mathematics changed; answers.py is unchanged.

## Blocking

1. **web-designer, lesson.md:15 (ΔT definition, 343 px at 360).** The display is now an `aligned` block with two rows, `Q = cmΔT` and `ΔT = T_loppu − T_alku`, aligned at `=`.
2. **web-designer, lesson.md:33-36 (solving for T, 345 px at 360).** Each equation now has its left side alone on one row and `= …` indented on the next row. All rows sit in one left-aligned column, because a plain `\\ &=` break keeps the block as wide as before: the column widths still add up. A 6 pt gap separates the two equations. The educator's middle row is included, see 7.
3. **web-designer, lesson.md:81 (worked example balance, 449 px).** Split the same way. The left side is on row 1 and `= 4190 J/(kg·K) · 0,300 kg · 4,5 K` is on row 2.
4. **web-designer, lesson.md:85 (worked example result, 461 px).** This is now an `aligned` block with three rows: `c_metalli = 5656,5 J / (0,200 kg · 75,5 K)`, then `= 374,6 J/(kg·K)`, then `≈ 3,7 · 10² J/(kg·K)`.
5. **web-designer, lesson.md:92-97 (35 °C working, 383 px).** The first equation is split over two rows as in 2. The remaining rows are `80 °C − T = 3T − 60 °C`, `140 °C = 4T` and `T = 35 °C`, all left-aligned. The order of the sides follows 6.

`check_layout.py fy3-6` prints OK at 360 px and at 390 px. I also checked each display in screenshots at 360 px; they are in the scratchpad, not the repo.

## Polish applied

6. **mathematician, lesson.md:93 (hot side on the left).** The working now starts `1,0 kg · (80 °C − T) = 3,0 kg · (T − 20 °C)`, as the mathematician suggested. The text says that the hot water is on the left, as in the general equation.
7. **educator, lesson.md:34-35 (two moves in one step).** Added the middle row `c₁m₁T₁ + c₂m₂T₂ = c₁m₁T + c₂m₂T` before the factored row `= (c₁m₁ + c₂m₂)T`.
8. **mathematician and editor, lesson.md:99 ("ja sulut on kerrottu auki").** The sentence now reads: "Kolmannella rivillä yhtälö on jaettu puolittain kilogrammalla ja sulut on kerrottu auki." It says "kolmannella" because the first equation now takes two rows.
9. **educator, lesson.md:42 and 99 (link to the weighted mean).** Added this sentence after the 35 °C working: "Sama tulos saadaan painotetulla keskiarvolla: T = (3,0 kg · 20 °C + 1,0 kg · 80 °C) / 4,0 kg = 35 °C." It is plain text, so the formula is not displayed a second time.
10. **educator and editor, lesson.md:87 (long paragraph).** Split after "ilmaan.". The heat-capacity comparison ("Huomaa myös, …") is now its own short paragraph.
11. **physics-expert and educator, lesson.md:87 (cause of the 0,1 K gap).** The sentence now says the gap "selittyy lukematarkkuudella tai sillä, että todellisuudessa osa lämmöstä siirtyi myös kalorimetrin astiaan ja ilmaan". The word "todellisuudessa" answers the educator's point that the example itself sets losses aside.
12. **educator, lesson.md:81, 85 (`c_\text{m}` looks like mass).** Renamed it to `c_\text{metalli}`.
13. **mathematician, solutions.md:53 (L2-02 without ΔT).** Added "ΔT = 95 °C − 15 °C = 80 K." before Q.
14. **physics-expert, solutions.md:87 (L3-02 upper limit).** Added: "Tulos on yläraja: todellinen nousu on pienempi, koska osa energiasta kuluu haihtumiseen ja säteilee yöllä pois."

## Skipped

- **editor, exercises.json (a level-3 task that determines c with the vessel's heat capacity).** The editor marked it optional. It would replace a level-3 task that four reviewers have passed and lengthen the longest FY3 lesson.
- **tester polish (no canvas assertions, slow time-based checks).** The tester marked both acceptable. Nothing to change.

## Checks

- `python3 -I answers.py`: unchanged, and every value matches exercises.json.
- `lint_lesson.py fy3-6`: 0 errors, 0 warnings. `check_latex.py content/FY3/fy3-6`: all 13 fragments ok.
- `build.py --all`: ok. `test_sims.py fy3-6`: PASS. `check_layout.py fy3-6`: OK at 360 px and at 390 px.

## Files changed

lesson.md and solutions.md.

Stale reviewers (my own hashes differ from the hashes in their reports): physics-expert, mathematician, educator, proofreader, editor, web-designer. The tester's hash is unchanged (22aa2b4fe3ce9aa9).
