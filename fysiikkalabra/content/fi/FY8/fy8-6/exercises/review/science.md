VERDICT: FAIL
CONTENT-HASH: 42a85f8ae42cb80b

## Blocking
- exercises.json:344 (fy8-6-L2-08) — **assessment (7)**. The correct option is the only one that mentions the uncertainty ("koska ero on epävarmuutta pienempi"), so it can be found from its form alone. — Fix: let distractor 340 also argue from the uncertainty, for example "…liian pieni, koska ero hyväksyttyyn arvoon on suurempi kuin mittausepävarmuus ±0,05 V".
- solutions.md:185, 187, 189 (fy8-6-L2-08) — **layout, measured from the render**. At 390 px the chains `h = ek = 1,602·10⁻¹⁹ C · 3,98·10⁻¹⁵ V s = 6,376·10⁻³⁴ J s` (about 520 px), `Δh = …` (about 558 px), the difference chain (about 450 px) and the inline check `3,98·10⁻¹⁵ V s · 4,76·10¹⁴ Hz − 0,07 V = 1,82 V` (about 427 px) are clipped, so the results cannot be read on a phone. — Fix: write symbolic, substituted and result lines separately, and make the inline check its own lines.

## Polish
- exercises.json:337 and solutions.md:191 — the text says "eroaa arvosta hf/e lähes yhtä paljon kaikilla LEDeillä", but in this data set hf/e − U_k ranges from 0,12 to 0,21 V. The offset grows with f, which is why the slope comes out 4 % below h/e. This is acceptable as a simplification at this level (C), but "suunnilleen" would be more honest.

## Checked
- I fitted the table by least squares: k = 3,976·10⁻¹⁵ V s, intercept −0,074 V and standard error of the slope 0,210·10⁻¹⁵ V s, all matching the task. Every residual is 0,048 V or less, within the ±0,05 V uncertainty ✓. h = 6,376·10⁻³⁴, Δh = 0,336·10⁻³⁴, and the difference from the accepted value, 0,25·10⁻³⁴, is less than Δh, so the correct option is right ✓.
- Distractors: "not through the origin" is the chapter's warned error, "systematic error" reads a difference within the uncertainty as significant, and the voltage-sets-photon-energy option is the chapter's first misconception. Each is really wrong and its feedback is right ✓.
- Scope: eU_k ≈ hf and h = ek are both taught ✓. The data are labelled esimerkkiaineisto.
- Render: preview/fy8-6.html at 390 px, with feedback and the solution opened, plus a screenshot. The hash is the same at the start and the end.
