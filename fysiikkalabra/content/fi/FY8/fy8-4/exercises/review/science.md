VERDICT: PASS
CONTENT-HASH: e9be860c13569231
Round: 2

## Blocking

## Polish
- solutions.md:701 (L3-05 Vastaus): the gap is blamed on Δλ being known to three figures. Rounding (±0,005 pm) gives only 852,7–854,9 eV and never reaches 850 eV. The real cause is the datum 3,66 pm, which is 0,02 pm above Compton's 2,426 · 1,5 = 3,64 pm. Fix: "johtuu aallonpituuksien mittausepävarmuudesta (noin 0,02 pm Δλ:ssa)".
- solutions.md:679 (L2-07 Muunnokset): "virhe on 10^{-9}-kertainen fotonin energiassa". Fix: "fotonin energia tuli 10^{-9}-kertaiseksi".
- solutions.md:661 (L2-05 Järkevyys): "tummille kaistoille osuu vain noin 4 %". That is the share of each dark strip; all four together get about 16 %. Fix: "kullekin tummalle kaistalle".
- exercises.json:325 (L2-05): the answer box holds 11,4, but the solution says "noin 11", two significant figures. Both are within tolerance. If wanted, store 11.
- docs/exercise-bank/FY8.md:27 (carried over): the plan's L1 task "miksi Comptonin ilmiö vaatii hiukkasmallin" has no exercise. Update the plan, or set L1-08 in a Compton context.

## Checked
- Round-1 blocker fixed: L3-04 now says that 20 % of the arriving photons pass the slits and reach the detector, and that 40 % of those are registered (exercises.json and the solution). Recomputed: r = 321,4 1/s, t = 15,56 s, d = 74,6 km, 0,25 ms and 5 ns, all right.
- Round-1 polish fixed: L3-04 "15,6 s ≈ 16 s", L2-06 extrapolation stated with its reason, L2-05 √n estimate, L3-05 figures justified by Δλ.
- L2-07, changed to 633 nm and 2,0 mW: 3,138·10^-19 J and 6,37·10^15 1/s. The pupil's numbers reproduce the nm error.
- One script recomputed all 18 numeric answers: all agree with exercises.json and answers.py within 0,5 %.
- L2-06: through-origin k = 2,426 pm (free fit 2,432 pm, intercept −0,008 pm). L2-05: column sums 50, 500 and 5000; the shares and the √n figures are right.
- L3-05: the cosine rule and the triangle are right. Non-relativistic E_k is fine (about 0,1 %).
- L1-06 and L1-08: exactly one correct option each, and the feedback is right.
- At 1280 px, L2-07, L3-04 and L3-05 render cleanly. No de Broglie.
- Hash is the same at the start and the end.
