VERDICT: FAIL
CONTENT-HASH: ca15fc6e4d36dac3

## Blocking
- solutions.md:176 (L2-08) — "Rypistyvä keula ja turvatyyny pidentävät aikaa enemmän kuin nopeus kasvattaa liikemäärän muutosta" is stated as a general fact in a traffic-safety chapter, and it implies that higher speed is offset in a modern car. It holds only for these example values. In one car with about the same crash time, doubling the speed doubles F_ka. (Guardrails: safety statements exact; this is a type B finding, a missing condition.) Fix: "Näissä esimerkkikokeissa pysähtymisaika pitenee enemmän kuin liikemäärän muutos kasvaa. Samassa autossa kaksinkertainen nopeus kaksinkertaistaa keskimääräisen voiman, jos pysähtymisaika pysyy samana."

## Polish
- exercises.json:249 (L2-08) — test A, a belted dummy stopped in 0,030 s from 25 km/h, means a ride-down distance of only 0,10 m and about 24 g, and F ≈ 17 kN for 75 kg. That is more than the lesson's belted 10 kN at 50 km/h, and less than a belt stretches. You could give A at least 0,05 s and rebuild the options, or say that A's dummy hits a rigid steering wheel.

## Checked
- New task L2-08 (Ennuste muutoksesta), recomputed: F_B/F_A = (50/25)/(0,12/0,030) = 2/4 = 0,50, and with 75 kg the forces are 17,4 kN and 8,7 kN, as in the solution.
- Each distractor follows from its stated error: ×8 (multiplied by the time ratio), ×2 (speed only), unchanged (v² as for braking, 4/4) and ¼ (same Δp, the lesson's belt misconception).
- B: 0,12 s at 50 km/h (0,83 m, about 12 g) is consistent with the existing task at exercises.json:138 (0,100 s) and with the lesson.
- F_ka = mΔv/Δt with Δv a magnitude matches the brief. The mass is not needed, and the solution says so.
- The correct option can't be picked out by form: five short statements of the same pattern. The correct feedback is a one-line ratio.
- solutions.md:163–176 complete (Kysytty · Periaate · Mallivastaus). I checked the inline formulas from the text only, with no render; each is under about 200 px.
- answers.py comment agrees; the rest of the set is unchanged since the PASS. Hash is the same at the start and at the end.
