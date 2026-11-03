VERDICT: FAIL
CONTENT-HASH: 949a4995d7076cb8

## Blocking
- inquiry.json:164,180-182,223,236-238 (keys at 150,157,209,221) — untranslated Finnish shown to the student: "Initial state: hiukkanen: protoni", "Kept constant: hiukkanen", the exp-2 table column "hiukkanen", the instruction "Adjust hiukkanen", and the option values "protoni", "deuteroni", "alfahiukkanen" (shots #42-#45). Fix: names `"hiukkanen": "particle"`; values "proton", "deuteron", "alpha particle".

## Polish
- inquiry.json:koe-1/koe-2 — the opening question (how can a magnetic field sort particles that differ only in mass?) is never investigated: koe-1 varies only the speed of a proton, koe-2 shows that all particles pass straight. Add an optional step to koe-1 that varies the particle (proton, deuteron) at fixed v and B (d doubles), a prediction before it, and put it in the conclusion; at present only the optional reflect answers the hook.
- inquiry.json:koe-2 — the velocity selector never selects: the speed is locked, so the student sees no particle deflected. Let the student vary v around 1.0 Mm/s (or add a second varied step) so that "only v = E : B passes" can be refuted; the section's claim that faster particles curve with the magnetic force is not seen.
- inquiry.json:ennuste-2 — min 2 records do not guarantee the two speeds that the feedback cites (10.4 and 20.9 cm); require or say again "at least 1.0 and 2.0 Mm/s" in the table's prompt.
- inquiry.json:ennuste-2 correct option — "the radius doubles, because the path becomes gentler as the speed increases" restates the result; name the reason (the needed centripetal force grows as v², the force only as v).

## Checked
- Prerequisites fit (fy7-1 tesla, FY6 W = qU, circular motion); path is staged: electric field, magnetic force, no work, circle, selector, spectrometer, accelerator.
- Three predictions are arguable and refutable by koe-1/koe-2; feedback gated by reveal and repairs misconceptions; the model values (10.4, 20.9 cm; 24 and 48 fN) agree with the formulas.
- Worked example 7 stages, numbers verified (20.0 u, neon-22 at 27.4 cm); Find the error and transfer (0.225 T) with real mistakes (0.159, 0.00712) check out.
- Right-hand-rule figures consistent (force-dir, circle-path, track-sign: negative charge curves down).
- Check 2 needs the figure; check 4 (optional) criteria observable; exit ticket tests selector and charge sign.
- Figures legible; sim usable on a phone.
- Exercises: see exercises/review/pedagogy.md.
