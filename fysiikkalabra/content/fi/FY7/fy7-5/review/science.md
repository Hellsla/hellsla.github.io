VERDICT: FAIL
CONTENT-HASH: 2c7036d454efdc45

## Blocking
- lesson.md:199, lesson.md:479, inquiry.json:3 — **B.** These lines say that an unchanging field gives no voltage: "Käämi voimakkaassa mutta muuttumattomassa kentässä ei saa jännitettä", "Muuttumaton kenttä ei synnytä jännitettä" and "Magneettikenttä synnyttää jännitteen vain muuttuessaan". The same lesson teaches the opposite case. e = vBl arises in a constant B, the simulation's coil gets ±20 mV from a static field, and line 199 itself lists "käämi kääntyy kentässä" as a cause. The claim holds only for a coil at rest, or when the flux does not change. Line 199 also calls every listed cause a "kentän muutos", but area change and rotation change the flux, not the field. — Fix: write "Paikallaan oleva käämi muuttumattomassa kentässä ei saa jännitettä" (199). In the summary, write "Jos vuo ei muutu, jännitettä ei synny" (479). Change the contribution to "Jännite syntyy vain, kun käämin läpi kulkeva vuo muuttuu". In 199, say "käämin läpi kulkeva magneettikenttä tai sen läpäisemä pinta muuttuu", or move the cause list after the flux is defined. The glossary entry `induktio` ("Muuttumaton magneettikenttä ei synnytä jännitettä") has the same problem; fix it the same way.

## Polish
- inquiry.json ennuste-sisalla correct option — "koska käämin läpi kulkeva magneettikenttä ei silloin muutu": "vuo" would match the theory better.

## Checked
- Worked example 0,20 V, one turn 0,80 mV, cm²→m², symbolic first, 2 s.f. justified.
- Kaava graph to scale: Φmax 2,0 mWb, t = 0,5/1,5/2,5/3,5 s, e = ∓20 mV, sign consistent with e = −NΔΦ/Δt.
- Rod figure: F_m on the electron is downward (−e·v×B with B into the page), so the lower end is −, E points down and F_s points up. The derivation eE = evB → e = vBl and the flux-rule cross-check are both correct.
- sim.js: overlap(x), e = −NBlv / 0 / +NBlv, run 0,40 m fits the 8 s axis at v = 0,05 m/s, e_tulo/t_tulo/e_sisalla sampled correctly; no-current assumption stated.
- koe-1/koe-2 isolate v and N (B,N resp. v,B locked); model answer e·Δt = −20 mV·s = −NΔΦ correct.
- All option correctness and feedback numbers (−20/−40 mV, 1,00/0,50 s) recomputed.
- virhe 72 V → 0,72 V, distractor 0,36 V; siirto 4,8 V and mistakes 0,008/0,0048/4800.
- tarkistus-2 0,50 V and mistakes 50/1,0; tarkistus-3 model answer mechanism right.
- Exit ticket 20 mWb; zero voltage at the flux maximum correct.
- lesson-answers.py values agree with my independent recomputation.
