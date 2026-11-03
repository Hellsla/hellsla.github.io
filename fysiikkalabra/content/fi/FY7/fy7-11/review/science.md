VERDICT: FAIL
CONTENT-HASH: 30336ad38a24bd1e

## Blocking
- lesson.md:77-82, lessons/FY7/fy7-11/lesson-answers.py:4,11, assets/sims/fy7/fy7-11/sim.js:16 (and figures.py:17 "water") — **A**: the water column does not match its cited source. Daimon & Masumura, Appl. Opt. 46, 3811 (2007), 20,0 °C (refractiveindex.info main/H2O/Daimon-20.0C, Sellmeier evaluated; IAPWS 1997 gives the same to 5 decimals) gives **1,3315 / 1,3334 / 1,3375 / 1,3431** at 656 / 589 / 486 / 405 nm, not 1,3311 / 1,3330 / 1,3371 / 1,3435. The first three are the older relative-to-air handbook values; violet 1,3435 matches neither (relative to air it would be 1,3427). — Fix: use 1,3315 / 1,3334 / 1,3375 / 1,3431 (keeps violet bow 40,6°; red bow becomes 42,3°), refit the sim's and figures.py water Cauchy through them, and recompute what follows: water prism Δδ (A = 60°, α₁ = 50°) 0,91° → **0,85°** (inquiry johtopaatos model); siirto **25,4 mm** (answer 25.396; hint β_p = 40,57°, β_v = 40,15°; tan 0,85628 and 0,84358; mistake values sin 2·(sin β_p − sin β_v) and m-value redone); tarkistus-2 prompt/solution n values and answer **1946 km/s** (v_p = 225 310 km/s, v_v = 223 364 km/s; the 2000 mistake feedback text adjusted); lesson.md:288 violet "n = 1,3435" → 1,3431.

## Polish
- lessons/FY7/fy7-11/lesson-answers.py — stale comments: flint-ero says 3,34° (computes 3,92°), vesi-ero 0,72° (0,91°), siirto 26,8 mm (27,15 mm). Update after the fix.
- lesson.md:288 / theta-graph — the graph uses n = 1,331 for red while the table gives 1,3311 (after the fix 1,3315); say "n ≈ 1,331" or use the table value so the 42,4° and the glossary 42° read as one number.
- sim flint F2 fit: through 486/588/656 nm it matches SCHOTT F2 exactly there, but extrapolates to 1,6499 at 405 nm vs catalogue 1,6506 (Δδ 3,92° vs 4,01°). Fine as model values; optionally fit through 405 nm too.

## Checked
- N-BK7 table (1,5143/1,5167/1,5224/1,5302) and n-graph points 436 nm 1,5267, 546 nm 1,5187 agree with SCHOTT 2017 catalogue (refractiveindex.info specs/schott/optical/N-BK7) to 4 decimals; citation correct.
- Crown sim Cauchy fit reproduces the table red/violet to 4 decimals.
- Speeds 198 111 / 196 053 km/s; worked example 34,88° / 34,47° / 0,41°.
- Rainbow extremal ray: red 42,36° at α = 59,5°, violet 40,58°; secondary 50,4° / 53,6°; θ(90°) = 14,8°.
- koe-1 deviations and Δδ 0,53° … 1,40° … 4,45°; ennuste feedback 38,4° / 39,8°; all colours exit at the recorded settings.
- koe-2: δ_p 40,0° → min 38,43° near α₁ = 49° → 50,25°; violet exits for α₁ ≥ 35°.
- Etsi virhe 39,2° / 91,8° / 34,5°; exit ticket −8°.
- Prism relations α₂ + α₃ = A, δ = α₁ + α₄ − A and θ = 4β − 2α derivations correct, conditions stated.
- Mechanism (electron response toward UV absorption), Newton's two-prism argument, Alexander's dark band: correct at level.
