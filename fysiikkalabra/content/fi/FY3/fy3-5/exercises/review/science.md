VERDICT: PASS
CONTENT-HASH: a8a78cd65866b1c8

## Blocking

## Polish
- solutions.md:215 (fy3-5-L1-10) and :226 (fy3-5-L2-08): the Kaava stops before the combined form. One more row would finish each, $\Delta U = N \cdot 4{,}1868\,\text{J} + W$ and $\Delta U = \tfrac12(F_1+F_2)s$.
- exercises.json (fy3-5-L1-10, L2-07), carried over: the stored answers 11,3736 kJ and 50,4 J differ from the Vastaus values 11 kJ and 50 J.

## Checked
- The packet's diff shows the `aligned` blocks flattened. I read the real multi-row blocks on disk, one equation per row.
- Every changed Kaava now starts from $\Delta U = Q + W$ and then states $Q$ and $W$ for the situation. The signs follow the lesson's convention: $W > 0$ for work done on the system, $W < 0$ for expanding steam, $Q < 0$ out.
- Algebra checked row by row, all correct:
  - $Q = \Delta U - W$
  - $\Delta U = Pt - Q_\text{ulos}$
  - $t = (\Delta U - Q)/P$
  - $Q = -Fs$ at $\Delta U = 0$
  - $h = \Delta U/(n m g)$
  - $Q_\text{B} = Q_\text{A} + W_\text{A} - W_\text{B}$
  - $\Delta U = Pt$
  - $\Delta U = n F_\text{ka} s$
  - the trapezoid sum $W = \sum h(F_i+F_{i+1})/2$
  - $Q_\text{ulos} = E_\text{v} - \Delta U$
- I evaluated each final form again with the task data: −15 J, 160 kJ, 800 J, 40 s, −18 J, 1,70 m, 310 J, 36 kJ, 50,4 J, 18,72 J, 2,00 kW, 34,8 kJ and 14,5 %, 11,4 kJ and 60 J. All match the unchanged Sijoitus and answers.
- Guardrail: $\Delta U = 0$ at constant temperature is used only where the Periaate states an ideal gas (L1-08 and L3-04 slow compression, L3-01 path independence).
- The Joule-type task (falling weight) keeps $F = G$ at constant speed and $Q = 0$ for the insulated vessel, both stated in the task.
- The L3-05 Vastaus and the L1-09 statement paragraph splits change no claim.
- The hash was the same at the start and the end.
