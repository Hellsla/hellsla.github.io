VERDICT: PASS
CONTENT-HASH: f258a83e4f50ee9b

## Blocking

## Polish
- sim.js:1054 — after a slow push and pull-out the readout shows "T = 293 K (ΔT = −1 K)", because T = 292,57 K rounds to 293 and ΔT = −0,58 K rounds to −1. Fix: compute ΔT from the rounded T, or show ΔT to one decimal.
- inquiry.json:411 — at "T noin 293 K" the logged values are still Q −34,9 J, ΔU +0,1 J, and the logged T is 294 (293,5 K). They reach −35,1 J and 0 only later. Fix: "odota, kunnes ΔU on 0,0 J".

## Checked
- All 12 answers.py values, siirto 5,4 J (mistakes 6,6 and 599,4) and check-2 30 J (mistakes 230 and 10) recomputed: they match.
- Playwright, insulated, slow push: W = ΔU = 40,83 J, T 406,9 K, ΔT 113,7 K, p 1,85. The vx-only adiabatic theory gives 40,93 J and 407,15 K. A push 3,7 s after Alkuun gives the same numbers.
- Insulated, fast push: W = ΔU = 47,25 J, T 424,8 K, ΔT 131,6 K, done in 1,25 s. The real buttons at 3× give the same. ΔT/W = 2,786 K/J at both speeds, which is 1/C. pred-2, koe-1 and sim-spec agree.
- "Larger relative hit speed": each hit transfers momentum 2m(vₓ+u) and the hit rate is ∝ (vₓ+u), so the force on an advancing piston is ∝ ⟨(vₓ+u)²⟩, more than in the quasi-static case. Fast compression is irreversible, so 47,2 J > 40,9 J is correct. The real-pump caveat (v_rms ≈ 500 m/s) is right.
- Conducting, slow push: W 35,06 J, final Q −35,06 J, ΔU 0, 293,15 K, p 1,333. This matches koe-2, pred-1 (1,33 p₀, 35 J) and the koe-2 question.
- Real 0,50 g of air: adiabatic ΔT 35,8 K and W 12,8 J; isothermal W 12,1 J. Piston pressure 2,37 p₀ against the readout's 1,85. Lisätietoja is correct.
- Piston speed ratios: 213/4 ≈ 53 ("noin 50") and 213/60 ≈ 3,55. The slow stroke takes 75/4 = 18,75 s ("noin 19 s").
- ΔU − (Q + W) = 0 to rounding in every run.
- pred-2's correct option and all wrong-option feedback are consistent with the sim. check-3 (real pump: the difference comes through Q) does not contradict the model.
- Worked example, solutions (symbolic first, "ideaalikaasun"), exit ticket and check-1 are sound. Scope is the first law only.
