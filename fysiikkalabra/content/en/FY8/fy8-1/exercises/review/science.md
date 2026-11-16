VERDICT: PASS
CONTENT-HASH: 9939aab4e79fce7e
Mode: delta (added aineisto task fy8-1-L2-10)

## Blocking
(none)

## Polish
- exercises/solutions.md:431 — the Answer says the slider is read "to about $\pm 10\,\text{nm}$", while Given (line 408) says a reading "can differ by a few nanometres" — use one statement (the 530–550 nm range is the honest one).
- exercises/solutions.md:412 — "Other metals need a shorter wavelength" holds for the five named metals (W 2.9–6.3 eV) but the unknown "?" metal's work function is not verified — say "the other named metals".

## Checked
- Recomputed: f0 = c/539 nm = 5.562e14 Hz, hf0 = 3.686e-19 J = 2.30 eV; answers.py 2.3006; box 2.3 eV with relative tolerance 0.05 (2.19–2.42 eV) covers readings 513–567 nm, so 530–550 nm (2.25–2.34 eV) is inside.
- Sodium W = 2.3 eV in the PhET model gives λ0 = 539 nm, consistent with the example reading; the lesson's 2.28 eV gives 544 nm as the Reasonableness says.
- Source claims (metals, work functions of zinc 4.3 eV and platinum 6.3 eV, wavelength and intensity sliders, current and energy graphs) are within the verified list; the 538/540 nm reading is labelled as a dated example.
- Principle hf0 = W and the threshold condition hf ≥ W stated correctly; symbolic f0 = c/λ0, E = hf0 before substitution.
- Part c): intensity changes the current, not E_k,max; frequency raises E_k,max = hf − W; stopping-voltage method correct.
- Part d): wave-model predictions (threshold-free emission, intensity-dependent energy) correctly contrasted with observations.
- Two significant figures justified by the slider reading.
- Hash 9939aab4e79fce7e at start and end.
