VERDICT: PASS
CONTENT-HASH: d7cc99d546a9be81
Round 1, science, mode full. Scope: the new YO-skill task fy6-16-L2-08 (order of magnitude, type 5); the rest of the set was PASS and is unchanged. Checked from text only, no renders.

## Blocking

## Polish
- fy6-16/exercises/exercises.json:230 — the chapter's own warned mistake (multiplying by η instead of dividing, 24 · 0,85 : 1,84 ≈ 11 h) leads to the credited "noin 15 h", because 11 h is nearest to 15 h. In a magnitude task this cannot be a separate option, but no distractor catches it, and the task does not test it. Pedagogy should decide whether that is acceptable, or add a closing line in the solution that shows ÷η vs. ×η.
- fy6-16/exercises/exercises.json:230 — the options are a factor 10, 100 and 1000 apart (docs/exercise-types.md asks for 10–100). The 15 000 h distractor (Wh with kW) is still a real error, so keep it if pedagogy agrees.

## Checked
- Recomputed: P = 230 V · 8,0 A = 1,84 kW and t = 24 kWh : (0,85 · 1,84 kW) = 15,3 h. The distractors were checked against their stated errors: 0,0153 h (kWh with W), 0,153 h (η = 85), 15 345 h (Wh with kW), and 15 345 h is about 1,75 a, so "lähes kaksi vuotta" holds.
- The model is the lesson's, t = W_akku : (ηP) with P = UI single-phase. The stem states the assumption of constant power, which the lesson requires.
- The data are realistic: an 8 A Mode-2 cable and 85 % efficiency.
- The correct choice's feedback gives the chain without overflowing. Each wrong option's feedback names its error.
- Form: the options differ only in value, so none can be picked out by form.
- The solution is complete (Kysytty · Periaate · Mallivastaus) and has a real reasonableness check (≈1,6 kWh per hour).
- All numeric answers of the set were recomputed from answers.py in one call: no mismatch.
