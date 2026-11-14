VERDICT: FAIL
CONTENT-HASH: e93513bb291d3171

## Blocking
- solutions.md:249 (L2-09, Järkevyys) — A: "eikä kappale enää hehku" at 1000 K (727 °C) is wrong: a body at 1000 K still glows dull red, and this set's own L3-05 puts the end of the glow at 800 K — fix: "Uusi huippu on kaukana infrapuna-alueella; kappale hehkuu enää himmeän punaisena, koska vain pieni osa säteilystä on näkyvää valoa."

## Polish
- solutions.md:238 (L1-09) — "1,4 · 5772 K ≈ 8200 K": 1,4 · 5772 K = 8081 K; use the ratio 502 : 350 = 1,43, giving ≈ 8300 K.

## Checked
- Delta: L1-09 and L2-09 added; hash identical at start and end.
- L1-09: T = b/λ_max with MAFY b = 2,8978·10⁻³ m·K: 8279 K = answers.py; black-body assumption stated; 350 nm is UV, right.
- spectrum-task: Planck curve at 2415 K, peak computed at 1,200 µm and height 1,057 MW/(m²·µm), as the description says.
- L2-09: λ₂ = b/T₂ = 2,898 µm, shift 1,698 µm = answers.py; 2 % tolerance fits.
