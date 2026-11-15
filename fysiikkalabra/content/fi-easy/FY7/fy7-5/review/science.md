VERDICT: PASS
CONTENT-HASH: 0ba3dd3b118ba940

## Blocking

## Polish
- lesson.md:201 — "Polkupyörän napadynamossa magneetti pyörii käämien keskellä" turns the build around. In a hub dynamo the stator coil is fixed to the axle, and the multipole magnet ring turns with the hub around it. The physics (relative motion changes the flux) is unaffected. — Write "magneettirengas pyörii navan mukana paikallaan olevan käämin ympäri", or just "magneetti ja käämi liikkuvat toistensa suhteen".
- inquiry.json:18 (hook) — "Mitä lujempaa ajat, sitä kirkkaammin lamppu palaa" is true only at low speeds. A real hub dynamo's output levels off at about 15 km/h, and the reason (self-induction) is outside the course. It is a fair C simplification for the hook. Optionally add "hitailla nopeuksilla".
- inquiry.json:301 (check-1) — In the distractor "Käämi liikkuu tasaisesti kokonaan homogeenisen kentän sisällä", "liikkuu" also covers turning, and a turning coil does get a voltage. The feedback assumes the coil only translates. — Write "liikkuu suoraviivaisesti kääntymättä".

## Checked
- Recomputed in one script: the worked example (0,20 V; 0,80 mV per turn), virhe (72 V, 0,72 V, 0,36 V), siirto (4,8 V and its mistakes 0,0080 V, 0,0048 V, 4800 V), tarkistus-2 (0,50 V; 50 V; 1,0 V), exit ticket (20 mWb). All agree with lesson-answers.py.
- The Kaava graph is to scale as its label says. Φ: 0 → 2,0 mWb over 0,5–1,5 s, falling over 2,5–3,5 s. e = ∓20 mV = N·B·l·v. Pixel positions checked against both axes.
- Rod derivation and figure: v right with B into the page gives F = (−e)v×B downward on an electron. So the lower end is −, E points downward and F_s points upward, as drawn. e = vBl also follows from ΔΦ = Blv·Δt.
- Φ = BA states its condition (B perpendicular to the loop). Induction law: average vs instantaneous, the minus sign deferred to Lenz, Wb/s = V.
- sim.js implements Φ = B·l·overlap and e = −NBlv / 0 / +NBlv. finish() samples e_tulo in mid-entry and e_sisalla mid-field, and t_tulo = l/v. The 8 s axis covers the slowest run (0,40 m at 0,05 m/s). The slider steps include 0,15 m/s. The model box states the no-current, no-braking and sharp-edge assumptions. Values are called model values.
- koe-1 locks B and N and varies v. koe-2 locks v and B and varies N. Both record keys that simState exposes. The predictions' correct options and every feedback number match the model (−20/−40 mV, 1,00/0,50 s).
- The johtopäätös model answer has e·Δt = −20 mV·s = −NΔΦ. It notes that mV·s = mWb.
- Each choice item has exactly one correct option, and each distractor's feedback names the actual error.
- Scope: Φ, the induction law and e = vBl, as the slot's täsmennys asks. No self-induction. Lenz is deferred.
- The tarkistus-3 model answer and criteria match the theory's force-balance mechanism.
