VERDICT: PASS
CONTENT-HASH: b3a2dcf56d69fd0e

## Blocking

## Polish
- fy5-s1 d (solutions.md:688): "Keskipakoisvoimaa ei ole" matches fy5-4 and holds in the ground frame (C). Add "maasta katsottuna". Under Hyväksytään myös, accept a rotating-frame "näennäisvoima, ei vuorovaikutus" answer when the force diagram has only $\overline{G}$ and $\overline{S}$.
- fy5-s2 c: 9,93 h is the rotation of the interior (System III). Equatorial clouds go round in about 9,84 h, which still gives about 159 000 km, inside the tolerance. Say "saman kohdan yläpuolella".
- fy5-s3 c: a timing uncertainty of 0,02 s in $T$ is about 0,02–0,03 s² in $T^2$, as large as the intercept. The conclusion still holds through the scatter (largest residual 0,005 s², σ of the intercept 0,004 s²), so state the argument in $T^2$. The static $k$ has two significant figures (9,8 cm): write ≈ 20 N/m, not 20,0.
- fy5-s4 c: the solution claims one significant figure, but tasks.json stores 5,2. This is harmless, because tolerance only compares the file with answers.py. Storing `5` would match the claim.

## Checked
- I recomputed everything independently (scratchpad fy5rev/recompute.py):
  - s1: 21 m; 2579 kg; 412 / 608 kNm; Δm 1,92 t; tip load 3,06 t; θ 0,598°; shift 0,16 m
  - s2: fit 1,271·10¹⁷, M 1,90·10²⁷; r 160 200 km
  - s3: k 19,91, m_eff 14 g, 18,89 through the origin; 0,446 m/s
  - s4: 0,686 m; Δf 5,25 Hz; 94 dB, 0,995 h; 0,127 W
- Jupiter's moons: the radii and periods match the JPL mean elements to the stated rounding. I checked from known values; ssd.jpl.nasa.gov was unreachable. Each moon's 4π²r³/T² is within 0,2 % of GM = 1,2669·10¹⁷.
- The s2 b accepted range agrees with the accepted slopes.
- The signal has maxima of 1,7 and −0,3, 2 ms apart, so T = 4 ms.
- fy5-16 teaches the 85 dB / 8 h / 3 dB rule.
- Scope: no ω and no rotational dynamics; γ notation.
- The s1 d force diagram is right.
- The points add up to 18/15/14/17, and the s3 data are labelled simulated.
- Hash identical at start and end.
