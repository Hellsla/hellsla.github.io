VERDICT: PASS
CONTENT-HASH: cf73b6eb91e31ba3

## Blocking
None.

## Polish
- fy8-s2 d: the answer $1790\,\text{W}$ has three figures, while b) justifies two ("tehossa on kaksi") and $t = 14\,\text{a}$ has two. Say why three are kept, or give $1800\,\text{W}$ (inside the tolerance either way).
- fy8-s2 b, Vastaus: the figures are justified by the fuel mass, which is not used for $m$; the limiting datum is the power.
- fy8-s3 d: "Lähteen valmistajan mukaan … $3{,}0\,\mu\text{Sv/h}$" is not covered by the source note, which only says the pulse counts are model-made. The magnitude is realistic (about 0,4 MBq of Cs-137); add it to the note as an example value.
- fy8-s3 a, criterion `conclusion`: "Todennäköisin syy on …" asks more than "Mitä kuvaajasta voi päätellä?"; the solution itself says "Esimerkiksi". Accept any justified cause (distance offset, source or window not point-like).
- fy8-s5 text: "loput $99{,}274\,\%$" — the two shares sum to 99,994 % (U-234); "ja $99{,}274\,\%$ on uraani-238:aa" is exact.
- fy8-s4 text states "suhde muuttui vain silloin, kun vapaat neutronit hajosivat" as fact, and d) asks the student to name it as an assumption; "oletetaan, että" in the text would match.

## Checked
- Hash cf73b6eb91e31ba3 at start and end. Every number recomputed in my own script from the task data; all agree with solutions.md, answers.py, the rubric details and tasks.json answers within tolerance.
- s1: 2,223 and 1,968 eV match level differences 2,22 and 1,97; third line 295,9 nm (UV; real 297,2 nm); 5000/4,19 = 1193; Si limit 1107 nm; 1500 nm is 0,827 eV. Quenching explanation (lifetimes 0,7 s and 110 s against collision rate) is the actual mechanism; photon count versus photon energy correct.
- s2: Δm = 0,006005 u, Q = 5,594 MeV (literature 5,593); A = 2,232·10^15 Bq, N = 8,911·10^24, m = 3,52 kg, Pu in PuO2 4,23 kg, share 83 %, 0,57 W/g; Po-210 0,160 in a year; U-238 ratio 5,1·10^7 (about 2·10^8 kg); 1791 W and 98,5 W; dose chain 2,83·10^-4 J, 2,36·10^-4 Gy, 4,71 mSv, 0,566 mSv; alternative 0,56 mSv.
- s3: background 22,4 1/min, all nine net rates, $Rr^2$ and $R^{-1/2}$ values; least-squares d = 1,31 cm, read line gives k = 5,63·10^-3, r = −1,30 cm, K = 3,15·10^4; uncertainties 14 % and 1,8 %, 6 % from 1 mm; r = 36,2 cm, 0,23 µSv/h (dose correctly uses r, not r + d; alternative 0,27). Both figures' data and marked points agree. Data honestly declared as model-made.
- s4: 0,782 MeV; decay equation, d → u, weak interaction, W⁻; p/n = 7,16; N_n = 0,8575, 135 s (+1 s); 1 : 5 gives 0,735 and 271 s; 14 % and 26,5 % decayed; T½ = 608,9 s from 878,4 s.
- s5: factors 7,165 and 1,364, share 3,67 %, ratio 0,038; moderator and void feedback correct; 3,49 a; 4,73·10^17 J, 1,48·10^28 fissions, 5,8 t; 82 988 half-lives; Pu-239 → U-235 by alpha.
- Scope: all inside FY8 central contents; no de Broglie, no later-course physics. Points sum per part and task (15, 20, 17, 16, 16). Every task has "Hyväksytään myös" with valid alternative methods. Energy level figure to scale (56 px/eV).
