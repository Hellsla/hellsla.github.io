VERDICT: FAIL
CONTENT-HASH: 7b95ca37c7355e5a

## Blocking
- [Critical] inquiry.json, simulation box *Laskennan selitys* (`calc`) — the three definitions (B, k₁, k₂) are merged into one chain: `B = μ₀NI/(2l) · (k₁ − k₂)k₁` / `= (x + l/2)/√(…) k₂` / `= (x − l/2)/√(…)` at 390 and 1280 px. It now states B = k₁-expression = k₂-expression and prints "(k₁ − k₂)k₁"; broken notation. Fix: `\begin{aligned} B &= \frac{\mu_0 N I}{2l}(k_1 - k_2) \\[6pt] k_1 &= … \\[6pt] k_2 &= … \end{aligned}`, each definition its own row with its own left side. Check fi and fi-easy.

## Polish
- none

## Checked
- batch delta review: queue 5d reflow. The content changed during the review (commit 7e4ba8466f); this report judges the new hash: the page was rebuilt (build.py) and recaptured. review/shots is stale for this hash and has no phone captures of opened states, so every aligned formula of inquiry.json and exit-ticket.json (4 rendered blocks) was captured from preview/en/fy7-3.html at 390 px and 1280 px with every box, hint, solution and choice feedback forced open, and each capture was read; box overflow measured at 390 and 1280 px. Figures and the formula-name / teacher-figure categories were not re-judged.
