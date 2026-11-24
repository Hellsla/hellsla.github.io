VERDICT: PASS
CONTENT-HASH: 50198d3c27fde7f4

## Blocking

## Polish
- lesson.md:93: the energy balance $mgh = \tfrac12 mv^2 + Q$ assumes the magnet starts from rest and that air resistance and wall friction can be ignored. The worked example and the sim's model box say so, but the formula section does not. Fix: add "dropped from rest, air resistance and friction ignored" to the sentence.
- lesson.md:104: "the power at which kinetic energy is converted into internal energy". For the falling magnet at a steady speed, the energy converted is potential energy, not kinetic energy. Fix: write "mechanical energy (in a vehicle brake, kinetic energy)".
- inquiry.json:90: "about twice that of the plastic tube". The model ratio is $0.82 : 0.45 \approx 1.8$. Fix: "almost twice".
- assets/sims/fy7/fy7-6/sim.js:119: the length label is hard-coded as `1{,}00`, so the English page shows a decimal comma (visible in fy7-6-sim-1280.png). Fix: use `tx(H, 2)`. This is notation, not physics.

## Checked
- Lenz directions in the ring figure (shot fig-2): the cross and dot currents, $\overline{B}_\text{ind}$ left or right, N or S facing the magnet, and $\overline{F}$ against $\overline{v}$ in both panels are all right (right-hand rule worked through in coordinates).
- Tube figure (shot fig-3): below the N pole the flux increases, so $B_\text{ind}$ points up and the current is anticlockwise from above; above the S pole $B_\text{ind}$ points down. The wall crosses and dots and the top view agree, and $G = F_\text{j}$ at steady speed.
- Energy bar chart is to scale: 1.05 px per mJ, so 196.2 mJ is 206 px, and copper $E_\text{k} = 0.225\,\text{mJ}$ is labelled 0.2 mJ.
- Sim physics: $F_\text{j} = Mgv/v_\text{t} = kv$, and $y(t)$ and $v(t)$ are the exact solutions with $\tau = v_\text{t}/g$. Aluminium's $k = 0.633 \times$ copper's (σ ratio), the slit tube's $k$ is one tenth (stated as an estimate), and the steel object is in free fall. The Lenz sense of the rings is right. The limits are stated in `model`.
- Recomputed: fall times 0.452, 6.682, 4.241 and 0.819 s; end speeds 4.43, 0.150, 0.237 and 1.493 m/s; $Q$ 195.98, 195.64 and 173.91 mJ; $mgh$ 196.2 mJ. All match the predictions, the conclusion and lesson-answers.py.
- Worked example: $v = 0.15\,\text{m/s}$, $Q = 0.29402\,\text{J} \to 0.29\,\text{J}$, $E_\text{k}$ share 0.096 %, $\Delta T = 0.0025\,\text{K}$. Solved symbolically first; two significant figures justified.
- Pysähdy: $P = 0.0589\,\text{W}$. Siirto: $F = 21\,\text{kN}$; the 25, 9.0 and 42 kN mistakes reproduce; $a = 8.75\,\text{m/s}^2$, 630 kJ.
- tarkistus-2: 42.38 mW gives 42 mW; the 4.32 and 0.518 mistakes reproduce.
- Exactly one correct option in kertaus, both predictions, virhe and check-1; each distractor's feedback is physically right. The exit ticket and the tarkistus-3 model answer agree with the theory.
- koe-1 and koe-2 lock the object and vary only the tube. simState gives `aika`, `vLoppu` and `lampo` once a run has finished. Scope is inside the FY7 contents (no self-induction), and "internal energy" is used per guardrail P1.
