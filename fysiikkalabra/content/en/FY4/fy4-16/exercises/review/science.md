VERDICT: PASS
CONTENT-HASH: 9c8d836bec078c7a
## Blocking

## Polish
- content/en/FY4/fy4-16/exercises/solutions.md:435 (L3-05) — still "in uniformly changing motion the mean speed of an interval is the mean of its end speeds", applied to a deceleration that is not uniform (16.2 then 1.1 m/s per interval) — "the mean of the end speeds is used as an estimate of each interval's mean speed".
- content/en/FY4/fy4-16/exercises/solutions.md:403 (L3-04) — $W_{\mu 1}$ and $W_{\mu 2}$ appear after only $W_\mu = -F_\mu s$ is defined; name them "on the slope $W_{\mu 1} = -\mu_1 mg\cos\alpha\cdot L$, on the flat $W_{\mu 2} = -\mu_2 mgd$".
- content/en/FY4/fy4-16/exercises/solutions.md:129, 193, 403, 435 — label hyphen "Work-energy principle" vs the en dash "work–energy principle" in the Principle lines; use the en dash.

## Checked
- Captures opened: none (Formula rewrites and paragraph splits; judged from the diff and solutions.md).
- Round 1 Blocking fixed: L2-02 (129) $W_\mu = -F_\mu L$, L3-01 (193) $W_\mu = -F_\mu s$, L3-03 (236) and L3-05 (435) $W_\text{d} = -F_\text{d} h$, L3-04 (403) negative work on both parts; each now writes $E_\text{initial} + W = E_\text{final}$, agreeing with its Principle line and the glossary.
- The signed forms reduce to the unchanged equations: $mgL\sin\alpha - \mu mg\cos\alpha L = \tfrac12 mv_2^2$ ($\mu = 0.1373$), $mgh - \mu mg x = 0$ ($x = 37.5\,\text{m}$), $L = \mu_2 d/(\sin\alpha - \mu_1\cos\alpha) = 16.33\,\text{m}$, $v = 7.67\,\text{m/s}$, $F_\text{d} = mg + (E_{\text{k}0} - E_\text{k})/h$ ($2124\,\text{N}$, $2205\,\text{N}$).
- L1-04 stopping sled: $E_\text{k,final} = E_\text{k,initial} + W$, $W = -\mu mg s$, $s = 22.94\,\text{m}$; signed, right.
- L2-03: $\Delta E_\text{mech} = E_\text{final} - E_\text{initial}$, magnitude $221\,\text{kJ}$, consistent with negative air-resistance work.
- Lift and slope tasks: $\Sigma F = ma$ or $\Sigma F = 0$ with the positive direction stated first; results unchanged.
- New Reasonableness lines (L1-08 $mg\sin\alpha = 98.1\,\text{N}$; L3-04 $0.060 \cdot 15.85 = 0.95\,\text{m}$, $0.150 \cdot 20.0 = 3.00\,\text{m}$, sum $3.95\,\text{m}$; L3-05 mean acceleration $12.7\,\text{m/s}^2$) are right.
- Internal-energy wording follows P1; exercises.json presentation only.
- Hash identical at start and end.
