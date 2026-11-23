VERDICT: PASS
CONTENT-HASH: 2202db538a6cde53

## Blocking

## Polish
- exercises.json fy5-13-L3-04 a) (unchanged from earlier rounds): "pysyy mittausepävarmuuden rajoissa vakiona" names an uncertainty the task does not give. "pysyy likimain vakiona" would ask only for what the data gives.
- solutions.md L1-09 (unchanged): check helium 971 m/s and air 331,5 m/s against the MAFY table. The ±4 % tolerance covers the usual differences.

## Checked
- The diff rewrites only the Kaava steps of 16 solutions. Sijoitus, answers and tolerances are unchanged.
- Kieli and avoin putki (L1-01, L1-02, L2-03, L3-01, L2-09): each starts from L = nλ_n/2 and v = f_nλ_n and simplifies to f_n = nv/(2L), with L = 3v/(2f_3) for n = 3. This matches the lesson's Kaava. Suljettu putki (L1-03, L3-03): L = nλ_n/4 with n odd, so f_n = nv/(4L), as the lesson says.
- L2-01 and L1-09: λ = 2L → f = v/(2L) → Δf = (v_2 − v_1)/(2L). This is right because L is the same in both cases.
- L2-02: L = λ/4, v = fλ = 4Lf, with no end correction, as the task states.
- L2-06: L_1 = λ/4 − e and L_3 = 5λ/4 − e (the first and third resonances are λ/4 and 5λ/4), so λ = L_3 − L_1 and e = λ/4 − L_1. The sign of e matches the earlier Järkevyys (λ/4 = L + e), and the correction cancels in the difference.
- L2-08: f_s = v/(4L) = ½ · v/(2L) = f_a/2 is right.
- L3-02 and L3-03: the consecutive-resonance differences f_1 = f_b − f_a (string) and 2f_1 (closed pipe) are right. 510 Hz and 850 Hz are 3f_1 and 5f_1 for f_1 = 170 Hz.
- L2-05 and L3-05: f_1 = f_n/n, then v = 2Lf_1 (string or open pipe) or v = 4Lf_1 (closed pipe).
- Recomputed every Sijoitus value in one script: 41,0; 515,2; 32,69; 5,385; 339,68; 33,33 cm; 60,0; 131; 110; 170 and 0,500 m; 100; 95,96 → 122,8; 343,0 and 0,45 cm; 639,5; 31,25. All agree.
- Hash 2202db538a6cde53 at the start and at the end.
