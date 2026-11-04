VERDICT: PASS
CONTENT-HASH: 5bc3d59d4aa9537c

## Blocking

## Polish

## Checked
- Translation fidelity: every number in lesson.md, inquiry.json and exit-ticket.json equals the Finnish version; correct-option flags, reveal gates, experiment initial/locked/vary/measure keys and numeric answers/mistakes are identical to fi.
- Recomputed in one script: worked example |e| = 250 · 0.40 T · 4.0e-4 m² / 0.20 s = 0.20 V (one turn 0.80 mV); siirto 4.8 V and its mistakes 0.0080 / 0.0048 / 4800 V; tarkistus-2 0.50 V (mistakes 50, 1.0); virhe 72 V vs 0.72 V; exit ticket 20 mWb.
- Kaava graph and sim default: Φmax = 2.0 mWb, e = ∓NBlv = ∓20 mV, entry 1.0 s (0.5–1.5 s), exit 2.5–3.5 s; koe-1 −40 mV at 0.20 m/s, e·Δt = −20 mV·s = −NΔΦ; koe-2 −10 / −40 mV at N = 5 / 20.
- sim.js implements Φ = B·l·overlap(x), e = −NBlv / 0 / +NBlv; simState e_tulo, t_tulo, e_sisalla read at the right moments; model limits (sharp edge, no current, no braking) stated in the sim box.
- e = vBl derivation (eE = evB, voltage = El) and its perpendicularity condition stated; Φ = BA with its perpendicular-field condition.
- Predictions: exactly one correct option each; distractor feedback names the physics (field vs change in flux; same ΔΦ in half the time).
- Lenz sign deferred to the next chapter consistently; magnitudes as |e|.
- Sim and experiment captures (390 px) show English labels and the right default values.
