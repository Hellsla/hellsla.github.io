VERDICT: PASS
CONTENT-HASH: b3bf46f46d777be7

## Blocking

## Polish
- lesson.md:94 — $mgh = \tfrac12 mv^2 + Q$ is stated without its condition; only the worked example says air resistance is negligible — add "kun ilmanvastus ja kitka jätetään huomiotta" (one clause).
- inquiry.json simulaatio.model — the slit tube's $k$ = one tenth of copper's is an unsourced estimate; it is labelled "arviona" and the numbers are model values, so acceptable, but a source or the word "karkea arvio" would help the claim "noin kaksinkertainen muoviputkeen verrattuna" not read as a measurement.

## Checked
- Lenz directions recomputed with the right-hand rule: ring figure (approach: ⊗ top/⊙ bottom, $\overline B_\text{ind}$ toward magnet, N facing; recede: reversed, S facing, force with the motion's opposite), tube figure (below N-down magnet: field up, right wall into page, anticlockwise from above; above: reversed; $F_\text{j}=G$ at constant speed), sim `ring()` arrowheads (front arc to the right = anticlockwise from above below the magnet).
- All pysähdy answers, virhe, check-1, kertaus and exit ticket: exactly one correct option, distractor feedback physically right; "lähestyvää hylkii, loittonevaa vetää" consistent everywhere.
- Worked example recomputed: $v=0{,}15\,$m/s, $Q=0{,}29430-0{,}00028=0{,}29402\,$J → $0{,}29\,$J, $E_\text{k}$ share 0,096 %, $\Delta T\approx0{,}0025\,$K; symbolic first, 2 s.f. justified.
- Pysähdy power $0{,}020\cdot9{,}81\cdot0{,}30=0{,}059\,$W; tarkistus-2 42,4 mW → 42 mW, mistakes 4,32 and 0,518 correct; siirto $F=m(v_1^2-v_2^2)/2s=21\,$kN, mistakes 25/9/42 kN, $a=8{,}75\,$m/s², 630 kJ.
- Sim model ($F_\text{j}=kv$, $v_t=mg/k$) recomputed independently by bisection: Cu 6,68 s / 0,15 m/s / 196,0 mJ, Al 4,24 s / 0,24 m/s / 195,6 mJ, slit 0,82 s / 1,49 m/s / 173,9 mJ, plastic 0,45 s / 4,43 m/s; all feedback and the johtopäätös model answer match; lesson-answers.py agrees.
- sim.js implements the stated model (analytic $y(t)$, $v(t)$, Newton fall time, Q = ΔEp − Ek, steel = free fall in any tube, speed select changes pace only); simState gives `aika`, `vLoppu`, `lampo` for koe-1/koe-2; experiments lock `kappale` and vary only `putki`.
- Al/Cu conductivity ratio 3,77/5,96 = 0,633 and $k\propto\sigma$ for equal geometry: fair (C).
- Energy figure to scale: 196,2 mJ → 206 px at 52,5 px/50 mJ; copper $E_\text{k}=0{,}225\,$mJ ≈ 0,2 mJ label.
- Energy terminology follows P1 (sisäenergia, no "lämmöksi"); induction hob, metal detector, eddy brake (weakens near stop) and laminated core explained by the right mechanism.
- Scope: Lenz and eddy currents are FY7 central content; no self-induction or later-course physics.
