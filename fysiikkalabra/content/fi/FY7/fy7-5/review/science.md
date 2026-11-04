VERDICT: PASS
CONTENT-HASH: 2f29d9f694dda152

## Blocking

## Polish
- lesson.md:199 "käämin läpi kulkeva magneettikenttä **muuttuu**", and the correct option of inquiry.json ennuste-sisalla, "koska käämin läpi kulkeva magneettikenttä ei silloin muutu". These read as "how much field passes through the coil", which matches the informal flux definition on the next lines, so they are not an error. Writing "vuo" would still match the induction law better.

## Checked
- Round-1 blocker fixed. lesson.md:199 now says "Paikallaan oleva käämi … muuttumattomassa kentässä ei saa jännitettä", and the cause list says "Muutos", not "Kentän muutos". The summary says "Jos vuo ei muutu, jännitettä ei synny". The contribution says "Käämiin syntyy jännite vain, kun sen läpi kulkeva magneettivuo muuttuu". The glossary entry `induktio` uses the same flux wording. These are now consistent with e = vBl in a constant B and with the sim's ±20 mV.
- Yleinen virhekäsitys, the hook, the exit ticket and check-1 all state the condition (a coil at rest, or flux that does not change), and none contradicts the moving-coil case.
- Worked example: 0,20 V, one turn 0,80 mV, cm²→m², symbolic first, 2 s.f.
- Kaava graph: Φmax 2,0 mWb, e = ∓20 mV, and the sign agrees with e = −NΔΦ/Δt.
- Rod: eE = evB → e = vBl, with the flux-rule cross-check.
- sim.js is unchanged since round 1. It still uses overlap(x), e = −NBlv / 0 / +NBlv, and samples e_tulo, t_tulo and e_sisalla correctly.
- koe-1 and koe-2 isolate v and N. The model answer e·Δt = −20 mV·s = −NΔΦ is right.
- I recomputed the virhe values (0,72 V, 72 V, 0,36 V), siirto 4,8 V with its mistakes, tarkistus-2 0,50 V with its mistakes, and exit 20 mWb in one script.
- Every choice item has exactly one correct option, and each distractor's feedback is right.
