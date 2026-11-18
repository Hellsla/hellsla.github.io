VERDICT: PASS
CONTENT-HASH: d4743ff8db0e733b

## Blocking

## Polish
- solutions.md:118 (L3-02) — the row before last reads $|e| = N\,\Delta\Phi : \Delta t$ right after $|\Delta\Phi| = 2BA$; writing $|e| = N\,|\Delta\Phi| : \Delta t$ there would match the lesson's form for the magnitude.
- solutions.md:128 (L3-03) — $|A|$ for the area under the $(t, e)$ graph shares the letter with the coil area $A$ used elsewhere in the set; L3-05 uses $|A_\text{a}|$, which avoids the clash.
- exercises.json (L1-07) — still stands from the previous round: the exact 2,25 V sits on a half, so a student who writes 2,2 V is marked wrong.

## Checked
- Hash identical at start and end (d4743ff8db0e733b), the same as the packet's.
- On disk, each rewritten Kaava step is an aligned block, one relation per row. The packet's diff joins the rows, but they are separate in the file.
- Every new Kaava chain starts from the basic law (Φ = BA, F_m = |q|vB and F_s = |q|E, the induction law, Ohm's law e = RI, v = at, e Δt = −NΔΦ). It derives the asked quantity symbolically, and its last row is the form the unchanged Sijoitus substitutes into.
- L1-03: the force balance gives E = vB, then e = El = vBl, which agrees with the lesson's derivation.
- L3-02: Φ₁ = BA and Φ₂ = −BA give |ΔΦ| = 2BA, so B = |e|Δt : (2NA).
- L3-04: e = vBl with v = at gives slope k = aBl, so a = k : (Bl). Part b uses s = ½at².
- Recomputed in one script: 0,20 V; 0,36 mWb; 0,50 m/s; 48 mV; 0,30 A; 75 mV; 50 µT; 0,060 mWb; 2,25 V; 0,060 T; 0,15 T; 1,64 m/s² and 1,18 m; 0,0778 mWb. All agree with the unchanged substitutions.
- The split paragraphs (L1-06, L2-05, L2-07, L3-05) change no word, number or sign.
