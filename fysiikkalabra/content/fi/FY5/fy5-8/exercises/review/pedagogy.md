VERDICT: PASS
CONTENT-HASH: 4ae84ded355a8eeb

## Blocking
(none)

## Polish
- exercises.json fy5-8-L2-05 tolerance 0,05 — a student who wrongly keeps the 500 g point gets 23,4 N/m (4 % off) and passes; the exercise's lesson is to exclude it. Set tolerance 0,03 (24,4 ± 0,7).
- solutions.md L2-05 Kuvaajan lukeminen — the fitted-line points (0,050 m; 1,22 N) and (0,100 m; 2,44 N) appear without derivation, and Vastaus says "24 N/m" while Sijoitus and the stored answer are 24,4. Say "käsin sovitettu suora (tai laskimen sovitus origon kautta) antaa 24,4 N/m" and give 24 N/m or 24,4 N/m consistently; the same for L2-06 (24,525 vs "25").
- exercises.json L1-08 — repeats L1-04 (read k from a line); with L2-04 it also shares the figure ex-kaksi, so a student sees A's k in L1-08. Ask instead "kumpi jousi on jäykempi ja miksi" (plan level 2).
- exercises.json L3-04 b) — the area under a rubber band's loading curve is the work done, not all stored elastic energy; add "suuruusluokka-arvio" or "tehty työ" in the solution.

## Checked
- Counts 8/7/5, ids and levels fit; L1-06..08 conceptual/graph, L2 data/error/reasoning, L3 rubber band and jousipyssy per plan.
- Recomputed: L2-05 24,4 N/m; L2-06 24,525 N/m (venymä 8,0 cm, not 20,0 cm); L2-07 0,90, 0,30, Δ0,60 J; L3-04 0,255 J (0,36 J by formula, +41 %); L3-05 k = 302 N/m, 37,75 J, 27,6 J, 73 %. All match.
- L2-06 and L2-07 error analyses are real misconceptions, each named in the solution.
- L1-08 figure ex-kaksi values checked from figures.py: B passes (0,10 m; 2,5 N).
- Scope: Hooke's law validity, k from slope, E = ½kx² and area interpretation; nothing beyond slot.
- Solutions have full steps and sanity checks; Finnish and units fine.
- No 360 px exercise captures listed; overflow not judgeable from images.
