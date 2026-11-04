VERDICT: PASS
CONTENT-HASH: 5ed5af187d8f9cb2

## Blocking

## Polish
- exercises/solutions.md:119 (L3-03) — "observed precisely the 511 keV photons produced in the annihilation of the positron and the capture of the neutron" can be read as neutron capture also giving 511 keV photons — write "the 511 keV photons from the positron's annihilation and, a moment later, the gamma rays of the neutron's capture" (carried, still open).
- lessons/FY8/fy8-15/answers.py:22 (L2-02) comment says "-> 37,8 MeV" while exercises.json and the solution give 37.84 MeV — align the comment (carried).
- Packet (tooling) — the en exercise brief is still empty (Finnish heading filter); not a content issue (carried).

## Checked
- Delta re-review: the only change since the passed version is commit fd2e54e95 in exercises/solutions.md (360 px narrowing); hash 5ed5af187d8f9cb2 equals the packet's, at start and end. No task, answer, unit, tolerance or other file changed.
- solutions.md:77 (L2-03) — `\dfrac{6.626·10⁻³⁴ J s · 2.998·10⁸ m/s}{X}` → `6.626·10⁻³⁴ J s · \dfrac{2.998·10⁸ m/s}{X}` is identical (a·b/X = a·(b/X)); X = 1.6372 · 10⁻¹³ J still the denominator, braces balanced (old numerator's closing brace now closes the new one), units J s · m/s / (J) give m; recomputed 1.2133 · 10⁻¹² m = 1.2133 pm, as written.
- Decimal point kept in every changed number; `\,\text{}` units unchanged.
- Previous review's recomputation of all 12 answers and its other checks stand (content unchanged).
