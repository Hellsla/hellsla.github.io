VERDICT: PASS
CONTENT-HASH: 67568178ef9a0b7f

## Blocking

## Polish
- exercises/review/packet-science.md:"Exercise brief" — the brief block is empty for the English lesson (the packet builder looks for the Finnish section names Kaava/Esimerkki/…, the English file has Formula/Worked example) — tooling, not content; fix the extractor's heading match for --lang en.

## Checked
- exercises.json: all 12 answers, units and tolerances identical to content/fi; task data identical after decimal comma → point.
- Recomputed all answers in one script with my own formulas: L1 1.2455e-27, 9.3193e-24, 184.06 nm, 5.996e-19 J, 3.185e15 1/s; L2 569.5 eV, 3.537e-22, 8.550e-28, 8.668e-15 W; L3 1.0187e4, 0.05210 nm, 0.6044 m/s — all match answers.py and solutions.md.
- Task conditions kept in translation: "almost free electron", "reflected straight back/perpendicularly", "all photons come straight against it", re-emitted photons ignored, atom initially at rest, recoil equal and opposite.
- solutions.md: every step (Given … Reasonableness) present, symbolic first, conversions and significant-figure reasons unchanged.
- Number words checked: "thousands of trillions" (≈3e15), "a millionth of a billionth of a watt" (1e-15), "about 10 000 photons", 656 nm for n = 3 → 2 (recomputed 656.5 nm).
- L1-04 answer field 6.0 vs solution 6.00 — same as the passed Finnish source, within tolerance.
