VERDICT: PASS
CONTENT-HASH: f400048870a9f0b4

## Blocking
None. All three blocking issues from the previous review are fixed:
1. Hanger hint (tuki O): both consistent ways now give a line through the origin with slope $k$, and the text says that mixing them (l0 without the hanger, hanger mass left out of $F$) gives the constant term $-m_\text{t} g$. This is correct and matches teacher.md.
2. teacher.md, first misconception: with $l$ on the axis the slope stays $k$ and only the line no longer passes through the origin. Swapped axes give $1/k$. This now agrees with the student tuki "Miksi juuri nämä akselit?" and with prediction 3.
3. Setup figure: $\overline{F}$ (296 to 206) and $\overline{G}$ (331 to 421) are both 90 px long and red, in figures.py and in the embedded SVG.

## Polish
- investigation.json, prerequisite fy3-1: "venyttää jousta painollaan" still says the weight acts on the spring. The body pulls the spring with a force equal to its weight. The Teoria text now states this correctly (Newton III), so only the prerequisite line is left.
- Mittaa tuki O: "lue pituus esimerkiksi telineen alareunasta" fits only the l0-with-hanger way. A student who measures $l_0$ without the hanger (way 1) cannot read it from the hanger's lower edge, and the hanger's length then becomes an offset in $x$. The slope is unchanged. Consider tying the reading point to the chosen way.
- "suora tasoittaa yksittäisten mittausten virheitä": this applies to random errors only. A systematic offset survives the fit (minor; still open from last time).

## Checked
- Definitions: $x = l - l_0$, $F = kx$ with the condition "kun jousta ei venytetä liikaa", unit N/m, $F = G = mg$ at rest, and Newton III for the pull on the spring.
- Models: the line through the origin with slope $k$ (model graph, both Δ points on the line). Close-wound spring initial tension, in tuki and teacher.md, is handled by excluding the start of the data.
- Extension: $T = 2\pi\sqrt{m/k}$ with $m$ including the hanger; $T^2 = (4\pi^2/k)\cdot m$; $k = 4\pi^2/a$; $\Delta k/k = \Delta a/a$. The spring's own mass gives a positive intercept and leaves the slope unchanged, as drawn in the oscillation figure. Timing ten periods is explained correctly.
- Uncertainty: fit standard error or the steepest/shallowest line with $\Delta k = (k_\text{max} - k_\text{min})/2$. Rounding rule. Overlapping intervals now read as "sopusoinnussa", not "proven equal" (guardrail satisfied).
- Internal consistency: predictions, tuki, Käsittele questions, teacher.md misconceptions and Raportoi agree.
- House rules: $\overline{F}$ and $\overline{G}$ (no \vec), \cdot, red forces. No invented measurement data, and both graphs say they show models.
- Scope: FY1, FY3, FY4 and an FY5 preview explained on the page. Variants F1/E1 and F2/E3 are plausible.
- `scripts/reviews.py hash` does not cover investigations, so this review uses the hash given in the prompt.
- Polish diff to hash f400048870a9f0b4 checked: it adds no physics error. It fixes all three polish points: the prerequisite now says the body pulls the spring, the length is read from the spring's hook for l0 as well, and the line smooths random errors only. It also adds tuki I and prediction 4.
