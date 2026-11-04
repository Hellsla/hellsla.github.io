VERDICT: FAIL
CONTENT-HASH: 1e3ebaffa0ccf48f

Visual and editorial review, round 2, of the en translation of fy9-sailymislait, 2026-11-04.

Method: rebuilt with `python3 scripts/build.py fy9-sailymislait` (preview/en/fy9-sailymislait.html, which build.py reports as "reviewed") and opened in Playwright at 390 and 1280 px with every details element open.

Results:
- No horizontal scroll (scrollWidth 390 at 390 px, 1280 at 1280 px).
- No KaTeX errors, no console errors and no raw `$` left in the text.
- No decimal commas.
- No Finnish words in the HTML text.
- At 390 px the figures are 358 px wide (hero, kartta, tormays), 324 px (buffer graph) and 298 px (the two s3 graphs).

The round-1 Polish 4 ("when he stops") is fixed.

## Blocking
1. **Still not fixed**: unit.md, concept map `kartta` (Theory summary). The three branch headings are still drawn as **energia**, **liikemäärä** and **sovellukset** at 390 and 1280. The preview HTML contains `$\textbf{energia}$` and `$\textbf{sovellukset}$`.
   - The round-1 fix added `"energia"`, `"liikemäärä"` and `"sovellukset"` to figures.json. That has no effect, because `scripts/figlib.py` `translate()` still rewrites only `\text`, `\mathrm` and `\textsf` (its regex), and lessons/units/fy9-sailymislait/figures.py line 125 still draws `r"\textbf{" + head + "}"`.
   - check_i18n still passes, because `\textbf` words are never reported as MISSING.
   - A hand edit of the SVG in unit.md would fail check_i18n ("figures differ from figures.py"), and a translation reviewer may not edit scripts/ or lessons/. So the fix has to come from the developer or orchestrator, in one of two ways:
     - (a) in scripts/figlib.py `translate`, add `textbf` to the group `(?:text|mathrm|textsf)`, then redraw with `python3 scripts/units.py figures fy9-sailymislait --lang en`. The figures.json entries are already in place.
     - (b) in figures.py, write `r"\textbf{\text{" + head + "}}"`. This changes the Finnish hash, so the fi reviews would need re-stamping.

## Polish
1. Ratio colon "a : b" ($F_\text{avg} = |\Delta p| : \Delta t$, $\mu = a : g$) is Finnish typography; English uses "/" or a fraction. This is a project-wide decision, so it is left as it is.
2. $s_\text{p}$ for stopping distance (fy4-11 in English uses $s_\text{stop}$). See science Polish 1.
3. The s3 graphs (298 px) and the buffer graph (324 px) have axis labels of about 10 px at 390. They are readable, but at the limit.

## Shared issues
- scripts/figlib.py `translate`/MISSING ignores `\textbf{}`. This very likely affects content/fi-easy/units/fy9-sailymislait too, and any other figure that writes words in `\textbf`.
