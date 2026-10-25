VERDICT: DONE

Round 1 fixes for fy3-6. The proofreader's diff was empty, so there was nothing to apply.

## Blocking

1. **editor, lesson.md:23 (solving for T is never shown).** Under `## Kaava` the lesson now solves the balance equation for T step by step. It expands the brackets, collects the T terms and factors T out, in an `aligned` display. The result `T = (c₁m₁T₁ + c₂m₂T₂)/(c₁m₁ + c₂m₂)` is shown once in display LaTeX, with one sentence calling it a weighted mean (weighted by c₁m₁ and c₂m₂).
2. **editor, exercises.json L2-01 (near-duplicate of L1-02).** Replaced with a water–water mixing task in grams that asks for T: 160 g at 95 °C plus 40 g at 8,0 °C gives 77,6 °C, answered as 78 °C with tolerance 0,02. The solution notes that c cancels and that the grams need no conversion. answers.py and solutions.md are updated.
3. **editor, lesson.md:8 (C = cm only inline).** The C sentence moved from Ydinajatus to `## Kaava`, where `C = c m` has its own display with C (J/K), c and m named. It is displayed only once. The summary keeps its inline reference.
4. **educator, lesson.md:71 (35 °C only asserted).** The misconception now shows the working in an `aligned` display: 3,0 kg·(T − 20 °C) = 1,0 kg·(80 °C − T) → 3T − 60 °C = 80 °C − T → 4T = 140 °C → T = 35 °C. The text says that c cancels and that line 2 divides by kg.
5. **educator, exercises.json L2-04 (rearrangement duplicate).** Replaced with a metal–water task that asks for T: a 0,25 kg aluminium ladle at 95 °C dropped into 0,40 kg of water at 18 °C gives 27,11 °C, answered as 27 °C with tolerance 0,02. It differs from the new L2-01 in both substances and difficulty. L2-01 is water–water in grams with c cancelling; L2-04 has two different c values in kg, and the solution computes C₁ = 225 J/K and C₂ = 1676 J/K.
6. **web-designer, sim.js:28-39 (Upota out of reach on a phone).** The DOM order is now canvas, then controls with "Upota" first, then the readout, then the note. Measured from canvas top to button bottom: 291 px at 390×844 and 244 px at 360×640, so both fit on one screen. The animation step is clamped with `tAnim += Math.min(p.deltaTime, 100) / 1000`. I started the animation, scrolled away for 3 s and came back: simState.t was 0,64 s, so the motion no longer jumps ahead.

## Polish applied

7. **web-designer, string through the label.** The string now starts at `max(76, ts(18)+ts(19)+ts(7))` and is drawn only when there is room above the body. Checked in screenshots at 360 and 390 px.
8. **web-designer, T label touching the legend.** When Teq is in the top 15 % of the axis, both the "T" and its value are drawn below the dashed line. Checked at 360 px with 0 °C aluminium in 1,00 kg of water at 20 °C (Teq 19,2 °C).
9. **web-designer, slider labels wrapping at 1280 px.** The label spans are `white-space: nowrap`. Every span is now one line (27 px) at 1280, 390 and 360 px, with no horizontal overflow (scrollWidth − innerWidth = 0 at all three widths).
10. **physics-expert, mathematician and educator, ΔT undefined.** The display under Kaava is now `Q = c m ΔT, ΔT = T_loppu − T_alku`, and the text says that ΔT and Q are positive on heating and negative on cooling.
11. **educator and mathematician, both sides are magnitudes.** Added a sentence after the balance equation: both sides are positive heat amounts, so the hot body uses alku − loppu and the cold body loppu − alku.
12. **mathematician, T₁/T₂ notation.** The single-body solutions (L1-01 to L1-05, L2-02 and L2-03) now use T_alku and T_loppu and state the formula they rearrange. T₁ and T₂ are kept only for the two-body tasks, as in the lesson.
13. **physics-expert and mathematician, significant figures of 375.** The example now gives c = 374,6 ≈ 3,7·10² J/(kg·K). One sentence explains that the 4,5 K change has 2 significant figures and that a reading 0,1 K higher would give 383 J/(kg·K).
14. **physics-expert, sim 24,6 °C vs measured 24,5 °C.** Added one sentence: with no losses, the copper would raise the water to 24,6 °C (try it in the simulation), and the measured reading, 0,1 K lower, is explained by losses to the vessel and the air.
15. **educator, sand reason.** The sentence now starts "Tärkeä syy on, että …", and the physics-expert's point is added: the sun heats only the thin surface layer of the sand, while in water the heat spreads deeper.
16. **educator, C values without working.** The text now shows the calculations: 0,300 kg · 4190 J/(kg·K) = 1257 J/K and 0,200 kg · 374,6 J/(kg·K) ≈ 75 J/K.
17. **proofreader, "tasapainolämpötila" missing from the glossary.** Added it to glossary.json (two Finnish sentences, see_also lämpötasapaino and lämpökapasiteetti, lesson fy3-6) and to meta.json `glossary`.
18. **tester, no test for equal start temperatures.** Added the requested assertion (Q = 0 and Teq = 40) and one more that checks the readout text "Lämpötilat ovat samat, joten lämpöä ei siirry.". I also added a layout assertion: Upota is the first control and the controls come before the readout. This guards finding 6.
19. **mathematician and physics-expert, solutions.md L3-01.** The sanity check now names both factors: the stones cool 8,7 times as much as the water warms, which lowers the mass needed, and their c is 5,2 times smaller, which raises it. The mass ratio is about 0,60.
20. **Summary.** The third bullet now says that T is found by collecting the T terms, and that it is a weighted mean, not the plain average.

## Skipped

- **web-designer, drop the "Lämpömittarit nyt" readout line.** Kept. After the reorder the readout no longer pushes Upota out of reach, which was the reason for dropping it. The line is the only DOM text that gives the live temperatures (NOTES: numeric readouts are DOM text). Existing assertion 24 in tests/sims/fy3-6.json checks it and does not contradict sim-spec.md, and I may not change or loosen such a test.
- **editor polish, measurement steps and error sources; a level-3 task with the calorimeter's heat capacity.** Both are optional extensions, not corrections. Adding them would lengthen the lesson and change the level-3 set that the educator and physics-expert passed.
- **tester polish, canvas assertions and slow time-based checks.** The tester itself marked these acceptable.

## Checks

- `python3 -I content/FY3/fy3-6/answers.py`: L2-01 77,6 and L2-04 27,11; the other ten values are unchanged.
- `lint_lesson.py fy3-6`: 0 errors, 0 warnings.
- `check_latex.py content/FY3/fy3-6`: all 13 fragments ok. `^\circ` after `\,` needs `{}` (`20\,{}^\circ\text{C}`), otherwise KaTeX fails.
- `build.py --all`: ok.
- `test_sims.py fy3-6`: PASS with 45 assertions, no console errors.
- Screenshots at 390, 360 and 1280 px, before and after Upota, for the cold body and the large body. They are in the scratchpad, not the repo.
- Running `gate.py fy3-6` wrote `review/gate.md` as its audit trail.

## Files changed

lesson.md, exercises.json, solutions.md, answers.py, sim.js, meta.json (glossary only), tests/sims/fy3-6.json, glossary.json.

Stale reviewers (gate.py): tester, physics-expert, mathematician, educator, proofreader, editor, web-designer. All seven have to run again.
