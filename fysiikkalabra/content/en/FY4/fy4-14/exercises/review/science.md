VERDICT: PASS
CONTENT-HASH: f1b54f3657d64f1b

## Blocking

## Polish
- solutions.md (L2-08, Reasonableness, last paragraph) — "because this skydiver falls in a wider position (a larger cross-sectional area, for example a loose suit)" states as the cause one of several possible ones for invented data, and a loose suit raises the drag constant rather than the cross-section — "the drag constant is larger, $k = mg/v^2 \approx 0.32\,\text{kg/m}$ instead of $0.26\,\text{kg/m}$, for example because of a wider posture or a loose suit".
- solutions.md (L1-03, Reasonableness) — the estimate changed from $3.5$ to $3.3\,\text{m/s}^2$; $2\,\text{N} : 0.6\,\text{kg} = 3.3$ is right, but "about $2.1\,\text{N}$" would make the check meet the answer $3.52\,\text{m/s}^2$.

## Checked
- Hash f1b54f3657d64f1b at start and end; answers, tolerances, tasks and ids unchanged; answers.py run: L2-08 still 623.25 N; the added line `vT_model_75` is a comment value only, not an answer.
- Captures: none opened; judged from the text and the packet's diff.
- `vT_model_75` recomputed: $\sqrt{75.0 \cdot 9.81 / 0.26} = 53.2\,\text{m/s}$; $k = 0.26\,\text{kg/m}$ belly down agrees with lesson-answers.py (the simulation's model); $mg/48^2 = 0.319\,\text{kg/m}$.
- Every Kaava step now starts from $\Sigma F = ma$ (with $a = 0$ at terminal or constant speed), writes $\Sigma F$ from the forces with the stated positive direction, then solves; final forms unchanged.
- L2-03 ball moving up: $\Sigma F = -G - F_\text{v}$ with up positive, $a = -(g + F_\text{v}/m)$ right.
- L3-02 up and down (positive down): $a_1 = g + F_\text{v}/m$, $a_2 = g - F_\text{v}/m$, $\Delta a = 2F_\text{v}/m = 6.00\,\text{m/s}^2$ right.
- L2-04 car coasting: $\Sigma F = -F_\text{v} - F_\text{r}$, $a = -0.525\,\text{m/s}^2$ right.
- L3-05 raindrop b: $v^2 = v_0^2 + 2as$ with $a = g$ justified by $\Sigma F = mg$ without air resistance; $171.55\,\text{m/s}$ unchanged.
- L1-08: $\Sigma F = G - F_\text{v}$, $-911.4\,\text{N}$, direction up; the student's error explanation kept.
- exercises.json: only "(example data)" removed from captions and paragraphs reflowed; no value changed. Paragraph splits move no claim.
