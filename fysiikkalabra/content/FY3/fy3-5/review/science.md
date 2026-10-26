VERDICT: PASS
CONTENT-HASH: 1985815b7b66e3f6

## Blocking

## Polish
- sim.js:124, inquiry.json:105 — "vastaa 0,50 g:aa ilmaa" holds only for the heat capacity. Real air under the same stroke: adiabatic about 13 J and 36 K (the model gives 41 J and 114 K), isothermal about 12 J (the model gives 36 J). Fix: "lämpökapasiteetiltaan vastaa", and give the real values in Lisätietoja.
- sim.js:87 — the p readout assumes an isotropic gas, but only the piston changes vx. After an insulated push the piston pressure is 2,37 p₀, while the readout shows 1,85. W itself is exact. Fix: take p from the piston impulse, or say in Lisätietoja that p is a direction average.
- sim.js:124 — the extra heating comes mostly from 2D (a mixed 2D gas gives 391 K) and partly from the vx-only pumping (407 K). Name both causes.
- inquiry.json:84, 88, 93 — "Mittauksissa/Mittaukset" for sim numbers. Fix: "mallin lukemissa".
- solutions.md:77, 93 — "riippuu käytännössä vain lämpötilasta" should say "ideaalikaasun".

## Checked
- All 12 exercise answers, siirto 5,4 J (mistakes 6,6 and 599,4) and check-2 30 J (mistakes 230 and 10) recomputed: they match.
- Sign convention W on the system: consistent everywhere. Worked example 110 J is solved symbolically first.
- Playwright, insulated, push right after Alkuun: slow 40,7 J / 406,4 K, fast 40,9 J / 407,0 K. The theoretical value is 407,2 K. Matches pred-2.
- A delayed start gives 111–116 K. The "muutaman kelvinin" caveat covers this.
- Conducting slow push: W 35,8 J. At T 293 K, Q −35,7 J and ΔU 0,1 J; the final values are Q −35,8 J, ΔU 0, p 1,33. Matches koe-2 and pred-1.
- Haaste: 40,9 J and 407 K, then Q → −40,9 J and ΔU → 0. Matches.
- ΔU − (Q + W) < 1e-13 J in all runs.
- The v' = 2u − v reflection gives W = force × distance. The √(T0/T) wall rule is stated honestly in Lisätietoja and is fine for FY3.
- pred-2 "about equal" (u ≪ v) and check-3 (the difference via Q) are consistent with each other.
- check-1, the exit ticket and the fire-piston magnitude are sound. Scope is the first law only.
