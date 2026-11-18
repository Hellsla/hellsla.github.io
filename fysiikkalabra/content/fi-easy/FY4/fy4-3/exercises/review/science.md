VERDICT: PASS
CONTENT-HASH: ca39db1b688f8190
## Blocking

## Polish
- lessons/FY4/fy4-3/figures.py:433 — at $t = T_1 = 0{,}15\,\text{s}$ the float $\sin^2\pi \approx 10^{-32} > 0$ lets the noise in, so the readings are $0{,}03\,\text{N}$ and $0{,}01\,\text{N}$ instead of exactly 0 (invisible at the 5 N scale, but L2-09 says "palaa nollaan hetkellä 0,15 s") — test `T0 < t < T1` or round F before `F > 0`.
- content/fi-easy/FY4/fy4-3/exercises/solutions.md (L1-09 Kaava) — $F_{AB} = |F_B|$ follows directly from what sensor B measures; the third law is what makes $|F_A| = |F_B|$ a check. One clause "kolmannen lain mukaan myös $|F_A|$ on sama" would make clear which law gives what.
- content/fi-easy/FY4/fy4-3/exercises/solutions.md (L2-06) — $v_\text{k}$ now names the mean of six readings, $\Sigma v / n$, while the course (FY4.1) defines $v_\text{k} = \Delta x / \Delta t$; for constant velocity they coincide, but "lukemien keskiarvo" in words would avoid two meanings of one symbol.
- content/fi-easy/FY4/fy4-3/exercises/solutions.md (L3-03, L3-05, paragraph splits) — new paragraphs open with "Kolmannen lain mukaan …" and "Voimat ovat silti …", which lean on the previous paragraph; acceptable.

## Checked
- New L1-09 (answer 4,0 N, tol 4 %): generator data at 0,10 s give $F_A = -4{,}02\,\text{N}$, $F_B = +3{,}94\,\text{N}$; both inside the tolerance; direction "oikealle" right for a positive reading of B.
- New L2-09 (0,10 s, tol 10 %): readings are zero up to 0,05 s and from 0,15 s (data recomputed, 0,01 s steps); $\Delta t = t_2 - t_1 = 0{,}10\,\text{s}$; answers.py prints 4.0 and 0.1.
- Figure and its description give every value the tasks need (time grid at 0,05 s steps, ±4 N gridlines); neither marks the answer.
- Both new tasks and their answers, units, tolerances and figure equal the Finnish set.
- Kaava rewrites: every balance now opens from $\Sigma F = 0$ (first law) and then solves; signs and algebra right in all thirteen; numbers unchanged.
- L3-05: "Oppilasta ei vedä kärry vaan köysi" corrects the earlier third-law pairing (cart–rope, rope–hand): right.
- L3-05 Kaava $F_\text{ka} - F_\text{k} = 0$ at constant velocity, $10{,}2/3 = 3{,}40\,\text{N}$ recomputed.
- L2-08 "Esimerkkiarvot:" removed and captions' marker removed: no physics change.
- Captures opened: none (judged from the text, the generator data and the packet).
