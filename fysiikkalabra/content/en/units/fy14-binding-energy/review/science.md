VERDICT: PASS
CONTENT-HASH: c4cb2276f3c98102

Science re-review of fy14-binding-energy, 2026-11-01, after commit 7843fefa (unit) and 371c50b6 (binding.js, nuclides.json).

## Previous findings
All three are fixed:
1. The text now says "A large B/A means a tightly bound nucleus"; the stability claim is gone.
2. Meitner and Frisch now explain fission "at Christmas 1938 (published February 1939)", and the teacher note says "the end of 1938".
3. binding.js now says "Mass difference" for the Δm of a reaction.

## Changes checked
- **Explorer question and its model.** Silver-107 has /A = 8.55$ MeV and tin-120 8.50 MeV, against 8.79 MeV for iron-56, so fusing two iron nuclei into  \approx 112$ would need energy. The model and the criterion are correct. Both nuclides are in the explorer's list (checked in the browser).
- **li6 reaction.** It gives  = 4.78$ MeV from the masses, and the same from $\Sigma B$.
- **Teacher extension, D + He-3 → He-4 + p.**  = 18.35$ MeV, so 3.67 MeV per nucleon against 3.52 for D–T; "≈ 18.4 MeV, 3.7 MeV" is right. The reason given (higher Coulomb barrier because helium-3 has  = 2$, and helium-3 is rare) is correct.
- **check-2's new distractor, 22.2 MeV.** It is a power-of-ten error, and its feedback is right. **check-3's new correct option**, "because medium nuclei are bound best", is right.
- **Worked example.** The answer is now $\Delta m = 0.0304$ u. The significant-figure reason is acceptable.
- **binding.js.** The labels are now placed automatically, with /A$ up to 10 MeV. The Q-value and the $\Sigma B$ check are unchanged, and there are no console or KaTeX errors in the browser.

## Blocking
None.

## Polish
None.

## Checked
Physics, mathematics, every option and its feedback, the explorer's computations and data, history and sources.
