VERDICT: PASS
CONTENT-HASH: 13bbadfdc5fe3724

## Blocking
None.

## Polish
- fy7-s2 (task, criteria, solutions a, c): the task says "effective value" throughout, but the fy7-7 lesson it links to teaches "**rms value** (effective value)". Writing "rms (effective) value" at first use and "rms value" after it would match the lesson. The physics is not wrong.
- The fi round 2 polish points carry over unchanged: s3 e gives the time-averaged force, and s4 e's 500 nm reflection equals bare glass.

## Checked
- I compared en with the reviewed fi (af9c16707d86ff5d) string by string and section by section. That covers tasks.json (25 parts with their criteria and details), solutions.md (35 sections) and figures.json.
- Every non-text value is identical: answers, units, tolerances, points (83) and links. practice.py check reports OK.
- A script compared the math with `\text{}` set aside and commas read as points. Every formula is identical, and so is every number in the prose. That includes the s1 d split, `mv = 1.3256·10⁻²⁰ kg·m/s`, which gives B = 0.2069 T.
- I read the physics in full and found no condition lost or added:
  - s1: the right-hand rule, the upper plate positive, and "selects speed, not mass".
  - s2: e₀ ∝ f ∝ v with its no-load caveat, Lenz's law with energy conservation, and the eddy currents and laminated core.
  - s3: the 2·25 km circuit, the I² argument, and AC currents that repel at all times.
  - s4: Wien's law assumes a black body. Grey and wavelength-dependent emissivity are told apart. The angle is 90° − β. Both reflections invert, so d = λ/(4n).
  - s5: d sin θ = kλ, the ±3 nm and ±1 nm uncertainties, and dispersion against interference.
- Rendered page (Playwright, 390 and 1280 px, every solution open):
  - The page's main text has no word with ä or ö. The solution headings render as "Also accepted" and "Common mistakes".
  - The figure labels are in English with decimal points.
  - The F_m on the + ion points up (v × B = x̂ × (−ẑ) = +ŷ), and the beam curves up to the slit.
  - check_layout FY7-sovella --width 340 reports OK.
- The hash was 13bbadfdc5fe3724 at the start and at the end.
