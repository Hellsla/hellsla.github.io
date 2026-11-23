VERDICT: PASS
CONTENT-HASH: 1cc3d386f9a407a0
SCOPE: full; the change is three new ```pysahdy boxes in unit.md (the webp figures in the diff are teacher-approved, docs/teacher-figures.tsv 2026-11-22)

## Blocking
None.

## Polish
- Pysähdy 2 has $\approx$ in its chain and then "$= 6\,\text{kV}$". The text before it says "noin", so this is fine; "$\approx 6\,\text{kV}$" at the end would match the 9 kV sentence above it. This is not a physics issue.
- Earlier polish items on s7 and s8 still stand (see the previous report: s7 plate position, s7 a vacuum/air comparison, s8 c $\approx 125\,\Omega$ from the curve).

## Checked
- `units.py hash fy9-sahkokentta` at the start and the end: 1cc3d386f9a407a0. `practice.py check: OK`; the packet has no `physics [...]` warnings.
- Pysähdy boxes, judged first:
  - (1) Field to the right gives a force on the electron to the left, from $\overline{F} = q\overline{E}$ with $q<0$. This is correct and agrees with the Ydinajatus text, lt-2 and the levyt figure.
  - (2) $U = E_\text{max}d = 3\,\text{MV/m}\cdot 2\,\text{mm} = 6\,\text{kV}$. The uniform-field condition is stated in the Kaava text and in the johda box. It agrees with the 3 mm → 9 kV sentence.
  - (3) $d \to 2d$ halves $C$ ($C \propto 1/d$, with the other quantities held constant). The condition for the plate formula is stated in the sentence just before. It agrees with lt-4 (disconnected: $U$ doubles).
  - All three are classed C at most; none is A or B.
- My own script (scratchpad `recompute.py`) recomputed every number from the task text. These numbers all agree:
  - Unit text: 0,9 µC, 4,05 mJ, ratio 55 600 > 50 000.
  - Inquiry: 43×, 7264 km/s and its three mistake values; 35,95 / 50,33 / 43,14 / 7,19 µN; 6,008 pN with its mistakes; 1690 V / 1195 V; 3,865 / 3,478 / 11,59 / 3,13 h; 187 Ω → 190 Ω and 8,5 mA; 5,0 µF and 0,49 mJ; 112,6 / 225,3 / 0,352 mJ.
  - s1: 0,493 mN, 18,74 nC, 0,2465 mN; 6,35 cm both exactly and with small angles.
  - s2: 184,5 pF, 0,8301 µC, 1,868 mJ, 1,5 MV/m, 803,6 V, 0,3335 mJ.
  - s3: my own least-squares fit gives a slope of 353,7 pF·mm, $\varepsilon_0$ = 8,843 pF/m and an intercept of 22,2 pF.
  - s4: 1,5 mV, 11,5 kV and 4 mm.
  - s5: 0,989 W and 16,5 %; the R = U/I check passes.
  - s6: 40,21 km/s, 1,1 MV/m, 87,54 mN, 349 m/s, 5,64 kg, 1,76 kW, and the ~76 kg chemical comparison.
  - s7: 5,0 kV/m, 2,411e11 m/s², 98,2 km/s, −50 V.
  - s8: 17,27 mA, 65,6 mW, 63,3 %, 126,7 Ω, 440 Ω and 110 Ω.
- Physics in the unit text was checked and is correct:
  - the conditions for Coulomb's law and for U = Ed;
  - the sign of the work and $|Q|U$;
  - ½QU, and why the other half goes to internal energy;
  - a disconnected capacitor with a dielectric inserted;
  - Kirchhoff's voltage-law derivation for the series resistor;
  - fuse versus residual-current device.
- Inquiry: every choice item has exactly one correct option, and its distractor feedback is right. The explain criteria (charge conservation, polarisation, the 1/r² asymmetry, the force balance) match the model answer.
- s4–s6 worked solutions, read in full:
  - the phase-to-earth voltage $20/\sqrt3$;
  - the 4 mm stated as a lower bound and not as a safe distance;
  - step voltage and how to leave the area;
  - $U_tI_k$ as the systematic error;
  - thrust from momentum, $F = 2P/v$, and the alternative method.
- Scope: everything is from FY6, with FY4 momentum in s6.
