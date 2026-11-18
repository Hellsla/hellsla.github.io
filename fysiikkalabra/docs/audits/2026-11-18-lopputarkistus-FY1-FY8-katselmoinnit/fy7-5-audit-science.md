VERDICT: FAIL
CONTENT-HASH: b7de1d98afc92688

## Blocking
- lesson.md:201 (Muutos synnyttää jännitteen) — "Polkupyörän napadynamossa magneetti pyörii käämien keskellä" describes the device the wrong way round: in a hub dynamo the multipole ring magnet turns with the hub shell around the stator coil fixed to the axle (a magnet turning inside the coil is a bottle dynamo). A, Minor. — Fix: "napadynamossa navan mukana pyörivä rengasmagneetti kiertää akseliin kiinnitetyn käämin ympäri", or just "magneetti pyörii käämin suhteen".
- exit-ticket.json:8 (question 2) — "Nolla … vuon kuvaaja on hetken vaakasuora" holds only when the flux reaches its maximum smoothly. The question does not say so, and the lesson's own graphs have corners where e jumps (at a sharp peak e flips sign and is never zero). The answer also calls the instantaneous rate ΔΦ : Δt, though lesson.md:273 uses the tangent's slope. B, Minor. — Fix: in q, "kasvaa, kääntyy tasaisesti kaartuen huippuunsa hetkellä t₁ …"; in a, "tangentin kulmakerroin on nolla".

## Polish
- inquiry.json:348 (tarkistus-3 criterion 4) — it asks about a rod at rest, which the prompt does not ask. Drop it or add to the prompt. Minor.
- inquiry.json:195 (johtopäätos criterion 1) — "kaksinkertaistuu, kun kierrosten lukumäärä kaksinkertaistuu", but the intro suggests N = 5 and 20, which is a factor of four. Say "on verrannollinen". Minor.
- inquiry.json:335 (tarkistus-2 Järkevyys) — "0,50 m · 4,0 m = 2,0 m²" should read "0,50 m · 4,0 m/s = 2,0 m²/s". Minor.
- lesson.md:122 — Faraday read a galvanometer (current), not a "jännitemittari". This is fine for the modern setup but loose as history. Minor.
- inquiry.json:26 (kertaus-voima) — a free electron flying into a hub dynamo's magnet is an artificial scene. A beam tube would be more honest. Minor.

## Checked
- One script recomputed every number from the task data and reproduced lesson-answers.py exactly: worked example 0,20 V and one turn 0,80 mV, retrieval 1,6·10⁻¹³ N, virhe 0,72/72/0,36 V, siirto 4,8 V and its three mistakes, rod 0,50/50/1,0 V, exit 20 mWb.
- Sim numbers per koe: koe-1 gives −10/−20/−30/−40 mV with Δt 2,00/1,00/0,67/0,50 s and e·Δt ≈ −20 mV·s; koe-2 gives −2/−10/−20/−40 mV.
- Sim code matches the model: overlap(x), e = ∓NBlv, e_tulo, t_tulo and e_sisalla in simState after a run. The run time fits the 8 s axis at 0,05 m/s. Each experiment locks the two other parameters.
- The graph figure is truly to scale: t = 0,5/1,5/2,5/3,5 s, Φmax = 2,0 mWb, ±20 mV, and the sign follows e = −N dΦ/dt.
- Rod figure: v×B with q < 0 pushes the electrons down. The + and − ends, the E direction and the F_s and F_m arrows are all correct. The perpendicularity condition is stated.
- Flux figure: 5 and 3 field lines cross the loop. The projection is right.
- Every prediction, check-1 and virhe option has exactly one correct choice, and every distractor's feedback is right.
- Scope: no self-induction. The law, Φ = BA and e = vBl are as in the slot. The sign is deferred to the chapter Lenzin laki.

## Scores
- **1 Physics and mathematical correctness: 3.** Every computation, figure and the sim are correct. Only two small Blocking findings remain: one A about a device description and one B in the exit ticket. No physics of induction is taught wrong.
- **6 Experimental reasoning (physics): 4.** The variables are cleanly controlled, the values are labelled as model values, and the sim's assumptions (no current, sharp edge, constant v) are stated. There is no uncertainty element, which this kind of sim does not call for.
