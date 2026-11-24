VERDICT: PASS
CONTENT-HASH: 6142c4376e8e3b18

## Blocking

## Polish
- solutions.md:254 (fy3-2-L2-09): the Kaava stops at $F_\text{ka} = W/s$ while $W$ is still a separate row. One more row would finish the symbolic step: $F_\text{ka} = (F_1 s_1 + F_2 s_2)/s$.
- solutions.md:98 (fy3-2-L3-01) and :201 (fy3-2-L3-04): the same gap. Each could end in one combined form, $F_\text{ka} = F(\tfrac12 s_1 + s_2 + \tfrac12 s_3)/s$ and $h = F s/(2 m g)$. The physics is right as it stands.
- exercises.json (fy3-2-L1-09), carried over: the stored answer is 18,4 kJ but the Vastaus says 18 kJ.

## Checked
- The packet's diff shows the `aligned` blocks flattened onto one line. I read the 18 real multi-row blocks on disk (solutions.md:15–254), one equation per row.
- Every changed Kaava starts from a basic law and then substitutes the next one. The basic laws are $W = F s$ or $W = F h$, $P = W/t$, $F = G = m g$, $m = \rho V$ and work as an area.
- Algebra checked row by row, all correct:
  - $W = G h$, $W = F_1s_1 + F_2s_2$, $s = W/F$, $W = Pt$, $W = mgh$, $W = \rho V g h$
  - $P = Fvt/t = Fv$, $v = P/F$, $P = mgv$
  - $t = mgh/P$, $\Delta U = n m g h$, $h = W/(mg)$
  - $P = m g n h_1/t_\text{ka}$
  - trapezoid $0{,}5(F_1+F_2)s_2$
  - There are no slips in units, powers of ten or signs.
- I evaluated each final form again with the task data: 180 J, 190 J, 60 W, 30 m, 360 kJ, 250 kJ, 100 J, 60 J and 30 N, 589 J, 45,4 min, 1,5 m/s, 55,3 J, 230 W, 18,4 kJ and 19 N. All match the unchanged Sijoitus.
- L2-06 now writes $P = W/t_\text{ka}$ first and then fills in $W$ and $h$. The order of the derivation is right, and the mean time is still used.
- L3-05: $F = G$ at constant speed is still argued from the lesson, not from Newton's laws, so FY3 scope holds.
- The Mallivastaus paragraph splits in L1-06, L2-08, L3-04 and L3-05 move text only and change no claim.
- The hash was the same at the start and the end.
