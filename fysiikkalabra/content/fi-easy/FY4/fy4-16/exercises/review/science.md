VERDICT: PASS
CONTENT-HASH: 90c89598d4a1e0f7
Mode: delta (round 2)

## Blocking

## Polish
- content/fi-easy/FY4/fy4-16/exercises/solutions.md:351 (L3-05 Kaava) — the new clause "tasaisesti muuttuvassa liikkeessä välin keskinopeus on päätenopeuksien keskiarvo" states the condition, but the canopy deceleration is not uniform. Add "likimain" to the sum for $h$.
- solutions.md:179 (L3-01 Kaava) — still open: "$x = s\cos\alpha$" uses $s$ for each part's own length. Name the length per part.
- solutions.md (L3-04, L3-05 Järkevyys) — still open: a one-sentence paragraph is left after the breaks.

## Checked
- Hash 90c89598d4a1e0f7 at the start and the end.
- The round 1 Blocking item is fixed. Every resisting force's work is now signed, and the balance is written as $E_\text{alku} + W = E_\text{loppu}$:
  - L2-02: $W_\mu = -F_\mu L$;
  - L3-01: $W_\mu = -F_\mu s$, each part $-\mu mg x$;
  - L3-03: $W_\text{v} = -F_\text{v} h$;
  - L3-04: $W_{\mu 1} + W_{\mu 2}$ with $W_\mu = -F_\mu s$;
  - L3-05: $W_\text{v} = -F_\text{v} h$.
- The signed form agrees with L1-03 ($W = -F_\mu s$) and with the brief's lesson.
- The equations after each lead-in are unchanged and right. Results recomputed: $\mu = 23{,}71/172{,}72 = 0{,}1373$, $x = 4{,}50/0{,}120 = 37{,}5\,\text{m}$, $F_\text{v} = 686{,}7 + 1437{,}3 = 2124\,\text{N}$, $L = 3{,}00/0{,}1837 = 16{,}33\,\text{m}$, $v = 7{,}67\,\text{m/s}$.
- The Newton's-law Kaava lines (L1-01, L1-05, L2-03, L2-08, L3-02, the lift tasks) now open from $\Sigma F = ma$ or $\Sigma F = 0$ with the positive direction stated. The signs are right.
- L2-03: $\mu mg = m|a|$ uses $F_\mu = \mu N$ with $N = mg$. This is right.
- Hoist: $T = mg$, $W = Th$, $P = W/t$. This is right.
- The exercises.json change and the Mallivastaus splits are presentation only, word for word the same.
- Captures opened: none. I judged from the diff, the file on disk and the packet.
