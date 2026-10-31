VERDICT: PASS
CONTENT-HASH: 77d0c5813b2c4c1b

## Blocking

## Polish
- lesson.md:462 (vt aria-label): "Hetkeen t = 3,0 s asti pyöräilijä on edellä ja etumatka kasvaa" still reads as if the cyclist leads only until 3,0 s. Fix: "Pyöräilijä on edellä, ja hetkeen 3,0 s asti etumatka kasvaa". The en version has the same wording.
- lesson.md:616: "etumatka on suurimmillaan tai pienimmillään" is fine in the same-direction context. Writing "välimatka" would make it read right for any direction.

## Checked
- Round 1 item 1 is fixed. The sim `calc` (inquiry.json:144) now says that $x_\text{B} - x_\text{A}$ tells how much larger B's position coordinate is and that it is zero at the meeting. It calls it B's etumatka only when the bodies move in the positive direction. The en and fi-easy versions say the same.
- Round 1 item 2 is fixed. Koe 1's hints 1–3 and its solution say "paikkojen ero" and nowhere "etumatka" or "edellä", in fi, fi-easy and en. Pred-1 and check-2, the other head-on items, use neither word.
- lesson.md:338 keeps the teacher's two sentences word for word. It then adds the direction rule: in the +x direction the higher line belongs to the body ahead, and in the −x direction the lower line does. This is correct, because in the −x direction the body ahead has the smaller x.
- Every other use of edellä, takana, jäljessä and etumatka was scanned: the hook, pred-2/3, Koe 2, Koe 3, ei-kohtaa, the conclusion, Etsi virhe, siirto, check-3, the v–t paragraph and the summary. Each one is in a situation where both bodies move in the +x direction. Koe 3 uses "etumatka $x_\text{B}-x_\text{A}$" with motion in +x, so it is consistent.
- No text equates a higher line, or a positive $x_\text{B}-x_\text{A}$, with "ahead" without the direction condition. This covers lesson.md, the captions, the exit ticket, sim-spec, sim.js and its readout and case labels ("edellä oleva on nopeampi" is case 4, in +x).
- All numbers were recomputed in one script and agree:
  - head-on: 12 s, 36 m
  - same-start pass: 6,0 s, 36 m, 2v, largest gap 9 m
  - example: 8,0 s, 64 m, 16 m/s, other root −2,0 s, 25 m
  - case 1: 50 m
  - case 4: −10 s
  - case 5: 1,55 s and 6,45 s
  - siirto: 24 m/s (96 m)
  - check-2: 6,0 s
- simState provides xA, xB, vA, gap and meetings, which are the keys the experiments measure.
- Each choice item has exactly one correct option, and its feedback is right.
- The hash is the same at the start and at the end.
