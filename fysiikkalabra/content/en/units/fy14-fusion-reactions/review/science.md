VERDICT: FAIL
CONTENT-HASH: c24379ba79d6f049

Science review of fy14-fusion-reactions, 2026-11-01 (full review). I recomputed every number using AME2020 and CODATA 2018. I checked the 1934 letter (ChemTeam copy) and the Wikipedia articles on the pp chain and nuclear fusion.

## Blocking
1. **A, `inquiry.json`, Investigation 2 text: "The arrows are to scale".** In `reaction.js` the approaching deuteron's arrow is 80 px and the alpha particle's is 38 px. So the alpha looks half as fast as the fuel nucleus. At about 10 keV the deuteron moves at about 1·10⁶ m/s, while the alpha (3.5 MeV) moves at 1.3·10⁷ m/s and the neutron at 5.2·10⁷ m/s. The products are really 10–50 times faster, and the picture hides where the 17.6 MeV went. Fix in the unit: "Within each step the arrows are to scale; the products are really 10–50 times faster than the fuel nuclei." See also Shared issue 1.

## Decision on the open question (Coulomb barrier)
The unit's 0.5 MeV is correct as stated: ke²/r at 3 fm gives 0.48 MeV, the top of the barrier. Wikipedia's "0.1 MeV" for D–T is a different quantity. It is the collision energy at which D–T fusion becomes likely (the cross-section peak is near 0.1 MeV deuteron energy), already far below the top because of tunnelling. Keep 0.5 MeV, and add one sentence to *Key idea* after "Coulomb barrier":
"Because of tunnelling, deuterium and tritium already fuse readily at collision energies of about $0.1\ \text{MeV}$, well below the top of the barrier, and in a reactor plasma (about $15\ \text{keV}$) the fastest nuclei do most of the fusing."
This is polish, not blocking.

## Polish
1. `inquiry.json`, `describe-process` model, and `reaction.js` step 3: "about 10⁻¹⁵ m" contradicts "about 3 fm" in the theory and prediction 1. Fix: "about $3 \cdot 10^{-15}\ \text{m}$". The model also leaves out tunnelling. Fix: "…close enough to tunnel through the rest of the barrier, …".
2. `unit.md`, *Summary*: "the thermal energy of a few keV" is true for the Sun (2 keV) but not for a reactor (kT ≈ 13 keV). Fix: "a few keV in the Sun, about $10\text{–}20\ \text{keV}$ in a reactor".
3. French corner: *tritium* is pronounced [tʁi.tjɔm], with the *t* sound, not "tree-SYOM". Fix: "tree-TYOM". (This is for the visual and editorial review.)

## Checked
- **Energy and rates.** pp chain: 1.442, 5.493, 12.860 MeV, total 26.73 MeV, 2.0 % to neutrinos. The 9-billion-year wait and Bethe and Critchfield 1938 match Wikipedia. Sun's core: 1.5 kT = 2.03 keV, and the barrier is 237 times higher. D–T: Q = 17.589 MeV. Shares from nuclear masses: 14.05 / 3.54 MeV (with Q = 17.6: 14.06 / 3.54). The neutron takes 80 %, and the teacher's speed figure of 5.2·10⁷ m/s is right.
- **Fuel energy per kilogram.** D–T: 3.37·10¹⁴ J/kg, about 1.04·10⁷ times coal. U-235: 8.21·10¹³ J/kg.
- **Sun versus ITER.** Sun's core: 276 W/m³, about 3.6·10¹¹ times denser than ITER's plasma. ITER: 500 MW in 840 m³ = 0.6 MW/m³. ITER's 150 million degrees is 9.6 times the Sun's core.
- **The 1934 letter.** Dated 9 March, *Nature* 133, 413 (17 March). The summary matches the letter: 20 kV, 100 kV beyond what their amplifier could follow, equal groups, mass 3, neutrons/He-3, ordinary protons with no comparable effect.
- **Oliphant's life.** Matches the source.
- **Barrier figure.** U = ke²/r at 3 fm is 0.48 MeV. The turning point for 0.1 MeV is 14.4 fm.
- **Balance and choices.** The reactions are balanced. Exactly one correct option everywhere, with right feedback.
- **Hazard and gain claims.** "Hotter than the Sun" is limited to temperature. The roles of the neutron and the alpha particle are right. No Q or electricity claims are made.

## Shared issues
1. `assets/units/fy14/fx/reaction.js`, `STEPS` (vD = 80, vN = 150): the approach and product arrows share one scale but are not in proportion to real speeds. The header comment and the legend ("length proportional to speed") claim they are. Fix one of two ways. Either draw the approach at a small length (vD ≈ 4–8 px) with a note "fuel nuclei: about 10⁶ m/s; products: 10⁷–10⁸ m/s". Or label the arrows "to scale within each step only".
2. `reaction.js`, step 2 text: "only very fast nuclei … get close enough (helped by quantum tunnelling)" makes tunnelling sound like an extra. Fix: "only the fastest nuclei come close enough to tunnel through the rest of the barrier". Step 3 says 10⁻¹⁵ m; change it to "about $3 \cdot 10^{-15}$ m".
3. `reaction.js` energy-scales chart at 390 px: the bars do not line up with the axis (the developer's Shared issue 2). The printed values are right, so this is not blocking for science, but a phone user reads the wrong order of magnitude from the bars.
4. `nuclides.json` `energy_scales.methane`: the per-molecule value uses the higher heating value (9.23 eV), while the per-kg value uses the lower one (50.0 MJ/kg). Use one of them for both: the HHV gives 55.5 MJ/kg, the LHV gives 8.31 eV.
5. `nuclides.json`: half-life texts are a mix of plain text ("12.3 years") and LaTeX. Check U-238 (shown as 4.46·10⁹ a) against NUBASE2020 itself: the evaluations I remember give 4.463–4.468·10⁹ a. Every mass and B/A value (50 nuclides) agrees with B = (Z m(¹H) + N mₙ − m)c² to 10⁻⁴ MeV. The stable flags and the other half-lives that I checked are correct.
