VERDICT: PASS
CONTENT-HASH: 67de3653400246d8

## Blocking

## Polish
- solutions.md:182 (fy7-5-L3-04 Vastaus) — b) gives $s \approx 1{,}2\,\text{m}$ but no reason for its two figures, though a) has one — add "kaksi merkitsevää numeroa, kuten kiihtyvyydessä".
- solutions.md:127 (fy7-5-L1-07) — $2{,}25 \to 2{,}3\,\text{V}$ is right (round half up), and the 3 % tolerance accepts 2,25. A student who rounds half to even gets 2,2, which is 4 % off and is rejected — optional: say "pyöristetään ylöspäin" in the Sijoitus step.

## Checked
- I recomputed all 19 numeric answers in one script with my own formulas (Φ = BA, |e| = N|ΔΦ|/Δt, e = vBl, I = e/R, e = NBlv, ΔΦ = 2BA for the flip coil, triangle and trapezoid areas, least-squares fits through the origin). All agree with answers.py. The largest gap between a stored answer and the exact value is L3-04 (1,6 vs 1,643, −2,6 %), inside its 0,04 tolerance; L1-07 is +2,2 % inside 0,03; every other answer is within 1 %.
- L1-09 ordering: C 0 V, D 0,60 V, A 1,2 V, E 2,0 V, B 3,0 V. The order and the Järkevyys claim (E has the fastest flux change, 2,0 Wb/s) are both right.
- L2-05 interval changes: 0,98, 1,05, 0,97, 0,01, 1,21 and 1,20 mWb. The steepest interval is 0,40–0,50 s, giving 1,452 V; the rising part gives 1,2 V, as stated.
- L3-05 trapezoid areas: 0,01946 V·s for the first pulse and −0,01968 V·s for the second (0,0778 and 0,0787 mWb). The explanation is sound: opposite signs because the flux rises then falls; equal areas because the total flux change is the same; the second pulse is higher and narrower because the magnet accelerates.
- L3-01 physics: only the vertical component gives a force along the axle (the horizontal component is along v or gives a vertical force). 4,23 mV, and the 50 µT vertical component is realistic for southern Finland.
- L3-02: the half-turn flip gives ΔΦ = 2BA and 50 µT; the plausibility check names the wrong-ΔΦ mistake.
- Choice tasks L1-06 and L2-07: exactly one correct option each, and each distractor's feedback states the right physics (the voltage causes the current, not the reverse; v ∥ B gives no force). The L2-07 model answer adds the flux-sweep view, which agrees.
- Figures flux-task and flux-task-2, read from figures.py: the drawn breakpoints match what the solutions read (4,0 mWb at 0,20 / 0,50 / 0,60 s; 5,0 → −3,0 mWb by 0,40 s). The alt texts give the same values and neither figure gives the answer away.
- Units and figures: every value is in SI with the right mWb, µT and mV conversions; the rounding reasons name the limiting datum. The proofread words ("milliwebereinä", "tesloina", "mikrotesloina") are correct.
- Scope: everything stays within induction, flux and e = vBl, with no Lenz direction (that is the later chapter) and no self-induction; the notation matches the brief.
