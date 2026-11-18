VERDICT: PASS
CONTENT-HASH: 9c8d836bec078c7a

## Blocking
None.

## Polish
- solutions.md:403 and :435 (Formula rows) — still about 110-120 words each; split after the first derived result (earlier polish, open).
- solutions.md:228 vs :236/:435 — the sign of the air-resistance work is explained in words at :228 only; the later rows rely on it, which is fine for a reader going in order.
- "$E_\text{initial}$/$E_\text{final}$" are still not defined once in words (earlier polish).

## Checked
- Round 2, delta (work queue 8g): five Formula rows changed (L2-02, L3-01, L3-03, L3-04, L3-05); no number, answer, task or tolerance changed.
- Friction and air-resistance work is now signed in every row ($W_\mu = -F_\mu s$, $W_\text{d} = -F_\text{d}h$) and the equation is written $E_\text{initial} + W = E_\text{final}$; I grepped the whole file and found no unsigned work left (line 68 was already $-F_\mu s$).
- Results unchanged and still follow: $\mu = (gL\sin\alpha - \tfrac12 v_2^2)/(gL\cos\alpha)$, $x = h/\mu$, $F_\text{d} = mg + (E_\text{k0} - E_\text{k})/h$, $L = \mu_2 d/(\sin\alpha - \mu_1\cos\alpha)$ and $v = \sqrt{2gL(\sin\alpha - \mu_1\cos\alpha)}$.
- Substitution rows untouched and still use the last symbolic form.
- Captures not opened: text-only change.
