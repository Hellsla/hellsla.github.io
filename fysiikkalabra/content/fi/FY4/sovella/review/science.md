VERDICT: PASS
CONTENT-HASH: 2978c7bdbfea8fbf

## Blocking
None. Round-1 items verified:
1. fy4-s2 c now reuses b's work $5234\,\text{J}$ ($9123 - 3889$, consistent with the shown values; exact $5234{,}7$). $13\,979 - 5234 = 8745\,\text{J}$, $v = 13{,}57\,\text{m/s}$. Fixed.
2. fy4-s2 text: $h$ and $s$ are now from the platform to the brake's start, where the speed is measured; solution Annettu and answers.py agree. $F_\text{vast} = 29{,}08\,\text{N}$. Fixed.
3. Significant figures: s2 c and s3 b answer $14\,\text{m/s}$ with a stated two-figure reason; rubric accepts $13{,}6$ too; tolerances $5\,\%$ cover $13{,}6$ and $13{,}71$ (from rounded $v' = 7{,}9$). s3 c with $7{,}9$: $4477\,\text{N}$, within $4{,}4$–$4{,}5\,\text{kN}$. Fixed.
4. fy4-s2 `### Hyväksytään myös` added: rounded $29\,\text{N}$ gives $5220\,\text{J}$ and $13{,}58\,\text{m/s}$ (correct); d sizing to $17{,}2\,\text{m/s}$ or with a margin earns the point, also in the rubric detail. Fixed.

## Polish
- fy4-s2 c rubric: "$13{,}98\,\text{kJ} - 5{,}23\,\text{kJ} \approx 8{,}74\,\text{kJ}$" reads as $8{,}75$ from the shown figures; quote $8{,}74$ or $8{,}75$ consistently with the solution's $8745\,\text{J}$.
- Carried over: fy4-s3 c "pääosin selkänoja" (seat friction also acts); fy4-s1 air drag ($C_\text{d}A \approx 0{,}5\,\text{m}^2$) is worth about $0{,}006$/$0{,}004$ in $\mu$, more than the slope-reading uncertainty.

## Checked
Recomputed the changed numbers independently: s2 $E_\text{p} = 9123\,\text{J}$, $E_\text{k} = 3889\,\text{J}$, $W = 5235\,\text{J}$, $F = 29{,}1\,\text{N}$, $E_\text{p,95} = 13\,979\,\text{J}$, $v = 13{,}57$ ($13{,}58$ with $29\,\text{N}$) $\,\text{m/s} \approx 49\,\text{km/h}$; s3 $v' = 7{,}86\,\text{m/s}$, $v_\text{B} = 13{,}64\,\text{m/s}$ ($50\,\text{km/h}$ at two figures), $F_\text{ka} = 4455\,\text{N}$. s2 d reasoning (c estimate an upper bound, second instructor's a lower bound, size to the larger) consistent with the new $14\,\text{m/s}$. The added s1 b note on dashed $G_x$, $G_y$ as components, not forces, matches docs/force-diagrams.md. answers.py keys match the solutions; practice.py check OK; points sum per part; hash unchanged start to end. Unchanged parts as in round 1.
