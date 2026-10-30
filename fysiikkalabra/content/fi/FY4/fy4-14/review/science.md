VERDICT: FAIL
CONTENT-HASH: accdbc2f51810aa8

## Blocking
- lesson.md:82 (+ pudotus figure *alussa*, inquiry.json:72, :136 sim `model`) — B: "nopeus on nolla, joten ilmanvastusta ei vielä ole" is said of a jump from an aeroplane. The jumper leaves with the plane's airspeed (about 35–40 m/s), so F_v ≠ 0. — Add "hyppääjä lähtee ilman suhteen levosta (koneen vauhti jätetään huomiotta)" here and in `model`.
- inquiry.json:68 — B: "Mikään ei kasvata ilmanvastusta painoa suuremmaksi" holds only at constant air density. Falling from 4 km into denser air does slow a jumper. — Prefix "Kun ilman tiheys on sama (mallin oletus),".
- lesson.md:470, :475 — B: "Samanmuotoisista … raskaammalla suurempi rajanopeus" also needs equal size. A big styrofoam ball outweighs a small lead ball, yet its terminal speed is lower. — "samankokoisista ja -muotoisista". The glossary's *rajanopeus* needs the same fix.
- lesson.md:281 (figures.py:220 aria), :470, inquiry.json:122, :136, :503 — A: *vapaa pudotus* means falling under the weight alone, with a = g. Here it names a fall with air resistance at the terminal speed. — "ilman varjoa" / "ennen varjon avaamista".

## Polish
- lesson.md:79 — "ilman suhteen paikallaan olevaan"; "Vedessä vastus … samalla nopeudella".
- inquiry.json:122 — *kuvaaja* means the camera operator and the graph in consecutive sentences.
- inquiry.json:151 — "massa m" → "massa $m$" (all symbols LaTeX).

## Checked
- Every lesson-answers.py number was recomputed independently, and all match: v_T 47,6/54,9/61,4/88,6 m/s, canopy 5,11 m/s, F_v,max 3,92 kN = 5,0 G, vt figure, example −18,4 m/s², siirto 304 N and its mistakes, check-2 628 N.
- sim.js: G − kv² = ma, the k-ramp, the simState keys. The experiments isolate m, varjo and asento.
- Worked example: solved symbolically first, conversion, 3 sf justified, a real check.
- Force diagrams (checklist): G from the centre, F_v push or pull beside it, ΣF apart, F red, v blue, a orange. No point particles, no third-law pairs. The b, c and d distractors each carry one error.
- Predictions, experiment questions, check-1: exactly one correct option each, feedback right. Check-3's criteria and model are right.
- Notation: \overline, \cdot. Scope: F_v is qualitative, and kv² appears only as the sim's model.
