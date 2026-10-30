VERDICT: FAIL
CONTENT-HASH: 23c8f56ca94e5cab

## Blocking
1. **fy4-s2 c, solutions (A, item 4).** "$29{,}1\,\text{N} \cdot 180\,\text{m} = 5235\,\text{J}$" is wrong: $29{,}1 \cdot 180 = 5238$. Use $5238\,\text{J}$, or reuse b's unrounded $5235\,\text{J}$ directly (answer $13{,}6\,\text{m/s}$ stands).
2. **fy4-s2 task text (B, item 2).** The speed is measured "jarrun alussa", but $h = 15{,}0\,\text{m}$ is to "vaijerin loppupää" and $s = 180\,\text{m}$ is the whole cable, which includes the brake section. Using $s = 170\,\text{m}$ gives $F \approx 31\,\text{N}$, outside the $5\,\%$ tolerance. State that the height difference and the length are to the brake's start (or that the brake section is short).
3. **Significant figures (A, items 6–7).** fy4-s2 c: $95\,\text{kg}$ and $F_\text{vast} \approx 29\,\text{N}$ are two figures, yet the answer is given to three with no rounding reason ("arvio on vain yhtä hyvä kuin sen oletus" is not one). fy4-s3 b: "kaksi tai kolme" from a two-figure $v'$. The `units_precision` details demand $13{,}6\,\text{m/s}$, so a student who rounds correctly to $14\,\text{m/s}$ could lose the point. Give one reason and accept both values (or two figures) in the rubric.
4. **fy4-s2 has no `### Hyväksytään myös` (item 7).** At least: d sized to the frictionless upper bound $17{,}2\,\text{m/s}$ (or with a margin for heavier riders) is a correct, safer conclusion and must earn the `conclusion` point; b and c with the rounded $29\,\text{N}$ ($13{,}6\,\text{m/s}$ again) are accepted.

## Polish
- fy4-s3 c: seat-cushion friction also acts on the driver; "pääosin selkänoja" would be exact (C).
- fy4-s1: with a realistic $C_\text{d}A \approx 0{,}5\,\text{m}^2$ the air drag is worth about $0{,}006$ (A) and $0{,}004$ (B) in $\mu$, so it matters more than the slope-reading uncertainty; the direction argument is correct.

## Checked
Recomputed every number independently (scratchpad `recompute.py`): s1 fits $0{,}3895$ and $0{,}2447\,\text{m/s}^2$, the read points lie on the fitted lines, $\mu_\text{A} = 0{,}030$, $\mu_\text{B} = 0{,}045$, accepted slope ranges stay within the tolerance, $\pm 0{,}1^\circ \to 0{,}0018$; s2 $17{,}2\,\text{m/s}$, $29{,}1\,\text{N}$, $0{,}574$, $13{,}57\,\text{m/s}$; s3 $7{,}86\,\text{m/s}$, $13{,}64\,\text{m/s}$ ($49\,\text{km/h}$), $42\,\%$ kinetic energy lost, $4455\,\text{N}$ ($6{,}7\,mg$), friction impulse $2605\,\text{N·s}$ ($11\,\%$, $v_\text{B} \le 15{,}2\,\text{m/s}$), $\mu \approx 0{,}50$ for $40\,\text{km/h}$. Points sum per part. Scope within FY4. Force diagram s1 b per docs/force-diagrams.md (rectangle, $\overline{G}$ from centre, $\overline{N}$ from the surface, $\overline{F}_\mu$ from the contact corner, components dashed, $\overline{a}$ orange off the body, $\overline{v}$ blue, $\overline{p}$ purple); equations match it. Whiplash and impulse reasoning correct; $F_\text{ka}$, LaTeX symbols, provenance labels OK.
