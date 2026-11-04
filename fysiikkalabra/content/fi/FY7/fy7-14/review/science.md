VERDICT: PASS
CONTENT-HASH: 2097bec4c0ac2497

## Blocking

## Polish
- lessons/FY7/fy7-14/lesson-answers.py:60,71 — stale comments: koe-3 says "400: 6,8 %, 700: 3,9 %" and thin-20 "0,5 %", but the code (and inquiry.json) give 5,83 %, 3,77 % and 0,74 % — update the comments.
- content/fi/FY7/fy7-14/lesson.md:206 — "Silloin molemmat aallot ovat kääntyneet" reads as if wave 2 were also inverted by a reflection; it is delayed by half a wavelength — e.g. "aalto 2 on jäänyt puoli aallonpituutta jälkeen, mikä vastaa kääntymistä, joten aallot ovat samassa vaiheessa".
- content/fi/FY7/fy7-14/lesson.md:405 — "heijastus pienenee noin 4,3 %:sta noin 1,3 %:iin" is per surface (back face not counted); add "pinnasta" so it does not contradict the "kummastakin pinnastaan noin 4 %" just above.

## Checked
- Theory: 2nd at normal incidence, λ_n = λ : n (550 : 1,33 = 413,5 nm), half-wave shift rule, one-shift vs two-/no-shift condition swap, oil (1,47/1,5) on water one shift; all consistent across Ydinajatus, Kaava, Tiivistelmä, glossary, exit ticket.
- Recomputed (own exact single-layer Airy script): bare glass 4,258 %, quarter-wave MgF2 1,260 % at 99,64 nm, soap max 7,71 % at 103,38 nm, koe-1 R at 0/20/50/103/150/207 nm = 0/0,74/3,81/7,71/4,60/0 %, koe-2 0/50/100/150/199 nm = 4,26/2,77/1,26/2,81/4,26 %, koe-3 200 nm at 400/532/700 nm = 5,83/0/3,77 % — all match inquiry.json.
- Worked example 380 nm: 673,9 and 404,3 nm constructive, 505 nm destructive, k = 0 and 3 outside visible; 7 steps, symbolic first.
- 200 nm film: 532 nm cancelled, red/violet reflected → purple (correct, no visible maximum claimed).
- 5 µm film: 14 constructive wavelengths in 400–700 nm (recomputed).
- √1,52 = 1,233 ideal index condition; Dodge 1984 MgF2 n_o(550) = 1,3785.
- Graph figure: green polyline recomputed point by point (400: 2,21, 550: 1,26, 700: 1,60 %) — to scale as captioned.
- inquiry.json: exactly one correct option in kertaus, ennuste-ohut, ennuste-pinnoite, virhe, check-1; every distractor feedback correct; numeric answers 103,38 / 204,08 / 443,3 nm and their mistakes (206,8, 137,5, 300, 102,0, 408,2, 1330, 665, 266) are the stated errors.
- Experiments: tilanne and λ (or d) locked, varied parameter isolated; simState exposes q and R.
- sim.js: Fresnel amplitudes, δ = 4πnd/λ, exact R, shift count and vahvistava/heikentävä classification correct for both situations; wave 2 amplitude r2(1 − r1²); limits (no dispersion, no absorption, no back face, scaled colour) stated in the model text.
