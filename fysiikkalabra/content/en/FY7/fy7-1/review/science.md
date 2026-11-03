VERDICT: PASS
CONTENT-HASH: 509c09404476f503

## Blocking

## Polish
- inquiry.json:129,141,200,212 — the experiments' `names`/`values` keep Finnish strings ("magneetti", "mukana", "pois"); the page shows "Kept constant: direction φ, magneetti, Earth's field" (shot exp-exp-1-390-2) — translate to "magnet", "on", "off" (language only, not physics).

## Checked
- Fidelity: every number in lesson.md, inquiry.json and exit-ticket.json matches the Finnish source (scripted comparison of all numerals; none added or dropped).
- Terms: magnetic flux density, tesla, inclination, magnetic domains, ferromagnetic, Curie temperature, field lines used correctly; Earth's magnetic south pole near the geographic North Pole stated consistently in theory, misconception, summary, check-1.
- Recomputed: B_h = 52 cos 74° = 14.3 µT, B_v = 50.0 µT; worked example 14 tan 52° = 17.9 µT, total 22.7 µT both ways; virhe 22.8 µT / 52.1°; siirto 37.6° with mistakes 55.0°, 59.0°, 52.4°; exit ticket 5000 µT, ratio 96.
- Sim model (two poles ±4 cm, 1/d², B_m = 30.0 µT at 10 cm): exp-1 B_m 30.0/15.5/9.15/2.87 µT, θ 65.0/47.9/33.2/11.6°; ratio 10.45 (answer 10.4, readout route 10.3 inside tolerance); exp-2 θ = 90° on both axis sides, −90° at the side — all inquiry texts agree.
- Predictions: pred-1 correct option (≈3 µT, about a tenth) and the 1/r² single-pole distractor feedback right; pred-2 west correct; exp-2 choice and check-2 (like poles, kind undeterminable) exactly one correct.
- Worked example direction: S pole facing the compass from the east gives B_m east — correct; vector-sum and inclination figures to scale (140:98 px = 20:14; 60:210 px ≈ 14:50).
- Scope: no para-/diamagnetism (aluminium/copper "effects too weak" is a fair C), Curie point qualitative.
- Sim UI translated at runtime (shot sim-390): readout B = 33.1 µT at 10 cm matches √(30² + 14²).
