VERDICT: FAIL
CONTENT-HASH: a7d94497271df0b3

## Blocking
- **A, setup figure (fig `setup`, "Tarkista kirjauksesi tästä").** Since the last PASS (hash 96467992) a committed change (36f68f6e8b, b1765649cb) replaced the drawn carts, track, sensors and arrows with `<image href="pics/fy10/fy10-liikemaara-setup.webp">`. That WebP (identical in assets/ and preview/) shows a **hydropower setup**: a water tank with a height arrow, a pipe onto a turbine wheel, a generator and a circuit with a resistor and two meters. It shows no carts, no motion sensors, no velocity arrows and no positive-direction arrow. The overlaid labels $m_1$, $m_2$, $\overline{v}_1$, $\overline{v}_2$, "anturi 1: +", "anturi 2: +" and "positiivinen suunta +" now sit on top of the wrong apparatus. The sign convention the text depends on (sensor 2 measures toward the left, opposite to the chosen positive direction) is therefore no longer shown, and the aria-label describes a picture that is not there. Fix: put back the vector drawing that figures.py `setup()` still generates, or use a raster of the correct two-cart setup that contains those arrows.

## Polish
- The aria-label change you asked about ("Mallikuvaaja: … funktiona mallin mukaan, jos liikemäärä säilyy") is correct: it describes the line $p_\text{kok}' = p_\text{kok}$, slope 1, through the origin, with no measured points, and it matches the text. Nothing physical changed in it.

## Checked
- Hash at start and end: a7d94497271df0b3. The current working-tree diff against HEAD changes only the model figure's aria-label, in investigation.md and figures.py.
- The diff from the commit that recorded the earlier PASS (647f02fe00) to HEAD shows that investigation.md's setup SVG was replaced by a raster image and that the label box's width changed (w=170). No other text, formula or json change, so the earlier report's physics checks still hold.
- Looked at assets/pics/fy10/fy10-liikemaara-setup.webp. It is not the vesivoima-setup file (different md5), but its content is a hydropower diagram.
