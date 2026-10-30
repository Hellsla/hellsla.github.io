VERDICT: FAIL
CONTENT-HASH: 7a9c77253199c80c

## Blocking
- lesson.md:416 — **B.** "Kitka ja ilmanvastus tekevät aina negatiivista työtä" leaves out a condition. Friction does positive work on a box carried by a belt or an accelerating truck. fy4-6 teaches that static friction adapts to the situation, and a tailwind can also do positive work. — Add the condition, e.g. "Kun kappale liikkuu paikallaan olevaa alustaa pitkin, kitka ja ilmanvastus vastustavat liikettä ja tekevät negatiivista työtä, joten …"

## Polish
- lesson.md:358 — fy4-7 already defines **konservatiivinen voima**, but here it is introduced as new. Make it a recall ("kuten luvussa *Liike-energia, potentiaalienergia ja mekaaninen energia* opit") and add the new point: the work depends only on the height difference.
- lesson.md vs fy4-7 — fy4-7 says "painovoima" and fy4-8 says "paino". Connect the two names once ("paino eli painovoima").
- inquiry.json:474 — In check-3, criterion 2 joins two ideas with a wrong "koska". Energy conservation limits the train to the start height. Leftover kinetic energy at the top is why later hills are lower. Split it.
- lesson.md (Kaava) — W = F_∥ s is given for straight-line motion, but −F s is then used along curved track. Consider adding "kun vastusvoima on koko ajan liikettä vastaan" next to the formula.

## Checked
- I recomputed all lesson and inquiry numbers in one script (sled −645 J, 9,90 m/s, 41 %, 26,9 N; cart; virhe; swing; check-2 and its mistake values). All match.
- I checked the sim with an independent energy model. v_pohja is 14,0 m/s for every mass and both tracks. At 100/200 N: h2 8,79/7,66 m, s 47,4/45,9 m, ΔE_mek −4,74/−9,19 kJ = −F s, final E_mek 30,1 kJ. Feedback and model answers match.
- sim.js implements Newton II along the track with F against the motion and stops at the first stop. The model box states its assumptions.
- The experiments isolate the varied parameter, and simState gives the measured keys.
- Each choice item has exactly one correct option, and the distractor feedback is right.
- The derivations of W_kok = ΔE_k and of the energy principle are correct.
- Figures: palkit is to scale (160 − 64 = 96). The laakso bars and the force directions in the work figure are right.
- Notation matches fy4-7 (E_\text{k}, E_\text{p}, E_\text{mek}, zero level stated) and builds on fy4-7's E_mek and friction-to-internal-energy idea.
- The summary and exit ticket agree with the theory.
