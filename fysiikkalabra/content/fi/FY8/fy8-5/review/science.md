VERDICT: FAIL
CONTENT-HASH: 2af55821b25eb665

## Blocking
- lesson.md:177 and lesson.md:1401 (Tiivistelmä) — **B**: "Mitä enemmän aallossa on solmuja, sitä suurempi on tilan energia" is stated for atoms in general. It is true only in hydrogen. In K and Ca, 4s (3 nodes) lies below 3d (2 nodes), which students know from chemistry. — Fix: write "Vetyatomissa: mitä enemmän solmuja, sitä suurempi energia" in both places, or "saman muotoisilla tiloilla (s, p, …)".

## Polish
- lesson.md:179 (string figure aria-label) and inquiry.json:355 (tarkistus-2 feedback "kuten kielessä, jokainen lisäsolmu nostaa värähtelytavan energiaa") — a string's energy also depends on its amplitude; the nodes set the frequency. — Write "taajuus" for the string.
- lesson.md:245 (cloud figure) — the figure is a projection: 48 grey dots appear inside the 0,14 nm circle, but the aria-label says the grey dots are outside. — Add "läpivalaisu: osa harmaista on rajan edessä tai takana", as the sim's model box already says.
- sim.js:193 `boundary()` — for 2s it draws only the outer circle (R = 0,483 nm). The region's gap around the node, r ≈ 0,096–0,118 nm, is not drawn, so grey hits there appear inside the tinted disk. — Draw the two inner circles, or say this in the model box.
- inquiry.json:387 (tarkistus-3 Järkevyys) — "noin kolminkertainen näkyvän valon fotoneihin verrattuna": 10,2 eV is 3–6 times 1,6–3,3 eV. — Write "noin 3–6-kertainen".
- lessons/FY8/fy8-5/lesson-answers.py:74 — the key "tarkistus-2" computes tarkistus-3 (10,2 eV). — Rename it.

## Checked
- Recomputed: 656,47 nm; 10,2 eV and the mistakes 17,0 and 3,4; n², 2n². 1s: R90 = 0,1408 nm and peak a0. 2s: node 5,27 % and peak 0,277 nm. 2p: peak 0,212 nm. R90 is 0,483 nm for both 2s and 2p.
- Both figures that say they are to scale are to scale (cloud and energy levels).
- Ran sim.js sampling headless, seeds 1–5. The samplers and thresholds are correct, and seed 1 with N = 1000 gives 82 outside, which matches the feedback.
- 1s rpeak is 0,05 in every seed. 2s rpeak is 0,25–0,29 and 2p 0,19–0,23, which matches "0,2–0,3 nm" in johtopäätös.
- koe-1 and koe-2 each vary only one parameter, and simState holds every measured key.
- Every prediction, Etsi virhe and check has exactly one correct option, and the distractors' feedback is right. siirto: 2700, σ ≈ 39.
- No de Broglie or Schrödinger anywhere. The model stays qualitative, as the teacher decided.
