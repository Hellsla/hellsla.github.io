VERDICT: PASS
CONTENT-HASH: 7985c5caf17e486c

## Blocking

## Polish
- lessons/FY4/fy4-5/figures.py:249 (`malli-tyonto`) — the figure still draws the floor line, although its description says "Kuviossa on vain laatikko". — Drop the floor line, or say "laatikko lattialla".
- inquiry.json:60 — the feedback counts a component among "kolme voimaa", against step 7. — Reword, for example "kaksi voimaa ja narun voiman pystykomponentti".
- inquiry.json:508 — the `fbd_magnitudes` criterion asks for "komponentit katkoviivalla", but the model figure draws none. — Add F_x as a dashed component, or drop the clause.
- figures.py:282 — the docstring says L3-02; the figure belongs to L3-01.

## Checked
- `malli-tyonto` now shows only the box, apart from the floor line noted under Polish. F starts at the back top corner, where the handle is fixed, and points down and forward at 30°. N = 147,7 N > G = 117,7 N, F_μ = F_x = 52 N, and the net force is zero. The figure agrees with `fbd_object`, with `fbd_representation` and with guide step 3.
- sim.js:121: in the body model the push arrow starts on the sled, and the components start from the same point.
- The new hook and reflect questions ask about the normal force. The lesson and experiment 2 answer them (N = G ∓ F sin α); this replaces the old acceleration question, whose answer depended on friction.
- Lift options hissi a–d: the option texts are empty, and each figure's description lists its arrows. Exactly one option is correct, and each distractor has one error. The added prompt sentence gives nothing away.
- The lesson prose is unchanged since my last review: the guide, the worked example (a = 2,96 m/s², N = 71,8 N) and all other figures were checked then.
- All inquiry numbers and mistake values were recomputed in one script and agree (146 N, 50 N, 5,0/2,5 m/s², 4,886 N, 22,62 N, 51,22 N, 52/148 N).
- Every numeric solution writes its Voimakuvio step before its Kaava step.
- The exit ticket and the YTL citations match the theory and the force-diagrams table.
