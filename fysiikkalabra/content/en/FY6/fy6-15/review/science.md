VERDICT: PASS
CONTENT-HASH: d7a934506223dde6

## Blocking

## Polish
- lesson.md:357 (RCD figure aria-label, from figures.json) — the figure now labels the current through the person I_Δ and the equation I_L − I_N = I_Δ, but the alt text still says "the fault current I f" and "I L minus I N is I f". Elsewhere I_f is the fuse's rated current. Notation mismatch, not a physics error; fix: "residual current I Δ" in the alt text, and name the symbol once in the RCD paragraph ("the difference, I_Δ").
- lesson.md:310 vs 394 — the earthing figure uses I_fault, the RCD figure I_Δ. They are different currents, so two symbols are right; one clause would make that explicit (C-level).

## Checked
- Full review because en figures changed. In 99a4f9f4 the RCD label I_fault -> I_Δ is physically right: the residual current I_L − I_N equals the leakage to ground through the person, the usual I_Δ of RCD practice. The x-shift of I_fault in the earthing figure moves a label only.
- Figure labels against the Finnish: "extra-low voltage" (class III, at most 50 V AC / 120 V DC as the text says), "danger of fibrillation" (table and caption say ventricular fibrillation), "fault", "no earthing", "the fuse trips": correct.
- Scripted token diff: every number and formula token in lesson, inquiry, exercises and solutions equals the Finnish (only the order "10 A or 16 A" differs).
- Recomputed: 4500 W : 230 V = 19,6 A (9,6 + 4,3 + 5,7); 2300 W and 3680 W limits; 230 V : 1 kΩ = 230 mA; 3200 W : 230 V = 13,9 A; 2900 W : 230 V = 12,6 A; 0,60 Ω · (14,8 A)² = 131 W; (16 : 10)² = 2,6; 0,20 Ω · (16 A)² = 51 W.
- Conditions stated: rms voltage, shoes only if intact, dry and no other earthed contact, IEC 60479-1 indicative, E_max d only in a uniform field, RCD does not help against line-to-neutral contact, fuse never replaced with a larger one.
- Each prediction and check has one correct option with right distractor feedback; the solutions.md reasonableness wording ("little energy is transferred from it as heat to the surroundings") is the correct mechanism.
