VERDICT: PASS
CONTENT-HASH: 11fdfd0b3fe68e5d

## Blocking

## Polish
- lesson.md:118, inquiry.json `tyypit` and `check-c2` (right options): "veden liike-energia" should be "virtaavan veden mekaaninen energia". Hydro mainly uses the water's head (C at this level).
- lesson.md:260: $P_\text{L} = c\,q_m\,\Delta T$ needs its condition, so add "(vesi pysyy nesteenä)".
- lesson.md:124, sankey raster measured from the webp: the bands agree with one another to about 3 % (about 98 px per 100 MW). The scale bar is about 105 MW and the 12 MW arrow is about 15 MW wide. Tighten these on the next redraw.
- inquiry.json `tyypit`, generator feedback: "yli 0,95" clashes with the lesson's generator-and-transformer stage of 0,945. Write "generaattori yksin".
- inquiry.json `kertaus`, first feedback: "Laskit lämmöt yhteen" should be "Laskit lämmön ja työn yhteen".

## Checked
- I recomputed every number in one script and all of them match: ketju 248,4 MW (distractors 270 / 211,6 / 288,4 / 300), kaukolampo 48 MW, η 0,88, tarve 130 MW, siirto 8,64 MW (20 / 164,16 / 155,52), virhe 342 / 540 / 360 MW, check-2 216 MW, exit 0,432, kertaus 520 MJ, mean 0,78 against product 0,40.
- Worked example: 0,38038, 228 MW, 372 MW, condenser 306 MW, estimate 231 MW. The unknowns are solved symbolically first and the rounding is justified.
- SVG figures are to scale: the bars at 0,5 px/MW and the CHP area corners (194 / 218 / 78,8, x 526,9). The sankey image is scaled uniformly and its labels sit beside the right arrows.
- The definitions agree with the glossary and guardrails: chain efficiency is a product, and CHP's total and electrical efficiencies are kept apart. The heat-engine loss is unavoidable "ei kokonaan", that is, only in part.
- The CHP mechanism is right: a hotter condenser gives a smaller drop across the turbine and so less electricity. The feedback on all of the pred-2 models is right.
- Each choice item has exactly one correct option, and every distractor's feedback gives a correct reason.
- The typical efficiencies are plausible (wind is below the Betz limit), and the lesson says that the plant types use different denominators.
- The text has no "lämmöksi" phrasing and stays within the FY3 scope. The reason for having no simulation holds.
