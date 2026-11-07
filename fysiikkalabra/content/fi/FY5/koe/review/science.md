VERDICT: FAIL
CONTENT-HASH: 83bee0fd7c13c8b2

## Blocking
- B — tasks.json:986 (k7 stem) and solutions.md:506 (k7 b Periaate) — 'A-painotettuja äänenpainetasoja … oletetaan vapaan äänikentän tasoiksi, joten niitä käsitellään äänen intensiteettitasoina' gives the free field as the reason. In a free field only the unweighted SPL equals the intensity level; an A-weighted reading can differ by several dB (concert bass), and k7 a computes an absolute intensity from it. — Fix: 'Tehtävässä oletetaan, että ääni etenee vapaasti ja että A-painotus ei juuri muuta lukemaa, joten tasoja käsitellään intensiteettitasoina.' and the same in b Periaate.

## Polish

## Checked
- light delta review (teacher 2026-11-07), round 2: HEAD~1 diff and the whole diff against origin/main (earlier FAIL). k7 c now compares 95 dB without plugs with the action values and 83 dB at the ear with 87 dB(A): earlier Blocking fixed; k7 b 'alle vertailutason 85 dB': Polish fixed. Recomputed: 2,0·10⁻² W/m², ×63; 7,5 min; 2,0 h (L_EX 88 dB > 87); 95,0 dB; 12,7 h (L_EX 80 dB); 150 %; 40,3 h, 9,9 %. k1 c wording right.
