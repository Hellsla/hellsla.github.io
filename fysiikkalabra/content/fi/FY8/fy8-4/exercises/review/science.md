VERDICT: FAIL
CONTENT-HASH: b16791ea77c9736e

## Blocking
- exercises.json:293 and solutions.md:173 (L3-04) — B, missing condition: the power is given for light *arriving at* the slits, but the 20 % is of photons that *passed through* them; the solution (r = 0,20 · 0,40 · P/hf = 321 1/s, t = 15,6 s) silently assumes every arriving photon passes the slits. — Write "Rakoihin tulevista fotoneista 20 % kulkee rakojen läpi ja osuu ilmaisimen alueelle, ja ilmaisin rekisteröi 40 % siihen osuvista fotoneista." in exercises.json and the same wording in solutions.md Annettu.

## Polish
- solutions.md:172 (L3-04 Vastaus) — "16 s (laskettu 15,6 s)" while the answer box is 15,6; pick one (state 15,6 s ≈ 16 s, two significant figures) so answer and solution read the same.
- solutions.md:151 (L2-06) — the value at 180° extrapolates the fit from 1 − cos θ = 1,866 to 2; say so and why it is justified (linear model through the origin). The rounding "kolme numeroa kuten 71,10 pm" is not the limiting datum: Δλ is known to ±0,01 pm (2–3 figures).
- solutions.md:141 (L2-05) — b) 11,4 to three figures overstates a ratio of counts (208 ± √208 ≈ ±14, about 7 %); c) says "ei erotu vaihtelusta" without an estimate; one sentence with √n would meet the plan's "tilastollisen vaihtelun arviointi".
- solutions.md:182 (L3-05 Vastaus) — "kolme merkitsevää numeroa kuten aallonpituuksissa": the wavelengths have four; justify three by Δλ = 3,66 pm instead.
- docs/exercise-bank/FY8.md — the set departs from the fy8-4 plan (no "miksi Comptonin ilmiö vaatii hiukkasmallin" at L1, no which-slit reasoning task at L3; L1-07 and L3-05 instead); update the plan or the tasks so they agree.

## Checked
- One script recomputed all 20 answers with my own formulas: all agree with exercises.json and answers.py within tolerance (L2-06 free fit 4,86 pm also inside 4 %).
- L2-06 data match Compton's Δλ = 2,426 pm (1 − cos θ) within 0,04 pm; through-origin line has a physical reason (θ = 0).
- L3-05 cosine rule and triangle angle right; E_k from p 850 eV vs energy 854 eV (exact Compton 850/849 eV), so the 0,5 % gap is from the data, as stated; v/c = 0,058 so p²/2m is valid.
- L2-07 pupil's numbers (3,06·10⁻²⁸ J, 1,6·10²⁵ 1/s) reproduce the nm-for-m error.
- L1-06 and L1-08: exactly one correct option each; distractor feedback physics right.
- No de Broglie; render of L3-05 at 1280 px clean.
- Hash identical at start and end.
