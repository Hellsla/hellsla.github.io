VERDICT: FAIL
CONTENT-HASH: 108b31c7b17d036a

## Blocking
- [Major] inquiry.json, Calculation task (receiver coil, B₀), Substitution — at 390 px the new second row `: (12 · 1.1 · 10⁻³ m² · 2π · 1.40 · 10⁵ Hz)` is wider than its box (content 310 px, box 296 px): the capture shows it cut at "H", the unit and the closing parenthesis must be scrolled to. That is the clipping queue 5d removes (teacher 2026-11-15). Fix: break the divisor between whole quantities, e.g. `B_0 &= 9.0\,\text{V} \\ &: (12 \cdot 1.1 \cdot 10^{-3}\,\text{m}^2 \\ &\quad \cdot 2\pi \cdot 1.40 \cdot 10^{5}\,\text{Hz}) \\ &= …`; the 1280 px row is fine.

## Polish
- [Minor] Substitution of the percentage task: now correct (`= … · 100 %` / `= … · 100 %` / `= 47.34 %`), but the left side `increase` stands as text above the formula; `\text{increase}` as the first row of the display would join them.

## Checked
- batch delta review: queue 5d reflow. The content changed during the review (commit 7e4ba8466f); this report judges the new hash: the page was rebuilt (build.py) and recaptured. review/shots is stale for this hash and has no phone captures of opened states, so every aligned formula of inquiry.json and exit-ticket.json (3 rendered blocks) was captured from preview/en/fy7-16.html at 390 px and 1280 px with every box, hint, solution and choice feedback forced open, and each capture was read; box overflow measured at 390 and 1280 px. Figures and the formula-name / teacher-figure categories were not re-judged.
