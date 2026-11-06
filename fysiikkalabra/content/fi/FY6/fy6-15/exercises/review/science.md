VERDICT: PASS
CONTENT-HASH: 04b27443182f33ae
Round 1, science, mode full. Scope: the new YO-skill task fy6-15-L1-09 (ordering, type 9); the rest of the set was PASS and is unchanged. Checked from text only, no renders.

## Blocking

## Polish
- fy6-15/exercises/solutions.md:86 — "B jää alle irrottamiskynnyksen" (dry hand, shoes on, 230 V) without a caveat can read as "shoes make 230 V safe". The lesson says "Kenkiä ei saa pitää sähköiskulta suojaavana varusteena … eikä mitään virtaa voi pitää varmasti turvallisena", and the set's own L3-02 solution (line 176) says so — add one clause: wet floor, a damaged shoe or touching a tap bypasses the shoes, so no value is surely safe.

## Checked
- Currents recomputed: A 1,2 mA, B 5,0 mA, C 143,75 mA ≈ 140 mA (two significant figures from 1,6 kΩ), D 40 mA. The order A, B, D, C is right. `order`, `answer` and the solution agree.
- The prompt names the quantity and the direction ("pienimmästä suurimpaan").
- The task carries the lesson's warned mistake ("suuri jännite yksin vaarallinen"): D has the highest voltage, but C has the largest current.
- The thresholds in the solution match the lesson's table: 0,5 / 10 / 30 / over 50 mA.
- The values are labelled as example values. The resistances fit the lesson's ranges: about 1 kΩ for wet skin, tens to hundreds of kΩ for dry skin.
- The model is I = U : R (Ohm's law, fy6-3), as the lesson uses it for 50 Hz mains.
- All numeric answers of the set were recomputed from answers.py in one call: no mismatch.
- Inline width (text estimate): `I_C = 230 V : 1,6 kΩ ≈ 144 mA` is about 220 px, fine.
