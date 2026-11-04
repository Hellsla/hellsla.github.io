VERDICT: PASS
CONTENT-HASH: 80734f621c253d2d

## Blocking

## Polish
- inquiry.json:364 (tarkistus-2 solution, Reasonableness) — "The radiation in the graph therefore has a slightly higher energy than that of caesium-137" infers photon energy from a 5 cm vs 4 cm half-value thickness, but concrete density and composition vary; the inference is not supported by the data (same in the Finnish source) — soften to "may have a somewhat higher energy, or the concrete is less dense" or drop the sentence.
- Packet: `check_lesson.py has not been run` for the translation; run the deterministic checks before release (not a physics finding).

## Checked
- One script recomputed every number from the task text with own formulas: worked example (D 1.67 mGy, H_T 33 mSv, H_E 4.0 mSv), siirto 12.5 µSv and all four mistake values (37.5, 25, 50, 750), virhe 1.2 mSv, koe-1/koe-2 model values (40/10/4.44/2.50; 40/20/10/5.00/1.25), 1 Gy → 2.4·10⁻⁴ K in water, shares 68 % / 86 % / 5×, chart and vaimennus graph (80 → 40 at 5.0 cm, 2.5 at 25 cm).
- ICRP 103 w_R (γ, β 1; α 20; n 2.5–20) and w_T (0.12/0.08/0.04/0.01, sum 1) correct; H_E notation explained.
- STUK-A263 figures (5.9, 4, 1.1, 0.76→0.8, <0.1 mSv), radon 94 Bq/m³, reference levels 300/200 (STM 1044/2018), dose limits 20/1 mSv (859/2018), Rn-222 T½ 3.82 d, Po-218/Po-214 alpha: correct and identical to the Finnish lesson.
- Cs-137 half-value thickness ≈ 5.5 mm Pb, ≈ 4 cm concrete agrees with narrow-beam μ/ρ (5.5 mm, 3.9 cm).
- Inverse-square law and half-value-layer model stated with conditions (small source, little air attenuation; narrow beam, scattered photons ignored, safety margin).
- Sim (shared sim.js) implements 40 µSv/h·(1 m/r)²·(½)^(x/6 mm), H = Ḣt; English UI strings in the 1280 px capture match the howto; experiments lock x,t / r,t and isolate the varied parameter; simState Hdot measured.
- Every choice item has exactly one correct option; distractor feedback names the right mechanism (spreading over 4πr², each layer halves what arrives, w_R and w_T).
- tarkistus-3 model answer and criteria: decay products, alpha w_R 20, lungs 0.12, stack-effect underpressure in winter — physically right.
- Figures painotus, etaisyys, suoja, lahteet: numbers match the text and are to scale where they say so.
- Exit ticket matches the theory.
