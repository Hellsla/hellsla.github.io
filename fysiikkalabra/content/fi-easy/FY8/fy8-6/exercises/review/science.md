VERDICT: PASS
CONTENT-HASH: c010ca2f09a936a7

## Blocking

## Polish
- content/fi-easy/FY8/fy8-6/exercises/solutions.md:473 (L2-09) — "kolme merkitsevää numeroa kuten … kuvaajan luetussa arvossa": the read frequency 5,8·10¹⁴ Hz has two — say two (5,2·10² nm) or justify the third by the grid crossing; the 3 % tolerance accepts both.
- content/fi-easy/FY8/fy8-6/exercises/solutions.md:474 (L2-09) — "Suoran kaava antaisi … hc/(eU_k) = 539 nm": that is the model's formula, not the line's — "Malli U_k = hf/e antaisi".

## Checked
- Round-1 Blocking fixed: lines 119 and 442 now say "yleensä hieman pienempi" and "tämän luvun aineistoissa noin 0,1 V", as the lesson does.
- Recomputed: line through (4,6; 1,80) and (7,0; 2,80), slope 1/2,4 V per 10¹⁴ Hz (h = ek = 6,68e-34 J s), intercept −0,117 V ("noin 0,12 V" ✓); L2-09 f = 5,80·10¹⁴ Hz, λ = 516,9 nm (517 ✓, green ✓); L2-10 hf/e = 2,895 V − 2,80 V = 0,0953 V (0,095 ✓). Figure fy8-6/ryhma draws this line.
- L2-10 model answer (c): model limits stated as a method-dependent approximation, gap varies between LEDs; no general 0,1 V claim.
- Changed Kaava steps: eU_k = hf = hc/λ to λ, U_k, h; E_g = hc/λ; N = I/e, P = NE = Ihc/(eλ); N_f/N_e = Pλe/(hcI); ΔE = hc/λ1 − hc/λ2; I1 = k(U1 − U_k): all correct.
- L2-04 now "sisäenergiaksi" (P1 guardrail) ✓; caption marker removals only.
- L2-06 Kaava: h_0 had lost its 10^-34 in the 8g edit (6,626 J s); fixed during this review to 6,626·10^-34 J s (hash 267c… → c010…), rechecked; c010ca2f09a936a7 at the end.
