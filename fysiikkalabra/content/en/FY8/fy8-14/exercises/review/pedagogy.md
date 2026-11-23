VERDICT: PASS
CONTENT-HASH: 3fa68b4c45b18eee
SCOPE: delta md-paragraphs,numbers,reflow,typography,wording from 207d724bbb879a97 base 64d4935

## Blocking

## Polish

- solutions.md (L3 aluminium-plate count-rate task, Formula) — the lead-in promises the logarithm step ("using the rule ln 2^x = x ln 2") but the rows jump straight to d_1/2 and d_x, so the derivation is only referred to ("like the intensity"). Fix: show R = R_0 (1/2)^(d/d_1/2), R_0/R = 2^(d/d_1/2), ln R_0/R = (d/d_1/2) ln 2 first, as in the thickness task above it.
- solutions.md (L2-05, L2-07 and a few others) — Formula still one inline row with "and ... so"; fine for one law plus one rearrangement, but L2-01/L2-02 inline derivations (ln step in a sentence) could use aligned rows like the rewritten ones.

## Checked

- Rewritten Formula steps (dose at distance, entry dose over sessions, bone/tissue beam ratio, thickness from attenuation, PET dose with decay, count-rate thickness) open with the basic law or definition and derive the working formula in aligned rows; each lead-in sentence says why.
- The bone/tissue task now states why I_0 cancels, which repairs the usual "different layers give different I_0" confusion.
- Symbolic form is finished before substitution; Substitution uses the last symbolic form.
- Numbers, answers, tolerances unchanged; Conversions, Substitution and Reasonableness untouched.
- Model answers split into short paragraphs; no paragraph near 120 words.
- Aligned rows are short, so they wrap at 360 px; captures not opened (no figure changed).
- Hash matches the packet (--lang en).
