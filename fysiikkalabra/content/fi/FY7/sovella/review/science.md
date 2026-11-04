VERDICT: PASS
CONTENT-HASH: af9c16707d86ff5d

## Blocking
None.

## Polish
- s3 e: the force is worked out from effective currents, as the stated DC model says, so it is the time-averaged force. With AC the momentary force swings between 0 and about twice that value at 100 Hz. A real fault current with a DC offset peaks even higher. One sentence in Järkevyys ("hetkellinen voima on vaihtovirralla jopa kaksinkertainen") would make the "noin kaksinkertainen painoon nähden" claim safer. This fits the stated model (C), so it is not blocking.
- s4 e: "vihreä valo vahvistuu" is right in the interference sense. At 500 nm the film reflects exactly as much as bare glass, about 4 %, against about 1,4 % at 400 and 667 nm. Saying "heijastaa yhtä paljon kuin pinnoittamaton lasi" would prevent the picture of a film that reflects green strongly.

## Checked
- Round 3 (delta from 0c3028a551af5e7c): the only change is s1 d) Sijoitus, where B is split into $mv = 1{,}8281\cdot10^{-26}\cdot7{,}251\cdot10^{5} = 1{,}3256\cdot10^{-20}$ kg·m/s, joten $B = 1{,}3256\cdot10^{-20} : (1{,}602\cdot10^{-19}\cdot0{,}400) = 0{,}2069$ T. Recomputed: 1,32556·10⁻²⁰ kg·m/s and 0,20686 T. The units are right, the value agrees with answers.py (0,20687) and the Vastaus 0,207 T is unchanged. Nothing else changed, so the round 2 findings below stand.
- Round 1 fixes: the s4 a °C step now reads $(1449-273)\,{}^\circ$C. The s2 d causality runs the right way ("koska…levyistä"). s3 now says "siirretään noin 6,0 MW". s4 d says that a grey body does not move the peak and that wavelength-dependent emissivity does. The s4 range is now 0,5–2,5 µm, and the fibre material is unnamed. The s5 d second order is said to be "vain niukasti" enough (±1,03 nm against 1,4 nm, 0,14° against 0,1°).
- s3 e, recomputed: I = 300 A, B = 4,0·10⁻⁵ T, F/l = 0,012 N/m. In the short circuit, B = 1,07 mT and F/l = 8,53 N/m. G/l = 3,97 N/m, so the ratios are 0,30 % and 2,15, the currents differ by 26,7× and the forces by 711×. The currents are opposite, so the conductors repel. AC reverses both currents together, which the solution states. Using the long-wire approximation (l ≫ r) is justified, and the force law is FY7 central content.
- s4 e, recomputed: both reflections invert (1,00 → 1,38 → 1,50), so d = λ/(4n) = 362,3 nm and 2nd = 1000 nm. That gives maxima at 1000, 500 and 333 nm and minima at 2000, 667 and 400 nm. A full thin-film reflectance calculation confirms the green tint, with 4,0 % at 500 nm and 1,4 % at 400 and 667 nm. The Yleisiä virheitä values of 725 nm and 500 nm are right.
- s1 a, new: v×B points up, F_s points down, F_m = F_s, the upper plate is +, and the forces figure agrees. s1 e: W₁₀/W₁₁ = 0,9095 is inside a 10 % spread after acceleration, and v₁₀ = 7,60·10⁵ m/s.
- s2 e: F = 0,955 N, against 10 N of resistance. A 1 % slope for 90 kg gives 8,8 N, which the solution rounds to ≈ 9 N.
- I recomputed every other number in s1–s5 with my own script, and they match answers.py. All s5 table angles agree within 0,05°.
- practice.py check is OK. The points are 16+16+17+17+17 = 83, and each rubric criterion asks only what its task gives. The scope stays within FY7. The hash was the same at the start and the end.
