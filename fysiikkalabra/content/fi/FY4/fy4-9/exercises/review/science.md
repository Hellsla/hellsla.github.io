VERDICT: PASS
CONTENT-HASH: e4df9939d9e9aaf6

## Blocking

## Polish
- exercises.json:108–125 (L1-09) — the options 0,4 / 400 / 4000 / 400 000 N are a factor 1000, 10 and 100 apart; docs/exercise-types.md type 5 asks for 10–100. The 0,4 N distractor is fine as a physics check, so this is only a note on the spec.

## Checked
- New task L1-09 (Suuruusluokka), recomputed in one python call: F_ka = 0,020 · 20 / 0,0010 = 400 N; distractors 0,4 N (Δt as 1,0 s), 4000 (½mv²/Δt = 4,0 J / 1 ms) and 400 000 N (m in grams) all come out exactly from the error each feedback names.
- Weight 0,196 N ≈ 0,20 N, about 2000 times smaller than F_ka. Neglecting it is stated in the task and justified in the solution; "0,4 N ≈ kaksi kertaa paino" is right.
- Data realistic: a 20 g hailstone (about 3–4 cm) has a terminal speed of about 20 m/s, and 1 ms is a plausible stopping time. The values are labelled esimerkkiarvot.
- Distractors catch the chapter's own warned mistake (momentum vs kinetic energy, lesson "Kolmas virhe"). The 4000 feedback correctly says that energy per time is power in W.
- The correct option can't be picked out by form: all four are bare values with the mantissa 4. The correct feedback is a short calculation, and the task is not two-stage.
- Notation F_ka = |Δp|/Δt and the impulse principle match the brief. The task stays inside fy4-9.
- solutions.md:199–212 complete (Kysytty · Periaate · Mallivastaus): symbolic first, conversions shown, reasonableness check real.
- Inline chains split with "eli". I judged from the text only that each piece fits about 300 px; I did no render (screenshots not yet made).
- answers.py comment line agrees; the rest of the set is unchanged since the PASS. Hash is the same at the start and at the end.
