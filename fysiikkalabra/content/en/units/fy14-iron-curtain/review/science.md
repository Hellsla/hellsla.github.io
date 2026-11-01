VERDICT: PASS
CONTENT-HASH: 57a7914428d502bd

Science re-review of fy14-iron-curtain, 2026-11-01. It covers the changes in commit 3ed55db3 and what they touch.

## New content
- **thomson-data.** I recomputed the widths. The Doppler FWHM at 90° for 694.3 nm is $2\sqrt{2\ln 2}\cdot 2\lambda\sin 45^\circ\sqrt{k_\text{B}T_\text{e}/m_ec^2}$. It gives 32.3, 64.7 and 129.4 nm at 0.10, 0.40 and 1.6 keV, and 102.3 nm at 1.0 keV. The table's 32, 65 and 129 are right, and "about 100 nm ↔ about 1 keV" holds. Relativistic corrections at 1 keV are a few per cent, which the `model` badge covers.
- **thomson-data options.** Exactly one is correct. The distractor "width doubles when T doubles" is rightly answered with √T, since four times the temperature gives twice the width.
- **pred-thomson.** The shortened prompt and the new option wording keep the physics right: the correct option is "wider".
- **`learn`, the moved `doubt` and the light/temperature wording:** correct.
- **kev-kelvin.** The new Answer and Reasonableness wording is correct: $1.16\cdot10^{7}$ K, which is 11.6 million kelvin.
- **"Artsimovitch".** The note on the original spelling matches the ITER Newsline source.

## Blocking
None.

## Polish
1. **`inquiry.json` thomson-data, text.** It says "In Moscow in 1969 the scattered light from T-3 **had** a width of about 100 nm". This is stated as a historical measurement. The source note says the width is a value matched to the reported temperature, not a number from the paper. Fix: "A width of about 100 nm matches the temperature the Culham team reported in 1969". Then the student text says what the note says.

## Checked
The diff, the thomson figure's colours (no physics change), and the unchanged facts from my first review.

2026-11-01: re-checked the intro sentence changed to "written for this course from historical documents" (Sources and verification no longer published); accurate, clear at B1-B2, no remaining pointer to a hidden section in unit.md or inquiry.json.

## Re-check 2026-11-01: photographs
Artsimovich (1909–1973) is correct. The image shows him pointing at a machine while visitors look on, as the alt says. The caption dates the photo (1967, Kurchatov) and does not repeat the T-3 claim, which the text already covers. CC BY 4.0 with creators named, and linked in the credits.
