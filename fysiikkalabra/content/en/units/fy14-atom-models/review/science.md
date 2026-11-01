VERDICT: FAIL
CONTENT-HASH: 4f300b7cb4a81aa3

Science review of fy14-atom-models, 2026-11-01 (full review: unit.md, inquiry.json, teacher.md, figures.py).

## Blocking
1. **A, assessment.** `inquiry.json` `pred-gold`: the prompt asks "Imagine that Thomson's model is how you picture the atom. What do you expect Geiger and Marsden to see?" Under that premise, the answer is the first option (all pass, tiny deflections). Its own feedback says "This is what Thomson's model predicts", but the key marks the observed result, "Most pass almost straight, but a very few bounce back". A student who reasons correctly from the stated model is marked wrong. Fix: ask for the outcome itself, e.g. "Thomson's model was the accepted picture. What do you think Geiger and Marsden actually saw?" Then rewrite the first option's feedback to start "This is what Thomson's model predicts, but the experiment showed …". The alternative is to key the first option and drop "correct" from the second. Compare `fy14-classical-limits` `pred-share`, which keys the model's prediction for a model question.
2. **A, number.** `lessons/units/fy14-atom-models/figures.py` `scatter()` aria-label (and so the `scatter` SVG in unit.md): "The whole atom would be about 10 000 times wider than this drawing." The drawing is 600 units ≈ 17.6 d ≈ 480 fm wide, and a gold atom is about 288 pm = 288 000 fm across: about 600 times. Write "about 600 times wider than this drawing" (or "the whole atom is about 290 000 fm across"), then run `units.py figures`.

## Polish
3. `unit.md` *Bohr's quantum atom*: the "stationary states" sentence is fine. In Key idea, "send out a smear of all wavelengths" could say "a continuous spectrum" to match `check-3` and the word bank.
4. `unit.md` Worked example, Reasonableness: "a typical energy of alpha particles from radioactive decay". 8.3 MeV is at the high end of the 4–9 MeV range. Write "within the range of alpha particles from radioactive decay (about 4–9 MeV)".

## Checked
- Recomputed: worked example E_k = 1.328·10⁻¹² J = 8.29 MeV, kq₁q₂ = 3.645·10⁻²⁶ J·m, d = 2.74·10⁻¹⁴ m = 27 fm (exact constants 27.4 fm), atom/d ≈ 5250; 144 pm : 7 fm ≈ 20 000; m_α/m_e = 7290. Hydrogen with hc = 1240 eV·nm: 3→2 1.889 eV / 656 nm, 4→2 486, 5→2 434.2 nm (mistakes 2279, 365, 304), 6→2 410, 2→1 122 nm, 3→1 12.09 eV / 103 nm (wrong 821 nm), 4→3 0.661 eV / 1876 nm; red line 1.889 eV = 3.03·10⁻¹⁹ J (mistakes 3.027·10⁻¹⁹, 0.529); Balmer B = 364.6 nm; ionisation 91 nm.
- Figures: `scatter` paths integrated for a pure Coulomb force in units of the 27.4 fm head-on distance, nucleus drawn at 7.3 fm; `levels` to scale; `lines` at 410/434/486/656 nm.
- Every choice except pred-gold has exactly one correct option with sound distractor feedback. check-2's longest wavelength (4→3) is right.
- Facts (WebFetch, en.wikipedia.org *Rutherford scattering experiments*, 2026-11-01): platinum reflector, about 1 in 8000; the 15-inch-shell quote (1936); Rutherford's head-on upper limit about 27 fm; gold nucleus about 7.3 fm. Bohr in Manchester 1912, model July 1913, institute 1921, Nobel 1922 with that motivation; Marsden 1889–1970, DSIR 1926; Thomson 1904; Balmer 1885.
