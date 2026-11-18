VERDICT: PASS
CONTENT-HASH: 856d6753f79d091c
Mode: delta (round 2)

## Blocking

## Polish
- content/fi-easy/FY4/fy4-8/exercises/solutions.md (L2-09 Kaava) — "Siis $-F_\mu s$ on sama kuin $(E_\text{p} + E_\text{k}) - (E_{\text{p}0} + E_{\text{k}0})$" puts an equation in words. One formula, $-F_\mu s = (E_\text{p} + E_\text{k}) - (E_{\text{p}0} + E_{\text{k}0})$, is clearer.
- solutions.md:150, 276 — the earlier items (the significant figures of $h$; 1500 kg) are still open. They are not part of this change.

## Checked
- Hash 856d6753f79d091c at the start and the end. Only the Kaava lines of solutions.md and some paragraph splits changed. No number, answer or tolerance changed. The exercises.json change is presentation only.
- Each Kaava now starts from its basic equation and then sets each term from the situation:
  - energy conservation, $E_{\text{p}0} + E_{\text{k}0} = E_\text{p} + E_\text{k}$: L1-01, L1-02, L1-05, L1-06, L2-05, L2-08;
  - the energy principle, with $W$: L1-08, L2-01, L2-02, L2-07, L2-09, L3-04;
  - the work principle, $E_{\text{k}0} + W = E_\text{k}$: L1-04, L1-07, L1-09, L2-06.
- Every resisting force has signed work: $W = -F_\mu s$, $W = -F_\text{vast} s$, $W = -F(L + s_\text{ka})$ and $W = -FL$. The stick's work is $+Fs$, along the motion. The signs are right.
- L2-07 (radan A–D): the step now says $E_{\text{mek}0} + W = E_\text{mek}$, then $W = -F\Delta s$, then $F = -W/\Delta s$. The values 94, 107 and 157 N are unchanged.
- L3-05: $r_n = mgh_{n+1}/(mgh_n) = h_{n+1}/h_n$, and $\Delta E = mg(h_0 - h_1)$. Both are right.
- L2-10: only the paragraph splits changed, word for word the same.
- The notation matches the brief's lesson ($E_{\text{p}0} + E_{\text{k}0} + W = E_\text{p} + E_\text{k}$).
- Captures opened: none. I judged from the diff and the packet.
