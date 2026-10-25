VERDICT: DONE

Lesson-form rework of fy3-9 to the human rules (CLAUDE.md "Human decisions on lesson form", NOTES.md section 4). Round 1 fixes are kept. No number or answer changed. Checks: answers.py OK, lint 0 errors 0 warnings, check_latex OK (13 fragments), build --all OK, check_layout OK at 360 and 390 px, test_sims PASS. Looked at the page at 360 px: all three figures, the staged example (stage 1 with "Näytä seuraava vaihe", and all five stages) and the misconception list.

## Findings and changes
1. No figure in Ydinajatus (lint ERROR). Split the micro-model paragraph after "Paine kaksinkertaistuu." and added an inline SVG right after it: the same eight particles in a cylinder at V (gas column 220 px) and at V/2 (110 px, ratio 2 : 1 to scale), velocity arrows of equal length (same speed, T vakio), and hit marks on piston and bottom, 4 against 8, with a small legend "osuma"; labels "V ja p" and "V/2 ja 2p". The aria-label calls it a schematic and states the 2 : 1 ratio. Text 24–26 px, currentColor, viewBox 0 0 600 300.
2. Figure placement in Kaava. Moved the existing two-panel (V, p) / (1/V, p) graph so it directly follows the paragraph that explains it (the 1/V paragraph). Its content is unchanged.
3. Isobaric and isochoric laws. After the V/T and p/T display added one sentence ("Tilavuus tai paine on siis suoraan verrannollinen kelvinlämpötilaan, ja (T, V)- tai (T, p)-kuvaajan suoran jatke kulkee origon eli absoluuttisen nollapisteen 0 K kautta.") and a to-scale graph: x-axis T (K) with ticks 0 and 273 at 1,2 px/K, points at 253–373 K on a line through the origin, the extrapolation dashed and labelled "jatke".
4. Paragraph length. All paragraphs were already under 120 words. The micro-model paragraph (106 words) is now split around the figure, and the misconception paragraph (112 words, three cases) is a short bullet list, one bold lead-in per misconception. Wording unchanged apart from the lead-ins.
5. Worked example not staged and substituting before solving (lint ERRORs). ## Esimerkki now has 5 stages separated by `<!-- vaihe -->`: **Tunnetut ja kysytty.**, **Kaava ratkaistuna.** (p₁V₁ = p₂V₂ → V₂ = p₁V₁/p₂), **Sijoitus.** (symbolic first row, then the values with units; kPa cancels), **Tulos.** (V₂ = 1,036… l ≈ 1,0 l, two significant figures, about 30 %, the bag puffs up), **Järkevyys.** (pressure falls so volume grows; 101/78 ≈ 1,3 and 0,80 l · 1,3 ≈ 1,0 l). Every display starts with a symbolic row and fits 360 px. In math the litre is now `\textsf{l}`: in the KaTeX serif font `0{,}80\,\text{l}` read as "0,801" at 360 px.
6. solutions.md Kaava lines. Each now ends with the formula solved for the asked quantity in symbols, and numbers with units appear only in Sijoitus:
   - L1-04, L1-05, L2-02: "(T kelvineinä)" added; the conversion constant 273,15 K moved from Kaava (L1-04) into Sijoitus as T₁ = (22 + 273,15) K = 295,15 K etc.; L2-02 ends with T₂ = T₁p₂/p₁ and Sijoitus writes θ₂ = (362,8 − 273,15) °C.
   - L2-03: ends with k = pV = p / (1/V); the duplicate sentence in Sijoitus was removed.
   - L2-04: ends with ΔV = V₂ − V₁; Sijoitus names ΔV.
   - L3-01: p₁ = p₀ + ρgh, then p₁V₁ = p₀V₂, ending with V₂ = p₁V₁ / p₀.
   - L3-02: introduces Δp for the gauge reading (Annettu Δp₁ = 250 kPa) and ends with Δp₂ = p₂ − p₀; the first Järkevyys sentence (now repeated in Kaava) was dropped.
   - L3-03: Annettu names L₁, p₁ = p₀ and Δp; Kaava ends with L₂ = p₁L₁ / p₂ and s = L₁ − L₂; Sijoitus writes s = …; Järkevyys shortened.
   L2-03 to L3-03 were trimmed so that every solution stays under the lint's 130-word limit (120–128 words).

## Not done here
- sim.js and tests/sims/fy3-9.json were left alone on purpose: the graphics agent is reworking the simulation's visuals.

## Files changed
lesson.md, solutions.md. Unchanged: meta.json, exercises.json, exit-ticket.json, answers.py, sim.js, sim-spec.md, tests/sims/fy3-9.json.

Stale reviewers (must run again): physics-expert, mathematician, educator, proofreader, editor, web-designer (lesson.md and solutions.md are in their domains). The tester is stale only because of the parallel sim.js work, not because of this fix.
