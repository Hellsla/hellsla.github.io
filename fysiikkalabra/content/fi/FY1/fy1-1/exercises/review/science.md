VERDICT: PASS
CONTENT-HASH: 2df6a3c752c09239

## Blocking

## Polish
- answers.py:2,6 — docstring and comments write ratios as k = d2 / d1 and Δn = n₂ − n₁; use d_suurempi / d_pienempi and "askelia" as the lesson and solutions do (not seen by students).
- answers.py:6,8 — comments use conversion factors (m/µm, m/km); write the replacement (1 µm = 10⁻⁶ m) as the solutions do.
- solutions.md L2-04 — $d_\text{A}$, $d_\text{M}$ are correct; $d_\text{Aurinko}$, $d_\text{Maa}$ would match the lesson's descriptive subscripts.

## Checked
- All 12 answers recomputed independently and by answers.py: every one matches exercises.json within tolerance (L2-02 4,23 a with 365,25 d; L3-01 118 m; L3-03 375 cm).
- Rounding to the data's significant figures stays inside the tolerance in every task (L2-03 24 against 23,5 inside 0,03).
- L2-04 now asks the volume ratio, and Järkevyys says why solid spheres would fit fewer: the earlier packing error is gone.
- L2-02 years now from "how many year-lengths fit in t" with ':'; no s/a factor formula.
- Data realistic: lead atom 3,5·10⁻¹⁰ m and nucleus 1,4·10⁻¹⁴ m, Proxima 4,2 ly, Earth–Sun model 118 m, virus 10⁻⁷ m.
- Teacher's 2026-10-28 rules: \cdot throughout, no × or \times; divisions as operations with ':'; ratios as \frac with descriptive subscripts; no error quantity in this set.
- Orders of magnitude follow the glossary rule (a under about 3 → 10ⁿ); L3-02 20 against 15.
- Every solution has the seven parts, symbolic first; reasonableness checks are real checks.
- Scope inside FY1; s = ct and V ∝ d³ are given in the task text.
