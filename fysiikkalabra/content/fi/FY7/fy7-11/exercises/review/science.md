VERDICT: PASS
CONTENT-HASH: 6125beade01a1c5a

## Blocking

## Polish
- solutions.md fy7-11-L1-03 Järkevyys: it says 1,516 lies "between red (1,5143) and blue (1,5224), where green should be". For crown glass, green (about 530 nm) is about 1,519, between yellow 1,5167 and blue. 1,516 lies between red and yellow. It agrees within the angles' ±0,05° (Δn ≈ ±0,003), and the task does not say the glass is crown. Say "about 1,52, close to the table's crown-glass values; the difference fits the measuring accuracy of the angles".
- solutions.md fy7-11-L3-02: it compares with the red edge at 42,3°. With the task's own n = 1,332, the maximum is 42,2° (at α ≈ 59,5°). The conclusion holds either way. Optionally say "about 42°".
- exercises.json fy7-11-L2-03 / figure flint-points: the figure's description gives no n values, so a screen-reader user cannot read n(450 nm). Optionally add "at 450 nm n ≈ 1,639" to the description, or flag this to the visual reviewer.

## Checked
- Recomputed all 12 answers independently in one script: L1 35,107° / 196 078 km/s / 1,5161 / 37,0° / 42,0°; L2 265,0 ns / 34,983° / 183 072 km/s / 15,646°; L3 0,9659° / 30,703° / 1,6650°. All agree with answers.py and exercises.json.
- Round-1 Blocking fixed: L2-01 states the v = c : n assumption in the task, and its Periaate names the group-velocity simplification.
- L1-01 and L3-02 now use n = 1,332. L3-03 uses the lesson-table values 1,3315 / 1,3431; its intermediates 42,296° / 40,632° are right, and 1,664° is given as ≈ 1,7°.
- L1-05 and L1-03 data are physically consistent (sin 55° : sin 38° = 1,331).
- L2-02: the ray leaves the second face (n sin α₃ = 0,871, α₄ = 60,6°), as the Järkevyys says.
- L2-03: the curve is the F2 fit, n(450) = 1,6387 (SCHOTT 1,6388), readable as 1,639. The ±0,1 % reading uncertainty is within tolerance.
- L2-04: violet extremal ray at α = 58,8° for n = 1,343 (θ_max 40,65°); the red top at 17,2° is right.
- L3-01: δ_p = 29,84°, δ_v = 30,80°, and the single-surface spread is 0,31° (the solution says "noin 0,3°").
- Notation (α₁…α₄, A, δ, θ = 4β − 2α), symbolic-first solving, conversions and the reasons for rounding are consistent with the lesson.
