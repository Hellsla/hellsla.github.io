VERDICT: FAIL
CONTENT-HASH: c355f45d310c2f53

## Blocking
- solutions.md:382 and tasks.json:464 (fy8-s3 d, conclusion) — A, an error: "with this counting time the tube cannot distinguish it from the variation of the background" / "the tube can no longer distinguish it". At r ≈ 36 cm the net rate equals the background, 22.4 1/min. In a 1.0 min count that is about 45 pulses against 22.4 ± 0.9 (five-minute background), so net = 22 ± 7 1/min, about 3σ. The source is still clearly detected there, and a student who says so would lose the point. — Write that the source's count rate (and dose rate) has fallen to the size of the background, so further away it is soon lost in the background's random variation; the radiation does not stop. Use the same words in the rubric detail and in the Finnish version.

## Polish
- solutions.md fy8-s3 a/b — Cs-137 also emits beta particles, which air absorbs over tens of centimetres. One clause saying the tube is taken to count the 662 keV gamma photons (or the betas are stopped by the capsule) would make the inverse-square model's condition explicit.

## Checked
- One script recomputed every number from the task data: s1 2.223 / 1.968 eV, λ_3 = 295.9 nm, n = 1193, λ_max = 1107 nm, 0.83 eV; s2 Q = 5.594 MeV, A = 2.232·10¹⁵ Bq, m = 3.52 kg, 83 %, 1791 W, 98.5 W, H_E = 0.566 mSv, Po 0.160; s3 r = 36.2 cm, H = 0.229 μSv/h (0.272 with r + d); s4 7.16, 0.8575, 136 s, 1:5 → 271.5 s; s5 3.67 %, 3.49 a, 5.8 t U-235, 82 988 half-lives. All agree with answers.py and the solutions.
- Physics: oxygen 557.7 nm = 4.19→1.97 eV and 630.0 nm = 1.97→0, lifetimes 0.7 s / 110 s and collisional quenching; Q from atomic masses with the electrons cancelling; P = AQ, A = λN; dose chain D, H_T = w_R D, H_E = w_T H_T; inverse-square law with an offset d; n → p e⁻ ν̄ by the weak interaction, d → u; Y = 2N_n/(N_n + N_p); Oklo enrichment, water as moderator and void feedback.
- Kaava steps start from basic laws (E = hf, c = fλ, Q = Δm c², P = AQ, E = Pt, E = NQ) before the combined formula.
- Scope: everything is in FY8 central contents; no later-course physics.
- Sig figs and rounding reasons justified (5 keV → about 1200, order-of-magnitude powers → 3.5 a, 2.0·10⁹ a → 3.7 %).
- Rubric criteria match what each task gives and asks, and the points add up (15, 20, 17, 16, 16). Alternative methods are listed (e^{−λt}, 1240 eV nm, two-point d, ratio form).
- s3 data is labelled as model data with random variation added; no invented data is presented as measured.
- Hash c355f45d310c2f53 at start and end.
