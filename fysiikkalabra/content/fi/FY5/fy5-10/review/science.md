VERDICT: PASS
CONTENT-HASH: 3efbc288e36bc5e2

## Blocking

## Polish
- inquiry.json koe-2/koe-3, johtopäätös — sim.js:1407 computes the λ readout as `v / f`, so "fλ = v joka rivillä" holds by construction; the independent evidence is the λ bracket on the ruler. Fix: have the prompt compare the readout λ with the ruler before forming fλ.
- lesson-answers.py:1295 — the comment mentions "440 Hz", which the lesson never uses. Fix: drop it.

## Checked
- One script recomputed every lesson and inquiry number. Kertaus 2,0 Hz. Koe 1: 6,0 m in 3 s, P's max 5,0 cm. Koe 2: λ 4/2/1 m. Koe 3: 1,0 m. Example: 0,80 m (2 s.f. right). Etsi virhe. Siirto: 4,0 s, mistakes 25 and 9. Tarkistus 2: 2,7 m/s, mistakes 1,35, 0,833 and 5,4. Tarkistus 1. Exit: λ/3. All match lesson-answers.py.
- sim.js uses y = A sin(2πf(t − x/v)) behind the front. The pulse is λ/2. The crest markers (phase ¼) and the compressions (max −du/dx) have the right sign. The coils never cross (peak strain 0,79). The view is 4,63 m, so the koe 1 and 0,5 Hz instructions hold.
- Each experiment locks all but its varied key. Changing aalto restarts the sim, so dyMax and dxMax belong to each row's wave type. The measured keys exist in simState.
- Mallin oletukset states the limits: no reflection or damping, enlarged rope displacement, spring to scale, model values.
- Figure "graphs": λ = 1,0 m and T = 0,50 s (px scales checked), consistent with one steady wave. Not claimed to scale.
- Figure "birth": front at λ/4…λ and source phase +A, 0, −A, 0 are correct. Figure "valokuva": crests at 0,5, 2,0 and 3,5 m on the gridlines.
- Theory: energy but no matter carried in the ideal model (drift and thermal motion noted); v set by tension and linear density; non-dispersive condition stated (water waves, tsunami); f kept across a boundary.
- Every choice item has exactly one correct option, and every distractor's feedback is right.
- In FY5 scope: no light, and reflection is deferred to its chapter.
