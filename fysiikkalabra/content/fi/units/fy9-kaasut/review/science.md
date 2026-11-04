VERDICT: PASS
CONTENT-HASH: 12867208110cf969

Round 2 (delta review of round 1 fixes; round 1 hash 795ad25aae986918)

## Blocking
(none)

## Verified
1. **Round 1 Blocking 1, S3 d (letku) is fixed.** The developer chose fix (a). In `sovella/tasks.json` s3 d the task now says the group adds the tube's 1,5 ml to every syringe reading, because the tube's air is part of the enclosed air. So the recorded volume is the bath air plus a constant 1,5 ml. Criterion 1 says the offset is the same each time, so the line moves up and the slope does not change. That is exact, with no "lähes". Criterion 2 gives θ₀ = −(V₀ + 1,5 ml)/k, shifted about 11 K colder. Criterion 3 says the error is systematic and gives the remedy: keep all the air in the bath, or leave the tube volume out of the total. `solutions.md` s3 d Periaate and Mallivastaus match this, and say that only the bath air follows V ∝ T. The model is now consistent with the task text.
2. I recomputed in Python. The least-squares fit gives k = 0,1351 ml/°C, b = 37,71 ml and θ₀ = −279,1 °C. With the tube offset θ₀ = −290,2 °C, a shift of 1,5/k = 11,1 K (the criterion's 1,5 : 37,5 · 273 K = 10,9 K). n = 1,647 mmol. Luukku is 17,66 kN, with a 1800 kg water column. Pallo is 3451 − 2619 = 832 kg. Manta is 750 J. All of them match.
3. Polish 2: the luukku Järkevyys now reads "noin yhden ison henkilöauton painoa".
4. Polish 3: the pallo Vastaus is now ≈ 830 kg with two significant figures. The rounding is justified, and the tolerance still accepts 832.
5. The new theory lines in `unit.md` are correct and match fy3-11. ΔU = Q − W_k is displayed with its symbols named, and a sentence relates the efficiency limit to the temperature difference T₁ − T₂ compared with T₁. No adiabatic or Carnot formula is introduced.
6. The s6 figures now show the pad. The force directions are unchanged and correct: in a, the pressure force is up, the weight is down and the rim force is zero at the limit; in b, F_p and N are horizontal and opposite, and static friction points up.
7. The built preview shows the new s3 d text. It has no .katex-error and no console errors.

## Polish
(none new)
