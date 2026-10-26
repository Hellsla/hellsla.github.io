VERDICT: PASS
CONTENT-HASH: e5b5703e06dfc20f

## Blocking

## Polish
- sim.js:133 — the "light, freely moving piston" is drawn fixed at the rim during boiling and the steam phase, which looks like the rigid closed vessel the model text explicitly excludes. Let the piston rise a little as the liquid fraction falls (still not to scale, as stated), so the picture matches the constant-pressure model.
- inquiry.json:132 (`simulaatio.model`) — under a piston at constant pressure part of the heater energy becomes the steam's work on the piston (p ΔV ≈ 170 kJ/kg at 101 kPa, about 7,5 % of r). The tabulated r = 2260 kJ/kg and c_p = 2,0 kJ/(kg·K) already include it, so the numbers are right; one clause such as "r ja höyryn c ovat vakiopaineen arvoja, joten ne sisältävät myös männän työntämiseen kuluvan energian" would close the gap with "kaikki kuumentimen energia siirtyy aineeseen".

## Checked
- All 12 exercise answers recomputed independently (Q = sm, Q = rm, Q = cmΔT + latent term, ice-in-juice balance, sauna stones, two-power loss subtraction): all match answers.py and exercises.json; L3-03 single-run values 2,45 / 2,67 MJ/kg and loss 60 W correct.
- Worked example r = Pt/Δm = 2,34 MJ/kg, symbolic first; the 3,7 % excess correctly attributed to losses to the air.
- Text ratios: r/s = 6,8, r/(c·100 K) = 5,4, s/c = 80 K ("0 → 80 °C"), steam vs water burn 2,52 kJ vs 0,26 kJ per gram (≈ 9,6×): all correct.
- Inquiry numbers: 210 kJ retrieval with its two distractors; tMelt/tBoil 83,5/565 s and 167/1130 s, 565 s at 2000 W, ratio 6,8; Etsi virhe 66,8 kJ; siirto 188 W with mistakes 27,8 and 11 300; check-2 0,597 kg with mistakes 0,677 and 4,04: all correct.
- Sim run headless at (0,50 kg, 1000 W), (0,50 kg, 2000 W), (0,25 kg, 1000 W): plateaus at 0 and 100 °C, durations sm/P and rm/P, Q = Pt; the piecewise T(Q) matches the lesson's model.
- Constant-pressure statement is physically consistent: 100 °C boiling, r and c_p of steam are 101 kPa values; the open-pot and rigid-vessel alternatives are described correctly.
- Experiments: exp-1 varies only P, exp-2 only m; simState carries tMelt and tBoil.
- Heating-curve figure: ice and steam slopes 1,97 and 1,96 vs water 0,98 (c ratios 2,0 and 2,1) as claimed; plateaus declared not to scale.
