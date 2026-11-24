VERDICT: PASS
CONTENT-HASH: af372740ea1dad74

## Blocking

## Polish
- lesson.md:209 (object-types, aria-label) — "Jokainen askel akselilla on kymmenkertainen koko" can be read as a tick interval, but the axis ticks are 2 powers of ten apart (labels 10^4, 10^8, …). The label also gives the neutron star as "noin 2 · 10^4 m", while the dot, the simulation and check-2 use 2,4·10^4 m. — Write "jokainen kymmenpotenssi on kymmenkertainen koko" and "noin 2,4 · 10^4 m".
- inquiry.json `simulaatio.calc` — the visible range is "noin 1/1000–3 kertaa näkymän leveys", while sim-spec.md says 1/2000–3. The code shows about 1/1200–3,5. — Make the two texts agree.

## Checked
- All text and inquiry numbers recomputed in one script against lesson-answers.py: example k = 6,47·10^4, Δn = 5; exp-2 Δn = 8; exp-3 midpoint −4; siirto d = 12 732 km with mistakes 40 000 / 6366 / 111; check-2 k = 5,79·10^4 and the inverse 1,73·10^-5; 4 ly = 3,8·10^16 m; 93 Gly = 8,8·10^26 m; reflect 42 and 62 orders.
- Physical values: Sgr A* horizon 2GM/c²·2 = 2,5·10^10 m for 4,3·10^6 M☉; the proton–proton ratio F_e/F_g = 1,2·10^36; Oort/heliopause = 17–830 ("kymmeniä tai jopa satoja"); 1 AU, heliopause 120 AU, Milky Way 10^5 ly = 9,5·10^20 m; the sim's OBJ values are right to their rounding.
- Sim in Playwright: the initial L −9, 7,7 and 27,5 give the nearest objects water, Earth and universe as the intros say. Jumping gives kohdeExp atom −10, proton −15, quark −18, Neptune radius 13, Milky Way 21, Planck −35, universe 27, hair −4, so the experiments' answers are reachable.
- Exactly one correct option, every distractor's feedback right: pred-1/2, exp-2, menetelmat, tunnista (pulsar; black-hole mass ≳ 3 M☉), vuorovaikutukset (K-40 β⁻ is the weak interaction), virhe, check-1 (4,0 > √10 → 10^17), check-c2.
- Figures scale-axis and object-types: the dot positions match log10 of the stated sizes. The "ei mittakaavassa" labels are present where needed; cosmic-address sizes right.
- Matter structure, the four interactions (the residual strong force, its range, β⁻, the weak interaction in the Sun) and the observable vs whole universe (expansion explains 93 > 2·13,8 Gly) are correct at FY1 level and within the scope notes.
- The worked example and the numeric solutions: symbolic first, rounding justified, real checks.
- The simplifications (electrons "liikkuvat", galaxy without dark matter, orbit labelled by radius but drawn by diameter, as said in the Mallin oletukset box) are C.
