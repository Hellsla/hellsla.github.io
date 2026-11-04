VERDICT: PASS
CONTENT-HASH: 9368ce31ea655078

## Blocking

## Polish

## Checked
- Round-1 Polish fixed correctly: "Hyvin ohut kalvo on musta" now says wave 2 lags half a wavelength, which is equivalent to an inversion (no second reflection inversion implied); coating text says "pinnasta 4,3 % → 1,3 %" (per surface, consistent with "kummastakin pinnastaan noin 4 %"); lesson-answers.py comments now 5,8 / 3,8 / 0,74 % as computed.
- Figure "reflections" (390 px capture): "ei siirtymää" now sits at the lower-surface reflection point, "½λ siirtymä" at the upper one — correct film–air vs air–film rule.
- Theory: 2nd at normal incidence, λ_n = λ : n, half-wave shift rule, condition swap for one vs zero/two shifts; consistent across Ydinajatus, Kaava, Tiivistelmä, glossary, exit ticket.
- Recomputed with an independent exact single-layer Airy script: bare glass 4,258 %; quarter-wave MgF2 99,64 nm → 1,260 %; soap max 103,38 nm → 7,71 %; koe-1 0/0,74/3,81/7,71/4,60/0 %; koe-2 4,26/2,77/1,26/2,81/4,26 %; koe-3 at 200 nm 5,83/0/3,77 % — all match inquiry.json.
- Worked example d = 380 nm: 673,9 and 404,3 nm constructive, 505 nm destructive, k = 0 and 3 outside visible; 7 steps, symbolic first; significant-figure sentence now separate and correct.
- 5 µm film: 14 constructive wavelengths in 400–700 nm; √1,52 = 1,233.
- Graph figure (to scale): 400/550/700 nm → 2,21/1,26/1,60 %, matches.
- inquiry.json numeric answers 103,38 / 204,08 (oil 1,47 on water, one shift, 2nd = λ) / 443,3 nm recomputed; correct options and distractor feedback unchanged since round 1 and still right.
- Experiments isolate the varied parameter (tilanne and λ or d locked); simState exposes q and R.
- sim.js unchanged: Fresnel amplitudes, δ = 4πnd/λ, exact R, shift-count classification; limits stated.
