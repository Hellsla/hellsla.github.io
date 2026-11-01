VERDICT: PASS
CONTENT-HASH: 9f4b777715798bfc

Science review of fy14-classical-limits, 2026-11-01 (full review: unit.md, inquiry.json, teacher.md, figures.py, the modern-physics era of `assets/units/fy14/data/timeline.json`).

## Blocking
None.

## Polish
1. `inquiry.json` `hook`, sentence 5: "the rule for how heat energy is shared among the parts of a body". Heat is energy in transfer (guardrails). Write "how energy is shared among the parts of a body (equipartition)".
2. `unit.md` Worked example, Reasonableness: "turns most of its electrical energy into heat, not light". The energy leaves mostly as infrared radiation. Write "into infrared radiation (and heat), not visible light".
3. `inquiry.json` `camera`, mistake 27.2: the label "You multiplied instead of dividing" fits only if the powers of ten are also dropped ($2.898 \cdot 9.4$). Either say "you multiplied $2.898$ by $9.4$" or drop the entry.

## Checked
- Recomputed with exact h, c, k_B (Python): Wien peaks 2000–6000 K (1449, 966, 724, 580, 483 nm, also as the numerical maximum of Planck's law), 10 000 K → 289.8 nm, mistake 805 nm; 9.4 µm → 308.3 K; 400 °C → 4.31 µm (wrong 7.2 µm); worked example 1.073 µm, 1.851·10⁻¹⁹ J, 1.155 eV; visible 1.65–3.26 eV; CMB 1.06 mm; Stefan factor 16.
- Figures: `curves` peak positions and heights (0.402 and 0.132 of the 6000 K peak) agree with Planck's law; `catastrophe` Rayleigh–Jeans reaches 2.0 × the Planck peak at 1127 nm, agrees in the drawn tail; `spectrum` boundaries and the 380–750 nm band are at the right log positions.
- Physics: equipartition over standing-wave modes, the catastrophe as a model prediction, Planck's quantised exchange vs Einstein's light quanta, k_BT argument, the iron-bar colour sequence (peak stays infrared; text does not claim otherwise). Every choice has exactly one correct option with correct distractor feedback.
- History (WebFetch, en.wikipedia.org, 2026-11-01): Kelvin, Royal Institution, 27 April 1900, clouds = aether and equipartition; Planck 19 Oct and 14 Dec 1900; Rayleigh 1900 / Rayleigh–Jeans 1905; Ehrenfest 1911; Wien 1893. Timeline order 1900, 1905, 1911, 1913, 1924, 1928 matches the data.

## Shared issues
- `assets/units/fy14/data/timeline.json` `aston-1919`: "about 0.8 percent" lighter than four hydrogen atoms. Modern masses give 0.71 % ((4·1.007825 − 4.002603) : 4.031300); 0.8 % is roughly the 1920 value. Write "about 0.7 percent" (or "Aston's numbers gave about 0.8 percent; today's value is 0.7 percent") so it agrees with the chapter 2 binding-energy numbers. Not blocking here.
- The developer's shared issue 3 (Bohr 1913 place) is already fixed in timeline.json (Copenhagen).
