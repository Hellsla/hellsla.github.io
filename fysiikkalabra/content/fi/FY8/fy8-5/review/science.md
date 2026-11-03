VERDICT: PASS
CONTENT-HASH: 9bd5989c80f873f4

## Blocking

## Polish

## Checked
- Round-1 fixes are in: "vetyatomissa" now qualifies "mitä enemmän solmuja, sitä suurempi energia" in the Ydinajatus, the Tiivistelmä and tarkistus-2, with "saman muotoisiin tiloihin" for many-electron atoms. The string figure and feedback say "taajuus", the cloud figure is marked "läpivalaisu", tarkistus-3 says "3–6-kertainen", and the lesson-answers key is renamed.
- sim.js 2s boundary: the even-odd path of three circles (R, g1, g0) leaves the gap at 0,0961–0,1177 nm untinted, which matches the model box and sim-spec. The gap radii agree with my exact radial integration.
- Recomputed in one script (my own integrals, independent of lesson-answers.py): 656,47 nm; 10,2 eV, with the mistakes 17,0 and 3,4 eV; ratios 3,1 and 6,4. 1s R50 is 0,0707 nm and R90 0,1408 nm. The 2s node holds 5,27 %, and the region's inner ball 5,25 %. R90 is 0,4831 nm for 2s and 0,4829 nm for 2p. The peaks are a0, 0,277 nm and 0,212 nm.
- Ran the sim's own sampler headless, seeds 1–5. 1s gave N = 10 → 8, 9, 9, 10 and N = 1000 → 918, 901, 908, 903, which matches the feedback of ennuste-1. The 1s rpeak was 0,05 nm in every seed, and about 90 of 5000 hits fell beyond 0,2 nm. The 2s rpeak was 0,25–0,29 nm and the 2p 0,19–0,23 nm, so johtopäätös's "0,2–0,3 nm" and "0,48 nm" hold.
- Samplers are correct: 1s Γ(3, ½), 2p Γ(5) with μ = ∛(2u − 1) for the cos² law, and 2s an inverse CDF. binProb normalisations 0,25, 8 and 24 are right.
- Binomial claims: P(8–10 of 10) = 93 %, σ(1000) = 0,95 points, siirto 2700 with σ ≈ 39.
- Figures: the cloud figure (90 % circle 0,14 nm against the 0,1 nm bar) and the energy-level figure are to scale. The nodes figure is labelled "ei mittakaavassa" and shows the right node counts.
- koe-1 varies only N and koe-2 only orb, and simState holds k, out, frac, rpeak and R.
- Every choice item (kertaus, ennusteet, virhe, tarkistus-1/2) has exactly one correct option, and the distractors' feedback is right. The exit ticket (N: 1s² 2s² 2p³) is correct.
- Scope: no de Broglie and no Schrödinger equation. E_n is given as data, and the model is qualitative (standing waves, probability, threshold region), as the teacher decided.
