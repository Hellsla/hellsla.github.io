VERDICT: FAIL
CONTENT-HASH: bde30bba307db58e

## Blocking
- solutions.md:129 (L2-02), :193 (L3-01), :236 (L3-03), :403 (L3-04), :435 (L3-05) — the rewritten Kaava steps define the work of friction or air resistance as positive ("The work of friction is $F_\mu L$", "$W_\mu = F_\mu s$", "$W_\text{d} = F_\text{d} h$") and write the principle as $E_\text{initial} = E_\text{final} + W$. That contradicts the same solutions' Principle lines ("sliding friction does negative work", L3-05 "its work is $-F_\text{d} h$"), the glossary's energiaperiaate $\Delta E_\text{mek} = W_\text{muut}$ (signed work) and L1-04 of this set ($W = -F_\mu s$, $E_\text{k,final} = E_\text{k,initial} + W$).  The final equations are right — write the work signed, $W_\mu = -F_\mu s$ (and $W_\text{d} = -F_\text{d} h$), with $E_\text{final} = E_\text{initial} + W$ as in L1-04 and the glossary; or name the positive quantity $|W_\mu| = F_\mu s$ and write $E_\text{final} = E_\text{initial} - |W_\mu|$. The Finnish file has the same wording (fi solutions.md:179, :334), so fix it there too.

## Polish
- solutions.md (L3-05, Formula) — "in uniformly changing motion the mean speed of an interval is the mean of its end speeds" is applied to a deceleration that is not uniform (the speed falls by 16.2 and then 1.1 m/s per interval) — "the mean of the end speeds is used as an estimate of each interval's mean speed (the trapezoid rule)".

## Checked
- Hash bde30bba307db58e at start and end; answers, tolerances, tasks and ids unchanged; exercises.json paragraphs only.
- Captures: none opened; judged from the text and the packet's diff.
- Lift tasks (L1-01, L2-01, L3-02, L2-05, L2-09): $\Sigma F = ma$ with the stated positive direction first; $N = m(g + a)$, $a = g(L/m - 1)$, $v = v_0 + at$ with $v_0 = 0$ give the unchanged results.
- L1-03 chute: $E_\text{initial} = E_\text{final}$, $v_2 = \sqrt{2gh} = 7.924\,\text{m/s}$; the normal force does no work, stated.
- Constant-speed slopes (L1-05 angle, L2-07 box): $\Sigma F = 0$, $F_\mu = \mu N$, $N = mg\cos\alpha$ give $\tan\alpha = \mu$.
- L2-03: $\Delta E_\text{mech} = E_\text{final} - E_\text{initial}$ written with both energies; $221\,\text{kJ}$ unchanged.
- L2-04 lift car: $\Sigma F = 0$, $W = Th = mgh$, $P = W/t = 6.67\,\text{kW}$.
- L3-01, L3-04: each part's friction work $\mu mg x$ (horizontal length) is right; $x = h/\mu = 37.5\,\text{m}$, $L = 16.33\,\text{m}$, $v = 7.67\,\text{m/s}$ follow; L3-04 now substitutes into the last symbolic form.
