VERDICT: PASS
CONTENT-HASH: fda3f293d7b38a87

## Blocking

## Polish
- inquiry.json:438 (tarkistus-1, correct option) and lesson.md:42 (processes aria-label) — "Atomista lähtee kaksi fotonia" comes close to the misconception the lesson names ("absorboi fotonin ja lähettää kaksi"); the atom emits one photon and the incoming one passes on — e.g. "Atomin luota jatkaa kaksi fotonia, saapuva ja uusi, joilla on sama energia, suunta ja vaihe."
- lesson.md:124 — "yksiväristä, koska kaikki fotonit syntyvät samassa siirtymässä" holds for a lamp's spectral line too; the laser's narrow line comes from the selective amplification between the mirrors as well (C at this level; optionally add "ja peilien välissä vahvistuu vain kapea aallonpituusalue").
- lesson.md:194 and exit-ticket.json:8 — "kaivon paksuus valitsee aallonpituuden": the well's material sets the range and its thickness tunes it; "kaivon aine ja paksuus määräävät aallonpituuden".
- inquiry.json:293 (johtopaatos model) — "stimuloitu emissio purkaa ylätasoa yhtä nopeasti kuin pumppaus täyttää sitä": in the sim's model, spontaneous plus stimulated emission together balance the pump; "spontaani ja stimuloitu emissio purkavat yhdessä ylätasoa yhtä nopeasti kuin pumppaus täyttää sitä".

## Checked
- Recomputed in one script: rate graph (2,04/2,68/3,27·10^15 1/s), worked example 3,18·10^15 1/s and 633 nm, 1,91/3,06 eV, CdSe 713 nm, quantum-dot energies 2,58–2,00 eV, kertaus 1,89 eV/656 nm, siirto 96,3 W and mistakes 87,9/1096 W, virhe 1,3·10^25 vs 1,3·10^16 and 5 MW, tarkistus-2 532/397/228 nm: all match.
- Sim model (koe-1 0/0/12,5/35/80/125/170 mW, threshold 1,22 W, N2 clamped 55 %; koe-2 33,3/40,0/45,5 %; koe-3 66,7/83,3 % without beam) matches sim.js, lesson-answers.py, the model/calc boxes and every prediction feedback; rate equations for 2- and 3-level media correct.
- Experiments: levels and mirrors locked, only P varied; simState provides n2, inv, Pout; inv = N2 > N1 consistent with "≤ 50 % at 1,0 W".
- Exactly one correct option in kertaus, ennuste-1, ennuste-2, kvanttipisteet, virhe, tarkistus-1; distractor feedbacks correct.
- Figures: rate-graph line and markers to scale; qdots radii in ratio 2:3:4:5:6; inversion figure shows N2 > N1, 694 nm.
- Physics claims: two-level limit ½, thermal equilibrium no inversion, ruby ms lifetime vs 10^-8 s (~10^5), threshold, coherence, laser hazard via focusing, tunnelling (STM, flash, Josephson, alpha decay), Nobel 2023 chemistry and 2025 physics: correct.
- Scope: within FY8 central contents; tunnelling marked optional; no de Broglie wavelength.
