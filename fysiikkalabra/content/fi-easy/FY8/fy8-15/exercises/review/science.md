VERDICT: PASS
CONTENT-HASH: c4e7b71ee927ba5d

## Blocking

## Polish
- lessons/FY8/fy8-15/answers.py:22 (L2-02) comment says "-> 37,8 MeV" while exercises.json and the solution give 37,84 MeV — align the comment (carried).
- exercises.json L1-04 — "annihiloituvat eli tuhoutuvat kahdeksi fotoniksi": "muuttuvat kahdeksi fotoniksi" is safer (carried).

## Checked
- Delta re-review: the only change since the passed version is commit fd2e54e95 in exercises/solutions.md (360 px narrowing); hash c4e7b71ee927ba5d equals the packet's, at start and end. No task, answer, unit, tolerance or other file changed.
- solutions.md:77 (L2-03) — `\dfrac{6,626·10⁻³⁴ J s · 2,998·10⁸ m/s}{X}` → `6,626·10⁻³⁴ J s · \dfrac{2,998·10⁸ m/s}{X}` is identical (a·b/X = a·(b/X)); X = 1,6372 · 10⁻¹³ J still the denominator, braces balanced (old numerator's closing brace now closes the new one), units J s · m/s / (J) give m; recomputed 1,2133 · 10⁻¹² m = 1,2133 pm, as written.
- Decimal comma `{,}` kept in every changed number; `\,\text{}` units unchanged.
- Previous review's recomputation of all 12 answers and its other checks stand (content unchanged).
