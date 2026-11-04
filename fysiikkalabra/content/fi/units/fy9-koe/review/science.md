VERDICT: PASS
CONTENT-HASH: 210723c3675594ef

Round 2 (delta review of the developer's Round 1 fixes; round 1 hash 23902d39dc18f729).

## Blocking

None. All three round 1 Blocking findings are fixed:
1. `inquiry.json` testi-15: the prompt now says "ensimmäisestä riippumatonta kohinaa", and the correct feedback says "Kahden toisistaan riippumattoman lähteen intensiteetit summautuvat". The +3 dB is valid (10·lg 2 = 3,01 dB).
2. `sovella/solutions.md` s2, Yleisiä virheitä: "jaetaan vain kymmenellä eikä sadalla, jolloin T² on kymmenen kertaa liian suuri" is correct (t₁₀²/10 = 10 T²).
3. `sovella/solutions.md` s2 c), Järkevyys: "enintään noin ±0,3 m/s²" matches the worst case (Δg ≈ 0,31 m/s²).

## Polish

1. `inquiry.json` testi-20, the third distractor ("Jännite indusoituisi, jos käämissä kulkisi ensin virta paristosta"): switching on a battery current would change the flux, so a careful reader may call this partly true. Its feedback is fine. Optional: write "…jos käämissä kulkisi tasavirta paristosta".

## Checked

- Round 1 Polish items are fixed: the testi-12 mistake value is 11,57 m/s (√(1250·225/2100) = 11,573), testi-10 says "noin 0,8 g" (7,8125/9,81 = 0,80), and testi-22 uses an ultraviolet lamp.
- The rebalanced choice options (19 items): I re-read every option and its feedback. Each item has exactly one correct option, every distractor is still physically wrong, and no rewording added a claim that holds only under an unstated condition.
- I recomputed every numeric item and its mistake values in one Python script with my own formulas: 2700 kg/m³ (2,7; 2,7·10⁶; 0,37), 0,60 kW (0,69; 1,35), 26,25 MJ (37,5; 53,57), 458,8 kJ (534,2; 2251), 277,4 kPa (−236,25; 357,7), 7,8125 m/s² (15,625; 0,625), 8,9286 m/s (11,57), 0,7795 m (1,283; 150 920), 72,0 Ω (0,013889), 28,90° (58,75; 30,08), 0,30 N (30; 0,75), 656,5 nm (91,2; 364,7), and check-2 0,4444 m/s² (0,4; 1,6; 900). All agree.
- s1 a) has a new Järkevyys check: a 2 kW kettle running for 18 s uses 36 kJ, which matches 36,2 kJ. pred-6: 40 kg of water heated by 30 K needs ≈ 5,0 MJ, which matches "noin 5 MJ".
- The Tutki model and criteria still match the rubric: A gets 1 point (no point for a substitution without units) and B gets 4. The answer is 71 N, and B's 7,1 N gives only 0,11 m/s².
- `practice.py check` passes (61 p). The build runs with no katex errors and no raw `$`. The hash is the same at the start and the end.
- The earlier full-review passes stay: the s2 fit, the figures, the scope and the rubrics.

## Shared issues

None.
