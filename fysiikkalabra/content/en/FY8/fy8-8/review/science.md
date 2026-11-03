VERDICT: PASS
CONTENT-HASH: 0e1654f7d66a7eee

## Blocking

## Polish
- lesson.md:"Energy levels of the nucleus" — "typically tens of kiloelectronvolts or more, hundreds of thousands of times larger" than eV: tens of keV is ~10^4 times an eV; the 10^5–10^6 factor holds for hundreds of keV–MeV (Co-60, Cs-137). Say "hundreds of kiloelectronvolts or more" or "ten thousand to a million times" (C, carried from the Finnish source).
- inquiry.json:kertaus correct feedback — "Today the same principle is carried over" reads oddly; "In this chapter the same principle…".
- figure fy8-8/spectrum (shot fig-5) — the vertical-axis label "fotonien määrä" and the aria-label are still Finnish; "number of photons".

## Checked
- Recomputed in one script: worked example 1.0600e-13 J, λ = 1.874 pm, ratio to 500 nm ≈ 2.67e5; tarkistus-2 8.826 pm; kertaus 1.89 eV; siirto 7 alpha / 4 beta; gammaspektri 2505.7 keV.
- U-238 chain in sim.js and lesson-answers.py: 15 nuclides, every step obeys α (Z−2, A−4) / β− (Z+1); 8 α, 6 β−; stable cells Tl-203…Bi-209 correct as [Z, N].
- Co-60 levels 2505.8/1332.5 keV and gammas 1173.2/1332.5 keV match ENSDF; recoil explanation (≈0.03 keV total) correct; levels figure to scale.
- Decay equations, shift figure (α: Z−2, N−2; β−: Z+1, N−1; β+: Z−1, N+1), chart-of-nuclides β−/β+ sides correct.
- Beta-electron created in the decay, weak interaction, continuous beta spectrum vs discrete alpha/gamma: correct.
- Every prediction and choice item: exactly one correct option, distractor feedback physically right.
- Sim runtime labels translated (Decay, Speed, Reset, readout) consistent with the howto; model limits stated.
- Exit ticket: Po-210 → Pb-206 + α; C-14 6 p, 8 n.
- Translation introduces no change of physics versus the passed Finnish source.
