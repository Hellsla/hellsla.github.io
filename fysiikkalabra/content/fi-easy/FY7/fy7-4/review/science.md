VERDICT: FAIL
CONTENT-HASH: eaafcadf3d2b217b

## Blocking
- lesson.md:217 — **A (definition added in simplification, not in the fi version).** "Permeabiliteetti on vakio, joka kertoo, kuinka hyvin tyhjiö päästää magneettikentän läpi." This gives the wrong picture: it treats vacuum as a filter that lets a field through, well or badly. μ₀ is the natural constant that fixes how strong a field a current produces (B₁ = μ₀I₁ : (2πr)). It also does not match fy7-3 (fi-easy), where μ₀ is "luonnonvakio". — Fix: "Se on luonnonvakio, joka kertoo, kuinka voimakkaan magneettikentän sähkövirta synnyttää tyhjiössä (ja lähes samoin ilmassa)." Or drop the sentence, as the fi version does.

## Polish
- exercises/solutions.md:100 (L3-01 Järkevyys) — "langan jännitys olisi kaksinkertainen painoon verrattuna" reads as the tension in one thread, which is mg. The fi version says "jännitys" for both threads together. — Write "lankojen yhteinen jännitysvoima".

## Checked
- Compared with the passed fi version. The number multisets of inquiry.json, solutions.md, exercises.json and exit-ticket.json are identical. Every solution keeps all eight steps (12/12), and L2-02 keeps its graph-reading step. The figure SVG geometry is unchanged. The lesson keeps every condition: homogeneous field and straight wire for F = IlB sin α, only the perpendicular component B sin α, the field of a long straight wire, the third-law pair, and the reason for the radial field in the speaker.
- Recomputed in one script: L1 0,24 N, 0,193 N, 0,10 T, 1,019 N, 3,0 A. L2 3,2 mN, 0,0736 T (slope through the origin 0,2995 g/A gives 1,497 g at 5 A), 30°, 18 m/s². L3 2,354 A, −266,7 N, 1,813 kA.
- Worked example: l = 4,901 m, F = 6,98 N, about 70 times the cone's weight.
- Sim and inquiry: Δm 2,45 g at 6 A, readings 247,75 and 242,85 g, 1,22 g at 3 A and at 30°, 2,12 g at 60°, B = 0,080 T. siirto 0,60 N, with mistakes 0,006, 3,77 and 0,30. check-2 0,20 N, with the cos mistake 0,346. virhe 0,15 and 0,26 N. Exit ticket 0,30 N.
- Directions:
  - swing: B down, current into the page, force to the left.
  - angle: force into the page.
  - wires: parallel currents attract.
  - speaker: both sides pushed toward the cone.
  - L3-03: east × north gives up.
  - Exit ticket 2: up.
  - sim: the force on the wire is up for I > 0 and the reading rises, which is consistent with the third law.
- Each prediction has exactly one correct option. Every distractor's feedback is correct.
- koe-1 varies only I, and koe-2 only α. simState gives lukema.
