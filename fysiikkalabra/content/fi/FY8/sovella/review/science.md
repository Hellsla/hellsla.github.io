VERDICT: FAIL
CONTENT-HASH: 7bb6b1bc4ce3777f

## Blocking
1. **fy8-s5 c, A (internal consistency, assessment).** "Hyväksytään myös" accepts $6\,\text{t}$, but the answer is `value 5.8, tolerance 0.03` (relative), so 5,63–5,97 t. $6\,\text{t}$ is 3,4 % off and the checker would reject it. Fix: raise the tolerance to 0.05, or stop accepting $6\,\text{t}$.
2. **fy8-s4 d, B (criterion asks for what the task does not give or ask).** The fourth criterion awards a point for comparing with "ytimiä syntyi noin kolmen minuutin kohdalla". The task gives no such figure and does not ask for the comparison: it asks "Arvioi väitettä laskemalla. Mitä muuta c-kohdan tulos edellyttää?". Fix: give "noin kolme minuuttia" in the task and ask for the comparison, or change the criterion (for example to the third assumption, that all the neutrons end up in He-4).

## Polish
- fy8-s4 c: the Vastaus says "Kaksi merkitsevää numeroa riittää" but gives $136\,\text{s}$. Write $\approx 140\,\text{s}$, as the rubric does.
- fy8-s3: the residuals of the invented counts from the generating model alternate strictly +,−,+,−, all within about 0,5 $\sqrt{N}$. The data are honestly disclosed as invented. Still, a less regular scatter would look more like real counting.
- fy8-s4: the 1:6 freeze-out ratio with free decay only gives about 2 min, while full BBN gives about 3 min. d covers this through its assumptions, so this is acceptable (C).

## Checked
Hash 7bb6b1bc4ce3777f at start and end. I recomputed every number with my own script, and all agree with the solutions:
- s1: 2,22 / 1,97 eV, 296 nm, 1193, 1107 nm, 0,83 eV.
- s2: Δm 0,006005 u, Q 5,594 MeV, A 2,23·10¹⁵ Bq, 3,52 kg, 83 %, 1791 W, 98 W, Po 0,16, U ratio 5,1·10⁷, "satoja miljoonia kg" (≈2·10⁸ kg).
- s3: least-squares d = 1,31 cm; r = 36,0–36,4 cm and H 0,23 / 0,27 µSv/h for any d in 1,0–1,6 cm; uncertainties 14 % / 2 % / 6 %.
- s4: 0,782 MeV, 7,16, 0,8575, 136 s, 0,735, 271 s.
- s5: 7,165 and 1,3636, 3,67 %, 4,73·10¹⁷ J, 1,48·10²⁸ fissions, 5,77 t, 3,49 a, 82 988 half-lives.

Sources:
- AME2020 masses (Pu-238, U-234, He-4) and the NASA MMRTG figures (4,8 kg PuO₂, about 2000 W heat, 110 W electric) are correct.
- The half-lives (87,7 a, 138 d, 5,27 a, 4,47·10⁹ a, 7,04·10⁸ a, 24 100 a) and the IUPAC abundances are correct.
- From PDG 2024: n, p and e masses, τ 878,4 s (T½ 609 s) and Y_P 0,245.
- From NIST: the O I levels (1,97 / 4,19 eV, the 297 nm UV line) and the lifetimes of about 0,7 s and 110 s.
- Oklo: 0,440 %, about 2 Ga, a 30 min / 2–3 h cycle, about 5–6 t of U-235 consumed. OL3 runs at 4300 MW thermal.
- STUK: 0,05–0,30 µSv/h outdoors and 5,9 mSv a year.

Physics, models and conditions are sound. The points add up and match the rubrics, and other methods are accepted. No de Broglie wavelength appears anywhere, and nothing is beyond FY8 scope.
