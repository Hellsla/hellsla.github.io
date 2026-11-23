VERDICT: PASS
CONTENT-HASH: 4be01a53ba113b0e

## Blocking

## Polish
- exercises.json L2-10 (from the previous round, still open): the answer is stored as 11.905 but the solution gives 12 s. The tolerance accepts both. Store 11.9, or say in the solution that 12 is accepted.
- solutions.md L2-10 Kaava: the rewrite dropped the lead "Kohta c):", so the formula block no longer says which part it serves. Put the label back before the chain.

## Checked
- The diff rewrites only the Kaava steps, splits L2-10 a) and b) into paragraphs and makes small reflows in exercises.json. The files on disk are proper `aligned` blocks; the packet's diff dropped `&` and `\\`. Sijoitus, answers and tolerances are unchanged.
- Echoes (L1-01, L1-03, L1-04, L1-09, L2-09, L2-06): v = s/t with s = 2d gives d = vt/2, as the lesson's Kaava says. In L2-06 the layer thickness is v(t₃ − t₂)/2, which is right.
- Pulse rate (L2-03): t = 2d/v, so n = v/(2d). Right.
- L3-01, the moving bat: s = d + (d − v_lep t) = vt, so d = (v + v_lep)t/2. Right.
- L3-02, two layers: t_ras = 2d_ras/v_ras, and the rest of the time is spent in the muscle. Right.
- Seismic waves (L2-01, L2-04, L3-04, L2-10): t_P = d/v_P and t_S = d/v_S, so Δt = d(v_P − v_S)/(v_P v_S) and d = v_P v_S Δt/(v_P − v_S). This is the lesson's derivation. In L3-04, x²+y² = d_A² gives d_B² = d_A² − 240x + 14 400 and the x formula. Right.
- Tsunami (L3-03, L3-05): λ = vT with the same T and v = √(gh), so λ₂ = λ₁√(h₂/h₁). The travel time is the sum of the sections' times. Right, within the shallow-water condition the Periaate states.
- L2-02 and L2-07: λ = 0,150 mm and f = v/λ in L2-02; v_i = 2L_i/t_i and the mean in L2-07. Right.
- Recomputed in one script: 7,007 cm; 0,2053 mm; 23,68 m; 2,57 m; 168 km; 10,27 MHz; 3,85 kHz; 117,6 km and 19,6 s; 7,06 m; 5,96 cm; 10,0 km; 3,873 cm; 1481 m/s; (72,9; 41,8) with 49,9 km to C and 132,4 km for the other point; 57,1 min; 14,02 m; 6,93 cm; 11,905 s. All agree with the solutions.
- Hash 4be01a53ba113b0e at the start and at the end.
