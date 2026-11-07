VERDICT: FAIL
CONTENT-HASH: 24c498bba9ee31a5

## Blocking
- A — solutions.md:39 (L1-04 Järkevyys) — "Taso [83 dB under the protectors] on kuitenkin yli alemman toiminta-arvon 80 dB" compares the level under protectors with an action value. Action values are applied to the exposure without protectors (VNA 85/2006); what the protected level is compared with is the limit value 87 dB(A). — Fix: "Ilman suojaimia taso 106 dB ylittää kummankin toiminta-arvon, joten suojaimia on käytettävä. Korvalle tuleva 83 dB jää raja-arvon 87 dB(A) alle, mutta vertailuannoksen alittaminen ei takaa kuulon turvallisuutta."

## Polish
- solutions.md:103, 105, 204, 207, 219 (L3-01, L3-04) — t_{sall,i} is left over beside the renamed t_v; rename to t_{v,i}.

## Checked
- light delta review (teacher 2026-11-07): only the passages changed against origin/main were judged, in context, not a full review; packet says Mode full; per the teacher only the diff was judged. 'Vertailuaika/energia-annos' rewording of L1-01, L2-01, L2-07, L3-05 stems and solutions correct; recomputed 2,0 h, 4,0 h, 1,875 min, 92 dB → 1,59 h and 190 %, 86 dB → 6,35 h and 47 %; L3-01 125 % gives L_EX,8h ≈ 86,0 dB(A), so 'ylittää ylemmän toiminta-arvon' is right; the L2-08 option feedback (85 dB unprotected exceeds 80 dB) is right; answers.py unchanged.
