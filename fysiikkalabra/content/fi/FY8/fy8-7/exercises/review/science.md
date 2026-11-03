VERDICT: PASS
CONTENT-HASH: 63f3b6ea06a48048
## Blocking

## Polish
- exercises/solutions.md:fy8-7-L3-02 — the answer key holds 2,03·10¹⁸ but the Vastaus gives 2,0·10¹⁸ (2 sig. figs from 1,0 W); both lie within the 2 % tolerance — consider making the key  2.0e18 so it matches the stated rounding.
- exercises/solutions.md:fy8-7-L3-01 — "yli puolet … eli vähintään N/2" mixes strict and non-strict; the closing remark ("inversio vaatii hieman tätä enemmän") already covers it — optionally write "noin N/2 (hieman yli)".
- exercises/solutions.md:fy8-7-L2-03 — the reasonableness check cites the lesson's quantum-dot table (3,0 nm → 530 nm), which the brief does not carry; I could not verify it — keep it only if it matches the lesson's table.

## Checked
- All 12 answers recomputed independently from the task text (hc/λ, P = (N/t)hf, η = λ_p/λ_L, N/2 inversion, P·λ_p/(2hc), c/(λf_q)); each agrees with the key within 0,9 %, inside tolerance 0,02.
- Previous blocker fixed: L1-04 intermediate 3,0·10⁻³ J · 1064·10⁻⁹ m = 3,192·10⁻⁹ J m, N = 1,6069·10¹⁶.
- answers.py: every line implements the physics of its task; units and tolerances fit the data.
- Solutions: symbolic first, conversions right, rounding follows the limiting datum, reasonableness checks numerically true (green 0,76 W < 1,0 W; qubit 2,07·10⁻⁵ eV; 1,17/1,53 eV; 3,27/2,04·10¹⁵ s⁻¹).
- Physics: ruby three-level with ground-state lower level, N₂ > N₁, quantum-defect limit, SHG energy conservation, quantum-dot size→gap trend, all consistent with the brief and glossary; within FY8 scope.
- Assumptions stated in tasks (no decay during pumping, one photon per pump photon, ideal conversion).
- Hash identical at start and end.
