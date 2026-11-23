VERDICT: PASS
CONTENT-HASH: c28ce49ad1728e55
SCOPE: full: unit.md (three new `pysahdy` boxes judged first; hero and ketju now raster images under unchanged labels), inquiry.json, teacher.md, Sovella tasks s1–s9 with solutions, answers.py, figures.py.

## Blocking
- (none)

## Polish
- Key idea (unchanged text): "most of it finally ends up as heat in the surroundings" can be read as heat being stored in the surroundings. The Finnish says "päätyy lopulta lämpönä ympäristöön". A closer wording would be "is finally transferred to the surroundings as heat". This is category C, not an error.

## Checked
- Hash at start and end is c28ce49ad1728e55. `practice.py check units/fy9-energia`: OK in fi, en and fi-easy (9 tasks, 134 points). For every part the criterion points add up to the part's points.
- The `pysahdy` boxes are against fi unit.md lines 15–19, 110–114 and 163–167. All three have the same placement, question and answer as the Finnish ones, with the same numbers (3.6 MJ; 0.90, 0.45, 0.98).
  - Box 1: power is the rate and efficiency is the useful share. This matches the Key idea and the recognition chart.
  - Box 2: the kWh is a unit of energy, the kW a unit of power, and 1 kWh = 1000 W · 3600 s = 3.6 MJ.
  - Box 3: the product is 0.397, which is below 0.45. "The product is smaller than the smallest factor" is true when every factor is below 1 and there are at least two of them. Both conditions are stated. This matches the derivation box, the Common mistakes list and the figure (≈ 0.40).
  - None of the boxes gives away a later task.
- I recomputed every number in one script with my own formulas, and all agree within rounding:
  - Theory and figure: ketju 450/203/198 MW and losses 50/248/4 MW (202.5, 198.45, 247.5, 4.05); petrol 322 MJ ≈ 90 kWh; 40 kWh at 2.3 kW ≈ 17 h.
  - Inquiry: lt-2 0.30 and 0.96 kWh; lt-4 0.729; lt-6 43.8 GWh; aineisto η₂ = 42.86 %, and the product of the stage efficiencies is 0.35, equal to P₃ : P₀ (distractors 37.5, 35 and 57.14 checked); sauna 43.2 MJ; car 50.76 kW (the 107.1 kW distractor checked); pellets 3.737 t; lift 8.371 kW; check 1 gives 1500 and 900 MW; check 2 gives 67.5 kJ.
  - Every choice question has exactly one correct option, and each distractor's feedback is right. The heat pump item uses the coefficient of performance, as the guardrails require.
  - s1 1.54, 1.84 and 1.26 kWh; s2 110.8 MW, 27 %, 90 %, 156.7 MW and 59.4 t; s3 least-squares slope −4.89, giving 204 W/K, 230 kWh and 16.5 °C; s4 5.26 GWh, 1.7 h, 2100 t and 3.09 GWh.
  - s5 83.4 % (87, 88, 88 and 79 % in the variations); s6 245.3 MWh, 35.97 MW, 288.5 MWh, 74.8 % and a 73 MWh loss; s7 −28.9, −42.9 and −45.8 %, 16.67 and 26.88 kWh per 100 km, 600 N and 16 %; s8 4.71 m/s, 58.8 N and 5.58 m/s; s9 1.5 kW, 21.6 €, 7.2 €, 73.6 % and 132 W.
- Since the passed commit 797f35f82, en solutions.md has changed only by paragraph splits in s1c, s2d, s3d, s4a and s4c and by blank lines before lists; no words or numbers changed. inquiry.json and tasks.json are unchanged.
- Energy wording follows P1 ("internal energy, transferred as heat"). "Turns into heat" appears only in the listed mistakes.
- Limit: I did not open the raster images. The labels laid over them are the same as in the version that passed, and judging the images is the visual reviewer's role.
