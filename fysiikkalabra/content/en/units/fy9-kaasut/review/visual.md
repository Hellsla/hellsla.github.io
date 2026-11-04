VERDICT: FAIL
CONTENT-HASH: d049914a3ec3f36c

Visual and editorial review (round 2) of the en translation of fy9-kaasut. I built preview/en/fy9-kaasut.html with `python3 scripts/build.py fy9-kaasut` and checked it in Playwright at 390 and 1280 px.

## Blocking
1. [Critical, not fixed since round 1] In the concept map `kartta`, the branch headings are still Finnish (**neste**, **kaasu**, **lämpövoimakone**). The capture /tmp/claude-0/tk/fy9-kaasut/kartta-390.png shows them. Everything else in the figure is English: "pressure", "at depth", "ideal gas law", "work done by gas", $W_\text{g}$. The figure's description (Liquid / Gas / Heat engine) does not match what is drawn.
   - Cause: figures.py line 120 uses `\textbf{head}`, and figlib translates only `\text{}`, `\mathrm{}` and `\textsf{}`.
   - This cannot be fixed in content/en. If unit.md is edited by hand, check_i18n fails with "figures differ from figures.py" (I tried this and reverted it).
   - Fix (shared issue, lessons/units/fy9-kaasut/figures.py): `r"\textbf{\text{" + head + "}}"`. Then add `"neste": "liquid"`, `"kaasu": "gas"` and `"lämpövoimakone": "heat engine"` to the en figures.json, and redraw. The box is 328 px wide, so "heat engine" fits.

## Polish
2. [Minor] $P_\text{l}$ (s2 c): a Finnish-derived subscript. It is defined in the text, so it is optional: $P_\text{h}$.

## Round-1 findings
- 2 ($W_\text{k}$ and $\eta_\text{kok}$): fixed in every en file and in the figure.
- Polish items "work done by gas", s1, s2 c and exit ticket 1.a: all fixed. The longer label "work done by gas" fits its row at 390 px without overlapping the formula.

## Checked
- scrollWidth equals the viewport at 390 and 1280. There are 0 KaTeX errors.
- check_i18n: en 0 errors.
- Decimal points are unchanged from round 1.
- In the page text, the only Finnish words are the three headings above.
